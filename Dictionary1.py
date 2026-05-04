w = {'name': 'virat', 'age': 37, 'skills': ['bowler', 'battesman', 'fielding', 'aggressive']}
#w['name'] = ['virat', 'rohit']
#w['name'][-1] = 'sachin'
#print(w)
#print(w['name'])
#w['age'] = 40
#print(w)

#**Methods**
#print(w.keys())
#print(w.values())
#print(w.get('name'))
#print(w.get('skills'))
#print(w.items())
#w['profession'] = 'cricketer'
#print(w)

#Update
#w.update({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
#print(w)

#pop
#print(w.pop('name'))

#popitems
#print(w.popitem())

#**Zip function**
city = ['haridwar', 'guwahati', 'nashik', 'delhi']
river = ['ganga', 'brahmaputra', 'godavari', 'yamuna']
#print(dict(zip(city, river)))
#print(list(zip(city, river)))
#print(tuple(zip(city, river)))
#print(set(zip(city, river)))
print(list(zip(city, river)))