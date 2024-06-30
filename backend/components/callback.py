from dash.dependencies import Input, Output

def register_callbacks(app):
    @app.callback(
        Output('output-div', 'children'),
        [Input('input-text', 'value')]
    )
    def update_output(value):
        return f'You\'ve entered: {value}'
