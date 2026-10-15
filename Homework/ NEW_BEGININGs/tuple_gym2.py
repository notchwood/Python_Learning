desktop_ai = ('mike_desktip', ['gemma2:2b', 'llama3'])

model = desktop_ai[1]

model.append('gemma2:9b')

print(f"the latest model loaded is: {model[-1]}")