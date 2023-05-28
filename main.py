from fastapi import FastAPI
from modem import Modem



app = FastAPI()
modem_list = []


@app.get("/")
async def modem_shop():
    print(f"inside modem_shop")
    return {"message": "Welcome to the Modem Shop"}

@app.get("/modems")
async def get_modems():
    print(f"Get all books list")
    return {"available _modems": modem_list}

@app.post("/new-modem")
def add_new_modem(modem: Modem):
    modem_list.append(modem.dict())
    return modem_list

@app.get("/modem/{id}")
def get_modem_by_id(id: int):
    for modem in modem_list:
        if modem['id'] == id:
            return modem
        

@app.delete("/modem/{id}")
def delete_modem_by_id(id: int):
    for modem in modem_list:
        if modem['id'] == id:
            modem_id = modem_list.index(modem)
            modem_list.pop(modem_id)
            return modem_list


# if __name__ == "__main__":
#     print(f"startup |")