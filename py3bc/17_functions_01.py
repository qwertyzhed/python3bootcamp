def generate_evens():
    return [x for x in range(0,50) if x % 2 == 0]

fg = generate_evens()
print(fg)