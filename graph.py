
class RailRoad:

	def __init__(self):
		self.graph ={}

	# Method to check if the string of graph have a correct form 
	def is_valid(self,string_railroad):

		try : 
			list_edges = string_railroad.split(", ") 
		except SyntaxError:
			print('The input graph must be a string')
			return False

		for elt in list_edges:
			if not (elt[0:2].isalpha()  and elt[0:2].isupper() and elt[2:].isdigit()):
				print('The input graph format is invalid. Example of correct string : "AB5, AC56, BD6, CT4" ')
				return False

		return True




	# Method to initialise self.graph
	def build(self,string_railroad):

		if not self.is_valid(string_railroad):
			print("The graph couldn't be filled")
		else:
			list_string_node = string_railroad.split(", ")
			for e in list_string_node:
				self.addroute(e)

	# Fill self.graph edge by edge
	def addroute(self,edge):
		dep = edge[0]
		arr = edge[1]
		dist = int(edge[2:])

		# An edge from a dep is a dict :
		my_road = {arr : dist}

		# I fill my graph depending if dep is already or not in my graph:
		if dep in self.graph :
			self.graph[dep].update(my_road)
		else:
			self.graph.update({dep : my_road})

	# Compute distance traveled for a given path (string of type 'A-B-C') 
	def distance(self, path_str):
		path_list = path_str.split('-')

		if len(path_list)== 0:
			return 0
		
		# Initialise actual town and next town, l is the distance traveled:
		l = 0
		actual_town = path_list[0]
		next_town =path_list[1]
		i=2

		for i in range(len(path_list)-1):
			actual_town = path_list[i]
			next_town = path_list[i+1]

			if next_town not in self.graph[actual_town]:
				return 'NO SUCH ROUTE'
			else:
				l+= self.graph[actual_town][next_town]
		return l

	# Method who gives all possibles path from the town dep whith maximum stops stops.
	# This methos essentially initialise a dictionary to give it as argument in the recursive method search_path .
	# Carreful the path {dep : 0} is given
	def possibles(self, dep, stops):
		dico_paths = {}
		self.search_paths( '', dep, 0, stops, dico_paths)
		return dico_paths

	# Method who recursivly browse in self.graph to fill the dictionary dico
	# It take as argument a dictionary, dico, of all path already found, a particular path to prolonguate by the town
	# A number of stops autorized. 
	def search_paths(self, path, town, length, stops, dico):
		#Initialisation :
		if stops == -1: 
			pass
		else :
			# I add my town to my path and add it to my dico:
			new_path = path + town 
			dico.update({new_path: length})

			#for every accessible town from where I am I call recursively my method with stops-1:
			for key,value in self.graph[town].items():
				self.search_paths(new_path, key, length + value, stops-1, dico)


	# Compute all possible path from a town de to a town arr with a maximal number of stops:
	# Carreful the path {dep : 0} is given
	def depart_arrival(self, dep, arr, stops):
		dico = self.possibles(dep, stops)
		result ={}

		for key, value in dico.items():
			if key[-1] == arr:
				result.update({key: value})
		return result

	# Compute all possibles path from a town de to a town arr with an exact number of stops:
	# Carreful the path {dep : 0} is given if dep == arr
	def dep_arr_stops(self,dep,arr, stops):
		dico = self.depart_arrival(dep,arr,stops)
		result = {}
		for key, value in dico.items():
			if len(key) == stops +1:
				result.update({key: value})
		return result

	# Compute the minimal distance between two towns (more than 0):
	def dist_min(self, dep, arr):
		dico = self.depart_arrival(dep,arr,10)
		if dep == arr :
			dico.pop(dep)

		list_dist = list(dico.values())
		list_dist.sort()
		 
		if list_dist == []:
			return 'NO SUCH ROUTE'
		else:
			return list_dist[0]

	# Compute the number of path betwenn dep and arr with at most max_length length.
	# Carrefull here we choose an arbitrary max numbre of stop, 10, it can be a good idea to change it depending of the length of the graph.
	def nb_chemin_max(self, dep, arr,max_length):
		dico = self.depart_arrival(dep,arr,10)

		list_dist = list(dico.values())
		list_max = [nb for nb in list_dist if nb < max_length]

		return len(list_max)






