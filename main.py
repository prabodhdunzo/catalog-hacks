import json
import sys

from sku import get_available, get_grocery, update_grocery
from stores import get_store

if __name__ == '__main__':
    print(get_store('67c00343-077a-4482-8622-368ab7f16bfe'))

    f = open('/Users/prabodh/tests/skus/ssk', 'r')
    b = json.load(f)

    avail = get_available('67c00343-077a-4482-8622-368ab7f16bfe')
    print(len(avail), avail)
    for a in avail:
        g = get_grocery(a[0])
        for gg in g:

            if a[1] not in b:
                continue
            gg['imageUrl'] = b[a[1]][0]
            gg['description'] = b[a[1]][1]

            update_grocery(gg)