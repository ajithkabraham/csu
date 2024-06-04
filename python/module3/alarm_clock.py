# program that sets the alarm after user required hours

# Get the current time
current_time = int(input('Enter the current time:\n'))

# Get the hours to add
hours_to_add = int(input('Enter the hours:\n'))

# calculate new time
alarm_time = (current_time + hours_to_add) % 24

# Print the output
print('Alarm will go off at: {:.0f}'.format(alarm_time),':00',sep='')
