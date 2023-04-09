from flask import Flask, render_template, request, session
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from AStar import AStarBonus
from AStar import Main
import json

app = Flask(__name__,template_folder='display')
app.secret_key = 'asterisk'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
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
@app.route('/result', methods=['POST'])
def result():
    array_adj, array_node = Main.readWithCoor('./test/'+session.get('name', None))
    idStart = request.form['Node1']
    idEnd = request.form['Node2']
    AstarResult = AStarBonus(array_adj, int(idStart)-1, int(idEnd)-1)
    nodes_json = []
    tempList = []
    print(len(AstarResult.list))
    for i in range (len(AstarResult.list)):
        tempList.extend(AstarResult.list[i].start.name, AstarResult.list[i].start.x, AstarResult.list[i].start.y)
    for el in tempList:
        node_dict = {
            'id': el[0],
            'x': el[1],
            'y': el[2]
        }
        nodes_json.append(node_dict)
        session['nodes_json'] = nodes_json
        session['nodes_notJSON'] = tempList
    return render_template('result.html', nodes_json = nodes_json)
@app.route('/calc', methods = ['POST'])
def calc():
    nodes_json = session.get('nodes_json', None)
    nodes_notJSON = session.get('nodes_notJSON', None)
    center = [-7, 108.773628]
    return render_template('index.html', nodes_json = nodes_json, center = center, nodes_notJSON = nodes_notJSON)
if __name__ == "__main__":
    app.run(debug=True)