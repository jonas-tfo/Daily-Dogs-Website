# run app using python DackelOfTheDay.py in terminal
# visit "http://127.0.0.1:8050/" in web browser 
# run "ssh -R 80:localhost:8050 nokey@localhost.run" to run
# run kill -9 $(lsof -ti:8050) in terminal to close

"""
start python DackelOfTheDay.py
visit: http://127.0.0.1:8050/ 
close: kill -9 $(lsof -ti:8050)
"""


import dash
from dash import html
from dash import dcc
from dash.dependencies import Output, Input
import urllib.request
from datetime import datetime, timedelta
import os
from PIL import Image

# image Dackel URLs for the different days of the week
image_urls_dackel = [
    "https://upload.wikimedia.org/wikipedia/commons/2/28/Dapple-Dachshund.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/d/de/Smooth_Dachshund_red_and_tan_portrait.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/0/02/Jamnik_d%C5%82ugow%C5%82osy_standardowy_LM_671.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/f/f4/MiniDachshund1_wb.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/1/14/Parti-colour_Longhaired_Dachshund.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/c/c8/Short_haired_dachshund_in_race.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/e/e2/Jamnik_Dachshund_puppies.jpg"
]

# image Corgi URLs for different day of the week

image_urls_corgi = [
    "https://upload.wikimedia.org/wikipedia/commons/9/99/Welsh_Pembroke_Corgi.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/7/78/14_year_old_Corgi.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/9/90/Champion_Dog_Show_Pembroke_Welsh_Corgi1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/8/87/Corgi_Dino_in_park.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/c/ca/Corgi-on-lawn-103631293746954vby.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/a/ae/Grupp_1%2C_WELSH_CORGI_PEMBROKE%2C_BE_CH_C.I.B._LU_CN_NL_CH_Siggen%E2%80%99s_Marguerita_%2823683385973%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/d/d0/Pembroke_in_Tallinn.JPG"
]

# Definition of the app
app = dash.Dash(__name__)

colors = {
    'background': '#ffdead',
    'text': '#213a85'
}   

# HTML Layout
app.layout = html.Div([
    html.H1("Here Are Your Daily Dogs!", style={'textAlign': 'left', 
                                                'color': colors['text'], 
                                                'fontSize': 55}),
    html.H2("Come back tomorrow for new dogs!!!", style={'textAlign': 'left', 
                                                         'color': colors['text'], 
                                                         'fontSize': 30}),
    html.Div([
        dcc.Dropdown(["Dackel", "Corgi", "None"], searchable = False, clearable = False, id = 'dropdown-menu', style={'height': '100px', 
                                                                                                                      'width': '950px'}),
      ], style={'top': '95px', 'width': '100%', 'zIndex': 100}),
    html.Div(id='image-container'),
    dcc.Interval(id='interval-component', interval=1000*60*60*24, n_intervals=0),
    html.Div(id = 'dm-output-container'), 
    html.Div([
        html.H4("Copyright Jonip 2024", style={'textAlign': 'left', 
                                               'top': '2000px', 
                                               'color': colors['text'], 
                                               'fontSize': 15})
    ], style={'position': 'fixed', 
              'bottom': 0, 
              'width': '100%', 
              'textAlign': 'center'})
], style = {
        'backgroundImage': 'url("https://static.basicinvite.com/media/bi/36985/little-dachshund-wallpaper-2x.jpg?q=1701899053")',
        'backgroundSize': 'cover',
        'backgroundRepeat': 'no-repeat',
        'backgroundPosition': 'center',
        'height': '100vh'
    })


# Define the callback to update the image

@app.callback(
    Output("image-container", "children"),
    [Input("interval-component", "n_intervals"),
     Input("dropdown-menu", "value")]
)

# function that updates the image every day

def update_image(n_intervals, value):

    # retrieves the correct URL

    current_day = datetime.today().weekday()

    # if statement that sets image according to user imput

    global image_url

    if value == "Dackel":
        image_url = image_urls_dackel[current_day]
    else:
        pass

    if value == "Corgi":
        image_url = image_urls_corgi[current_day]
    else:
        pass

    if value == "None":
        return html.H3("No dog selected"),
    else:
        pass

    if image_url != None:
       return html.Img(src = image_url) 
    else:
        pass
    

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False, port = 8050)
