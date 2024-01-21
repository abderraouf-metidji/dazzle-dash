from dash import html, dash_table, dcc
from dash_table.Format import Format

def generate_layout(df, years, variables_first_dropdown, variables_second_dropdown):
    # Create the main layout div
    layout = html.Div([
        # Title
        html.H1(children='Life expectancy Dashboard', style={'fontSize': 32, 'textAlign': 'center', 'fontFamily': 'Arial, sans-serif'}),
        
        # Horizontal line
        html.Hr(),
        
        # Data table
        dash_table.DataTable(
            id='data-table',
            data=df.to_dict('records'),
            page_size=10,
            style_table={'overflowX': 'auto', 'fontFamily': 'Arial, sans-serif'},
            style_header={'fontWeight': 'bold', 'fontSize': 18},
            style_cell={'fontSize': 14, 'textAlign': 'center'},    
        ),
        
        # First graph section
        html.Div([
            html.Div([
                # Dropdown for selecting year
                dcc.Dropdown(
                    id='year-dropdown-first-graph',
                    options=[{'label': year, 'value': year} for year in years],
                    value=2015,
                    style={'width': '50%', 'display': 'inline-block', 'marginRight': '20px'},
                ),
                # Dropdown for selecting variable
                dcc.Dropdown(
                    id='variable-dropdown-first-graph',
                    options=variables_first_dropdown,
                    value='Life expectancy',
                    style={'width': '50%', 'display': 'inline-block'},
                ),
            ], style={'padding': '20px', 'width': '70%', 'margin': '0 auto'}),
            
            # First graph
            dcc.Graph(figure={}, id='first-graph', style={'width': '70%', 'margin': '0 auto'}),
            
            # Second graph section
            html.Div([
                # Dropdown for selecting year
                dcc.Dropdown(
                    id='year-dropdown-second-graph',
                    options=[{'label': year, 'value': year} for year in years],
                    value=2015,
                    style={'width': '50%', 'display': 'inline-block', 'marginRight': '20px'},
                ),
                # Dropdown for selecting variable
                dcc.Dropdown(
                    id='variable-dropdown-second-graph',
                    options=variables_second_dropdown,
                    value='GDP vs Percentage expenditure',
                    style={'width': '50%', 'display': 'inline-block'},
                ),
            ], style={'padding': '20px', 'width': '70%', 'margin': '0 auto'}),
            
            # Second graph
            dcc.Graph(figure={}, id='second-graph', style={'width': '70%', 'margin': '0 auto'})
        ], style={'width': '80%', 'margin': '0 auto'})
    ])
    
    return layout