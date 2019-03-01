'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden & brentritzema
@version Mar 1, 2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
])

# i. P(Alarm | burglary ^ -earthquake)
# This calculates the probability that the alarm went off given that there was a
# burglary and not an earthquake. This one has a higher probability because in the setup of the bayes net
# you can see that the probability of an alarm given a burglary and earthquake is high, at 0.94 (aka, this probability
# is right off the chart)
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
print(elimination_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# ii. P(John | burglary ^ -earthquake)
# This calculates the probability that John calls given that there was a
# burglary and not an earthquake.  This one is a bit lower than the probability of the alarm
# because there's not a 100% chance John calls when the alarm goes off, so we need to account for that.
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
print(elimination_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# iii P(burglary | alarm)
# This calculates the probability of a burglary given that the alarm went off. This is fairly low because
# the probability of a burglary is low. However, it's not extremely low because the alarm doesn't go off too often
# unless there is a burglary or earthquake
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
print(elimination_ask('Burglary', dict(Alarm=T), burglary).show_approx())

# iv. P(burglary | john ^ mary)
# This calculates the probability of a burglary given John and Mary called. This one is even lower than the previous
# because the probability of Burglary is still so low and John and Mary both calling aren't as telling as
# just the alarm going off because they don't always call when the alarm goes off.
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
