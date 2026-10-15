# create the dictionary favorite_num
# then assign key value pair for each name and var. fovorite number of name
favorite_num = {
    'bob': '11',
    'michelle': '88',
    'jack': '23',
    'sally': '56',
    'mike': '33'
     }

# access the the value by using the fovorite_num [key] and print the value
# print(f"Bob's favorite number is {favorite_num['bob']}")
# print(f"Michelle's favorite number is {favorite_num['michelle']}")
# print(f"Jack's favorite number is {favorite_num['jack']}")
# print(f"Sally's favorite number is {favorite_num['sally']}")
# print(f"Mike's favorite number is {favorite_num['mike']}")

for name, fav_num in favorite_num.items():
    print(f"{name}'s favorite number is {fav_num}")