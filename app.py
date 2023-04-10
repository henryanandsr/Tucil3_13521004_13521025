from flask import Flask, render_template, request, session
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from AStar import AStarBonus
from AStar import Main
import folium
import json
from flask_autoindex import AutoIndex

app = Flask(__name__,template_folder='display')
app.secret_key = 'asterisk'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    print("aku saya")
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return render_template('home.html')
        else:
            # result = file.read().decode('utf-8')
            result = []
            array_adj, array_node = Main.readWithCoor('./test/'+file.filename)
            for i in range (len(array_node)):
                result.append(array_node[i].name)
            # result = result.split('\n')
            session['name'] = file.filename
            return render_template('home.html', result=result)
    else:
        return render_template('home.html')

@app.route('/calc', methods = ['POST','GET'])
def calc():
    selected_algorithm = request.form.get('options')
    print(selected_algorithm)
    array_adj, array_node = Main.readWithCoor('./test/'+session.get('name', None))
    idStart = request.form['Node1']
    idEnd = request.form['Node2']
    if (selected_algorithm ==  'A*B'):
        AstarResult = AStarBonus(array_adj, int(idStart)-1, int(idEnd)-1)
        result_list = []
        for i in range (len(AstarResult.list)):
            result_list.append([AstarResult.list[i].start.name, AstarResult.list[i].start.X, AstarResult.list[i].start.Y])
        cost = AstarResult.purecost
        # make a map folium
        m = folium.Map(location=[result_list[0][1], result_list[0][2]], zoom_start=12)
        # mark all node first
        for i in range (len(array_node)):
            folium.Marker(location=[array_node[i].X, array_node[i].Y], popup=array_node[i].name).add_to(m)
        # mark all adj
        for el in array_adj:
            for i in range(len(el.adjacent)):
                folium.PolyLine(locations=[[el.start.X, el.start.Y], [el.adjacent[i][0].X, el.adjacent[i][0].Y]], color='blue', weight = 2.5, opacity = 1 ).add_to(m)
                print(el.start.X, el.start.Y, el.adjacent[i][0].X, el.adjacent[i][0].Y)
        for i in range (len(result_list)):
            folium.Marker(location=[result_list[i][1], result_list[i][2]], popup=result_list[i][0]).add_to(m)
        # make edge
        for i in range (len(result_list)-1):
            folium.PolyLine(locations=[[result_list[i][1], result_list[i][2]], [result_list[i+1][1], result_list[i+1][2]]], color="red", weight=2.5, opacity=1).add_to(m)
    m.save('static/result.html')
    return render_template('index2.html', cost = cost, result = result_list)
if __name__ == "__main__":
    print("ghambar")
    app.run(debug=True)