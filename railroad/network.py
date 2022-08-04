# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

class RailroadNetwork:
    """
    This class represent a railroad network, witch is a oriented graph. The
    network is given as a string input. This string is a concatenation of
    different railroad (ex : "AB5, AC56, BD6, CT4").
    The graph structure of the network will be store in the graph attribute.
    We choose to store this graph structure as a dictionary of dictionary.
    Every town with at least on outgoing road will be a key in this
    dictionary. Value for this town will be a dictionary in which each key
    is an arrival town and the associated value is the length.

    Here the dictionary structure of the network given by the above string
    example :
    {'A' : {'B' : 5;
            'C' : 56;
           };
     'B' : {'D' : 6};
     'C' : {'T' : 4};
    }
    """

    def __init__(self):
        self.graph ={}


    def is_valid(self,string_network):
        """
        Method to check if the input string have a correct form.
        """

        try :
            nodes = string_network.split(", ")
        except SyntaxError:
            print('The input graph must be a string')
            return False

        for node in nodes:
            if not (node[0:2].isalpha() and
               node[0:2].isupper()      and
               node[2:].isdigit()):

                print('The input railroad network have invalid format. Example\
                     of correct string : "AB5, AC56, BD6, CT4" ')
                return False

        return True


    def build(self,string_network):
        """
        Method to initialise self.graph.
        """

        if not self.is_valid(string_network):
            print("The graph couldn't be initialized since input string network is invalid.")
        else:
            tracks = string_network.split(", ")
            for track in tracks:
                self.add_track(track)


    def add_track(self,track):
        """Fill the graph attribute node by node."""

        dep = track[0]
        arr = track[1]
        dist = int(track[2:])

        # The edge dictionary.
        new_road = {arr : dist}

        # I fill my graph depending if dep is already in my graph or not.
        if dep in self.graph :
            self.graph[dep].update(new_road)
        else:
            self.graph.update({dep : new_road})


    def distance(self, path_str):
        """Compute distance of given path which could cross several roads. The
        path is given as a string of type 'A-B-C'."""
        towns = path_str.split('-')

        if len(towns)== 0:
            return 0

        # Initialise actual town, next town and dist.
        dist = 0

        for i in range(len(towns)-1):
            actual_town = towns[i]
            next_town = towns[i+1]

            if next_town not in self.graph[actual_town]:
                return 'NO SUCH ROUTE'

            dist+= self.graph[actual_town][next_town]
        return dist


    def possible_paths(self, dep, max_stops):
        """
        This method gives all possible paths starting from the town dep with a
        maximal number of stops. The result is a dictionary where values are
        paths and associated key is the length of this path.
        """

        dict_paths = {}
        self.search_paths( '', dep, 0, max_stops, dict_paths)
        return dict_paths


    def search_paths(self, path, town, length, max_stops, dict_paths):
        """
        Method who recursively browse in the graph and fill the dictionary
        dict_paths.
        """

        # Initialization :
        if max_stops == -1:
            pass
        else :
            new_path = path + town
            dict_paths.update({new_path: length})

            # For every reachable new town we recursively run the method.
            for new_town, track_length in self.graph[town].items():
                self.search_paths(new_path, new_town, length + track_length,
                                  max_stops - 1, dict_paths)


    def depart_arrival(self, dep, arr, max_stops):
        """
        Compute all possible paths from the town dep to the town arr with a maximal
        number of stops.
        """
        all_paths = self.possible_paths(dep, max_stops)
        dep_arr_paths = {path:length for path, length in all_paths.items() if path[-1]== arr}
        return dep_arr_paths


    def dep_arr_stops(self, dep, arr, num_stops):
        """
        Compute all possibles path from the town dep to the town arr with an exact
        number of stops.
        """

        dep_arr_paths = self.depart_arrival(dep, arr, num_stops)
        exact_stops_paths = {path:length for path, length in dep_arr_paths.items()
                             if len(path) == num_stops +1}
        return exact_stops_paths


    def dist_min(self, dep, arr, max_stops):
        """
        Compute the minimal distance between two towns. The departure and
        arrival town could be the same but the path must take at least one
        track.
        """

        dep_arr_paths = self.depart_arrival(dep,arr,max_stops)
        if dep == arr :
            dep_arr_paths.pop(dep)

        list_dist = list(dep_arr_paths.values())
        list_dist.sort()

        if not list_dist:
            return 'NO SUCH ROUTE'
        return list_dist[0]


    def count_paths(self, dep, arr,max_length,max_stops):
        """
        Compute the number of path between dep and arr with at most max_length length.
        """

        dep_arr_paths = self.depart_arrival(dep,arr,max_stops)

        list_dist = list(dep_arr_paths.values())
        list_max = [nb for nb in list_dist if nb < max_length]

        return len(list_max)
