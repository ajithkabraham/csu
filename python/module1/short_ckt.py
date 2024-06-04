biking_dist = []
treadmill_dist = []
workout_date = []
more_dates = 'y'

while (more_dates == 'y'):
    workout_date.append(input('Enter the workout date\n'))
    biking_dist.append(input('Enter the distance biked today\n'))
    treadmill_dist.append(input('Enter the distance ran today\n'))
    more_dates = input('Do you have additional dates to enter? y or n')

for i in range(len(workout_date)):
    print('For the date', workout_date[i], 'you cycled',biking_dist[i], 'and ran',treadmill_dist[i])