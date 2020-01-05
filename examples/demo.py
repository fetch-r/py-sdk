from fetchr import FetchRClient
from pprint import pprint

import jwt

jwt_auth = jwt.encode({}, 'myCryptoSecret-tobechanged')

fr = FetchRClient.connect("http://127.0.0.1:9000")

fr = fr.with_headers(Authorization=jwt_auth)

pprint("Setting model and database")
pprint(fr.database_api.set_in_memory())
pprint(fr.models_api.set_model_from_files("./data/models/demo/model.json"))
pprint(fr.migrations_api.apply_from_files("./data/models/demo/migrations"))

fre = fr.entities

# Countries
print()
print("Inserting data")
(us, ch, de) = fre.country.insert({
    'data': [
        {'code': 'us', 'name': 'USA'},
        {'code': 'ch', 'name': 'Switzerland'},
        {'name': 'Germany'}
    ]
})

pprint((us, ch, de))

print()
print("Listing Countries")
pprint(fre.country.list())

# Cities
(gn, sf, ey, ny) = fre.city.insert({
    'data': [
        {'country': ch, 'name': 'Geneva'},
        {'country': us, 'name': 'San Francisco'},
        {'country': ch, 'name': 'Eysins'},
        {'country': ch, 'name': 'New York'},  # incorrect country reference
    ]
})

fre.city.update({'params': ny, 'data': {'country': us}})

pprint((gn, sf, ey, ny))

print()
print("Listing Cities")
pprint(fre.city.list(projection={
    "uuid": False,
    "timezone": False,
    "country": {"name": True},
}))

# Companies
print()
print("Inserting companies")
(panam, google, ibm, nexys) = fre.company.insert({
    'data': [
        {'city': ny, 'name': 'Panam'},
        {'city': sf, 'name': 'Google'},
        {'city': ey, 'name': 'Nexys'},
        {'name': 'IBM'},
    ]
})

pprint((panam, google, ibm, nexys))

fre.company.delete({'params': panam})
fre.company.update({'params': ibm, 'data': {'city': sf}})

print("Listing Companies")
pprint(fre.company.list(projection={
    "name": True, "city": {
        "country": True,
        "uuid": False,
    }
}))
