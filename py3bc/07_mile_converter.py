prompt = 'What distance would you like to convert to miles? '
kils = input(prompt)

miles = float(kils) / 1.60934
miles = round(miles, 2)
formatter = f'{kils}km is equal to {miles}m'

print(formatter)
