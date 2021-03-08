from PyJS import JSON
from PyJS.modules import fs

def route_for(route):
    return JSON.parse(fs.createReadStream('data/routes.json'))[route]