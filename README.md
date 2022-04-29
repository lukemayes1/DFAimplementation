# DFAimplementation
A simple program that implements a deterministic finite automaton.


 
## Description
This program will simulate the output of a DFA given an input string. The DFA is defined in a file that is then read by the program.
<img width="876" alt="33966" src="https://user-images.githubusercontent.com/15059155/165875295-115c20c2-3edd-4ef0-adbe-13f5ac22fdcf.png">



## Input File Format
Below is an example of what an input file for a DFA will look like.
```
ab        ; the alphabet of the DFA
2         ; number of states to read
1 0       ; state information
0 1       ; state inofrmation
0         ; the accept state
```
DFA that is defined in the file:
```{w over {a,b}* | w has at least 2 consecutive a's}```

![image](https://user-images.githubusercontent.com/15059155/165875985-cfa276a5-f412-4b37-b9c6-0a73ef7ec0fe.png)



## Dependencies
1. [colorama](https://pypi.org/project/colorama/)
      - ```pip instll colorama```
      or
      - ```conda install -c anaconda colorama```
3. [colorterm](https://colorterm.readthedocs.io/en/latest/)
      - ```pip install colorterm```
