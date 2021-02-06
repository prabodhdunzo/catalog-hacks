from pymongo import MongoClient

clt = MongoClient('mongodb://omega.dunzodev.in:27031/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
db = clt.dunzo_stores
store = db.store

def get_store(dzid):
    s = store.find({'dzid': dzid})
    return [ss.get('name') for ss in s]