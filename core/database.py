from pymongo import MongoClient
from PyJS import JSON
from PyJS.modules import fs

col = MongoClient(JSON.parse(fs.createReadStream('settings.json'))['mongo'])['BytesBump']['servers']

class Servers:
    def get_all(**checks):
        return [server for server in col.find(checks)]
    
    def get_one(**checks):
        return col.find_one(checks)