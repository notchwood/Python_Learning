# tiy 5.1 conditioal test

# Tuple used for word comparision for followning test
misc_strings = ("Semi", "Kenworth", "mack", "volvo", "sTopTiMe" )

'''
Self note:
== != <= >= < > in, and, or, not
Do using list, tuple, a variable(with string 
then an Int. try Nest sequence. Create a series of 10 test. Use remarks for 
each senarios, 5 evalute to True and 5 evaluate to True'''

# exmple 1)
# checking string in tuples won't match because alpha. case don't match
 # False - word matches but str case don't match
print("semi" in misc_strings, 'example 1')

# example 2)
# checking strings words by lowering case to match tuple
 # True - str and lower case match.
print("Kenworth".lower() == "kenworth", 'example 2')

# example 3)
# False - because alpha. case don't match
print(f"Kenworth" == "kenworth",  ' example 3') # False (equality check)

# Example 4)
'''False 
    Using ASCII value for comparision test of a str.
    "K"ascii value is actually less than the ascii value for small char. "k" 
    K(ASCII-75) is < small(107). k'''
print("Kenworth" > "kenworth", 'example 4') 

'''Example # 5)
    False - is not included in the set because the
    second key value is excluded in the set'''
print(5 in range(3,5), 'example 8')

# Example 6)
# False - Because the capt. K is < capt. S
print("Kenworth" > "Semi", 'example 6')

''' Example 7)
    because the comparision is betwenn two string that do not match
    and we're testing if that statement is true or not - the
    statment is true, so the expression evaluates to True - finall answer '''
print("semi" != "Semi", 'example 7') # True - Because str are case sensitive

'''Example 8)  
the num 5 is the set of 3,4,5
print(5 in range(3,6)) # True
# logic operation using "not" - the second key pair range is exluded'''
print(6 not in range(3,6), "example 8") # True

# Example 9)
word = "sTopTiMe"
print(word in misc_strings and 7 not in range(1, 7), "example 9")

# Example 10)
parent = 33; child = 10
print(parent > 21 or child > 12, "child can go on carnival ride - example 10")
parent = 33; child = 10
print(parent < 21 or child > 12, " example 10a")


# set_of_numbs = list(range(1,9))
# print(set_of_numbs)

# # print("semi" == "Semi") # False - Because str are case sensitive


# # toms_address = { ["number, 5"], ['street, main'], {"city", "Boston"}}

# # # nested sequence
# # nesteggs = ("robbin", 3), ("blueJay", 0), ("sparrow",2)
# # print(nesteggs(0,) == "robbin" ) # TRue
# # # string

# # # number

# # # in range

# # # not in range - number

# # # greater than on a string
# # # word_1 = "ladder"
# # # word_2 = "Fork Lift"


# print("looking for boolean result: True")
# print("looking for boolean result: False")

# # print(test_1 (car_model == "Buick"))
# # test_1 = False
# # print(test_1 == False)

# # car_model = "Buick"

# # print("Is car_model {Chevy.low} in car_model")
# # b_test = car_model != "Chevy"
# # print ("bolean is " b_test )



