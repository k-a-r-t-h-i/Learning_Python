#Dictionaries

d={}

d[101]="Hunt"
d[102]="Hopper"
d[105]="Karthi"

print(d)

print(d[102])
print(d.keys())
print(d.values())

for k,v in d.items():       #printing using values
    print(k,v)

'''
Output:
{101: 'Hunt', 102: 'Hopper', 105: 'Karthi'}
Hopper
dict_keys([101, 102, 105])
dict_values(['Hunt', 'Hopper', 'Karthi'])
101 Hunt
102 Hopper
105 Karthi
'''