answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

print(answer)
print(answer2)