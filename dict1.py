phonebook = {'Appu' : '12', 'Ammu':'13', 'Unni':'14'}
print(phonebook['Appu'])
phonebook['vichu']='15'
print(phonebook)
print(len(phonebook))
X=dict(name='kannan', age='18')
print(X)
del phonebook['Ammu']
print(phonebook)
names = {'Appu' : {
    'phone' :'12',
    'address' : 'abcd'
},'Ammu' : {
    'phone' :'13',
    'address':'erty'
}}
print(names)
print(names['Appu']['phone'])
names.clear()
print(names)
k = {}.fromkeys(['name','age'])
print(k)
print(phonebook.keys())
print(list(phonebook.keys()))
print(list(phonebook.values()))
print(sorted(phonebook.keys()))
print('name' in phonebook)
print('name' not in phonebook)
print(phonebook.items())
del phonebook['Appu']
print(phonebook)
X=dict(name='kannan', age='18')
y={'name':'seven','age':12}
X.update(y)
print(X)