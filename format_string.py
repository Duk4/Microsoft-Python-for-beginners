first_name = 'Dušan'
last_name = 'Tanasić'

output = 'Hello ' + first_name + ' ' + last_name
output = 'Hello {} {}'.format(first_name, last_name)
output = 'Hello {0} {1}'.format(first_name, last_name)
# Only in python 3.X
output = f'Hello {first_name} {last_name}'

print(output)
