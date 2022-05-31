class Agent4:
    def __init__(self, valence_table):
        """ Creating our agent """
        self.valence_table = valence_table
        self._action = None
        self.anticipated_outcome = None
        self.counter = 0
        self.previous_outcome = None
        self.previous_action = 0
        self.outcome_for_action0 = 0
        self.outcome_for_action1 = 0

    def action(self, outcome):
        """ tracing the previous cycle """

        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.valence_table[self._action][outcome]) +
                  "; counter: " + str(self.counter) + ")")

        if self._action is not None:
            self._action = random.randint (0, 2)

#mettre valence négative lorsque la tortue cogne le mur