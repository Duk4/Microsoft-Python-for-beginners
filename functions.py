# from datetime import datetime

# # Function to print current date and time
# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())

# print_time('task started')

# for x in range(0, 10):
#     print(x)

# print_time('task completed')

def get_initials(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter your first name: ')
initials = get_initials(first_name)

middle_name = input('Enter your middle name: ')
initials += get_initials(middle_name)

last_name = input('Enter your last name: ')
initials += get_initials(last_name)

print('Your initials are: ' + initials)