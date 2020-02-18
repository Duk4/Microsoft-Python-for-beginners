country = input('Enter the name of your home country? ')
# province = input('In what province do you live in? ')
# tax = 0

# if province == 'Alberta':
#     tax = 0.5
# if province == 'Nunavut':
#     tax = 0.5
# if province == 'Ontario':
#     tax = 0.13

if country.lower() == 'canada':
    province = input('In what province do you live in? ')
    # if province == 'Alberta' or province == 'Nunavut':
    if province in ('Alberta', 'Nunavut', 'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0

print('Tax rate is: ' + str(tax))
