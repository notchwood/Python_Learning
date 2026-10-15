# The double asterisk (**) packs named inputs into a dictionary named 'info'
def build_profile(racer_name, **info):
    profile = {'name': racer_name}
    
    # Loop through whatever extra data was provided
    for key, value in info.items():
        profile[key] = value
        
    return profile

# You can pass completely different details for different racers!
racer_1 = build_profile("Mike", car="Porsche", sponsor="Synology")
racer_2 = build_profile("Alice", team="Red Bull", podiums=14)

print(racer_1)
print(racer_2)
