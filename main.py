# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:50:27 2017

@author: Efe
"""

import modules as m
import networkx as nx
import heapq

#Question 1 - Creating a graph using given input file
print('Question1-Graph Creation')
inn1=input('Enter the file name(.json) = ')
authors_graph = m.create_authors_graph(str(inn1))

#Question 2 - 
print('\n\nQuestion2-Subgraph Creation and Centrailty Measures')
#4634
inn2=input('Id of the conference? = ')

confs_dict = m.create_conferences_dictionary(str(inn1))
subgraph=m.subgraph(authors_graph,confs_dict, int(inn2)) #Subgraph is created
print('Subgraph is saved as "subgraph" !')
m.visualize_graph(subgraph) 
degree, betweenness, closeness=m.get_centralities(subgraph) #Getting 3 centraility measures

m.visualize_histogram(degree, 'Degrees Histogram')
m.visualize_histogram(betweenness, 'Betweenness Histogram')
m.visualize_histogram(closeness, 'Closeness Histogram')
print('Centraility measures aree also saaved as "degree","betweenness" and "closeness" lists !')


#Question 2.b
print('\n\nQuestion 2b- Hop distance graph')
inn3=input('Author Id? = ')
inn4=input('Distance "d"? = ')
#256176 , 2
hop_graph=m.graph_distance(authors_graph, int(inn3), int(inn4))
print('Hop distance graph is saved as "hop_graph" !')
m.visualize_graph(hop_graph)

#Question 3.a
print('\n\nQuestion 3a- Shortest distance between 2 nodes!')
inn5=input('Source Node? = ')
inn6=input('Target node? = ')
#256176
#317546
ll=m.shortest_path(authors_graph, int(inn5), int(inn6)) #Shortest distance between 256176 and 317546
print('Shortest Distance: ',ll)
#Question 3.b
print('\n\nQuestion 3b- Given a subset of nodes, Groupnumber of all nodes are returned')
inn7=input('Subset of nodes?(seperated by space) = ')
inn7=list(map(int,inn7.split()))
#[256176,317546]
groups=m.group_number(authors_graph, inn7)
#print(groups)
print('GroupNumber is calculated for each node and saved to "groups" dictionary!')

