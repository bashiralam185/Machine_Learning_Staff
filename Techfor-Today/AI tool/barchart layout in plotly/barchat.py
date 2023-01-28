# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import plotly.graph_objects as go
# from dash import Dash, html, dcc, Input, Output

# # creating the dash app
# app = dash.Dash()

# #creating the dataset
# x = ['apple', 'banana', 'orange', 'grape']
# y = [4, 2, 3, 5]


# # creating a bar chart
# trace = go.Bar(x=x, y=y)

# # layout
# layout = go.Layout(
#     title='Fruit Counts',
#     xaxis={'title': 'Fruit'},
#     yaxis={'title': 'Count'}
# )

# layout = go.Layout(
#     title='Fruit Counts',
#     xaxis={'title': 'Fruit', 'range': [0, 5]},
#     yaxis={'title': 'Count', 'range': [0, 6]}
# )

# # giving the app  layout
# #this layout is done using html
# app.layout = html.Div([
#     html.H1('My Dashboard'),
#     html.Div([
#         dcc.Dropdown(
#             id='fruit-dropdown',
#             options=[{'label': fruit, 'value': fruit} for fruit in x],
#             value='apple'
#         ),
#         dcc.Graph(id='bar-chart', figure={'data': [trace], 'layout': layout})
#     ])
# ])



# @app.callback(
#     Output('bar-chart', 'figure'),
#     [Input('fruit-dropdown', 'value')]
# )
# def update_bar_chart(selected_fruit):
#     y = [4 if fruit == selected_fruit else 0 for fruit in x]
#     trace = go.Bar(x=x, y=y, marker={'color': ['red', 'green', 'blue', 'orange']})
#     layout = go.Layout(
#         title='Fruit Counts',
#         xaxis={'title': 'Fruit', 'range': [0, 5]},
#         yaxis={'title': 'Count', 'range': [0, 6]}
#     )
#     return {'data': [trace], 'layout': layout}





# #running the server
# if __name__ == '__main__':
#     app.run_server(debug=True)


import networkx as nx

G = nx.complete_graph(5)

nx.draw_networkx(G)
