from math import sqrt

from keras.layers import LSTM, Dense, concatenate
from keras.losses import mean_squared_error
from keras.models import Sequential
from pandas import read_csv, DataFrame, concat
from matplotlib import pyplot
from matplotlib.pyplot import savefig
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler


def plot_features(dataset):
    values = dataset.values
    print(dataset.head())
    # specify columns to plot
    groups = [0, 1, 2, 3, 4, 5]
    i = 1
    # plot each column
    pyplot.figure()
    for group in groups:
        pyplot.subplot(len(groups), 1, i)
        pyplot.plot(values[:, group])
        pyplot.title(dataset.columns[group], y=0.5, loc='right')
        i += 1
    savefig("./plots/all_features.png")


# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j + 1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j + 1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j + 1, i)) for j in range(n_vars)]
    # put it all together
    agg = concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg


def normalize(values):
    # integer encode direction
    encoder = LabelEncoder()
    values[:, 4] = encoder.fit_transform(values[:, 4])
    # ensure all data is float
    values = values.astype('float32')
    # normalize features
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(values)
    # frame as supervised learning
    reframed = series_to_supervised(scaled, 1, 1)
    # drop columns we don't want to predict
    print(reframed.head())
    return reframed


def create_training_set(reframed):
    # split into train and test sets
    values = reframed.values
    n_train = int(len(values) * 0.7)
    train = values[:n_train, :]
    test = values[len(values) - n_train:, :]
    # split into input and outputs
    train_X, train_y = train[:, :-1], train[:, -1]
    print(n_train, len(values) - n_train)
    print(len(train_X), len(train_y))

    test_X, test_y = test[:, :-1], test[:, -1]
    # reshape input to be 3D [samples, timesteps, features]
    train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
    test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
    print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)
    return train_X, train_y, test_X, test_y


def design_and_train(train_X, train_y, test_X, test_y):
    # design network
    model = Sequential()
    print((train_X.shape[1], train_X.shape[2]))
    model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    # fit network
    history = model.fit(train_X, train_y, epochs=50, batch_size=72, validation_data=(test_X, test_y), verbose=2,
                        shuffle=False)
    # plot history
    print(len(history.history['loss']))
    print(len(history.history['val_loss']))
    pyplot.plot(history.history['loss'], label='train')
    pyplot.legend()
    pyplot.plot(history.history['val_loss'], label='test')
    pyplot.legend()
    savefig("./plots/history.png")
    return model


def evaluate_model(model, test_X, test_y):
    scaler = MinMaxScaler(feature_range=(0, 1))
    # make a prediction
    yhat = model.predict(test_X)
    test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
    # invert scaling for forecast
    print(yhat,  test_X[:, 1:])

    inv_yhat = concatenate((yhat, test_X[:, 1:]), axis=1)
    inv_yhat = scaler.inverse_transform(inv_yhat)
    inv_yhat = inv_yhat[:, 0]
    # invert scaling for actual
    test_y = test_y.reshape((len(test_y), 1))
    inv_y = concatenate((test_y, test_X[:, 1:]), axis=1)
    inv_y = scaler.inverse_transform(inv_y)
    inv_y = inv_y[:, 0]
    # calculate RMSE
    # rmse = sqrt(mean_squared_error(inv_y, inv_yhat))
    mse = mean_squared_error(inv_y, inv_yhat)
    print('Test MSE: %.3f' % mse)


# load dataset
dataset = read_csv('./datasets/BTC-ETH.csv', header=0, index_col=0)
values = dataset.values
plot_features(dataset)

reframed = normalize(values)
train_X, train_y, test_X, test_y = create_training_set(reframed)

model = design_and_train(train_X, train_y, test_X, test_y)

evaluate_model(model, test_X, test_y)
