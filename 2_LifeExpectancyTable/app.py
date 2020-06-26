import dash
import dash_table
import pandas as pd
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Output, Input, State

df = pd.read_csv("life_expectancy_years.csv")

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container([
    dbc.Button("Previous", color="secondary", className="mr-1", id="b-prev"),
    dbc.Button("Next", color="secondary", className="mr-1", id="b-next"),
    dash_table.DataTable(
        id='table',
        # columns=[{"name": i, "id": i} for i in df.columns[0:10]],
        data=df.to_dict('records'),
        page_size=30,
    ),
    html.Div(id='page', hidden=True)
])


@app.callback(Output('page', 'children'),
              [Input('b-prev', 'n_clicks'),
               Input('b-next', 'n_clicks')],
              [State('page', 'children')])
def update_page(bprev, bnext, page):
    if page == None: page = 0
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'b-prev' in changed_id:
        page -= 1
    if 'b-next' in changed_id:
        page += 1
    return page


@app.callback(Output('table', 'columns'),
              [Input('page', 'children')]
              )
def paginate(page):
    if page == None: page = 0
    return [{"name": df.columns[0], "id": df.columns[0]}] + [{"name": i, "id": i} for i in df.columns[1+page*10:1+(page+1)*10]]


if __name__ == '__main__':
    app.run_server(debug=True)