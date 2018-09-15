import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def histoplot(L,bins,x_ticks,size=[13,6],title="",stacked=True,ranks=[20,50,80]):
    

    fig = plt.figure()
    fig.set_size_inches(size[0], size[1])
    H = plt.hist(L,bins=bins,stacked=stacked)
    plt.xticks(x_ticks)
    plt.title(title,size=20)

    if ranks == []:
        pass
    else:
        percentiles = np.percentile(L,ranks)
        for x in percentiles:
            plt.axvline(x,color='black',linewidth=3)
        percentile_legend = []
        for i,j in zip([str(r) for r in ranks],percentiles):
             percentile_legend.append("{}th Percentile: {:.1f}".format(i,j))
        plt.legend(percentile_legend)
    
    return H


def decisionTreeStruct(model):

    n_nodes = model.tree_.node_count
    children_left = model.tree_.children_left
    children_right = model.tree_.children_right
    feature = model.tree_.feature
    threshold = model.tree_.threshold
    
    node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
    is_leaves = np.zeros(shape=n_nodes, dtype=bool)
    stack = [(0, -1)]  # seed is the root node id and its parent depth
    while len(stack) > 0:
        node_id, parent_depth = stack.pop()
        node_depth[node_id] = parent_depth + 1
    
        # If we have a test node
        if (children_left[node_id] != children_right[node_id]):
            stack.append((children_left[node_id], parent_depth + 1))
            stack.append((children_right[node_id], parent_depth + 1))
        else:
            is_leaves[node_id] = True
    
    print("The binary tree structure has %s nodes and has "
          "the following tree structure:"
          % n_nodes)
    for i in range(n_nodes):
        if is_leaves[i]:
            print("%snode=%s leaf node." % (node_depth[i] * "\t", i))
        else:
            print("%snode=%s test node: go to node %s if X[:, %s] <= %s else to "
                  "node %s."
                  % (node_depth[i] * "\t",
                     i,
                     children_left[i],
                     feature[i],
                     threshold[i],
                     children_right[i],
                     ))
    print()
    