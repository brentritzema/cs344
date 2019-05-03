% Do these exercises from LPN!.
% Exercise 3.2
directlyIn(olga, katarina).
directlyIn(natasha, olga).
directlyIn(irina, natasha).

in(X,Y):- directlyIn(X,Y).
in(X,Y):- directlyIn(X,Z),
            in(Z,Y).
% Exercise 4.5
tran(eins,one). 
tran(zwei,two). 
tran(drei,three). 
tran(vier,four). 
tran(fuenf,five). 
tran(sechs,six). 
tran(sieben,seven). 
tran(acht,eight). 
tran(neun,nine).

listtran([],[]).
listtran([X|Ta],[Y|Tb]):- tran(X,Y),
                        listtran(Ta, Tb).

% Does Prolog implement a version of generalized modus ponens (i.e., modus ponens with variables and instatiation)? If so, demonstrate how it's done; if not, explain why not. If it doesn't, can you implement one? Why or why not?
% It does support it. See below.
man(socrates).
mortal(X):- man(X).

% Be sure that you can explain how you built your system and how Prolog does recursion.
% I built my system by following the examples of recursion, so I made sure I had some sort of base case and an optoion to recurse if needed. Prolog does recursion by continually trying to instantiate and retry the function until it finds an answer.


