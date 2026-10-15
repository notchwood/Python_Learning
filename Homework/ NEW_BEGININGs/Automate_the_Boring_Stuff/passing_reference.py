def eggs(someParameter):
    id(someParameter)
    print(f"the id of someParmeter is: {id(someParameter)}")
    someParameter.append('hello')
    return someParameter

spam2 =[]
spam = [1, 2, 3]
spam2 =['a', 'b', 'c']
print(f"the id of spam getting passed to egg() function: {id(spam)}")
spam3 = eggs(spam + spam2)
print(f"the id of spam is: {id(spam2)}")
print(spam)
print(f'this is the spam2 result\n{spam2}')
print(spam3)