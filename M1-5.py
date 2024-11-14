#Ask the user for the weather (sunny or raining) and their mood (happy or tired)
#Based on the inputs, print one of the following suggestions:

# Input weather and users mood

weather=(input ('Is it sunny or raining?'))
mood= (input('Are you happy or tired?'))

if (weather=='raining') or (mood=='tired'):
    print('Relax in doors')
else:
    print('Go for a hike!')
