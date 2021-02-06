from pymongo import MongoClient
from bson import ObjectId


clt = MongoClient('mongodb://omega.dunzodev.in:27031/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')
sku = clt.sku

availabilities = sku.availabilities
grocery = sku.grocery


def get_available(dzid):
    a = availabilities.find({'dzid': dzid})
    return [(aa.get('variantID'), aa.get('productID')) for aa in a]


def get_available_raw(dzid):
    a = availabilities.find({'dzid': dzid})
    return list(a)


def get_grocery(variantId):
    b = grocery.find({'variants._id': ObjectId(variantId)})
    return list(b)

def update_grocery(data):
    print('updating', data)
    grocery.replace_one({'_id': ObjectId(data['_id'])}, data)

def create_product(productId):
    pass


def get_products(product_ids):
    g = grocery.find({'_id': {'$in': list(map(ObjectId, product_ids))}})
    return list(g)