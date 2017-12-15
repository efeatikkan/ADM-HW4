PROCEDURES IN EXERCISE 1

a) Full or/and reduced file is loaded

b) Format of the data is changed. A dictionary is created where the key is the author_id and the
value is the publication id.

c) From using this dictionary, an undirected graph has been created using networkx library where
each node is represented by the author id, and authors that share a publiaction are connected by
en edge. 

d) Weight is given to the edges according to jaccard similarity between publications of
the authors.

PROCEDURES IN EXERCISE 2

a_2) A conference dictionary is created where eahc conference id represents the keys and 
the list of authors id who involved in that conference is the value.

b_2) Given a specific conference id a subgraph is created as follow:
	-Using the conference dictionary, author ids of the authors who attended are identified
	-Using networkx subgraph function we created a subgraph induced by list of authors id

c_3) Using this subgraph and necessary functions from networkx, some measures(degree,
closeness and betweeness) are calculated and visualized using histograms.

c_4) Given a graph, author id and an integer(d), a subgraph which contains the nodes that are
at most d hop-distance far from given auther id is created and viusalized.(graph_distance function)


FUNCTIONS IN MODULE.PY

In the modules.py following functions are written:

1) _open_file(filename) : this function takes in input a filename (as a string, in our case a
json file) and it opens the file.

2) _get_publications(pub_dict): using the loaded file, this function returns a dictionary with 
   key =  author_id and value = list of publication_ids.

3) _jaccard_similarity(pubs_author_1, pubs_author_2): it takes as input publications of two
   given authors and returns their jaccard similarity.

4) _get_authors_graph(file, pubs): the function takes as input the original file (.json) and
 the publication dictionary (output of get_publication function, see above). An undirected graph
is built where each node is an author id and edges are added id two authors share a publication.
Then the weigths are added using 1-jaccard similarity considering the set of publication of each
author.    

5) create_authors_graph(filename): This function takes input the file (json.) and creates
a graph using mainly get_publications,_jaccard_similarity and _get_authors_graph functions.

6) create_conferences_dictionary(filename): Takes input the file (.json), and its used
to create the conference_dictionary which will be used in subgraph task.

--
7)subgraph(authors_graph, conferences_dict, conference_id): This function takes input
the file (json.), conferences_dict(created by create_conferences_dictionary function) and 
a conference id. It returns a subgraph where nodes a authors id who participated to
the given conference. 

8)get_centralities(subgraph): This function takes in input a graph and returns a tuple with
	 3 items:
    - the first item is the degree of the graph
    - the second item is the betweenness of the graph
    - the third item is the closeness of the graph

9) graph_distance(graph, author_id, d): Creates a subgraph as described in c_4 point. Breadth
First Search(BFS) is implemented to visit efficiently  all nodes which are at most at distance d.

10)visualize_graph(graph, node_labels = True, edge_labels = True):This function draws the graph.

11)visualize_histogram(values_list, title): this function draws the histogram (usefull for plotting
 the degree, closness and betweness histograms)

12) shortest_dist(graph, source, target): the function takes in input the source node and
 target node (for default it's Aris' id), this function calculates the weight
    of the shortest path using Disjkstra algorithm and heapqueue).

13)groups(graph,I): the function has as input the authors graph and the set of nodes I. For each
node in the graph it computes the GroupNumber and it returns a dictionary where the key is each
node in the graph and the value is a tuple where the first element number is the Group number 
and the second one is the closest  node that belongs to set I.

14)shortest_path(graph, source): this function take in input the authors graph and a source node. 
It computes the shortest path between the source and all the nodes in the graph. This function 
uses other two functions to operate:
	- _search_node(heap, node): this function returns the position of the node in the
	 			    heap.  
	- _decrease(heap, node, distance): this function rearrange the heap. If node_distance of
					   the node is smaller than the distance of the parent node,
				           then the node with the parent node swaps in place in the
					   heap, until the parent node is smaller than the node or
    					   the root node as been reached.

  
