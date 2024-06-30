from dash import dcc, html

# Define the layout of the app
layout = html.Div([
    # Header
    html.Div([
        html.H1("Dash Application", style={'textAlign': 'center'}),
    ], style={'padding': '20px', 'backgroundColor': '#f8f9fa'}),

    # Input section
    html.Div([
        html.Label("Enter some text:"),
        dcc.Input(id='input-text', value='', type='text', style={'marginRight': '10px'}),
        html.Button('Submit', id='submit-button', n_clicks=0)
    ], style={'padding': '20px'}),

    # Output section
    html.Div([
        html.H3("Output:"),
        html.Div(id='output-div', style={'padding': '10px', 'border': '1px solid #ccc'})
    ], style={'padding': '20px'}),

    # Graph section
    html.Div([
        dcc.Graph(
            id='example',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'NYC'},
                ],
                'layout': {
                    'title': 'Bar Plots'
                }
            }
        )
    ], style={'padding': '20px'})
])
