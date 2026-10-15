print("Here is a list of methods, listed in z-order")
CONST = 30
# name = []
names = dir(str)
names.insert(0, '' )
num_elem = len(names)
# print(num_elem)
x = 1
y = 2
# x, y = 0, 1
temp = len(names[0])
if y < num_elem and temp > 0:


def main():
    for name in names:
        # temp = len(name)
        #print(temp)
        print(name)
        # repeat = CONST - temp
        # spacer = "|" * repeat
        if  y < num_elem and temp > 0:
            repeat = CONST - temp
            spacer = "|" * repeat
            print(f"{names[x]}{spacer}{names[y]}")

            # print("'name[x]'+'(CONST - len(name)) * "|"'+'name[y]'")
            x += 2
            y += 2


# print("'name[x]'+' 'CONST - 'len(name) * "|"'+'name[y]'")



    # print(each)
# num_elem = len(name)
# print(f"number of element is {num_elem}")
# x = 0
# y = 0
# print(f"{name[x + 0]}******************{name[y+2]}")
# # the_methods = []
# # ln_spaces = []
# const = 50
# meth = []
# #name = []
# for name in len(dir(str)):
#     meth = name

# print(meth)
# howmany = len(meth)

# num2 = 1
# for num in range(1,howmany):
#     ln_pad = const - len(meth)
#     if num >= num2:
#         num2 += 1



# # for each in range(dir(str)):
# #     ln_pad = const - len(each)
# #     # # space = (f"{each} {ln_pad}") 
# #     # x = 0
# #     # while x <= ln_pad:
# #     # '''    sp_char.append( )
# #     print(f"{each} ")
# #     # spaces = [] =     print(f"{each}   {space}")'''

# print(howmany)