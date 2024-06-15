# program that calculates the average rainfall per month
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# Get the number of years form the user
no_years = int(input('Enter the number of years:\n'))
rainfall_months = []
rainfall_years = []
total_rain = 0
total_months = no_years * 12

# Loop for each year
for year in range(no_years):
    # Loop for each month
    for month in months:
        rain_month = float(input('For the year ' + str(year + 1) + ' enter the rainfall for ' + month + ' '))
        total_rain = total_rain + rain_month
        rainfall_months.append(rain_month)
    rainfall_years.append(rainfall_months)
    rainfall_months = []

print("The total number of months:",total_months)
print("The total rainfall in inches:", total_rain)
print("The average rainfal per month for the period:", total_rain/total_months)
