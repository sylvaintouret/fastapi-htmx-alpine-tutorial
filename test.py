import json

file = "./app/src/books.json"

with open(file, "r") as f:
    data = json.loads(f.read())

# load it in to something to play with
