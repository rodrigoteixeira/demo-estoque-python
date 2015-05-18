#!flask/bin/python
from app_estoque import app
import os

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
