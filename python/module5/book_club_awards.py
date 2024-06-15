# program that awards points based on number of books purchased

no_books = int(input('Enter the number of books purchased\n'))
awards = 0
if (2 <= no_books < 4):
    awards = 5
elif (4 <= no_books < 6):
    awards = 15
elif (6 <= no_books < 8):
    awards = 30
elif (no_books >= 8):
    awards = 60

print("Number of points awarded:",awards)
