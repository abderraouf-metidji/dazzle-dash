from dash import callback, Output, Input
import plotly.express as px

def register_callbacks(app, df):
    # Callback to update first graph
    @app.callback(
        Output(component_id='first-graph', component_property='figure'),
        [Input(component_id='variable-dropdown-first-graph', component_property='value'),
         Input(component_id='year-dropdown-first-graph', component_property='value')]
    )
    def update_first_graph(selected_variable_first_graph, selected_year_first_graph):
        # Filter data based on selected year
        df_specific_variable_first_graph = df[df['Year'] == selected_year_first_graph]
        
        # Check if 'vs' is in the selected variable
        if 'vs' in selected_variable_first_graph:
            return {'data': [], 'layout': {}}
        else:
            # Create histogram figure
            fig = px.histogram(df_specific_variable_first_graph, x=selected_variable_first_graph,
                                title=f'Distribution of {selected_variable_first_graph}')
            fig.update_layout(template='plotly_dark')
            return fig
    
    # Callback to update second graph for variable vs variable
    @app.callback(
        Output(component_id='second-graph', component_property='figure'),
        [Input(component_id='variable-dropdown-second-graph', component_property='value'),
         Input(component_id='year-dropdown-second-graph', component_property='value')]
    )
    def update_second_graph(selected_variable_second_graph, selected_year_second_graph):
        # Filter data based on selected year
        df_specific_variable_second_graph = df[df['Year'] == selected_year_second_graph]
        
        # Check if 'vs' is not in the selected variable
        if 'vs' not in selected_variable_second_graph:
            return {'data': [], 'layout': {}}
        else:
            # Split the selected variable into two variables
            variable1, variable2 = selected_variable_second_graph.split(' vs ')
            
            # Create scatter plot figure
            fig = px.scatter(df_specific_variable_second_graph, x=variable1, y=variable2,
                              title=f'{variable1} vs {variable2}')
            fig.update_layout(template='plotly_dark')
            return fig