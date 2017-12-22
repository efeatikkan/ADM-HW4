<b>1: PROCEDURES IN EXERCISE 1</b>

<b>1.1</b>: Full or/and reduced file is loaded

<b>1.2</b>: Format of the data is changed. A dictionary is created where the key is the author_id and the
value is the publication id.

<b>1.3</b>: From using this dictionary, an undirected graph has been created using networkx library where
each node is represented by the author id, and authors that share a publiaction are connected by
en edge. 

<b>1.4</b>: Weight is given to the edges according to jaccard similarity between publications of
the authors.

<b>2: PROCEDURES IN EXERCISE 2</b>

<b>2.1</b>: A conference dictionary is created where each conference id represents the keys and 
the list of authors id who involved in that conference is the value.

<b>2.2</b>: Given a specific conference id a subgraph is created as follow:

	-Using the conference dictionary, author ids of the authors who attended are identified
	
	-Using networkx subgraph function we created a subgraph induced by list of authors id

<b>2.3</b>: Using this subgraph and necessary functions from networkx, some measures(degree,
closeness and betweeness) are calculated and visualized using histograms.

<b>2.4</b>: Given a graph, author id and an integer(d), a subgraph which contains the nodes that are
at most d hop-distance far from given auther id is created and viusalized.(graph_distance function)


<b>3: FUNCTIONS IN modules.py</b>

In the modules.py following functions are written:

<b>3.1: <i>_open_file(filename)</i></b><br/>
This function takes in input a filename (as a string, in our case a
json file) and it opens the file.

<b>3.2: <i>_get_publications(pub_dict)</i></b><br/>
Using the loaded file, this function returns a dictionary with  key =  author_id and value = list of publication_ids.

<b>3.3: <i>_jaccard_similarity(pubs_author_1, pubs_author_2)</i></b><br/>
The function takes as input publications of two given authors and returns their jaccard similarity.

<b>3.4: <i>_get_authors_graph(file, pubs)</i></b><br/>
The function takes as input the original file (.json) and the publication dictionary (output of get_publication function, see above).
An undirected graph is built where each node is an author id and edges are added id two authors share a publication.
Then the weigths are added using 1 - jaccard similarity considering the set of publication of each author.    

<b>3.5: <i>create_authors_graph(filename)</i></b><br/> 
This function takes input the file (json.) and creates a graph using mainly get_publications, _jaccard_similarity and _get_authors_graph functions.

<b>3.6: <i>create_conferences_dictionary(filename)</i></b><br/>
This function takes input the file (.json), and its used to create the conference_dictionary which will be used in subgraph task.

<b>3.7: <i>subgraph(authors_graph, conferences_dict, conference_id)</i></b><br/> 
This function takes input the file (json.), conferences_dict(created by create_conferences_dictionary function) and 
a conference id. It returns a subgraph where nodes a authors id who participated to the given conference. 

<b>3.8: <i>get_centralities(subgraph)</i></b><br/>
This function takes in input a graph and returns a tuple with
	 3 items:
    - the first item is the degree of the graph
    - the second item is the betweenness of the graph
    - the third item is the closeness of the graph

<b>3.9: <i>graph_distance(graph, author_id, d)</i></b><br/>
This function creates a subgraph as described in c_4 point. Breadth First Search(BFS) is implemented to visit efficiently  all nodes which are at most at distance d.

<b>3.10: <i>visualize_graph(graph, node_labels = True, edge_labels = True, root_node = None)</i></b><br/>
This function draws the graph.

<b>3.11: <i>visualize_histogram(values_list, title)</i></b><br/>
This function draws the histogram (usefull for plotting the degree, closness and betweness histograms)

<b>3.12: <i>shortest_path(graph, source, target)</i></b><br/>
This function takes in input a graph, a source node, a target node and 
returns the minimum sum of the weigths for the path from the source node to the target node (Dijkstra algorithm)

<b>3.13: <i>group_number(graph, nodes_set)</i></b><br/>
This function takes in input a graph, a set/list of nodes and returns the  dictionary of the shortest paths which contains all 
the nodes of the graph as keys and the shortest path from u to the other nodes of the graph as values, for each u in nodes_set
  
