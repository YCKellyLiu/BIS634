# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import Flask, render_template, request
from flask import render_template_string, jsonify
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from plotly.utils import PlotlyJSONEncoder
import plotly.graph_objs as go
import logging
from logging import Formatter, FileHandler
import numpy as np
import pandas as pd
import pickle
import json
import os
import seaborn as sns
from datetime import datetime
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

def PCA_analysis(data):
    global pca_data
    scaler = StandardScaler()
    scaler.fit(data)
    scaled_df = pd.DataFrame(scaler.transform(data), columns=data.columns)
    # The number of dimensions as 3
    pca = PCA(n_components=3)
    pca.fit(scaled_df)
    pca_data = pd.DataFrame(pca.transform(scaled_df), columns=["c1", "c2", "c3"])
    x = pca_data["c1"]
    y = pca_data["c2"]
    z = pca_data["c3"]
    layout = {
    "margin": {
        "l": 200,
        "r": 220,
        "b": 0,
        "t": 0,
    },
    "title":{'text': "3D Plot of Size-Reduced Data",'y':0.9,
            'x':0.5,'xanchor': 'center','yanchor': 'top'},
    }
    data =[{
        "x":x.to_list(),"y":y.to_list(),"z":z.to_list(),"type":"scatter3d","name":"PCA 3D Plot",
        "mode":"markers","marker":{"size":6,"color":x.to_list(),"opacity":0.8},
    }]
    graphJSON = (jsonify([{"data":data, "layout":layout}]))
    return graphJSON

def Kmeans_analysis(pca_data):
    wcss = []
    k = range(1,18)
    if True:
        for i in k:
            model = KMeans(n_clusters=i)
            model.fit(pca_data)
            wcss.append(model.inertia_)   
        layout = {
        "margin": {
            "l": 50,
            "r": 50,
            "b": 100,
            "t": 100,
            "pad": 4
        },
        "colorway" : ['#f3cec9', '#e7a4b6', '#cd7eaf', '#a262a9', '#6f4d96', '#3d3b72', '#182844'],
        "template":"seaborn",
        "title": "The Elbow Method",
        "xaxis":{"title":'Number of Clusters'}, 
        "yaxis":{"title":"WCSS"}
        }
        data =[{"x": list(k), "y": wcss, "type": "scatter","name":"The Elbow Method","mode":'lines+markers'
               }
              ]
        graphJSON = (jsonify([{"data":data, "layout":layout}]))
        return graphJSON
    else:
        print("error!")
        return "error!"

def Kmeans_results(ts,pca_data,k=4):
    ts_temp = ts
    k_means = KMeans(n_clusters = k, random_state = 50)
    y_pred = k_means.fit_predict(pca_data)
#     pca_data_temp['Cluster'] = y_pred
    ts_temp['Cluster'] = y_pred
    layout = {
        "margin": {
            "l": 50,
            "r": 50,
            "b": 100,
            "t": 100,
            "pad": 4
        },
        "colorway" : ['#f3cec9', '#e7a4b6', '#cd7eaf', '#a262a9', '#6f4d96', '#3d3b72', '#182844'],
        "template":"seaborn",
        "xaxis":{"title":'Cluster'}, 
        "yaxis":{"title":"Count"}
        }
    count = ts_temp['Cluster'].value_counts()
    data = [{"x": count.index.tolist(), "y": count.values.tolist(), "type": "bar","name":"Count"},]
    graphJSON = (jsonify([{"data":data, "layout":layout}]))
    return graphJSON
        
def create_plot(ts,feature="Bar"):
    if feature=="Bar":
        x = [str(i)[:10] for i in ts.index.to_list()]
        layout = {
            "margin": {
                "l": 50,
                "r": 50,
                "b": 100,
                "t": 100,
                "pad": 4
            },
            "colorway" : ['#f3cec9', '#e7a4b6', '#cd7eaf', '#a262a9', '#6f4d96', '#3d3b72', '#182844'],
            "template":"seaborn"
            }
        data = [
            {"x": x, "y": ts["Education"].to_list(), "type": "bar","name":"Education","color":'#636EFA'},
            {"x": x, "y": ts["Marital_Status"].to_list(), "type": "bar","name":"Marital_Status"},
            {"x": x, "y": ts["Income"].to_list(), "type": "bar","name":"Income"},
            {"x": x, "y": ts["Recency"].to_list(), "type": "bar","name":"Recency"},
            {"x": x, "y": ts["Complain"].to_list(), "type": "bar","name":"Complain"},
            {"x": x, "y": ts["Age"].to_list(), "type": "bar","name":"Age"},
            {"x": x, "y": ts["Engaged_Days"].to_list(), "type": "bar","name":"Engaged_Days"},
            {"x": x, "y": ts["Kids"].to_list(), "type": "bar","name":"Kids"},
            {"x": x, "y": ts["TotalAcceptedCampaign"].to_list(), "type": "bar","name":"TotalAcceptedCampaign"},
            {"x": x, "y": ts["NumTotalPurchases"].to_list(), "type": "bar","name":"NumTotalPurchases"},
            {"x": x, "y": ts["Expenses"].to_list(), "type": "bar","name":"Expenses"},
        ]        
        graphJSON = (jsonify([{"data":data, "layout":layout}]))
    if feature=="box":
        layout = {
            "margin": {
                "l": 50,
                "r": 50,
                "b": 100,
                "t": 100,
                "pad": 4
            },
            "colorway" : ['#f3cec9', '#e7a4b6', '#cd7eaf', '#a262a9', '#6f4d96', '#3d3b72', '#182844'],
            "template":"seaborn"
            }
        data = [
            {"y": ts["Education"].to_list(), "type": "box","name":"Education","color":'#636EFA'},
            {"y": ts["Marital_Status"].to_list(), "type": "box","name":"Marital_Status"},
            {"y": ts["Income"].to_list(), "type": "box","name":"Income"},
            {"y": ts["Recency"].to_list(), "type": "box","name":"Recency"},
            {"y": ts["Complain"].to_list(), "type": "box","name":"Complain"},
            {"y": ts["Age"].to_list(), "type": "box","name":"Age"},
            {"y": ts["Engaged_Days"].to_list(), "type": "box","name":"Engaged_Days"},
            {"y": ts["Kids"].to_list(), "type": "box","name":"Kids"},
            {"y": ts["TotalAcceptedCampaign"].to_list(), "type": "box","name":"TotalAcceptedCampaign"},
            {"y": ts["NumTotalPurchases"].to_list(), "type": "box","name":"NumTotalPurchases"},
            { "y": ts["Expenses"].to_list(), "type": "box","name":"Expenses"},
        ]
        graphJSON = (jsonify([{"data":data, "layout":layout}]))
    if feature=="heatmap":
        layout = {
            "margin": {
                "l": 50,
                "r": 50,
                "b": 100,
                "t": 100,
                "pad": 40
            },
            "colorway" : ['#f3cec9', '#e7a4b6', '#cd7eaf', '#a262a9', '#6f4d96', '#3d3b72', '#182844'],
            "template":"seaborn"
            }
        ts = ts.corr()
        data = [{
        "z":[ts["Education"].to_list(),ts["Marital_Status"].to_list(),ts["Income"].to_list(),ts["Recency"].to_list(),
            ts["Complain"].to_list(),ts["Age"].to_list(),ts["Engaged_Days"].to_list(),ts["Kids"].to_list(),ts["TotalAcceptedCampaign"].to_list(),
             ts["NumTotalPurchases"].to_list(),ts["Expenses"].to_list()],
        "x":["Education","Marital_Status","Income","Recency","Complain","Age",
            "Engaged_Days","Kids","TotalAcceptedCampaign","NumTotalPurchases", "Expenses"],
        "y":["Education","Marital_Status","Income","Recency","Complain","Age",
            "Engaged_Days","Kids","TotalAcceptedCampaign","NumTotalPurchases", "Expenses"],"type": "heatmap","name":"corr",
        "square":True,"vmin":-1,"vmax":1,"center":0,"annot":True,"camp":"coolwarm","fmt":".2f"
        }
        ]
        graphJSON = (jsonify([{"data":data}]))
    return graphJSON


sns.set(style="whitegrid")
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('pages/placeholder.home.html')

@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')

@app.route('/graphable')
def graphable():
    date = [str(i)[:10] for i in ts.index.to_list()]
    if request.method == 'POST':
        return render_template('pages/placeholder.eda.html',
                                listStatus = date,
                                data = (min(date),max(date)))
    else:   
        select_start = request.form.get('date-select-start')
        select_end = request.form.get('date-select-end')
        return render_template('pages/placeholder.eda.html',
                                listStatus = date,
                                data = (select_start,select_end))

@app.route('/Cluster')
def Cluster():
    values = [str(i) for i in range(1,18)]
    return render_template('pages/placeholder.cluster.html',Kvalue=values)

@app.route('/Prediction')
def Prediction():
    return render_template('pages/placeholder.model.html')

@app.route('/bar', methods=['GET', 'POST'])
def change_features():
    graphJSON= create_plot(ts,"Bar")
    return graphJSON

@app.route('/box', methods=['GET', 'POST'])
def box():
    graphJSON= create_plot(ts,"box")
    return graphJSON
@app.route('/heatmap', methods=['GET', 'POST'])
def heatmap():
    graphJSON= create_plot(ts,"heatmap")
    return graphJSON
@app.route('/pca', methods=['GET', 'POST'])
def pca():
    graphJSON= PCA_analysis(ts)
    return graphJSON
@app.route('/kmeans', methods=['GET', 'POST'])
def kmeans():
    global pca_data
    graphJSON= Kmeans_analysis(pca_data)
    return graphJSON
@app.route('/kmeans_results', methods=['GET', 'POST'])
def kmeans_results():
    global pca_data
    k_v = request.args.get('k_value')
    if k_v:
        graphJSON= Kmeans_results(ts,pca_data,k=int(k_v))
        return graphJSON
    else:
        graphJSON= Kmeans_results(ts,pca_data,k=4)
        return graphJSON
@app.route('/predection_result', methods=['GET', 'POST'])
def predection_result():
    Paras = request.args.get('Paras')
    input_x = json.loads(Paras)
    input_x = input_x[0]["data"]
    input_x = list(map(float,input_x))
    input_x = np.array(input_x).reshape(1,10)
    xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 3, alpha = 10, n_estimators = 200)
    loaded_model = pickle.load(open("models/model.dat", "rb"))
    preds = loaded_model.predict(input_x)
    return str(preds[0])
#     global pca_data
#     graphJSON= Kmeans_analysis(pca_data)
#     return graphJSON
#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    path = "data/data.csv"  
    ts = pd.read_csv(path,index_col=False)
    pca_data = None
    app.run(host="127.0.0.1")

