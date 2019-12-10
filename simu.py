import numpy as np
import matplotlib.pyplot as plt
import networkx as nx 
import time
import networkx as nx 
  
G = nx.read_weighted_edgelist('edge_list.txt', delimiter =" ") 
  
population = { 
        'T1' : 100, 
        'T2' : 100, 
        'T3' : 100, 
        'T4' : 100, 
        'T5' : 100, 
        'T6' : 100, 
        'T7' : 100, 
        'T8' : 100, 
        'T9' : 100, 
        'T10' : 100, 
        'T11' : 100, 
        'T12' : 100, 
        'T13' : 100, 
        'T14' : 100
        } 
  
# We have to set the population attribute for each of the 14 nodes 
for i in list(G.nodes()): 
    G.nodes[i]['population'] = population[i] 
  
nx.draw_networkx(G, with_label = True) 
# This line allows us to visualize the Graph

##count = 0
#while count < 10 : 100*count+
for i in list(G.nodes()): 
    G.nodes[i]['population'] = population[i] 

# fixing the size of the figure 
plt.figure(figsize =(10, 7)) 

node_color = [G.degree(v) for v in G] 
# node colour is a list of degrees of nodes 

node_size = [1.5 * nx.get_node_attributes(G, 'population')[v] for v in G] 
# size of node is a list of population of cities 

edge_width = [0.0015 * G[u][v]['weight'] for u, v in G.edges()] 
# width of edge is a list of weight of edges 

nx.draw_networkx(G, node_size = node_size,  
                    node_color = node_color, alpha = 0.7, 
                    with_labels = True, width = edge_width, 
                    edge_color ='.4', cmap = plt.cm.Blues) 

plt.axis('off') 
plt.tight_layout(); 
#count+=1
#time.sleep(3)