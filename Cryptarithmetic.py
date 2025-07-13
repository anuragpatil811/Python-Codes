from itertools import permutations

letters = 'SENDMORY'
for p in permutations(range(10), len(letters)):
    s = dict(zip(letters, p))
    if s['S'] == 0 or s['M'] == 0:
        continue
    send = s['S']*1000 + s['E']*100 + s['N']*10 + s['D']
    more = s['M']*1000 + s['O']*100 + s['R']*10 + s['E']
    money = s['M']*10000 + s['O']*1000 + s['N']*100 + s['E']*10 + s['Y']
    if send + more == money:
        print("SEND + MORE = MONEY:", send, "+", more, "=", money)
        break
