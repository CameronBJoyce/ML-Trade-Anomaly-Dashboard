import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

# Assuming 'trade_data' and 'anomalies' are already available

# Create Dash app
app = dash.Dash(__name__)

# Create layout
app.layout = html.Div(
    children=[
        html.H1('Trade Data Analysis Dashboard', style={'text-align': 'center', 'margin-top': '30px'}),
        html.H2('Trade Data Trends', style={'margin-top': '40px', 'margin-bottom': '20px'}),
        html.Div(
            children=[
                dcc.Graph(
                    id='trade-data-trends',
                    figure={
                        'data': [
                            go.Scatter(x=trade_data['Year'], y=trade_data['Import Value'], name='Import Value'),
                            go.Scatter(x=trade_data['Year'], y=trade_data['Export Value'], name='Export Value'),
                            go.Scatter(x=trade_data['Year'], y=trade_data['Total Trade Value'], name='Total Trade Value')
                        ],
                        'layout': go.Layout(
                            xaxis={'title': 'Year'},
                            yaxis={'title': 'Trade Value'},
                            hovermode='closest',
                            height=400
                        )
                    }
                )
            ],
            style={'width': '80%', 'margin': 'auto'}
        ),
        html.H2('Detected Anomalies', style={'margin-top': '40px', 'margin-bottom': '20px'}),
        html.Div(
            children=[
                dcc.Graph(
                    id='detected-anomalies',
                    figure={
                        'data': [
                            go.Scatter(
                                x=anomalies['Trade Data'],
                                y=anomalies['Reconstruction Error'],
                                mode='markers',
                                marker=dict(
                                    color=anomalies['Anomaly'],
                                    colorscale='Viridis',
                                    size=8,
                                    showscale=True
                                )
                            )
                        ],
                        'layout': go.Layout(
                            xaxis={'title': 'Trade Data'},
                            yaxis={'title': 'Reconstruction Error'},
                            hovermode='closest',
                            height=400
                        )
                    }
                )
            ],
            style={'width': '80%', 'margin': 'auto'}
        ),
        html.H2('Trade Data Summary', style={'margin-top': '40px', 'margin-bottom': '20px'}),
        html.Div(
            children=[
                dcc.Markdown(
                    '''
                    The trade data summary includes the statistics and aggregated values of the trade data.
                    '''
                ),
                html.Table(
                    children=[
                        html.Tr(
                            [html.Th(col) for col in trade_data.columns],
                            style={'background-color': '#f2f2f2'}
                        ),
                        *[
                            html.Tr([html.Td(data) for data in row.values])
                            for _, row in trade_data.describe().iterrows()
                        ]
                    ],
                    style={'margin': '20px'}
                )
            ],
            style={'width': '80%', 'margin': 'auto'}
        )
    ],
    style={'font-family': 'Arial'}
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
