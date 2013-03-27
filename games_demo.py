# A demo showing the usage of the game class
#
# Author: Ivo Chichkov

import sys
# make sure to append correct lib path
sys.path.append(r"./lib")
import game

print "\n"
print "Prisoner's Dilemma"
# Prisoner's Dilemma
b = game.Game(payoff_matrix=[[(3,3),(1,4)],[(4,1),(2,2)]], moves_A=["Cooperate", "Defect"], moves_B=["Cooperate", "Defect"])
print b
print b.calculate_pure_nash()

# Laundry vs. Smoke
print "Laundry vs. Smoke"
a = game.Game(payoff_matrix=[[(-1,-1),(2.5,0)],[(0,1),(2.7,0)]], moves_A=["Laundry_SS", "Laundry_OR"], moves_B=["Don't coop", "Coop"])
print a
print a.calculate_pure_nash()
