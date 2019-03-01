'''
This module implements the Bayesian network for exercise 5.2 in lab05 of CS344

@author: brentritzema
@version Mar 1, 2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
])

# a.
# i. P(Raise | sunny)
# This probability is easy to calculate, because getting being sunny has no influence on the probability of a
# raise. Therefore the probability is just P(Raise) = 0.01, and the distribution is <0.01,0.99>
print(enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())
print(elimination_ask('Raise', dict(Sunny=T), happy).show_approx())


# ii. P(Raise | happy ^ sunny)
# The fact that happy is true might have been a result of getting a raise, so it raises the likelihood that
# a raise happened. You can see the calculation below.
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())
print(elimination_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())

# P(Raise | happy ^ sunny)
# = alpha * <P(Raise) * P(sunny) * P(happy | raise ^ sunny),
#            P(-Raise) * P(sunny) * P(happy | -raise ^ sunny)>
# = alpha * <0.01 * 0.7 * 1, 0.99 * 0.7 * 0.7>
# = alpha * <0.007, 0.4851>
# = <0.0142, 0.986>

# b.
# i. P(Raise | happy)
# This probability makes sense because the probability of getting a raise is so low and the probability of it being
# sunny is so high that if you're happy, it's most likely because it's sunny
print(enumeration_ask('Raise', dict(Happy=T), happy).show_approx())
print(elimination_ask('Raise', dict(Happy=T), happy).show_approx())


# ii. P(Raise | happy ^ -sunny)
# This probability makes sense because when it's not sunny you are much more likely to be happy because of the raise
# and you are not very likely to be happy if it's not sunny and you didn't get a raise. However, the probability of
# getting a raise is still so low that this probability is still very low.
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())
print(elimination_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())
