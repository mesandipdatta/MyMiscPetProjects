def dashapp(graph_type,app):
    import dash
    from dash.dependencies import Event, Output
    import dash_html_components as html
    import dash
    from dash.dependencies import Input, Output
    import dash_core_components as dcc
    import dash_html_components as html
    from pandas_datareader import data as web
    from datetime import datetime as dt
    import pandas as pd

    # Functionality Specific
    import sys

    gtype = graph_type
    print "===== Building the Data & Graph layout ====="
    print "===== Plotting a "+ gtype


    def barchart(app):
        app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for Python.
        '''),

        dcc.Graph(
            id='example-graph',
            figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization'
                    }
                }
            )
        ])

    def scatterplot(app):
        app.layout = html.Div([
                      html.H1('Hello - Stock Tickers'),
                      dcc.Dropdown( id='my-dropdown',
                                    options=[ {'label': 'Coca Cola', 'value': 'COKE'},
                                            {'label': 'Tesla', 'value': 'TSLA'},
                                            {'label': 'Apple', 'value': 'AAPL'},
                                            {'label': 'Amazon', 'value': 'AMZN'},
                                            {'label': 'Microsoft', 'value': 'MSFT'},
                                            {'label': 'Google', 'value': 'GOOG'} 
                                          ],
                                    value='MSFT'  # Default on the drop-down
                                    ),
                      dcc.Graph(id='my-graph')
                      ])

        @app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
        def update_graph(selected_dropdown_value):
            df = web.DataReader(selected_dropdown_value, 
                                data_source='google',
                                start=dt(2017, 7, 1), 
                                end=dt.now() )
            
            # Print and check the raw stock data downloaded
            #print df

            # Define the Graph to be created
            return {
                    'data': [{'x': df.index, # X-axis data
                              'y': df.Close  # Y-axis data - Stock "Close" price 
                            }]
                    }

    def htmltable(app):
        df = pd.read_csv(
        'https://gist.githubusercontent.com/chriddyp/'
        'c78bf172206ce24f77d6363a2d754b59/raw/'
        'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
        'usa-agricultural-exports-2011.csv')

        def generate_table(dataframe, max_rows=10):
            return html.Table(
                # Header
                [html.Tr([html.Th(col) for col in dataframe.columns])] +

                # Body
                [html.Tr([
                    html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ]) for i in range(min(len(dataframe), max_rows))]
            )

        app.layout = html.Div(children=[
        html.H4(children='US Agriculture Exports (2011)'),
        generate_table(df)
        ])


    #=== Bar Chart
    if gtype == "bar" :
        barchart(app)

    #=== Scatter Plot
    if gtype == "scatter" :
        scatterplot(app)

    #=== HTML table
    if gtype == "table" :
        htmltable(app)

    #=== Run Dash Server
    # app.run_server(debug=True)


