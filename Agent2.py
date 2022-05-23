class Agent2:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = 0
        self.previous_action = 0
        self.anticipated_outcome = None
        self.counter = 0
        self.previous_outcome = 0
        self.outcome_for_action1 = 0
        self.outcome_for_action0 = 0

    def action(self, outcome):
        """ tracing the previous cycle """
        if self._action is not None:
            print("Action: " + str(self._action) +
                  ", Anticipation: " + str(self.anticipated_outcome) +
                  ", Outcome: " + str(outcome) +
                  ", Satisfaction: (anticipation: " + str(self.anticipated_outcome == outcome) +
                  ", valence: " + str(self.hedonist_table[self._action][outcome]) +
                  "; counter: " + str(self.counter) + ")")

        # Choisir la prochaine action
        """ Computing the next action to enact """
        if self._action == 0:
            self.outcome_for_action0 = outcome
            self._action = 1
        else:
            self.outcome_for_action1 = outcome
            self._action = 0

        # annonce l'anticipation
        if self._action == 0:
            self.anticipated_outcome = self.outcome_for_action0
        else:
            self.anticipated_outcome = self.outcome_for_action1

        return self._action