looksLikeWitch(connie).
dressedAsWitch(connie).
hasAWart(connie).
turnedManIntoNewt(connie).
burns(X):- isMadeOfWood(X).
isMadeOfWood(X):- floats(X).
floats(X):- sameWeightAsDuck(X).
sameWeightAsDuck(connie).

witch(X):- looksLikeWitch(X), dressedAsWitch(X), hasAWart(X), turnedManIntoNewt(X), burns(X).
