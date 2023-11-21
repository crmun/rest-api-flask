from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "Store 1",
        "items": [
            {
                "name":"Chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store")
def get_stores():
    return {"stores":stores}

@app.post("/store")
def create_store():
    print("HEllo")
    req_data = request.get_json()
    new_store = {
                    "name":req_data["name"],
                    "items":[]
                }
    stores.append(new_store)
    print("Done")
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    req_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {
                "name":req_data["name"],
                "price":req_data["price"]    
            }
            store["items"].append(new_item)
            return new_item, 201
    return {"message":"Store not found"}, 404

@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store, 201
    return {"message":"Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_items(name):
    for store in stores:
        if store["name"] == name:
            return store["items"], 201
    return {"message":"Store not found"}, 404