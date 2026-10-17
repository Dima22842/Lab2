import json



with open("pokemon_full.json") as pokemon_json:
    data = json.load(pokemon_json)
    print(data)