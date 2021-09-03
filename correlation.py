from numpy.core.numeric import correlate
import pandas as pd
import statistics as st
import plotly.express as px
import numpy as np

def plot_graph(data, x, y):
    fig = px.scatter(data, x = x, y = y)
    fig.show()

def main():
    name = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    df = pd.read_csv(name)
    col_x = "Temperature"
    col_y = "Ice-cream Sales( ₹ )"
    correlation = np.corrcoef(df[col_x].tolist(), df[col_y].tolist())
    print(f"correlation between {col_x}and {col_y} is", correlation[0,1])
    plot_graph(df, col_x, col_y)

main()