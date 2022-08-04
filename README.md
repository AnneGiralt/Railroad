# Railroad

This repository is a exercise for beginner in Python. The purpose is to practice oriented object programming, dictionary handling and simple test realization. The subject here is about constructing a virtual railroad network and give some information to a potential customer about traveling such as length of a given traject, all possibles trajects between two cities or the minimal length between two cities.

A railroad is given as a oriented graph. Vertices represent towns and edges represent a railroad between two town (in an unique way). A railroad is given as a string with the two cities and the length. As an example : 'AB5' is a railroad from the town A to the town B of length 5. A railroad network is given as concatenation of railroad separate by a space and comma. As an example 'AB4, AC3, BD8' is a valid input as railroad network. We suppose that there can't be any loop, and he network can have severals railroad from the same departure and arrival towns, possibly with different lengths.

The exercise success will be validate by using unittest, checking for a list of questions from a potential passenger.

To run the test :
```
python -m unittest test.py
```
