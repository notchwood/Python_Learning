# Chapter 3 Introducing Lists
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# Accessing Elemnnts using zero-based and neqaiive indexing
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1].upper())

# Using an individual value from a list inside on f-string
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)