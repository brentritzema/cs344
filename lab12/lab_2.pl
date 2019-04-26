% a. From LPN!
%   Exercise 2.1, questions 1, 2, 8, 9, 14 - Give the necessary instantiations.
%       1. No instantiations, they are equal constants
%       2. Do not unify, different constants
%       8. If X is instantiated to bread, they unify
%       9. If X is instantiated to sausage, and Y to bread, they are unified
%       14. These cant be unified because one variable cant take on both food(bread) and drink(beer)
%
%   Exercise 2.2 - Explain how Prolog does its unification and reasoning. If you have issues getting the results youd expect, are there things you can do to game the system?
house_elf(dobby). 
witch(hermione). 
witch('McGonagall'). 
witch(rita_skeeter). 
magic(X):-  house_elf(X). 
magic(X):-  wizard(X). 
magic(X):-  witch(X).
% ?-  magic(house_elf). 
% ?-  wizard(harry).
% ?-  magic(wizard).
% ?-  magic('McGonagall').
% ?-  magic(Hermione).
%
%   Prolog does a sort of search for unification and reasoning. None of the queries, except the last one, are satisfied because there aren't variables passed in which can be instantiated to be satisfied. You can use variables to game the system, it will instantiate for you.
%
% b. Does inference in propositional logic use unification? Why or why not?
%   I don't believe so, it is a lower level idea than unification so it wouldn't make sense to use it. Unification is in the realm of FOL, not propositional logic.   
%
% c. Does Prolog inferencing use resolution? Why or why not?
%   It seems that when trying to inference using unification, in the area of FOL, resolution would not be used since that's a purely propositional logic method.

