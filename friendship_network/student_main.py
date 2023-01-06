
import pandas as pd
import networkx as nx
import plotly.graph_objects as go
import ipywidgets as w
from IPython.display import display

mark = input("Enter student id: ")
try:
    int(mark)
except ValueError:
    print("This is not a valid number")

Form_Responses_1_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="Form Responses 1")
year1_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="1st_year")
year2_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="2nd year")
year3_df2 = pd.read_excel("./RESPONSE.xlsx", sheet_name="3rd year")
activities_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="activities")
civil_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="civil")
me_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="me")
eee_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="eee")
cse_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="cse")

year1_df = year1_df1[(year1_df1['id']==int(mark))]
Form_Responses_1_df = Form_Responses_1_df1[Form_Responses_1_df1['Name:']==year1_df['Name:'].values[0]]
year2_df = year2_df1[(year2_df1['id']==int(mark))]
year3_df = year3_df2[(year3_df2['id']==int(mark))]
activities_df = activities_df1[(activities_df1['id']==int(mark))]
branchdata = ""

if(year1_df["Branch"].values[0] == "ME"):
    branchdata = me_df1[(me_df1['HALL TICKET Number']==int(mark))]
elif(year1_df["Branch"].values[0] == "CE"):
    branchdata = civil_df1[(civil_df1['HALL TICKET Number']==int(mark))]
elif(year1_df["Branch"].values[0] == "EEE"):
    branchdata = eee_df1[(eee_df1['HALL TICKET Number']==int(mark))]
elif(year1_df["Branch"].values[0] == "CSE"):
    branchdata = cse_df1[(cse_df1['HALL TICKET Number']==int(mark))]
else:
    print("Invalid branch")



def getyearlyfriendshipData(gotdata,year):
    print("=====================================================")


    if(year == 1):
        yeardata = year1_df1
    elif(year == 2):
        yeardata = year2_df1
    elif(year == 3):
        yeardata = year3_df2

    print(yeardata['Name:'].values[0])

    # print(    Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==int(gotdata['Friend 1'].values[0]))].values[0][1] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 1'].values[0]))].values)>0)  else "not available")

    gotdata.fillna("", inplace=True)

    data = {"id":[],"friend":[],"friendship":[],"gender":[],"Branch":[],"Region":[],"clubs":[],"sports":[]}
    if(len(str(gotdata['Friend 1'].values[0]))>1 and mark!=gotdata['Friend 1'].values[0]):
        data["id"].append(gotdata['id'].values[0])
        data["friend"].append(int(gotdata['Friend 1']))
        data["friendship"].append(int(gotdata['Scale your friends: [friend 1]']))
        data['gender'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 1'].values[0]))].values[0][3] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 1'].values[0]))].values)>0)  else "not available")
        data['Branch'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 1'].values[0]))].values[0][4] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 1'].values[0]))].values)>0)  else "not available")
        data['Region'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 1'].values[0]))].values[0][5] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 1'].values[0]))].values)>0)  else "not available")
        
        name = yeardata[(yeardata['id'] ==int(gotdata['Friend 1'].values[0]))].values[0][1] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 1'].values[0]))].values)>0)  else "not"
        
        data['clubs'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Clubs:"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
        data['sports'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Sports"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
  

    if(len(str(gotdata['Friend 2'].values[0]))>1 and mark!=gotdata['Friend 2'].values[0]):
        data["id"].append(gotdata['id'].values[0])
        data["friend"].append(int(gotdata['Friend 2'].values[0]))
        data["friendship"].append(int(gotdata['Scale your friends: [friend 2]']))
        data['gender'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 2'].values[0]))].values[0][3] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 2'].values[0]))].values)>0)  else "not available")
        data['Branch'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 2'].values[0]))].values[0][4] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 2'].values[0]))].values)>0)  else "not available")
        data['Region'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 2'].values[0]))].values[0][5] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 2'].values[0]))].values)>0)  else "not available")
         
        name = yeardata[(yeardata['id'] ==int(gotdata['Friend 2'].values[0]))].values[0][1] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 2'].values[0]))].values)>0)  else "not"
        
        data['clubs'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Clubs:"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
        data['sports'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Sports"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
  

    if(len(str(gotdata['Friend 3'].values[0]))>1 and mark!=gotdata['Friend 3'].values[0]):
        data["id"].append(gotdata['id'].values[0])
        data["friend"].append(int(gotdata['Friend 3'].values[0]))
        data["friendship"].append(int(gotdata['Scale your friends: [friend 3]']))
        data['gender'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 3'].values[0]))].values[0][3] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 3'].values[0]))].values)>0)  else "not available")
        data['Branch'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 3'].values[0]))].values[0][4] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 3'].values[0]))].values)>0)  else "not available")
        data['Region'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 3'].values[0]))].values[0][5] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 3'].values[0]))].values)>0)  else "not available")
         
        name = yeardata[(yeardata['id'] ==int(gotdata['Friend 3'].values[0]))].values[0][1] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 3'].values[0]))].values)>0)  else "not"
        
        data['clubs'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Clubs:"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
        data['sports'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Sports"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
  

    if(len(str(gotdata['Friend 4'].values[0]))>1 and mark!=gotdata['Friend 4'].values[0]):
        data["id"].append(gotdata['id'].values[0])
        data["friend"].append(int(gotdata['Friend 4'].values[0]))
        data["friendship"].append(int(gotdata['Scale your friends: [friend 4]']))
        data['gender'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 4'].values[0]))].values[0][3] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 4'].values[0]))].values)>0)  else "not available")
        data['Branch'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 4'].values[0]))].values[0][4] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 4'].values[0]))].values)>0)  else "not available")
        data['Region'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 4'].values[0]))].values[0][5] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 4'].values[0]))].values)>0)  else "not available")
         
        name = yeardata[(yeardata['id'] ==int(gotdata['Friend 4'].values[0]))].values[0][1] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 4'].values[0]))].values)>0)  else "not"
        
        data['clubs'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Clubs:"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
        data['sports'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Sports"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
  
    if (len(str(gotdata['Friend 5'].values[0]))>1 and mark!=gotdata['Friend 5'].values[0]):
        data["id"].append(gotdata['id'].values[0])
        data["friend"].append(int(gotdata['Friend 5'].values[0]))
        data["friendship"].append(int(gotdata['Scale your friends: [friend 5]']))
        data['gender'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 5'].values[0]))].values[0][3] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 5'].values[0]))].values)>0)  else "not available")
        data['Branch'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 5'].values[0]))].values[0][4] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 5'].values[0]))].values)>0)  else "not available")
        data['Region'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 5'].values[0]))].values[0][5] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 5'].values[0]))].values)>0)  else "not available")
         
        name = yeardata[(yeardata['id'] ==int(gotdata['Friend 5'].values[0]))].values[0][1] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 5'].values[0]))].values)>0)  else "not"
        
        data['clubs'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Clubs:"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
        data['sports'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Sports"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
  

    if(len(str(gotdata['Friend 6'].values[0]))>1 and mark!=gotdata['Friend 6'].values[0]):
        data["id"].append(gotdata['id'].values[0])
        data["friend"].append(int(gotdata['Friend 6'].values[0]))
        data["friendship"].append(int(gotdata['Scale your friends: [friend 6]']))
        data['gender'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 6'].values[0]))].values[0][3] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 6'].values[0]))].values)>0)  else "not available")
        data['Branch'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 6'].values[0]))].values[0][4] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 6'].values[0]))].values)>0)  else "not available")
        data['Region'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 6'].values[0]))].values[0][5] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 6'].values[0]))].values)>0)  else "not available")
         
        name = yeardata[(yeardata['id'] ==int(gotdata['Friend 6'].values[0]))].values[0][1] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 6'].values[0]))].values)>0)  else "not"
        
        data['clubs'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Clubs:"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
        data['sports'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Sports"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
  

    if (len(str(gotdata['Friend 7'].values[0]))>1 and mark!=gotdata['Friend 7'].values[0]):
        data["id"].append(gotdata['id'].values[0])
        data["friend"].append(int(gotdata['Friend 7'].values[0]))
        data["friendship"].append(int(gotdata['Scale your friends: [friend 7]']))
        data['gender'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 7'].values[0]))].values[0][3] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 7'].values[0]))].values)>0)  else "not available")
        data['Branch'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 7'].values[0]))].values[0][4] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 7'].values[0]))].values)>0)  else "not available")
        data['Region'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 7'].values[0]))].values[0][5] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 7'].values[0]))].values)>0)  else "not available")
         
        name = yeardata[(yeardata['id'] ==int(gotdata['Friend 7'].values[0]))].values[0][1] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 7'].values[0]))].values)>0)  else "not"
        
        data['clubs'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Clubs:"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
        data['sports'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Sports"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
  

    if(len(str(gotdata['Friend 8'].values[0]))>1 and mark!=gotdata['Friend 8'].values[0]):
        data["id"].append(gotdata['id'].values[0])
        data["friend"].append(gotdata['Friend 8'].values[0])
        data["friendship"].append(int(gotdata['Scale your friends: [friend 8]']))
        data['gender'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 8'].values[0]))].values[0][3] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 8'].values[0]))].values)>0)  else "not available")
        data['Branch'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 8'].values[0]))].values[0][4] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 8'].values[0]))].values)>0)  else "not available")
        data['Region'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 8'].values[0]))].values[0][5] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 8'].values[0]))].values)>0)  else "not available")
         
        name = yeardata[(yeardata['id'] ==int(gotdata['Friend 8'].values[0]))].values[0][1] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 8'].values[0]))].values)>0)  else "not"
        
        data['clubs'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Clubs:"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
        data['sports'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Sports"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
  

    if(len(str(gotdata['Friend 9'].values[0]))>1 and mark!=gotdata['Friend 9'].values[0]):
        data["id"].append(gotdata['id'].values[0])
        data["friend"].append(int(gotdata['Friend 9'].values[0]))
        data["friendship"].append(int(gotdata['Scale your friends: [friend 9]']))
        data['gender'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 9'].values[0]))].values[0][3] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 9'].values[0]))].values)>0)  else "not available")
        data['Branch'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 9'].values[0]))].values[0][4] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 9'].values[0]))].values)>0)  else "not available")
        data['Region'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 9'].values[0]))].values[0][5] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 9'].values[0]))].values)>0)  else "not available")
         
        name = yeardata[(yeardata['id'] ==int(gotdata['Friend 9'].values[0]))].values[0][1] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 9'].values[0]))].values)>0)  else "not"
        
        data['clubs'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Clubs:"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
        data['sports'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Sports"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
  

    if(len(str(gotdata['Friend 10'].values[0]))>1 and mark!=gotdata['Friend 10'].values[0]):
        data["id"].append(gotdata['id'].values[0])
        data["friend"].append(int(gotdata['Friend 10'].values[0]))
        data["friendship"].append(int(gotdata['Scale your friends: [friend 10]']))
        data['gender'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 10'].values[0]))].values[0][3] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 10'].values[0]))].values)>0)  else "not available")
        data['Branch'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 10'].values[0]))].values[0][4] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 10'].values[0]))].values)>0)  else "not available")
        data['Region'].append(yeardata[(yeardata['id'] ==int(gotdata['Friend 10'].values[0]))].values[0][5] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 10'].values[0]))].values)>0)  else "not available")
         
        name = yeardata[(yeardata['id'] ==int(gotdata['Friend 1'].values[0]))].values[0][1] if (len(yeardata[(yeardata['id'] ==int(gotdata['Friend 10'].values[0]))].values)>0)  else "not"
        
        data['clubs'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Clubs:"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
        data['sports'].append(Form_Responses_1_df1[(Form_Responses_1_df1['Name:'] ==name)]["Sports"].values[0] if (len(yeardata[(Form_Responses_1_df1['Name:'] ==name)].values)>0)  else "not available")
  


    df = pd.DataFrame(data)

    import os
    if os.path.exists('STUDENT_id_based.csv'):
        os.remove('STUDENT_id_based.csv')

    df.to_csv('STUDENT_id_based.csv', mode='a', index=False, header=True)
    csvdata = pd.read_csv("./STUDENT_id_based.csv")

    G = nx.from_pandas_edgelist(csvdata, source='id', target='friend', create_using=nx.Graph())
    pos = nx.spring_layout(G)
    nx.set_node_attributes(G, pos, 'pos')
    # print(len(G.nodes()))
    # print(len(G.edges()))
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
        edgeddata = getparsescores(edge[0],edge[1])
        mnode_txt.extend([f"({edge[0]}:{edgeddata[0]}, {edge[1]}:{edgeddata[1]})"]) # hovertext

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

    mnode_trace = go.Scatter(x = mnode_x, y = mnode_y, name="mnode_trace", mode = "markers+text", 
                            hovertext=mnode_txt,
                            marker=dict(showscale=True,
                colorscale='YlGnBu',
                # reversescale=True,
                color=[2],
                size=2))

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        customdata=df['friendship'].tolist(),
        hovertemplate='<br>Friendship Score(Density):%{customdata}',
        textposition='top center',
        textfont=dict(color='#E58606'),
        # hovertemplate="Score: %{text} <br>",
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

    node_adjacencies = []
    node_text = []
    for node, adjacencies in enumerate(G.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        node_text.append("id: "+str(adjacencies[0])+' has '+str(len(adjacencies[1]))+" connections ")

    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text
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
    if(year == 3):
        dictitem.append(dict(
                        text="CGPA <br>"+yearsemdata(),
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=+0.05 ))

    fig = go.Figure(data=[edge_trace, node_trace,mnode_trace],
                layout=go.Layout(
                    title=str(Form_Responses_1_df['Name:'].values[0])+'<br> Friendship '+str(year)+' year Network',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',

                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=dictitem,
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )

    previousdata = []


    button_all = dict(label = 'All',
                      method = 'update',
                      args = [{"marker": {"color":node_adjacencies,"showscale":True,"size":10,},
                      "text":node_text}])
    print(node_adjacencies)
    def create_layout_button(column):
        
        if(column == "gender"):
            previousdata = df["gender"].tolist()
            print(df['gender'].tolist())
            genderarray = [previousdata,df['gender'].values]
            print(genderarray)
            cs = [7 if t2=="Male" else 8 if t2=="not available" else 9 for t2 in df['gender'].values]
            return dict(label = column,
                        method = 'update',
                        args = [{"marker": {"color":cs,"showscale":True,"size":10},
                            "text":genderarray}])

        elif(column == "Branch"):
            previousdata = df["Branch"].tolist()
            genderarray = [previousdata,df['Branch'].values]
            cs = [10 if t2=="EEE" else 6 if t2=="ECE" else 5 if t2=="CSE" else 2 if t2=="ME" else 7 for t2 in df['Branch'].values]
            return dict(label = column,
                        method = 'update',
                        args = [{"marker": {"color":cs,"showscale":True,"size":10},
                            "text":genderarray}])

        elif(column == "Region"):
            previousdata = df["Region"].tolist()
            genderarray = [previousdata,df['Region'].values]
            cs = [7 if t2=="Telangana" else 8 if t2=="Andhra Pradesh" else 9 if t2=="Rajasthan" else 10 if t2=="West Bengal"  else 11 if t2=="Maharashtra" else 12 if t2=="Kerala" else 6 if t2=="Punjab" else 5 for t2 in df['Region'].values]
            return dict(label = column,
                        method = 'update',
                        args = [{"marker": {"color":cs,"showscale":True,"size":10},
                            "text":genderarray}])
        elif(column == "clubs"):
            previousdata = df["clubs"].tolist()
            genderarray = [previousdata,df['clubs'].values]
            cs = [t2 for t2 in range(0,len(df['clubs'].values))]
            return dict(label = column,
                        method = 'update',
                        args = [{"marker": {"color":cs,"showscale":True,"size":10},
                            "text":genderarray}])
        elif(column == "sports"):
            previousdata = df["sports"].tolist()
            genderarray = [previousdata,df['sports'].values]
            cs = [t2 for t2 in range(0,len(df['sports'].values))]
            
            return dict(label = column,
                        method = 'update',
                        args = [{"marker": {"color":cs,"showscale":True,"size":10},
                            "text":genderarray}])

        else:
            previousdata = df["friendship"].tolist()
            return dict(label = column,
                        method = 'update',
                        args = [{"marker": {"color":node_adjacencies,"showscale":True,"size":10},
                            "text":node_text,}])


    fig.update_traces(textposition='top center')

    fig.update_layout(
        # yaxis = dict(scaleanchor = "x", scaleratio = 1), plot_bgcolor='rgb(255,255,255)',
    
        updatemenus=[go.layout.Updatemenu(
            active = 0,
            buttons = ([button_all] * True) + list( df.columns[::1].map(lambda column: create_layout_button(column)))
            )
        ])
         
    fig.show()


def getstudydata():

    data = {"id":[],"friend":[]}
    for i in Form_Responses_1_df['With whom do you study during exams? (with their ID)'].values[0].split(","):
        data['id'].append(str(Form_Responses_1_df['Name:'].values[0])+" "+mark)
        data['friend'].append(i)

    print(data)

    df = pd.DataFrame(data)

    import os
    if(os.path.exists('STUDENT_study_id_based.csv')):
        os.remove('STUDENT_study_id_based.csv')

    df.to_csv('STUDENT_study_id_based.csv', mode='a', index=False, header=True)
    csvdata = pd.read_csv("./STUDENT_study_id_based.csv")

    G = nx.from_pandas_edgelist(csvdata, source='id', target='friend', create_using=nx.Graph())
    pos = nx.spring_layout(G)
    nx.set_node_attributes(G, pos, 'pos')
    # print(G.nodes(data=True))
    # print(G.edges(data=True))
    # print(pos)

    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

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

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        text=list(G.nodes()),
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

    node_adjacencies = []
    node_text = []
    for node, adjacencies in enumerate(G.adjacency()):
        print(adjacencies[0])
        node_adjacencies.append(len(adjacencies[1]))
        node_text.append("id: "+str(adjacencies[0])+' has '+str(len(adjacencies[1]))+" connections ")

    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text

    fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='<br>With whom do you study during exams? (with their ID) Network',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[ dict(
                        text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002 ) ],
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
    fig.show()

    




def yearsemdata():
    firststyeargpa = float(float(branchdata["I-SEM"].values[0])+float(branchdata["II-SEM"].values[0]))/2
    secondstyeargpa = float(float(branchdata["III-SEM"].values[0])+float(branchdata["IV-SEM"].values[0]))/2
    thirdstyeargpa = float(float(branchdata["V-SEM"].values[0])+float(branchdata["VI-SEM"].values[0]))/2

    return "1st year cgpa: "+str(round(firststyeargpa,2))+"<br> 2nd year cgpa: "+str(round(secondstyeargpa,2))+"<br>3rd year cgpa: "+str(round(thirdstyeargpa,2))+"<br>Over all CGPA: "+str(round(((firststyeargpa+secondstyeargpa+thirdstyeargpa)/3),2))






getstudydata()

getyearlyfriendshipData(year1_df,1)
getyearlyfriendshipData(year2_df,2)
getyearlyfriendshipData(year3_df,3)



