import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def plot1D(x, color):
    fig = px.scatter(
        x=x,
        y=[1 for _ in range(len(x))],
        color=color,
        title="Plot in 1D",
        labels = {"0": "Type 0"}
    )
    fig.show()

def plot3D(df, line=False):
    if line:
        fig = go.Figure()
        fig = fig.add_trace(
            go.Scatter(
                x=df["x"],
                y=df["y"],
                z=df["z"]
            )
        )
    else:
        fig = px.scatter_3d(
            df, x="x", y="y", z="z", 
            color=df['color'],
            title="Plot in 3D",
            labels={'0': 'Type 0', '1': 'Type 1', '2': 'Type 2'}
        )
    fig.show()

def todf3D(x,y,z,col_type):
    dfx = pd.DataFrame({"x": x})
    dfy = pd.DataFrame({"y": y})
    dfz = pd.DataFrame({"z": z})
    dfcolors = pd.DataFrame({"color": col_type})
    df = pd.concat([dfx, dfy, dfz, dfcolors], axis=1)
    return df

def plot2D(df, line=False):
    if line:
        fig = go.Figure()
        fig = fig.add_trace(
            go.Scatter(
                x=df["x"],
                y=df["y"]
            )
        )
    else:
        fig = px.scatter(
            df, x='x', y='y', 
            color=df['color'],
            title="Plot in 2D",
            labels={'0': 'Type 0', '1': 'Type 1'}
        )
    fig.show()

def todf2D(x, y, col_type):
    dfx = pd.DataFrame({"x": x})
    dfy = pd.DataFrame({"y": y})
    dfcolors = pd.DataFrame({"color": col_type})
    df = pd.concat([dfx, dfy, dfcolors], axis=1)
    return df

if __name__ == "__main__":
    x = [1,2,3]
    y = [1,2,3]
    z = [1,2,3]
    colors = [0,1,2]
    plot3D(todf3D(x,y,z,colors))