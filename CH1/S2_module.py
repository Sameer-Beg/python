import pyjokes

# Get one joke
print(pyjokes.get_joke())

# Get multiple jokes
for i in range(5):
    print(pyjokes.get_joke())

