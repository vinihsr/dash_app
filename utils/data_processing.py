import base64
import io
import pandas as pd
from dash import dcc, html

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an Excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        return html.Div([
            'There was an error processing this file.'
        ]), None
    
    return html.Div([
        html.H5(filename),
        html.H6('Last Modified: ' + str(pd.to_datetime('today'))),

        dcc.Graph(
            id='example-graph',
            figure=generate_graph(df)
        ),
        
        html.Hr(),  # horizontal line

        html.Div('Raw Content'),
        html.Pre(df.head().to_csv(index=False), style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ]), df

def generate_graph(df):
    # Create a sample graph
    return {
        'data': [{
            'x': df[df.columns[0]],
            'y': df[df.columns[1]],
            'type': 'line',
            'name': 'Line Graph'
        }],
        'layout': {
            'title': 'Sample Graph'
        }
    }
