% a.From LPN!
%    Exercise 1.4 - Explain why you built the representations as you did.
%        killer(butch)
%        married(mia, marsellus)
%        dead(zed)
%        kills(marsellus, X):- footmassage(X, mia)
%        loves(mia, X):- goodDancer(X)
%        eats(Jules, X):- nutritious(X); tasty(X)
%        
%        I built them in this way because I took verb functors to be read as arg1 verbs arg2. For example, Mia loves X or X footmassages Mia.
%
%    Exercise 1.5 - Explain how Prolog comes up with its answers.
%       wizard(ron). % Prolog consults the dictionary, returns true because the fact is stated
%       witch(ron). % Prolog returns an error because witch is not defined
%       wizard(hermione). % returns false, because even with the extra rule hermione doesnt have a broom and wand
%       witch(hermione). % returns an error because witch is not defined
%       wizard(harry). % returns true because it notices that harry is a quidditch player, and therefore has a broom, has a wand, and therefore is a wizard
%       wizard(Y). % returns ron and harry, ron is stated as fact, harry is inferred as above
%       witch(Y). % returns an error, not defined
%        
%
% b. Consider the well-known modus ponens. Does Prolog implement a version of modus ponens in propositional logic form? If so, demonstrate how it's done; if not, explain why not. If it doesn't, can you implement one? Why or why not?
%   It does implement it, because if a fact is stated, and a rule is only true if that fact is stated, it can infer the fact made true by the rule being true is now true. For example:
%   listens2Music(mia).
%   playsAirGuitar(mia):- listens2Music(mia).
%   ?- playsAirGuitar(mia) returns true
%
% c. Prolog supports representations in the form of Horn clauses. Compare and contrast the representational power they provide with that of propositional logic.
%   Prolog does support representation in the form of Horn clauses because they can allow for greater inference power with first-order logic rather than just propositional logic.
%
% d. Logical implementations generally distinguish the basic operations of TELL and ASK. Does Prolog support this distinction? If so, how; if not, why not?
%   Yes, knowledge bases are all about the TELL while queries are all about ASK.
