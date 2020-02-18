# price = input('How much did you pay? ')
# price = float(price)

# if price >= 1.00:
#     tax = 0.07
# else:
#     tax = 0
# print('Tax rate is: ' + str(tax))

country = input('Enter the name of your home country? ')
# if country == 'canada': - string comparisons are case sensitive
if country.lower() == 'canada':
    print('Oh you are a Canadian!')
else:
    print('You are not from Canada.')
