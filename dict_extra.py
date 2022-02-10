a={
    1:{'name':'karthi', 'year':'II'},
    2:{'name':'keerthi', 'year':'I'}
}

for k,v in a.items():
    print('ID',k)
    for key in v:
        print(key,' :  ',v[key])
    

#a[2].pop('name')
del a[2]['name']

print(a)