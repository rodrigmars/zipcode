from sanic import Request, Sanic, HTTPResponse, json

app = Sanic("zipcode")

@app.get("/zipcode/cep/<code:str>")
async def async_get_cep(request, code):

    print(f"code:{code}")

    address = [{
        "street": "Rua Serra Negra",
        "number": 980,
        "zip_code": "69310-729",
    }]


    # return json({"created": True, "id": new_thing.thing_id}, status=201)
    return json({"address": address}, status=200)
 
 
