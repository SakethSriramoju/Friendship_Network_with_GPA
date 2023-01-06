import plotly.graph_objects as go
import pandas as pd
import networkx as nx



def friendship_graph(year,df,year_no):
    csvdata = pd.read_csv("./RESPONSE_"+year+".csv")


    G = nx.from_pandas_edgelist(csvdata, source='id', target='friend', create_using=nx.Graph())# our dataset will converted to plotly dataset by networkx lib
    pos = nx.spring_layout(G)
    nx.set_node_attributes(G, pos, 'pos')# set the position of the nodes
    # print(G.nodes(data=True))
    # print(G.edges(data=True))
    # print(pos)

    def getparsescores(edge0,edge1):
        returndata = []
        edgevardata = csvdata[csvdata["id"] == edge0]

        if(len(edgevardata)>0 and len(edgevardata[edgevardata["friend"] == edge1])>0):
             returndata.append(edgevardata[edgevardata["friend"] == edge1]["friendship"].values[0])
        else:
            returndata.append("no")
        

        edge1vardata = csvdata[csvdata["id"] == edge1]
        if(len(edge1vardata)>0 and len(edge1vardata[edge1vardata["friend"] == edge0])>0):
             returndata.append(edge1vardata[edge1vardata["friend"] == edge0]["friendship"].values[0])
        else:
            returndata.append("no")
        # print(returndata)

        return returndata

        
    edge_x = []
    edge_y = []
    mnode_x, mnode_y, mnode_txt = [], [], []


    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)
        mnode_x.extend([(x0 + x1)/2]) # assuming values positive/get midpoint
        mnode_y.extend([(y0 + y1)/2]) # assumes positive vals/get midpoint
        edgeddata = getparsescores(edge[0],edge[1])
        mnode_txt.extend([f"({edge[0]}:{edgeddata[0]}, {edge[1]}:{edgeddata[1]})"]) # hovertext
        

       #overlay grapgh graph alignment 
    mnode_trace = go.Scatter(x = mnode_x, y = mnode_y, name="mnode_trace", mode = "markers+text", 
                        hovertext=mnode_txt,
                        marker=dict(showscale=True,
            colorscale='YlGnBu',
            # reversescale=True,
            color=[2],
            size=5))
# edge grapgh graph alignment 
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []

    for node in G.nodes:
        x, y = G.nodes[node]['pos']
        node_x.append(x)
        node_y.append(y)
   
#node grapgh graph alignment 
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        name="node_trace",
        mode='markers+text',
        hoverinfo='text',
        customdata=df['friend'].tolist(),
        hovertemplate='<br>id:%{customdata}',
        textposition='top center',
        textfont=dict(color='#E58606'),
        marker=dict(
            showscale=True,
            # colorscale options
            #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    #colour filter depending on node connctions
    node_adjacencies = []
    node_text = []
    for node, adjacencies in enumerate(G.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        node_text.append("id: "+str(adjacencies[0])+' has '+str(len(adjacencies[1]))+" connections ")

    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text

#extra html content
    dictitem = [dict(
                        text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002 ),
                        
                dict(
                        text="Number of nodes: "+str(len(G.nodes()))+" <br> Number of Edges: "+str(len(G.edges()))+"<br> connected components: "+str(max(node_adjacencies)),
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.9, y=+0.9 )]


# graphing layout using edgetrace, nodetrace and mnode trace
    fig = go.Figure(data=[edge_trace, node_trace,mnode_trace],
                layout=go.Layout(
                    title='<br>Global Friendship '+year+' Network',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=dictitem,
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
 


# assortion of buttons for the graph
    button_all = dict(label = 'All',
                      method = 'restyle',
                      args = [
                        {"marker": {"color":node_adjacencies,"showscale":True,"size":10,},
                      "text":[node_text,node_text],'type': 'scatter',"visible": True,
                      }])

    def create_layout_button(column):

        #based on condition filtering 

        if(column == "gender"):
            previousdata = df["gender"].tolist()
            genderarray = [previousdata,df['gender'].values]
            cs = [7 if t2=="Male" else 8 if t2=="Female" else 9 for t2 in df['gender'].values]
            return dict(label = column,
                        method = 'restyle',
                        args = [{"visible": [True,True,"legendonly"],
                            "marker": {"color":cs,"showscale":True,"size":10},
                            "text":genderarray}])

        elif(column == "Branch"):
            previousdata = df["Branch"].tolist()
            genderarray = [previousdata,df['Branch'].values]
            cs = [10 if t2=="EEE" else 6 if t2=="ECE" else 5 if t2=="CSE" else 2 if t2=="ME" else 7 for t2 in df['Branch'].values]
            return dict(label = column,
                        method = 'update',
                        args = [{"visible": [True,True,"legendonly"],"marker": {"color":cs,"showscale":True,"size":10},
                            "text":genderarray}])

        elif(column == "Region"):
            previousdata = df["Region"].tolist()
            genderarray = [previousdata,df['Region'].values]
            cs = [7 if t2=="Telangana" else 8 if t2=="Andhra Pradesh" else 9 if t2=="Rajasthan" else 10 if t2=="West Bengal"  else 11 if t2=="Maharashtra" else 12 if t2=="Kerala" else 6 if t2=="Punjab" else 5 for t2 in df['Region'].values]
            return dict(label = column,
                        method = 'update',
                        args = [{"visible": [True,True,"legendonly"],"marker": {"color":cs,"showscale":True,"size":10},
                            "text":genderarray}])
        elif(column == "clubs"):
            previousdata = df["clubs"].tolist()
            genderarray = [previousdata,df['clubs'].values]
            cs = [t2 for t2 in range(0,len(df['clubs'].values))]
            return dict(label = column,
                        method = 'update',
                        args = [{"visible": [True,True,"legendonly"],"marker": {"color":cs,"showscale":True,"size":10},
                            "text":genderarray}])
        elif(column == "sports"):
            previousdata = df["sports"].tolist()
            # print(df['sports'].tolist())
            genderarray = [previousdata,df['sports'].values]
            cs = [t2 for t2 in range(0,len(df['sports'].values))]
            
            return dict(label = column,
                        method = 'update',
                        args = [{"visible": [True,True,"legendonly"],"marker": {"color":cs,"showscale":True,"size":10},
                            "text":genderarray}])

        else:
            previousdata = df["friend"].tolist()
            return dict(label = column,
                        method = 'update',
                        args = [{"marker": {"color":node_adjacencies,"showscale":True,"size":10},
                            "text":node_text,}])

    fig.update_traces(textposition='top center')

    fig.update_layout(
        # yaxis = dict(scaleanchor = "x", scaleratio = 1), plot_bgcolor='rgb(255,255,255)',
    
        updatemenus=[go.layout.Updatemenu(
            active = 0,
            buttons = ([button_all] * True) + list( df.columns[::1].map(lambda column: create_layout_button(column))) #addding menu as dropdown for assortion
            )
        ])

   #visualizing the graph
    fig.show()

