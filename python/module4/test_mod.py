input_number = int(input())
bin_num = ''
while (input_number > 0 ):   
    bin_num = bin_num + str(input_number % 2)
    input_number = input_number //2
print(bin_num)