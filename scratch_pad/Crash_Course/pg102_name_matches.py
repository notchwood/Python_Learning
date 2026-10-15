fav_langs = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
friends = ['jen', 'edward']
# for name, language in fav_langs.items():
#     print(f"hello {name.title()}, nice to see you today")


# print("#" * 35)
# print("\n")
  
for name in fav_langs.keys():
    print(f"hi {name.title()}")
    if name in friends:
        language = fav_langs[name]
        print(f"\t{name.title()}, I see you love {language.title()}")
# this one was a tough one for me to follow and I had to referance the book
# many time to get it write! pg 102 PCC

if 'erin' not in fav_langs:
    print("Erin, please take our poll." )