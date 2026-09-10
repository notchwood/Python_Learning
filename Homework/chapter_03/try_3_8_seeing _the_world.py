# try_3_8_seeing _the_world.py

print("1. Create a list of places")
places = ["boston", "maine", "cape cod", "berkshires", "scottland", "nova scotia"]

print("2. This is the original ordered list")
print(places)

print("3. This is the temporly sorted ordered list")
print(sorted(places))

print("4. This is the original ordered list")
print(places)

print("5. This is the temporly REVERSED sorted ordered list")
print(sorted(places, reverse=True))

print("6. This is the original ordered list")
print(places)

print("7. This is the PERMANITlY REVERSED LIST ONLY (not alphabetical)")
places.reverse()
print(places)

print("8. re-reverse list again")
places.reverse()
print(places)

print("9. Permanently sort alpha. accending")
places.sort()
print(places)

print("10. sort list in reverse order permently")
places.sort(reverse = True)
print(places)


