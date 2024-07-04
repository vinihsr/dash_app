from dash import dcc, html

# Define the layout of the app
layout = html.Div([
    # Header
    html.Div([
        html.H1("File Analysis Dash App", style={'textAlign': 'center'}),
    ], style={'padding': '20px', 'backgroundColor': '#f8f9fa'}),

    # File upload section
    html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select a File')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Allow multiple files to be uploaded
            multiple=False
        ),
        html.Div(id='output-data-upload')
    ]),

    # Graph section
    html.Div([
        dcc.Graph(id='data-graph')
    ], style={'padding': '20px'})
])
