import flask
import requests
import json

app = flask.Flask(__name__)
res = requests.get("http://localhost:5000/dashboard")
assert res.status_code == 200, "Failed while fetching dashboard"
print(res.content)

res = requests.get("http://localhost:5000/post/0/5")
print(res.status_code)
assert res.status_code == 200, "Failed to fetch dashboard articles"
print(json.loads(res.content))

res = requests.get("http://localhost:5000/post/1")
print(res.status_code)
print(res.content)