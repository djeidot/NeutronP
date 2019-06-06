import requests

baseUrl = "http://10.44.37.98:8080"

def _url(path):
    return 'http://10.44.37.98:8080/' + path

def getGames():
    r = requests.get(_url("games/"))
    return r.json()




# public GamesPojo getGames() {
#     JsonObject jsonAnswer = target.path("games/").request().accept(MediaType.APPLICATION_JSON).get(JsonObject.class);
# return GamesPojo.deserialize(jsonAnswer);
# }