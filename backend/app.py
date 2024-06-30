import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from components.layout import layout
from components.callback import register_callbacks

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the layout
app.layout = layout

# Register callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
