# app/main.py
from flask import Flask
from config.config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# ...
