#global data sheet

# libs
import pandas as pd
import networkx as nx
import plotly.graph_objects as go
import friend_graph as fg # custom class


Form_Responses_1_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="Form Responses 1")

def friendship_graph(year,no):
     year1_df = pd.read_excel("./RESPONSE.xlsx", sheet_name=year)
     year1_df.fillna("", inplace=True)

     data = {"id":[],"friend":[],"friendship":[],"gender":[],"Branch":[],"Region":[],"clubs":[],"sports":[]}#dataset preperation

     for _,i in year1_df.iterrows():# for all rows
          i = i.fillna(0) # fill nan with 0
        
          # print(year1_df,i['Friend 1'])
          # print(name.values[0])
          # print(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name1.values[0]]["With whom do you study during exams? (with their ID)"].values)
          if(len(str(i['Friend 1']))>1 and i["id"]!=i['Friend 1']):
               name = year1_df[(year1_df['id'] ==int(i['Friend 1']))]["Name:"] if (len(year1_df[(year1_df['id'] ==int(i['Friend 1']))])>0)  else None
               if(type(name) == pd.core.series.Series):
                    data["id"].append(i['id'])
                    data["friend"].append(int(i['Friend 1']))
                    data["friendship"].append(int(i['Scale your friends: [friend 1]']) if ((not i['Scale your friends: [friend 1]']) == False) else 5)
                    data['gender'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values)>0)  else "not available")
                    data['Branch'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values)>0)  else "not available")
                    data['Region'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values)>0)  else "not available")
                    data['clubs'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values)>0)  else "not available")
                    data['sports'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values)>0)  else "not available")
               

          if(len(str(i['Friend 2']))>1 and i["id"]!=i['Friend 2']):
               name = year1_df[(year1_df['id'] ==int(i['Friend 2']))]["Name:"] if (len(year1_df[(year1_df['id'] ==int(i['Friend 2']))])>0)  else "not"

               if(type(name) == pd.core.series.Series):
                    data["id"].append(i['id'])
                    data["friend"].append(int(i['Friend 2']))
                    data["friendship"].append(int(i['Scale your friends: [friend 2]']) if ((not i['Scale your friends: [friend 2]']) == False) else 5)

                    data['gender'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values)>0)  else "not available")
                    data['Branch'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values)>0)  else "not available")
                    data['Region'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values)>0)  else "not available")
                    data['clubs'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values)>0)  else "not available")
                    data['sports'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values)>0)  else "not available")
               


          if(len(str(i['Friend 3']))>1 and i["id"]!=i['Friend 3']):
               name = year1_df[(year1_df['id'] ==int(i['Friend 3']))]["Name:"] if (len(year1_df[(year1_df['id'] ==int(i['Friend 3']))])>0)  else "not"
               if(type(name) == pd.core.series.Series):
                    data["id"].append(i['id'])
                    data["friend"].append(int(i['Friend 3']))
                    data["friendship"].append(int(i['Scale your friends: [friend 3]']) if ((not i['Scale your friends: [friend 3]']) == False) else 5)
                    data['gender'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values)>0)  else "not available")
                    data['Branch'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values)>0)  else "not available")
                    data['Region'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values)>0)  else "not available")
                    data['clubs'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values)>0)  else "not available")
                    data['sports'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values)>0)  else "not available")
               


          if(len(str(i['Friend 4']))>1 and i["id"]!=i['Friend 4']):
               name = year1_df[(year1_df['id'] ==int(i['Friend 4']))]["Name:"] if (len(year1_df[(year1_df['id'] ==int(i['Friend 4']))])>0)  else "not"
               if(type(name) == pd.core.series.Series):
                    data["id"].append(i['id'])
                    data["friend"].append(int(i['Friend 4']))
                    data["friendship"].append(int(i['Scale your friends: [friend 4]']) if ((not i['Scale your friends: [friend 4]']) == False) else 5)
                    data['gender'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values)>0)  else "not available")
                    data['Branch'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values)>0)  else "not available")
                    data['Region'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values)>0)  else "not available")
                    data['clubs'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values)>0)  else "not available")
                    data['sports'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values)>0)  else "not available")
               

          if (len(str(i['Friend 5']))>1 and i["id"]!=i['Friend 5']):
               name = year1_df[(year1_df['id'] ==int(i['Friend 5']))]["Name:"] if (len(year1_df[(year1_df['id'] ==int(i['Friend 5']))])>0)  else "not"
               if(type(name) == pd.core.series.Series):
                    data["id"].append(i['id'])
                    data["friend"].append(int(i['Friend 5']))
                    data["friendship"].append(int(i['Scale your friends: [friend 5]']) if ((not i['Scale your friends: [friend 5]']) == False) else 5)
                    data['gender'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values)>0)  else "not available")
                    data['Branch'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values)>0)  else "not available")
                    data['Region'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values)>0)  else "not available")
                    data['clubs'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values)>0)  else "not available")
                    data['sports'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values)>0)  else "not available")
               


          if(len(str(i['Friend 6']))>1 and i["id"]!=i['Friend 6']):
               name = year1_df[(year1_df['id'] ==int(i['Friend 6']))]["Name:"] if (len(year1_df[(year1_df['id'] ==int(i['Friend 6']))])>0)  else "not"
               if(type(name) == pd.core.series.Series):
                    data["id"].append(i['id'])
                    data["friend"].append(int(i['Friend 6']))
                    data["friendship"].append(int(i['Scale your friends: [friend 6]']) if ((not i['Scale your friends: [friend 6]']) == False) else 5)
                    data['gender'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values)>0)  else "not available")
                    data['Branch'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values)>0)  else "not available")
                    data['Region'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values)>0)  else "not available")
                    data['clubs'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values)>0)  else "not available")
                    data['sports'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values)>0)  else "not available")
               


          if (len(str(i['Friend 7']))>1 and i["id"]!=i['Friend 7']):
               name = year1_df[(year1_df['id'] ==int(i['Friend 7']))]["Name:"] if (len(year1_df[(year1_df['id'] ==int(i['Friend 7']))])>0)  else "not"
               if(type(name) == pd.core.series.Series):
                    data["id"].append(i['id'])
                    data["friend"].append(int(i['Friend 7']))
                    data["friendship"].append(int(i['Scale your friends: [friend 7]']) if ((not i['Scale your friends: [friend 7]']) == False) else 5)
                    data['gender'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values)>0)  else "not available")
                    data['Branch'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values)>0)  else "not available")
                    data['Region'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values)>0)  else "not available")
                    data['clubs'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values)>0)  else "not available")
                    data['sports'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values)>0)  else "not available")
               


          if(len(str(i['Friend 8']))>1 and i["id"]!=i['Friend 8']):
               name = year1_df[(year1_df['id'] ==int(i['Friend 8']))]["Name:"] if (len(year1_df[(year1_df['id'] ==int(i['Friend 8']))])>0)  else "not"
               if(type(name) == pd.core.series.Series):
                    data["id"].append(i['id'])
                    data["friend"].append(int(i['Friend 8']))
                    data["friendship"].append(int(i['Scale your friends: [friend 8]']) if ((not i['Scale your friends: [friend 8]']) == False) else 5)
                    data['gender'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values)>0)  else "not available")
                    data['Branch'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values)>0)  else "not available")
                    data['Region'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values)>0)  else "not available")
                    data['clubs'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values)>0)  else "not available")
                    data['sports'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values)>0)  else "not available")
               


          if(len(str(i['Friend 9']))>1 and i["id"]!=i['Friend 9']):
               name = year1_df[(year1_df['id'] ==int(i['Friend 9']))]["Name:"] if (len(year1_df[(year1_df['id'] ==int(i['Friend 9']))])>0)  else "not"
               if(type(name) == pd.core.series.Series):
                    data["id"].append(i['id'])
                    data["friend"].append(int(i['Friend 9']))
                    data["friendship"].append(int(i['Scale your friends: [friend 9]']) if ((not i['Scale your friends: [friend 9]']) == False) else 5)
                    data['gender'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values)>0)  else "not available")
                    data['Branch'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values)>0)  else "not available")
                    data['Region'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values)>0)  else "not available")
                    data['clubs'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values)>0)  else "not available")
                    data['sports'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values)>0)  else "not available")
               


          if(len(str(i['Friend 10']))>1 and i["id"]!=i['Friend 10']):
               name = year1_df[(year1_df['id'] ==int(i['Friend 10']))]["Name:"] if (len(year1_df[(year1_df['id'] ==int(i['Friend 10']))])>0)  else "not"
               if(type(name) == pd.core.series.Series):
                    data["id"].append(i['id'])
                    data["friend"].append(int(i['Friend 10']))
                    data["friendship"].append(int(i['Scale your friends: [friend 10]']) if ((not i['Scale your friends: [friend 10]']) == False) else 5)
                    data['gender'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Gender"].values)>0)  else "not available")
                    data['Branch'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Branch"].values)>0)  else "not available")
                    data['Region'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Region"].values)>0)  else "not available")
                    data['clubs'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Clubs:"].values)>0)  else "not available")
                    data['sports'].append(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values[0] if (len(Form_Responses_1_df1[Form_Responses_1_df1["Name:"] == name.values[0]]["Sports"].values)>0)  else "not available")
               


    
     df = pd.DataFrame(data) #dataset creation

     import os
     if os.path.exists('RESPONSE_'+year+'.csv'):
          os.remove('RESPONSE_'+year+'.csv')

     df.to_csv('RESPONSE_'+year+'.csv', mode='a', index=False, header=True)
     fg.friendship_graph(year,df,no)

     



def studydata():
     from collections import Counter



     year1_df = pd.read_excel("./RESPONSE.xlsx", sheet_name="Form Responses 1")
     year1_df.fillna("", inplace=True)
     branchdata = ""
     year1_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="1st_year")
     year2_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="2nd year")
     year3_df2 = pd.read_excel("./RESPONSE.xlsx", sheet_name="3rd year")

     civil_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="civil")
     me_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="me")
     eee_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="eee")
     cse_df1 = pd.read_excel("./RESPONSE.xlsx", sheet_name="cse")

     data = {"id":[],"friend":[],"cgpa":[]}
     for u in year1_df['Name:']:
          for i in year1_df[year1_df["Name:"] == u]['With whom do you study during exams? (with their ID)']:

               i = i.split("\n") if (type(i) != int) else ["alone"]
               for jk in i:
                    data["id"].append(u)
                    if(jk == "alone" or jk == "Alone" or jk == "none" or jk == "None"):
                         a = dict(Counter(data["friend"]))
                         # print(a.items())
                         if(len(a.values())>0):
                              jk = u
                         else:
                              jk = u
                    # print("=====================================")
                    
                    # print(year1_df1[(year1_df1['Name:']==jk)]["Branch"].values[0] if (len(year1_df1[(year1_df1['Name:']==jk)]["Branch"].values)>0) else ["not"])
                    year1_dff = year1_df1[(year1_df1['Name:']==jk)]
                    year2_dff = year2_df1[(year2_df1['Name:']==jk)]
                    year3_dff = year3_df2[(year3_df2['Name:']==jk)]

                    if(year1_df1[(year1_df1['Name:']==jk)]["Branch"].values[0] if (len(year1_df1[(year1_df1['Name:']==jk)]["Branch"].values)>0) else ["not"] == "ME"):
                         branchdata = me_df1[(me_df1['HALL TICKET Number']==int(year1_dff["id"]))]
                    elif(year1_df1[(year1_df1['Name:']==jk)]["Branch"].values[0] if (len(year1_df1[(year1_df1['Name:']==jk)]["Branch"].values)>0) else ["not"] == "CE"):
                         branchdata = civil_df1[(civil_df1['HALL TICKET Number']==int(year1_dff["id"]))]
                    elif(year1_df1[(year1_df1['Name:']==jk)]["Branch"].values[0] if (len(year1_df1[(year1_df1['Name:']==jk)]["Branch"].values)>0) else ["not"] == "EEE"):
                         branchdata = eee_df1[(eee_df1['HALL TICKET Number']==int(year1_dff["id"]))]
                    elif(year1_df1[(year1_df1['Name:']==jk)]["Branch"].values[0] if (len(year1_df1[(year1_df1['Name:']==jk)]["Branch"].values)>0) else ["not"] == "CSE"):
                         branchdata = cse_df1[(cse_df1['HALL TICKET Number']==int(year1_dff["id"]))]
                    else:
                         branchdata = "no"

                    # print(branchdata)
                    
                    if(type(branchdata) != str and len(branchdata.values)>0):
                         firststyeargpa = float(float(branchdata["I-SEM"].values[0])+float(branchdata["II-SEM"].values[0]))/2
                         secondstyeargpa = float(float(branchdata["III-SEM"].values[0])+float(branchdata["IV-SEM"].values[0]))/2
                         thirdstyeargpa = float(float(branchdata["V-SEM"].values[0])+float(branchdata["VI-SEM"].values[0]))/2

                         data["cgpa"].append((firststyeargpa+secondstyeargpa+thirdstyeargpa)/3)
                    else:
                         data["cgpa"].append("no data")


                    data["friend"].append(jk)
               

     df = pd.DataFrame(data)

     import os
     if(os.path.isfile('GLOBAL_STUDY_based.csv')):
          os.remove('GLOBAL_STUDY_based.csv')

     df.to_csv('GLOBAL_STUDY_based.csv', mode='a', index=False, header=True)
     csvdata = pd.read_csv("./GLOBAL_STUDY_based.csv")
          
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

     # print(nx.reciprocity(G))

     # df = nx.reciprocity(G)

     node_trace = go.Scatter(
          x=node_x, y=node_y,
          mode='markers+text',
          hoverinfo='text',
          # customdata=df['friendship'].tolist(),
          # hovertemplate='<br>Friendship Score(Density):%{customdata}',
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

     node_adjacencies = []
     node_text = []
     for node, adjacencies in enumerate(G.adjacency()):
          node_adjacencies.append(len(adjacencies[1]))
          node_text.append(str(adjacencies[0]))

     node_trace.marker.color = node_adjacencies
     node_trace.text = node_text

     alonearray = []
     grouparray = []
     for il in range(0,len(csvdata['id'].tolist())):
          id = csvdata['id'].tolist()[il]
          friend = csvdata['friend'].tolist()[il]
          if(id == friend):
               alonearray.append(friend)
          else:
               grouparray.append(friend)

     
     print(len(alonearray),len(grouparray))

     dictitem = [dict(
                         text="Alone people: "+str(len(alonearray))+" <br> Group people: "+str(len(grouparray))+"",
                         showarrow=False,
                         xref="paper", yref="paper",
                         x=0.005, y=-0.002 ),
                         
                    dict(
                         text="Number of nodes: "+str(len(G.nodes()))+" <br> Number of Edges: "+str(len(G.edges()))+"<br> Degree distribution: "+str(round(int(max(node_adjacencies))/len(G.nodes()),2)),
                         showarrow=False,
                         xref="paper", yref="paper",
                         x=0.95, y=+0.95 )]


     fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                    title='<br>Global Friendship study Network',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=dictitem,
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )
     # print(csvdata['id'].tolist(),csvdata['friend'].tolist())

    

          

  

     fig.show()




friendship_graph('1st_year',1)
friendship_graph('2nd year',2)
friendship_graph('3rd year',3)

studydata()