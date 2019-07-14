from flask import Flask

from instance.config import SECRET_KEY

app = Flask(__name__,template_folder="templates")
