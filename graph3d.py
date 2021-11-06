import pandas as pd
import plotly.express as px

def plot3D(df):
    fig = px.scatter_3d(
        df, x=0, y=1, z=2, 
        color=df['color'],
        title="Plot in 3D",
        labels={'0': 'Type 0', '1': 'Type 1', '2': 'Type 2'}
    )
    fig.savefig("out.png")

def todf(x,y,z,col_type):
    df = pd.DataFrame()
    df["x-axis"] = x
    df["y-axis"] = y
    df["z-axis"] = z
    df["color"] = col_type
    return df

def plot2D(df):
    fig = px.scatter_3d(
        df, x=0, y=1, 
        color=df['color'],
        title="Plot in 2D",
        labels={'0': 'Type 0', '1': 'Type 1'}
    )
    fig.savefig("out.png")

def todf(x,y,col_type):
    df = pd.DataFrame()
    df["x-axis"] = x
    df["y-axis"] = y
    df["color"] = col_type
    return df