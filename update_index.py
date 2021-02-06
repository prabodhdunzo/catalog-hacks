import json

from sku import get_available_raw, get_products
import requests


url = "http://omega.dunzodev.in:9410/syncDataES"
headers = {
  'Content-Type': 'application/json'
}


def send_request(payload):
    response = requests.request("POST", url, headers=headers, data=json.dumps({
        "sync_type": "PRODUCT",
        "index_type": "PRODUCT", # PRODUCTAUTOCOMPLETE
        "products": payload
    }))
    print(response.text)


if __name__ == '__main__':
    a = get_available_raw('67c00343-077a-4482-8622-368ab7f16bfe')
    product_ids = [aa.get('productID') for aa in a]
    prods = get_products(product_ids)
    a = {str(aa.get('productID')): aa for aa in a}

    z = []

    for p in prods:
        for v in p.get('variants'):
            if v.get('disabled', False):
                continue
            b = {
                "available": True,
                "brand_name": p.get('brandName'),
                "category": v.get('category', {}).get('name', p).get('category', {}).get('name', ''),
                "city_id": 1,
                "description": p.get('description'),
                "id": str(v.get('_id')),
                "sku_id": str(p.get('_id')),
                "variant_id": str(v.get('_id')),
                "dzid": "67c00343-077a-4482-8622-368ab7f16bfe",
                "location": {
                    "lat": 0,
                    "lng": 0
                },
                "merchantAvailabilityAfter": 31343400000,
                "name": p.get('itemName', '') + ' ' + v.get('name', ''),
                "productName": p.get('itemName', ''),
                "subCategory": v.get('category', {}).get('subCategory', {}).get('name', p).get('category', {}).get('subCategory', {}).get('name', ''),
                "subTag": "grocery",
                "variantName": v.get('name'),
                "item_type": 'COMBO' if p.get('isCombo', False) else 'SINGLE_ITEM'
            }

            z += [b]
    send_request(z)



