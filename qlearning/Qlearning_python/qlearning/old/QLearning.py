class QLearning(object):
    """docstring for QLearning."""
    def __init__(self, arg):
        super(QLearning, self).__init__()
        self.GAMMA_DISCOUNT_FACTOR = 0.95  #* Must be < 1, small values make it very greedy */
        self.LEARNING_RATE_CONSTANT = 10 # See alpha(), lower values are good for quick results in large and deterministic state spaces */
        self.explore_chance = 0.5 # The exploration chance during the exploration phase */
        self.REPEAT_ACTION_MAX = 30 
        self.iteration = 0 #/* Keeps track of how many iterations the agent has run */
        self.action_counter = 0 #/* Keeps track of how many times we have repeated the current action */
        self.print_counter = 0 # /* Makes printouts less spammy */ 
        self.Qtable = dict() #new Hashtable<String, Double>(); /* Contains the Q-values - the state-action utilities */
        self.Ntable = dict() #new Hashtable<String, Integer>(); /* Keeps track of how many times each state-action combination has been used */
        self.NUM_ACTIONS = 3

    def init(self):
        pass
    
    def reset(self):
        pass
    
    def performAction(self):
        pass
    
    def tick(self):
        pass

    def computeAlpha(self, num_tested: int):
        return (self.LEARNING_RATE_CONSTANT/(self.LEARNING_RATE_CONSTANT + num_tested))

    def selectAction(self, state):
        action = 0
        # Random rand = new Random();

		#if (explore && Math.abs(rand.nextDouble()) < explore_chance):
			#/* Taking random exploration action! */
		#	action = Math.abs(rand.nextInt()) % NUM_ACTIONS;
		#	return action;
		# Find action with highest Q-val (utility) in given state */
        maxQval = -999999999
        for i in range(0, self.NUM_ACTIONS):
            test_pair = state + i
            Qval = 0

            if self.Qtable.get(test_pair):
                Qval = self.Qtable.get(test_pair)
			
            if Qval > maxQval:
                maxQval = Qval
                action = i
        return action