# pi = 3.14159
# print(pi)

# first_number = 6
# second_number = 2
# print(first_number + second_number)
# print(first_number ** second_number)

# first_number = input('Enter first number: ')
# second_number = input('Enter second number: ')
# print(first_number + second_number) you get a string
# print(first_number ** second_number) strings can't have exponents
# print(int(first_number) + int(second_number))
# print(float(first_number) + float(second_number))

days_in_feb = 28
# print('There are ' + days_in_feb + ' days in February') won't work, because (string + int + string)
print('There are ' + str(days_in_feb) + ' days in February')
