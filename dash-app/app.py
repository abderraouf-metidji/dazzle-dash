import pandas as pd
from dash import Dash
import layout
import callbacks

# Read the csv file
df = pd.read_csv('data/life_expectancy_data.csv')

# Get unique years
years = df['Year'].unique()

# Define the options for the first dropdown
variables_first_dropdown = [
    {'label': 'Country', 'value': 'Country'},
    {'label': 'Status', 'value': 'Status'},
    {'label': 'Life expectancy', 'value': 'Life expectancy'},
    {'label': 'Adult Mortality', 'value': 'Adult Mortality'},
    {'label': 'Infant deaths', 'value': 'Infant deaths'},
    {'label': 'Alcohol', 'value': 'Alcohol'},
    {'label': 'Percentage expenditure', 'value': 'Percentage expenditure'},
    {'label': 'Hepatitis B', 'value': 'Hepatitis B'},
    {'label': 'Measles', 'value': 'Measles'},
    {'label': 'BMI', 'value': 'BMI'},
    {'label': 'Under-five deaths', 'value': 'Under-five deaths'},
    {'label': 'Polio', 'value': 'Polio'},
    {'label': 'Total expenditure', 'value': 'Total expenditure'},
    {'label': 'Diphtheria', 'value': 'Diphtheria'},
    {'label': 'HIV/AIDS', 'value': 'HIV/AIDS'},
    {'label': 'GDP', 'value': 'GDP'},
    {'label': 'Population', 'value': 'Population'},
    {'label': 'Thinness 1-19 years', 'value': 'Thinness 1-19 years'},
    {'label': 'Thinness 5-9 years', 'value': 'Thinness 5-9 years'},
    {'label': 'Income composition of resources', 'value': 'Income composition of resources'},
    {'label': 'Schooling', 'value': 'Schooling'}
]

# Define the options for the second dropdown
variables_second_dropdown = [
    {'label': 'GDP vs Percentage expenditure', 'value': 'GDP vs Percentage expenditure'},
    {'label': 'Life expectancy vs GDP', 'value': 'Life expectancy vs GDP'},
    {'label': 'Life expectancy vs Schooling', 'value': 'Life expectancy vs Schooling'},
    {'label': 'Life expectancy vs Percentage expenditure', 'value': 'Life expectancy vs Percentage expenditure'},
    {'label': 'Life expectancy vs BMI', 'value': 'Life expectancy vs BMI'},
    {'label': 'Life expectancy vs Polio', 'value': 'Life expectancy vs Polio'},
    {'label': 'Life expectancy vs Alcohol', 'value': 'Life expectancy vs Alcohol'},
    {'label': 'Life expectancy vs Population', 'value': 'Life expectancy vs Population'}
]

# Create the Dash app
app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

# Generate the layout using the layout module
app.layout = layout.generate_layout(df, years, variables_first_dropdown, variables_second_dropdown)

# Register the callbacks using the callbacks module
callbacks.register_callbacks(app, df)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)