from fasthtml_hf import setup_hf_backup
from fasthtml.common import *
from monsterui.franken import *
from monsterui.core import Theme


# Initialize app with MonsterUI Theme
theme = Theme.blue
app, rt = fast_app(hdrs=theme.headers(mode="light"))

@rt("/")
def get():
    return Titled("Hello World with FastHTML and MonsterUI",
                  Container(
                      H2("Welcome to FastHTML on Hugging Face Spaces!"),
                      P("This is a simple Hello World application using FastHTML and MonsterUI."),
                      Button("Click me!", cls="hello-btn", hx_post="/clicked", hx_swap="outerHTML"),
                      Div(id="result")
                  ))

@rt("/clicked")
def post():
    return Div(P("Thanks for clicking! You're awesome!"), id="result", cls="mt-4")

# Run the app
setup_hf_backup(app)
serve() 