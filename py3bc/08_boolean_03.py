# NO TOUCHING ======================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm'])
# NO TOUCHING ======================================

if food == 'apple' or food == 'grape':
    print('fruit')
elif food == "bacon" or food == 'steak':
    print('meat')
else:
    print('that is not food')