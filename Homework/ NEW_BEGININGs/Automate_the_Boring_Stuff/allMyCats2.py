# catNames = []
# while True:
#     print('Enter you cats name ' + str(len(catNames) + 1) + ' (or enter nothing to stop)')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name] # list concatenation
#     print('The cat names are:')
#     for name in catNames:
#         print(name)


# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for x in range(len(supplies)):
#     print('Index ' + str(x) + ' in supplies is: ' + supplies[x])

spam = ['hello', 'howdie', 'heyas', 'goodbye']

print(f"the index for the value '{spam[0]}' in list spam is: {spam.index('hello')}")
print(f"the index for the value '{spam[2]}' in list spam is: {spam.index('heyas')}")

spam_id = id(spam)
print(f"the id # of variable list 'spam' is: {spam_id}")
copy_spam = spam
sp_id2 = id(copy_spam)
print(f"the id # of variable list 'copy_spam' is: {spam_id}")

