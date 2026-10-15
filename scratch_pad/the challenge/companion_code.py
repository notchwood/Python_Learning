racers = {
    "j" : 11,
    'alice' : 4,
    'bob' : 2,
    'charlie' : 21,
    'david' : 1,
    'eva' : 5,
}
from operator import itemgetter
racers =sorted(racers.items(), key=itemgetter(1))
print(racers) 