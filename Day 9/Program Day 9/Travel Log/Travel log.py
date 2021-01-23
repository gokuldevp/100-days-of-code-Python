travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

def add_new_country(new_country, new_visits, new_cities):
    add_new = [{
        "country": new_country,
        "visits": new_visits,
        "cities": new_cities
    }]

    travel_log.extend(add_new)



#🚨 Do NOT change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


