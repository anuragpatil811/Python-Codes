import re

pattern = r"[A-Z] + ilm"
text = """1271 Avenue of the Americas is a 48-story skyscraper on Sixth Avenue, between 50th Street and 51st Street, in Midtown Manhattan, a neighborhood of New York City.
Designed by Wallace Harrison of Harrison, Abramovitz, and Harris, the building was developed between 1956 and 1960 as part of Rockefeller Center.
The building's eight-story base partially wraps around its 48-story main shaft.
The facade comprises glass panels between limestone columns.
The lobby has walls of white marble and stainless steel walls, and red-burgundy glass ceilings, with artwork by Josef Albers, Fritz Glarner, and Francis Brennan.
The ground floor also includes storefronts. Each of the upper floors covers 28,000 sq ft (2,600 m2), with the offices arranged around the core.
Construction started in May 1957, the building was topped out during November 1958, and the occupants took possession in late 1959."""
#match = re.search(pattern, text)
#print(match)
matches = re.finditer(pattern, text)
#print(next(matches))
#print(next(matches))
for items in matches:
    print(items)