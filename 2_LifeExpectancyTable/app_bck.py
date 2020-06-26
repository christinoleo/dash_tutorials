import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_table
import pandas as pd
from dash.dependencies import Output, Input, State

df = pd.read_csv('life_expectancy_years.csv')

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], show_undo_redo=True)

app.layout = dbc.Container([
    dbc.Button("Previous", className="mr-1", id='previous-page'),
    dbc.Button("Next", className="mr-1", id='next-page'),
    dash_table.DataTable(
        id='table',
        data=df.to_dict('records'),
        sort_action='native',
        page_size=30,
    ),
    html.Div(hidden=True, id='table-page')
], className="p-5", fluid=True)


@app.callback(
    output=Output('table-page', 'children'),
    inputs=[
        Input('next-page', 'n_clicks'),
        Input('previous-page', 'n_clicks'),
    ],
    state=[State('table-page', 'children')])
def paginate_table(next, prev, page):
    if page == None: page = 0
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'next-page' in changed_id:
        page += 1
    elif 'previous-page' in changed_id:
        page -= 1
    page = max(0, page)
    return page


@app.callback(
    output=Output('table', 'columns'),
    inputs=[Input('table-page', 'children'),],)
def paginate_table(page):
    if page == None: page = 0
    print(page)
    return [{"name": i, "id": i} for i in df.columns[page*10:(page+1)*10]]


if __name__ == "__main__":
    app.run_server(debug=True)
