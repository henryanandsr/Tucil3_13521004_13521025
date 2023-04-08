from flask import Flask, render_template
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__,template_folder='display')
@app.route("/")
def MainPage():
    x = np.arange(0, 20, 0.1)
    y = np.sin(x)
    fig = plt.figure()
    plt.plot(x, y)
    fig.savefig("./static/plot1.png")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)