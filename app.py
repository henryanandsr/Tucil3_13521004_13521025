from flask import Flask, render_template, request, session
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from AStar import AStarBonus, AStar
import reader as read
from UCS import UCS, UCS_B
import folium
import json
# from flask_autoindex import AutoIndex
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
            
            array_node, flag = read.getNode('./test/'+file.filename)
            for i in range (len(array_node)):
                result.append(array_node[i].name)
            # result = result.split('\n')
            session['name'] = file.filename
            return render_template('home.html', result=result, flag = flag)
    else:
        return render_template('home.html')

@app.route('/calc', methods=['POST', 'GET'])
def calc():
    selected_algorithm = request.form.get('options')
    idStart = request.form['Node1']
    idEnd = request.form['Node2']
    coor = False
    if selected_algorithm == 'A*B':
        coor = True
        array_adj, array_node = read.readWithCoor('./test/' + session.get('name', None))
        AstarResult = AStarBonus(array_adj, int(idStart)-1, int(idEnd)-1)
        if (AstarResult):
            result_list = []
            for i in range(len(AstarResult.list)):
                result_list.append([AstarResult.list[i].start.name, AstarResult.list[i].start.X, AstarResult.list[i].start.Y])
            cost = AstarResult.purecost
            # make a map folium
            m = folium.Map(location=[result_list[0][1], result_list[0][2]], zoom_start=12)
            # mark all node first
            for i in range(len(array_node)):
                folium.Marker(location=[array_node[i].X, array_node[i].Y], popup=array_node[i].name).add_to(m)
            # mark all adj
            for el in array_adj:
                for i in range(len(el.adjacent)):
                    folium.PolyLine(locations=[[el.start.X, el.start.Y], [el.adjacent[i][0].X, el.adjacent[i][0].Y]],
                                    color='blue', weight=2.5, opacity=1).add_to(m)
            for i in range(len(result_list)):
                folium.Marker(location=[result_list[i][1], result_list[i][2]], popup=result_list[i][0]).add_to(m)
            # make edge
            for i in range(len(result_list)-1):
                folium.PolyLine(locations=[[result_list[i][1], result_list[i][2]], [result_list[i+1][1], result_list[i+1][2]]],
                                color="red", weight=2.5, opacity=1).add_to(m)
            m.save('static/result.html')
        else:
            return render_template('home.html', msg="Tidak ada jalur")
    elif selected_algorithm == "A*":
        # clear plot
        plt.clf()
        array_adj, array_node = read.read('./test/'+session.get('name', None))
        AstarResult = AStar(array_adj, int(idStart)-1, int(idEnd)-1)
        if (AstarResult):
            result_list = []
            for i in range(len(AstarResult.list)):
                result_list.append(AstarResult.list[i].start.name)
            cost = AstarResult.cost
            # Visualisasi graf
            G = nx.DiGraph()
            for tempAdj in array_adj:
                for i in range(len(tempAdj.adjacent)):
                    G.add_edge(tempAdj.start.name, tempAdj.adjacent[i][0].name, weight=tempAdj.adjacent[i][1])
            # set warna edge
            edge_colors = [G[u][v]['color'] if 'color' in G[u][v] else 'black' for u, v in G.edges()]
            # set posisi node
            pos = nx.spring_layout(G)
            # gambar graf
            nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2, arrows=False)
            nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue')
            nx.draw_networkx_labels(G, pos, font_size=7, font_family='sans-serif')
            # set warna edge hasil
            red_edges = [(AstarResult.list[i].start.name, AstarResult.list[i+1].start.name) for i in range(len(AstarResult.list)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='red', width=2, arrows=False)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
            #save the graph
            plt.savefig('static/result.png')
        else:
            return render_template('home.html', msg="Tidak ada jalur")
        
    elif selected_algorithm == "UCS_B":    
        coor = True
        array_adj, array_node = read.readWithCoor('./test/' + session.get('name', None))
        try:
            UCS_Result = UCS_B(array_node[int(idStart)-1], array_node[int(idEnd)-1], array_adj)
        except:
            return render_template('home.html', msg="Terjadi Error")
    
        if (UCS_Result):
            result_list = []
            for i in range(len(UCS_Result[0])):
                result_list.append([UCS_Result[0][i].name, UCS_Result[0][i].X, UCS_Result[0][i].Y])
            cost = UCS_Result[1] / 100
            # make a map folium
            m = folium.Map(location=[result_list[0][1], result_list[0][2]], zoom_start=12)
            # mark all node first
            for i in range(len(array_node)):
                folium.Marker(location=[array_node[i].X, array_node[i].Y], popup=array_node[i].name).add_to(m)
            # mark all adj
            for el in array_adj:
                for i in range(len(el.adjacent)):
                    folium.PolyLine(locations=[[el.start.X, el.start.Y], [el.adjacent[i][0].X, el.adjacent[i][0].Y]],
                                    color='blue', weight=2.5, opacity=1).add_to(m)
            for i in range(len(result_list)):
                folium.Marker(location=[result_list[i][1], result_list[i][2]], popup=result_list[i][0]).add_to(m)
            # make edge
            for i in range(len(result_list)-1):
                folium.PolyLine(locations=[[result_list[i][1], result_list[i][2]], [result_list[i+1][1], result_list[i+1][2]]],
                                color="red", weight=2.5, opacity=1).add_to(m)
            m.save('static/result.html')
        else:
            return render_template('home.html', msg="Tidak ada jalur")
        
    elif selected_algorithm == "UCS":
        # clear plot
        plt.clf()
        array_adj, array_node = read.read('./test/'+session.get('name', None))
        try:
            UCS_Result = UCS(array_node[int(idStart)-1], array_node[int(idEnd)-1], array_adj)
        except:
            return render_template('home.html', msg="Terjadi Error")
    
        if (UCS_Result):
            result_list = []
            for i in range(len(UCS_Result[0])):
                result_list.append(UCS_Result[0][i].name)
            cost = UCS_Result[1] / 100
            # Visualisasi graf
            G = nx.DiGraph()
            for tempAdj in array_adj:
                for i in range(len(tempAdj.adjacent)):
                    G.add_edge(tempAdj.start.name, tempAdj.adjacent[i][0].name, weight=tempAdj.adjacent[i][1])
            # set warna edge
            edge_colors = [G[u][v]['color'] if 'color' in G[u][v] else 'black' for u, v in G.edges()]
            # set posisi node
            pos = nx.spring_layout(G)
            # gambar graf
            nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=2, arrows=False)
            nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='lightblue')
            nx.draw_networkx_labels(G, pos, font_size=7, font_family='sans-serif')
            # set warna edge hasil
            red_edges = [(UCS_Result[0][i].name, UCS_Result[0][i+1].name) for i in range(len(UCS_Result[0])-1)]
            nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='red', width=2, arrows=False)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
            #save the graph
            plt.savefig('static/result.png')
        else:
            return render_template('home.html', msg="Tidak ada jalur")
    
    if (coor):
        cost = cost* 111320
        return render_template('index2.html', cost = cost, result = result_list)
    else :
        return render_template('index.html', cost = cost, result  = result_list)
if __name__ == "__main__":
    app.run(debug=True)