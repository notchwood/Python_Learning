# try_4_5_summing_a_million.py

numbers = list(range(1, 100000001))
print(min(numbers))
print(max(numbers))
the_total = (sum(numbers))
print({type(the_total)})
print(f'{the_total:,}')