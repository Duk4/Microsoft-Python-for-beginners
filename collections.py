duke = {}
duke['first'] = 'Dušan'
duke['last'] = 'Tanasić'

bob = {}
bob['first'] = 'Bob'
bob['last'] = 'Marley'

people = []
people.append(duke)
people.append(bob)
people.append({
    'first': 'Marshall',
    'last': 'Mathers'
})

print(people)