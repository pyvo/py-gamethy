# A demo showing the usage of the game class
#
# Author: Ivo Chichkov

# make sure to append correct lib path
import sys
sys.path.append(r"./lib")

import game
import sympathy_game

########################################################
#                                                           
# Example 1: Prisoner's Dilemma, calculate pure Nash Eq      
#                                                           
########################################################
print "------------------------------------------------"
print "Prisoner's Dilemma"
# Prisoner's Dilemma
b = game.Game(payoff_matrix=[[(3,3),(1,4)],[(4,1),(2,2)]], moves_A=["Cooperate", "Defect"], moves_B=["Cooperate", "Defect"])
print b
print b.calculate_pure_nash()


########################################################
#                                                           
# Example 2: Laundry vs. Smoke (Hawks and Doves), calculate pure Nash Eq      
#                                                           
########################################################
print "------------------------------------------------"
print "Laundry vs. Smoke"
a = game.Game(payoff_matrix=[[(-1,-1),(2.5,0)],[(0,1),(2.7,0)]], moves_A=["Laundry_SS", "Laundry_OR"], moves_B=["Don't coop", "Coop"])
print a
print a.calculate_pure_nash()


########################################################
#                                                           
# Example 3: Laundry vs. Smoke with effective Sympathy A->B, calculate pure Nash Eq      
#                                                           
######################################################### 
print "------------------------------------------------"
print "Laundry vs. Smoke, effSym_AB = 0.5"
c = sympathy_game.EffectiveSympathyGame(payoff_matrix=[[(-1,-1),(2.5,0)],[(0,1),(2.7,0)]], moves_A=["Laundry_SS", "Laundry_OR"], moves_B=["Don't coop", "Coop"],
                                        effSym_AB=0.5)
c.incorporateEffectiveSympathy()
print c

########################################################
#                                                           
# Example 4: Laundry vs. Smoke with effective Sympathy B->A, calculate pure Nash Eq      
#                                                           
#########################################################
print "------------------------------------------------"
print "Laundry vs. Smoke, effSym_BA = 0.5"
c = sympathy_game.EffectiveSympathyGame(payoff_matrix=[[(-1,-1),(2.5,0)],[(0,1),(2.7,0)]], moves_A=["Laundry_SS", "Laundry_OR"], moves_B=["Don't coop", "Coop"],
                                        effSym_BA=0.5)
c.incorporateEffectiveSympathy()
print c
print c.calculate_pure_nash()
c.restoreOriginalPayoffs()
print "Restoring original payoffs..."
print c
print c.calculate_pure_nash()

