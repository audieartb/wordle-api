
async def getUsers():
    try:
        return[{"username":"rick"},{"username":"Morty"}]
    
    except:
        return [{"error": "error getting user"}]