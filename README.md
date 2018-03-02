# Rail_road

This is a object oriented project about railway. The railway is a wheighted oriented graph. Every vertex is associated to a town in the railway, and an edge between the towns A and B represents a road from A to B. The associated weight is the length of this road. The railway is given as a string concatenation of differents paths. For example an input railway could be : 'AB4 AC3 BD8'. In this case there is four towns A, B, C and D with three roads A to B, A to C, and B to D, with respective lengths 4,3 and 8.

The fist thing we do is to construct a graph structure from the input string. A graph here is given by a dictionary of dictionary. In the firt dictionary each key is a departure town A and the value is a dictionary. A key of this dictionary associated to the town A is also a town, B. In this case, there exist a road between A and B. The value associated the key B is the length of the path AB.

The firt principal method of the Railroad class calculates the length of a path given as a string as for example 'A-B-C' if it exists. The two next methods give all possible paths between two given towns with a fixed or maximal number of stops. The last method gives all possible routes between two given town with a maximal length.

The are two test files. Testbuild.py check if the convertion of the railway from string to graph is well realised, and test.py tests all methods of the railroad class.
