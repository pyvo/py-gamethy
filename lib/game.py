# A class for representing simple games
#
# Author: Ivo Chichkov

class Game:

    ## initialize the game
    #
    # @param payoff_matrix      the payoff matrix, 
    # @param moves_A            list of strings containing Player A's moves names
    # @param moves_B            list of strings containing Player B's moves names
    def __init__(self, payoff_matrix=[[]],  moves_A = [], moves_B = []):

        assert isinstance(payoff_matrix[0],list), "2-Dimensional Payoff matrix expected"
        self.payoff_matrix = payoff_matrix
        
        # update move names
        if moves_A != []:
            assert (len(moves_A)==len(payoff_matrix)), "Inconsistent number of moves for player A"
            self.moves_A = moves_A
        else:
            self.moves_A = []
            for i in range(len(payoff_matrix)):
                self.moves_A.append("[A] Move "+str(i))    
        if moves_B != []:
            assert (len(moves_B)==len(payoff_matrix[0])), "Inconsistent number of moves for player B"
            self.moves_B = moves_B
        else:
            self.moves_B = []
            for i in range(len(payoff_matrix[0])):
                self.moves_B.append("[B] Move "+str(i))    

    ## return the game table as a string
    def __str__(self):
        gametable = ""

        # draw a line
        for i in range(len(self.payoff_matrix[0])+1):
            gametable += "+------------"
        gametable += "+\n"

        # draw B's moves
        gametable += "|"+" "*12
        for i in range(len(self.payoff_matrix[0])):
            gametable += "|%12s" % self.moves_B[i] 
        gametable += "|\n"

        # draw a line
        for i in range(len(self.payoff_matrix[0])+1):
            gametable += "+------------"
        gametable += "+\n"

        # draw A's moves + payoff matrix
        for y in range(len(self.payoff_matrix)):
            gametable += "|%12s" % self.moves_A[y] 
            for x in range(len(self.payoff_matrix[y])):
                gametable += "|%12s" % str(self.payoff_matrix[y][x])
            gametable += "|\n"

            # draw a line
            for i in range(len(self.payoff_matrix[0])+1):
                gametable += "+------------"
            gametable += "+\n"

        return gametable

    # return a list of booleans with TRUE corresponding to a best move in moves
    def calculate_best_response(self, moves):
        best = [False]*len(moves) 
        m = max(moves)
        for b in [i for i, j in enumerate(moves) if j == m]:
            best[b]=True
        return best
        
    # return a matrix with best responses for both players
    def calculate_br_matrix(self):
        
        # calculate best responses for player A
        best_A = []
        for i in range(len(self.payoff_matrix[0])):
            best_A.append(self.calculate_best_response([y[i][0] for y in self.payoff_matrix]))

        # calculate best responses for player B
        best_B = []
        for i in range(len(self.payoff_matrix)):
            best_B.append(self.calculate_best_response([x[1] for x in self.payoff_matrix[i]]))

        # fill the br matrix
        eqMatrix  = []
        for y in range(len(self.payoff_matrix)):
            eqRow = []
            for x in range(len(self.payoff_matrix[0])):
                eqRow.append((best_A[x][y],best_B[y][x]))
            eqMatrix.append(eqRow)

        return eqMatrix

    # calculate pure nash equilibria
    def calculate_pure_nash(self):
        equilibria = []
        br_matrix = self.calculate_br_matrix()
        for y in range(len(self.payoff_matrix)):
            for x in range(len(self.payoff_matrix[0])):
                if br_matrix[y][x] == (True, True):
                    equilibria.append([self.moves_A[y], self.moves_B[x]])

        return equilibria
            
