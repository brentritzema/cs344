'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden & brentritzema
@version Jan 1, 2013
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch', 'Rain'])
T, F = True, False
P[T, T, T, T] = 0.054; P[T, T, F, T] = 0.006
P[F, T, T, T] = 0.036; P[F, T, F, T] = 0.004
P[T, F, T, T] = 0.008; P[T, F, F, T] = 0.032
P[F, F, T, T] = 0.072; P[F, F, F, T] = 0.288

P[T, T, T, F] = 0.054; P[T, T, F, F] = 0.006
P[F, T, T, F] = 0.036; P[F, T, F, F] = 0.004
P[T, F, T, F] = 0.008; P[T, F, F, F] = 0.032
P[F, F, T, F] = 0.072; P[F, F, F, F] = 0.288

# P(Cavity|Catch=T) = P(Cavity ^ Catch) / P(Catch) = 0.18 / 0.34 = 0.529
# P(Toothache | Rain) = P(Toothache ^ Rain) / P(Rain) = (0.054 + 0.008 + 0.006 + 0.032) / 0.5 = 0.2
PC = enumerate_joint_ask('Toothache', {'Rain': T}, P)
PB = enumerate_joint_ask('Toothache', {'Rain': F}, P)
print(PC.show_approx())
print(PB.show_approx())

# Answers to questions:
# i.   There are now 16 entries
# ii.  The probabilities do sum to 1, and they should otherwise there would be greater than 100% chance of either
#      having or not having a toothache.
# iii. I think you could use things other than true false, such as discrete numeric values, but then the size of
#      of the joint probability table would grow very large. In reality those discrete numeric values would be
#      better represented as either having that value or not having that value (a 20% cavity, whatever that means,
#      or not a 20% cavity). So, in conclusion I think it would be best to stick with strictly true and false values.
# iv.  The probabilities I chose indicated that whether or not it was raining had no effect on whether or not
#      there was a toothache, so it was independent
