'''
This module implements the Bayesian network for exercise 5.2 in lab05 of CS344

@author: brentritzema
@version Mar 1, 2019
'''

from probability import BayesNet, enumeration_ask, elimination_ask

# Utility variables
T, F = True, False

cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2}),
])

# a. P(Cancer | Test1 ^ Test2)
# This calculates the probability of cancer given that test1 and test2 were positive
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
print(elimination_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

# b. P(Cancer | Test1 ^ -Test2)
# This calculates the probability of cancer given that test1 was positive and test2 was negative
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())
print(elimination_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

# These results make sense. One failed test reduces the likelihood of having cancer by two orders of magnitude

# Here is P(Cancer | Test1 ^ Test2) worked out by hand
# = alpha * <P(cancer) * P(test1 | cancer) * P(test2 | cancer),
#            P(-cancer) * P(test1 | -cancer) * P(test2 | -cancer)>
# = alpha * <0.01 * 0.9 * 0.9, 0.99 * 0.2 * 0.2>
# = alpha * <0.0081, 0.0396>
# = <0.17, 0.83>
# This one is low, but still still a scary number because the probability of both test results returning true
# given that you have cancer are fairly high. However it still is very low because the probability of having
# cancer is so low.

# Here is P(Cancer | Test1 ^ -Test2) worked out by hand
# = alpha * <P(cancer) * P(test1 | cancer) * P(-test2 | cancer),
#            P(-cancer) * P(test1 | -cancer) * P(-test2 | -cancer)>
# = alpha * <0.01 * 0.9 * 0.1, 0.99 * 0.2 * 0.8>
# = alpha * <0.0009, 0.1584>
# = <0.00565, 0.994>
# This probability is very low because if you had cancer, which there is a very small chance of, then it's very
# likely that both tests will return positive. In this case since that didn't happen the probability is
# almost non-existent.
