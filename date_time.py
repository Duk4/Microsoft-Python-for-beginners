from datetime import datetime, timedelta

today = datetime.now()
# the now function returns a datetime object
print('Today is: ' + str(today))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print(f'Yesterday was: {yesterday}')

# specify what's needed
print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))

# converting strings to datetime objects
birthday = input('When is your birthday (dd/mm/yyyy)? ')
birth_day = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birth_day))
