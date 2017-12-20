# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:50:27 2017

@author: Efe
"""

import modules as m
import networkx as nx
import heapq

#Question 1 - Creating a graph using given input file
authors_graph = m.create_authors_graph('reduced_dblp.json')

#Question 2 - 
confs_dict = m.create_conferences_dictionary('reduced_dblp.json')
subgraph=m.subgraph(authors_graph,confs_dict, 3345) #Subgraph is created
m.visualize_graph(subgraph) 
degree, betweenness, closeness=m.get_centralities(subgraph) #Getting 3 centraility measures
m.visualize_histogram(degree, 'Degrees Histogram')
m.visualize_histogram(betweenness, 'Betweenness Histogram')
m.visualize_histogram(closeness, 'Closeness Histogram')

#Question 2.b
hop_graph=m.graph_distance(authors_graph, 256176, 2)
m.visualize_graph(hop_graph)

#Question 3.a
ll=m.shortest_path(authors_graph, 256176, 317546) #Shortest distance between 256176 and 317546

#Question 3.b
groups=m.group_number(authors_graph, [256176,317546]) 

