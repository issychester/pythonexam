Alchemist
==========

Alchemist is a program which uses a file representing two shelves to see which substances react. The shelf can hold any number, or multiples copies, of a substance. A substance can only react with its anti version, for example {a} can only react with anti{a}. Substances on the lower shelf are tried in order to see if they can react with randomly selected substances from the upper shelf. If they can react, they are removed from the shelf and the process continues to find all the substances which can react. This program will show you what substances are left on each shelf or the number of reactions. 

Usage:
    
Invoke the program with 'abracadabra <yaml file> <optional --reactions>' 

The file is yaml with 2 shelves named 'lower' and 'upper' and the substances listed. There can only be 2 shelves and they must be named 'lower' and 'upper'. The names of the shelves or substances are case-insensitive. Empty shelves are allowed but antianti products do not exist. If there are 2 or more of the same substance on a shelf and it is reactable, one of the products is selected randomly, removed from the shelf and used in the reaction. 

If the optional '--reactions' or '--r' is added, the number of reactions is given as the output; if not, the substances left on the shelves are given.

Example: 
alchemist.yml file: 
    lower:
    - involucrata
    - serpyllum
    - antifirma
    - antieycholra
    - psittaccina
    upper:
    - alcea
    - antiinvolucrata
    - campanula
    - serpyllum
    - antiinvolucrata
    - firma

with 'abracadabra alchemist.yml'
output: 
    lower: [serpyllum, antieycholra, psittaccina]
    upper: [alcea, antiinvolucrata, campanula, serpyllum]

with 'abracadabra alchemist.yml --reactions' or 'abracadabra alchemist.yml --r'
output:
    2