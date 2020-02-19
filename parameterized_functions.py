def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1].lower()
    return initial

first_name = input('Enter your first name: ')
# initial = get_initial(first_name)
initial = get_initial(force_uppercase=False, name=first_name)

print('Your initial is: ' + initial)