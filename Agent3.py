class Agent3:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = None
        self.anticipated_outcome = None
        self.counter = 0
        self.previous_outcome = None

    def action(self, outcome):
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) +
                  "; counter: " + str(self.counter) + ")")

        """ Computing the next action to enact """

        if self._action == 0:
            self._action = 1
        else:
            self._action = 0

        # anticipation
        if self._action == 0:
            self.anticipated_outcome = self.hedonist_table[-1][1]
        else:
            self.anticipated_outcome = self.hedonist_table[-1][1]

        return self._action


