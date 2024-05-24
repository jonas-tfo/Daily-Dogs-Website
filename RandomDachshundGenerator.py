import random
import dash
from dash import html, dcc
from dash.dependencies import Output, Input
from datetime import datetime
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup

# Function to check if an image meets the size threshold
def is_large_enough(image_url, min_width=100, min_height=100):
    try:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        width, height = image.size
        return width >= min_width and height >= min_height
    except Exception as e:
        return False

# Function to scrape image URLs from webpage and filter out small images
def scrape_image_urls(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        image_elements = soup.find_all('img')
        image_urls = [img['src'] for img in image_elements if 'src' in img.attrs]
        # Filter out small images (often website logos)
        large_image_urls = [url for url in image_urls if is_large_enough(url)]
        return large_image_urls
    else:
        return False

# Scrape image URLs for Dackel
image_urls_dogs = scrape_image_urls('https://unsplash.com/de/s/fotos/dachshund')

# Definition of the app
app = dash.Dash(__name__)

# HTML Layout
app.layout = html.Div([
    html.H1("Welcome to random dachshund generator!", style={'textAlign': 'left', 'fontSize': 55, 'color': '#1a3560'}),
    html.H2("Click below!", style={'textAlign': 'left', 'fontSize': 30, 'color': '#1a3560'}),
    html.Div([
        html.Button('Generate', id='dog-click', n_clicks=0, 
                    style={'font-size': '12px', 'height': '120px', 'width': '120px', 'display': 'inline-block', 'margin-bottom': '10px', 'margin-right': '5px', 'height':'37px', 'verticalAlign': 'top'})
    ], style={'top': '95px', 'width': '100%', 'zIndex': 100}),
    html.Div(id='image-container'),
    html.Div(id='dm-output-container'), 
    html.Div([
        html.H4("Copyright Jonip 2024", style={'textAlign': 'left', 'color': '#213a85', 'fontSize': 15})
    ], style={'position': 'fixed', 'bottom': 0, 'width': '100%', 'textAlign': 'center'})
], style={
    'backgroundImage': 'url("https://c4.wallpaperflare.com/wallpaper/720/104/998/dog-artwork-animals-minimalism-wallpaper-preview.jpg")',
    'backgroundSize': 'cover',
    'backgroundRepeat': 'no-repeat',
    'backgroundPosition': 'center',
    'height': '100vh'
})

# Define the callback to update the image
@app.callback(
    Output("image-container", "children"),
    Input('dog-click', 'n_clicks'),
    prevent_initial_call=True
)
def update_image(n_clicks):
    if not image_urls_dogs:
        return "No large images found."
    randnumber = random.randint(0, len(image_urls_dogs) - 1)
    image_url = image_urls_dogs[randnumber]
    return html.Img(src=image_url)

# Function that updates the output according to the input in the dropdown menu
@app.callback(
    Output("dm-output-container", "children"),
    Input("dog-click", "value")
)
def update_output(value):
    return

if __name__ == '__main__':
    app.run_server(debug=False)
