# A class derived from *Game* for representing Games with Effective Sympathy.
#
# If a player's utility is 0, he gains a fraction of other player's utility,
# depending on the sympathy factor between them. For a detailed explanation
# reffer to David Sally's publication (2002).
#
# Author: Ivo Chichkov

from copy import deepcopy
from game import Game

class EffectiveSympathyGame(Game):

    ## initialize
    #
    #  @param effSym_AB Effective Sympathy of A regarding B (A->B), 0 < effSym < 1
    #  @param effSym_BA Effective Sympathy of B regarding A (B->A), 0 < effSym < 1
    def __init__(self, payoff_matrix=[[]],  moves_A = [], moves_B = [], effSym_AB = 0, effSym_BA = 0):
        # init superclass
        Game.__init__(self, payoff_matrix,  moves_A, moves_B)

        self.effSym_AB = effSym_AB
        self.effSym_BA = effSym_BA

        # create a backup of the payoff matrix
        self.payoffBackup = deepcopy(payoff_matrix)

    # set the values for effective sympathy
    def setEffectiveSympathy(self, effSym_AB, effSym_BA):
        self.effSym_AB = effSym_AB
        self.effSym_BA = effSym_BA

    # get the values for effective sympathy
    def getEffectiveSympathy(self):
        return (self.effSym_AB, self.effSym_BA)

    # incorporate effective sympathy into the payoff matrix
    def incorporateEffectiveSympathy(self):
        for y in range(len(self.payoffBackup)):
            for x in range(len(self.payoffBackup[0])):
                # check zero payoff for player A
                if self.payoffBackup[y][x][0] == 0:
                    # calculate new utility = effective sympathy (A->B) * utility (B)
                    self.payoff_matrix[y][x] = (self.effSym_AB * self.payoffBackup[y][x][1], self.payoff_matrix[y][x][1])
                # check zero payoff for player B
                if self.payoffBackup[y][x][1] == 0:
                    # calculate new utility = effective sympathy (B->A) * utility (A)
                    self.payoff_matrix[y][x] = (self.payoff_matrix[y][x][0], self.effSym_BA * self.payoffBackup[y][x][0])

    # restore the original payoffs
    def restoreOriginalPayoffs(self):
        self.payoff_matrix = deepcopy(self.payoffBackup)
        
