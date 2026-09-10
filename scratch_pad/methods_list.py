print("Here is a list of methods")

# the_methods = []
# ln_spaces = []
const = 50
meth = []
#name = []
for name in len(dir(str)):
    meth = name

print(meth)
howmany = len(meth)

num2 = 1
for num in range(1,howmany):
    ln_pad = const - len(meth)
    if num >= num2:
        num2 += 1



# for each in range(dir(str)):
#     ln_pad = const - len(each)
#     # # space = (f"{each} {ln_pad}") 
#     # x = 0
#     # while x <= ln_pad:
#     # '''    sp_char.append( )
#     print(f"{each} ")
#     # spaces = [] =     print(f"{each}   {space}")'''

print(howmany)