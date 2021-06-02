import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import base64
# import sqlalchemy as db
#
# engine = db.create_engine('sqlite:///shows.db')
# connection = engine.connect()

# if i just had pictures flow from folder
#os.list_dir(pictures)
#how do they match them
#pd.read_csv(metadata.csv)? then i have to update this in additon to uploading pictures
#title, twitter user, page index

COOKIE = "https://todaysmama.com/.image/t_share/MTU5OTEwMzkyMDIyMTE1NzAz/cookie-monster.png"

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# i have to break it down to base64 encoding bc html
image_filename = '/kandinsky.jpeg' # logo
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
#'data:image/png;base64,{}'.format(encoded_image.decode())

app.layout = dbc.Container(
    [
        #2 x 3 of pictures fits well on phone the src will need to change when you go to the 'next page'
        dbc.Row(
            [
                dbc.Col(html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),id='img_click0',
                                 style={"width": "100%"})),
                dbc.Col(html.Img(src=COOKIE, id='img_click1', style={"width": "100%"})),
            ]
        ),

        dbc.Row(
            [
                dbc.Col(html.Img(src=COOKIE, id='img_click2', style={"width": "100%"})),
                dbc.Col(html.Img(src=COOKIE, id='img_click3', style={"width": "100%"})),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.Img(src=COOKIE, id='img_click4', style={"width": "100%"})),
                dbc.Col(html.Img(src=COOKIE, id='img_click5', style={"width": "100%"})),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Button("Prev page", id="button_prev")),
                dbc.Col(dbc.Button("Next Page", id="button_next")),
            ]
        ),

        # the modals are the pop outs of the picture they are in divs bc im going to reset them by rewriting
        # returning new dbc.Modal code with new img src
        html.Div(id='dynamic-modal-container0',
                 children=[
                     dbc.Modal(
                         [
                             dbc.ModalHeader("Cookies!"),
                             dbc.ModalBody(
                                 [html.A('cookie monster', href='https://en.wikipedia.org/wiki/Cookie_Monster'),
                                  html.Img(src=COOKIE, style={"width": "100%"}),
                                  html.Img(src=COOKIE, style={"width": "100%"}),
                                  html.Img(src=COOKIE, style={"width": "100%"})]),
                         ],
                         id="modal1",
                         is_open=False,
                     ),
                 ]),

        html.Div(id='dynamic-modal-container1',
                 children=[
                     dbc.Modal(
                         [
                             dbc.ModalHeader("Cookies!"),
                             dbc.ModalBody([html.A('cookie monster' ,href='https://en.wikipedia.org/wiki/Cookie_Monster'),html.Img(src=COOKIE, style={"width": "100%"}),html.Img(src=COOKIE, style={"width": "100%"}),html.Img(src=COOKIE, style={"width": "100%"})]),
                         ],
                         id="modal1",
                         is_open=False,
                     ),
                 ]),

        html.Div(id='dynamic-modal-container2',
                 children=[
                     dbc.Modal(
                         [
                             dbc.ModalHeader("Cookies!"),
                             dbc.ModalBody(html.Img(src=COOKIE, style={"width": "100%"})),
                         ],
                         id="modal2",
                         is_open=False,
                     ),
                 ]),

        html.Div(id='dynamic-modal-container3',
                 children=[
                     dbc.Modal(
                         [
                             dbc.ModalHeader("Cookies!"),
                             dbc.ModalBody(html.Img(src=COOKIE, style={"width": "100%"})),
                         ],
                         id="modal3",
                         is_open=False,
                     ),
                 ]),
        html.Div(id='dynamic-modal-container4',
                 children=[
                     dbc.Modal(
                         [
                             dbc.ModalHeader("Cookies!"),
                             dbc.ModalBody(html.Img(src=COOKIE, style={"width": "100%"})),
                         ],
                         id="modal4",
                         is_open=False,
                     ),
                 ]),
        html.Div(id='dynamic-modal-container5',
                 children=[
                     dbc.Modal(
                         [
                             dbc.ModalHeader("Cookies!"),
                             dbc.ModalBody(html.Img(src=COOKIE, style={"width": "100%"})),
                         ],
                         id="modal5",
                         is_open=False,
                     ),
                 ]),
    ],
    className="p-5",fluid=True
)


#can i do a for loop but with different id for callback ?
for i in range(6):
    @app.callback(
        Output("modal"+str(i), "is_open"),
        [Input('img_click'+str(i), "n_clicks")],
        [State("modal"+str(i), "is_open")],
    )
    def toggle_modal(n, is_open):
        if n:
            return not is_open
        return is_open



# @app.callback(Output('dynamic-modal-container0', 'children'),Input('button_prev', 'n_clicks'),Input('button_next', 'n_clicks'))
# def load_modal(prev, next):
#     #find which button was clicked
#     new_modal = dbc.Modal(
#                          [
#                              dbc.ModalHeader("Cookies!"),
#                              dbc.ModalBody([html.Img(src=COOKIE, style={"width": "100%"}),html.Img(src=COOKIE, style={"width": "100%"}),html.Img(src=COOKIE, style={"width": "100%"})]),
#                          ],
#                          id="modal1",
#                          is_open=False,
#                      ),
#
#     return new_modal

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0')