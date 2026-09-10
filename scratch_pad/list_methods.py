items = ["b", "a", "c"]

items.insert(0, "z")   # [z, b, a, c]
print(items)

popped = items.pop(1)  # removes b
print("popped:", popped)
print(items)

items.sort()
print("sorted:", items)

items.reverse()
print("reversed:", items)

print(f"{sorted(items, reverse=True)}")

items.sort(reverse=True)
print(items)

print(f"{sorted(items)}")
print(items)