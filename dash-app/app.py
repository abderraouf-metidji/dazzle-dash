# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('data/life_expectancy_data.csv')

df_specific_year = df[df['Year'] == 2015]

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='Life expectancy'),
    html.Hr(),
    dcc.RadioItems(
        id='controls-and-radio-item',
        options=[
            {'label': 'Life expectancy', 'value': 'Life expectancy'},
            {'label': 'GDP', 'value': 'GDP'},
            {'label': 'Population', 'value': 'Population'},
            {'label': 'HIV/AIDS', 'value': 'HIV/AIDS'}
        ],
        value='Life expectancy'
    ),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure={}, id='controls-and-graph')
])

@app.callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)

def update_graph(col_chosen):
    fig = px.histogram(df_specific_year, x=col_chosen)
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
