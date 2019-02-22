'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden & brentritzema
@version Jan 1, 2013
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)

# P(Cavity|Catch=T) = P(Cavity ^ Catch) / P(Catch) = 0.18 / 0.34 = 0.529
PB = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())
print(PB.show_approx())

Coin = JointProbDist(['Coin2', 'Coin1'])
Heads, Tails = True, False
Coin[Heads, Tails] = 0.25
Coin[Tails, Tails] = 0.25
Coin[Heads, Heads] = 0.25
Coin[Tails, Heads] = 0.25

# This answer confirms what I believe to be true about coins
PCoin = enumerate_joint_ask('Coin2', {'Coin1': Heads}, Coin)
print(PCoin.show_approx())

# I believe full joint is not generally used in probabilistic systems because you need to know all the
# values of the join probability distribution ahead of time
