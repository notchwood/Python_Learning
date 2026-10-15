



glossary = {
    "len" : "\t\t 1) Sort for length. a function used to get the length of \n\t\t\tstring, data structures i.e. tuple, list, dict. and sets?" ,
    "sub" : "\t\t 2) A vocal way to refer to an index of an item in list, and dictionary. \n\t\t\ti.e. give and example",
    "Annotation" : "\t 3) Indicate the type of variable being \n\t\t\tused",
    "Comprehension" : "4) A concise syntax for constructing lists, sets, or \n\t\t\tdictionaries.", 
    "Docstring" : "\t 5) Is a sequence of words to descripe a block of code\n\t\t\ti.e. a short paragraph that discripes a functions purpose.\n\t\t\tA large commented section describing a block of code using 3 quotation\n\t\t\tmarks at the begining and at the end of paragraph",
}
print("\n")
# print("*** LOOPs *** \n")
#print(glossary)
for terms in glossary.keys(): 
    print(f"{terms}:-> {glossary[terms]}\n")
