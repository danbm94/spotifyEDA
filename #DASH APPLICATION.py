#DASH APPLICATION
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import os 




df = pd.read_csv("collab.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Dash Application: Artist', style={'textAlign':'center'}),
    dcc.Dropdown(df.artist.unique(), 'Bándalos Chinos', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='gdpPercap')

if __name__ == '__main__':
    app.run(debug=True)
