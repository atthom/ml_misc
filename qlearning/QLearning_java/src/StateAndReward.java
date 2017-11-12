public class StateAndReward {
	

	/* State discretization function for the angle controller */
	public static String getStateAngle(double angle, double vx, double vy) {

		/* TODO: IMPLEMENT THIS FUNCTION */
		

		String state = "OneStateToRuleThemAll";
		if(angle<-2.355){
			state = "1";
		} else if(angle<-1.57){
			state = "2";
		} else if(angle<-0.785){
			state = "3";
		} else if (angle < 0) {
			state = "4";
		} else if (angle < 0.785) {
			state = "5";
		} else if (angle < 1.57) {
			state = "6";
		}else if (angle < 2.355) {
			state = "7";
		}else if (angle <= 3.15) {
			state = "8";
		}
		return state;
	}

	/* Reward function for the angle controller */
	public static double getRewardAngle(double angle, double vx, double vy) {

		double reward = 0;
       
		if(angle<1.30 && angle > -1.30){
			reward = 5;
		}
		if(angle<0.05 && angle > -0.05) {
			reward = 10;
		}
        return reward;
	}
	public static final int ANGLE_RESOLUTION = 11;
	public static final int VY_RESOLUTION = 7;
	
	public static final int VELOCITY_BOUND = 1;
	
	
	/*reward discretization function for the full hover controller */
	public static String getStateHover(double angle, double vx, double vy) {

		String state = "a-" + discretize(angle,11,-0.3,0.3) +
					   " vy-" + discretize(vy,7,-4,1);
		
		return state;
	}

	/* Reward function for the full hover controller */
	public static double getRewardHover(double angle, double vx, double vy) {
		int a_reward = 0, vy_reward =0;

		if(angle<1.30 && angle > -1.30){
			a_reward = 5;
		}
		if(angle<0.05 && angle > -0.05) {
			a_reward = 10;
		}
		
		if(vy<1 && vy > -1){
			vy_reward = 5;
		}
		if(vy<0.3 && vy > -0.3) {
			vy_reward = 10;
		}

		
		return a_reward + vy_reward;
	}

	

	// ///////////////////////////////////////////////////////////
	// discretize() performs a uniform discretization of the
	// value parameter.
	// It returns an integer between 0 and nrValues-1.
	// The min and max parameters are used to specify the interval
	// for the discretization.
	// If the value is lower than min, 0 is returned
	// If the value is higher than min, nrValues-1 is returned
	// otherwise a value between 1 and nrValues-2 is returned.
	//
	// Use discretize2() if you want a discretization method that does
	// not handle values lower than min and higher than max.
	// ///////////////////////////////////////////////////////////
	public static int discretize(double value, int nrValues, double min,
			double max) {
		if (nrValues < 2) {
			return 0;
		}

		double diff = max - min;

		if (value < min) {
			return 0;
		}
		if (value > max) {
			return nrValues - 1;
		}

		double tempValue = value - min;
		double ratio = tempValue / diff;

		return (int) (ratio * (nrValues - 2)) + 1;
	}

	// ///////////////////////////////////////////////////////////
	// discretize2() performs a uniform discretization of the
	// value parameter.
	// It returns an integer between 0 and nrValues-1.
	// The min and max parameters are used to specify the interval
	// for the discretization.
	// If the value is lower than min, 0 is returned
	// If the value is higher than min, nrValues-1 is returned
	// otherwise a value between 0 and nrValues-1 is returned.
	// ///////////////////////////////////////////////////////////
	public static int discretize2(double value, int nrValues, double min,
			double max) {
		double diff = max - min;

		if (value < min) {
			return 0;
		}
		if (value > max) {
			return nrValues - 1;
		}

		double tempValue = value - min;
		double ratio = tempValue / diff;

		return (int) (ratio * nrValues);
	}

}
