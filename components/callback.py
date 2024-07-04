import base64
import io
import pandas as pd
from dash.dependencies import Input, Output, State
from dash import dcc, html
from utils.data_processing import parse_contents, generate_graph

def register_callbacks(app):
    @app.callback(
        [Output('output-data-upload', 'children'),
         Output('data-graph', 'figure')],
        [Input('upload-data', 'contents')],
        [State('upload-data', 'filename'),
         State('upload-data', 'last_modified')]
    )
    def update_output(contents, filename, last_modified):
        if contents is not None:
            children, df = parse_contents(contents, filename)
            figure = generate_graph(df)
            return children, figure
        return html.Div(['No data uploaded']), {}
