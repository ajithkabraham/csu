# program that calculates the total amount of a meal purchased at a restaurant

# Get the charge for the food
charge_for_food = float(input('Enter the charge for the food:\n'))
# initialize tip percentage and tx
tip_percent = 18
tax_percent = 7

# Do the sum
tip_amount = charge_for_food*(18/100)
tax_amount = charge_for_food*(7/100)

# Print the output
print('\n18% gratuity: ${:.2f}'.format(tip_amount))
print('\n7% tax: ${:.2f}'.format(tax_amount))
print('Total: ${:.2f}'.format(charge_for_food + tip_amount + tax_amount))
