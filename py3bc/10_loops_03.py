count = 1
MAX = 10
while count < 11:
    spaces = MAX - count
    print(" " * spaces + "\U0001f600" * count)
    count += 1

print("\n")
MAX = 10

for x in range(1,11):
    spaces = MAX - x
    print(" " * spaces + "\U0001f600" * x)
