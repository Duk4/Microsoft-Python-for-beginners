import json

rapper_dict = {'first': 'Marshall', 'last': 'Mathers'}
rapper_dict['City'] = 'Detroit'

rap_dict = {}
rap_dict['Best Rapper Ever'] = rapper_dict

rap_json = json.dumps(rap_dict)

print()
print(rap_json)

songs = ['Lose Yourself', 'Without Me', 'I Will']
rapper_dict['songs'] = songs

rapper_json = json.dumps(rapper_dict)
print()
print(rapper_json)
