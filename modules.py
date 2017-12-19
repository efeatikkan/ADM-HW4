import json
import networkx as nx
import matplotlib.pyplot as plt
import heapq

'''---FUNCTIONS FOR PROBLEM 1---'''

def _open_file(filename):
    return json.loads(open(filename, 'r').read())

def _get_publications(pub_dict):
    '''This function takes in input a list and returns a dictionary with:
    key = author's id
    value = a list which contains the ids of the publications'''
    pubs = {}
    for publication in pub_dict:
        for author in publication['authors']:
            try:
                pubs[author['author_id']].append(publication['id_publication_int'])
            except:
                pubs[author['author_id']] = [publication['id_publication_int']]
    return pubs

def _jaccard_similarity(pubs_author_1, pubs_author_2):
    '''This function takes in input 2 lists and return their jaccard similarity coefficient'''
    intersection = set(pubs_author_1).intersection(set(pubs_author_2))
    union = set(pubs_author_1).union(set(pubs_author_2))
    return len(intersection) / len(union)

def _get_authors_graph(file, pubs):
    '''This function takes in input the dictionary of publications and returns a graph whose nodes are authors.
    Two nodes are connected if they share, at least, one publication. Each edge is weighted according to the following
    formula:
        w(a1, a2) = 1 - J(p1, p2)
    where J(p1, p2) is the Jaccard similarity between p1 and p2
    and p1 and p2 are the set of publication of the authors a1 and a2'''
    g = nx.Graph()
    for publication in file:
        for i in range(len(publication['authors'])):
            g.add_node(publication['authors'][i]['author_id'])
            for j in range(i + 1, len(publication['authors'])):
                g.add_node(publication['authors'][j]['author_id'])
                js = _jaccard_similarity(pubs[publication['authors'][i]['author_id']], pubs[publication['authors'][j]['author_id']])
                g.add_edge(publication['authors'][i]['author_id'], publication['authors'][j]['author_id'], weight = 1 - js)
    return g

def create_authors_graph(filename):
    '''This function takes in input a JSON file (as string) and returns the graph defined in PROBLEM 1'''
    print('Loading ' + filename + '...')
    publications_dict = _open_file(filename)
    print('Creating the dictionary of publications...')
    publications = _get_publications(publications_dict)
    print('Creating the authors graph...')
    g = _get_authors_graph(publications_dict, publications)
    print('Graph created!')
    return g

'''---FUNCTIONS FOR PROBLEM 2---'''

def create_conferences_dictionary(filename):
    '''This function takes in input a JSON file (as string) and returns the dictionary of conferences with:
        key = conference_id
        value = set(author_id)'''
    print('Loading ' + filename + '...')
    publications_dict = _open_file(filename)
    print('Creating the dictionary of conferences...')
    conferences = {}
    for publication in publications_dict:
        for author in publication['authors']:
            try:
                conferences[publication['id_conference_int']].update([author['author_id']])
            except:
                conferences[publication['id_conference_int']] = {author['author_id']}
    print('Dictionary created!')
    return conferences

def subgraph(authors_graph, conferences_dict, conference_id):
    '''This function takes in input the graph of the authors, the dictionary of conferences, a conference id and
    returns the subgraph induced by the set of authors who published at the conference id'''
    return authors_graph.subgraph(list(conferences_dict[conference_id]))

def get_centralities(subgraph):
    '''This function takes in input a graph and returns a tuple with 3 items:
    - the first item is the degree of the graph
    - the second item is the betweenness of the graph
    - the third item is the closeness of the graph'''
    return list(nx.degree(subgraph)), list(nx.betweenness_centrality(subgraph).values()), list(nx.closeness_centrality(subgraph).values())

def graph_distance(graph, author_id, d):
    '''This function takes in input the graph of the authors, an author id, an integer d and returns a subgraph produced
    by a Breadth First Search (BFS) visit limited to d'''
    subgraph = nx.Graph()
    q = [author_id]
    level = 1
    visited = {author_id : True}
    while level <= d:
        tmpq = []
        while len(q) > 0:
            node = q.pop(0)
            for adjacent_node in graph[node]:
                #if adjacent_node is already visited then do nothing
                #otherwhise mark the node as visited and append adjacent_node to tmpq
                try:
                    if visited[adjacent_node]:
                        pass
                except:
                    visited[adjacent_node] = True
                    tmpq.append(adjacent_node)
                subgraph.add_edge(node, adjacent_node, weight = graph[node][adjacent_node]['weight'])
        level += 1
        q = tmpq
    #connect the frontier nodes
    for frontier_node in q:
        for node in graph[frontier_node]:
            #if node is visited then add an edge that connects frontier_node to node
            #otherwhise do nothing
            try:
                if visited[node]:
                    subgraph.add_edge(frontier_node, node, weight = graph[frontier_node][node]['weight'])
            except:
                continue
    return subgraph

def visualize_graph(graph, node_labels = True, edge_labels = True):
    '''This function draws the graph'''
    plt.clf()
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels = node_labels)
    if edge_labels:
        nx.draw_networkx_edge_labels(graph, pos, edge_labels = nx.get_edge_attributes(graph, 'weight'))
    plt.show()

def visualize_histogram(values_list, title):
    '''This function draws the histogram'''
    plt.clf()
    plt.figure()
    plt.hist(values_list)
    plt.title(title)
    plt.show()

'''---FUNCTIONS FOR PROBLEM 3---'''

def shortest_path(graph, source, target):
    '''This function takes in input a graph, a source node, a target node and returns the sum of the weigths that
    minimizes the path from the source node to the target node'''
    # since the graph is undirected it is better to start from the node that has the minimum degree
    # between the source node and the target node
    if len(graph[target]) < len(graph[source]):
        tmp = source
        source = target
        target = tmp
    # the heap of the distances contains the pairs (node_distance, node)
    distance_heap = []
    visited = {}
    heapq.heappush(distance_heap, (0, source))
    while len(distance_heap) > 0:
        node_distance, node = heapq.heappop(distance_heap)
        # if the target node has been found then return his minimum distance
        if node == target:
            return node_distance
        try:
            if visited[node]:
                continue
        except:
            visited[node] = True
        for adjacent_node in graph[node]:
            try:
                if visited[adjacent_node]:
                    continue
            except:
                distance = node_distance + graph[node][adjacent_node]['weight']
                heapq.heappush(distance_heap, (distance, adjacent_node))
    print('There is not a path from', source, 'to', target)
    return float('inf')

def group_number(graph, source, nodes_set):
    to_find = {}
    distance = {}
    for node in nodes_set:
        to_find[node] = True
        distance[node] = float('inf')
    distance_heap = []
    visited = {}
    heapq.heappush(distance_heap, (0, source))
    while len(distance_heap) > 0:
        node_distance, node = heapq.heappop(distance_heap)
        try:
            if to_find[node]:
                distance[node] = node_distance
                del to_find[node]
                print('Found', node, node_distance)
                if len(to_find) == 0:
                    break
        except:
            pass
        try:
            if visited[node]:
                continue
        except:
            visited[node] = True
        for adjacent_node in graph[node]:
            try:
                if visited[adjacent_node]:
                    continue
            except:
                dist = node_distance + graph[node][adjacent_node]['weight']
                heapq.heappush(distance_heap, (dist, adjacent_node))
    return distance
