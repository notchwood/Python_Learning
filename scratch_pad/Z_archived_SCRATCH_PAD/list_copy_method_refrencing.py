a = ["car", "truck", "SUV", "scooter", "bus"]
b = a.copy() # new memory address  indendent of list A
c = a  # reference to "a's list" memory address
d = a[:] # new memory address indendent of list A
print("\n\n")
print("a original list:", a)
print("use a.copy to b list:", b)
print("assign a to c list:",c) 
print("slice a to d",d)     

a.append("plane")

print("\n\n")
print("a list",a)
print("b list",b)
print("c list appended 'plane':", c)
print("d list from a slice",d)
# a.append("train")
# print("a list again:", a)

b[4] = "train"

print("\n\n")
print("a list - original:",a)
print("b list assigned by index",b)
print("c list appended 'plane':", c)
print("d list from a slice",d)