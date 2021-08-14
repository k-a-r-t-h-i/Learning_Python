#list

l=[True,'karthi',100,3.89,8]
print(l)
print(l[2],'    ',l[2:5])

#reverse index
print(l[-1],l[-2])

l1=[9,2,5,10,4]
print(l1)

print(2 in l1 , 2 not in l1)

l1.reverse()           
print(l1)         #print(l1.reverse()) is wrong bcuz reverse does not return anything
print(l1[::-1])

l1.sort()
print(l1)

l1.sort(reverse=True)#sort in decending order
print(l1)

print(sum(l1))

for _ in l:
    print(_)

for i in range(0,len(l)):
    print(i,l[i])

#if duplicates are present in a list
#then it will give only first index
a=[1,2,2,3]
print(a.index(2))

a.append('add at end')   #adding to the last

a.pop() #remove last element

a.pop(2) #removes element at index 2

print(str(len(a))) #str() can be used to change data type to string

""" multi
line
comment
"""

#split function

dob='23-11-2001'
slist=dob.split('-')
print(slist)

"""
Output:

[True, 'karthi', 100, 3.89, 8]
100      [100, 3.89, 8]
8 3.89
[9, 2, 5, 10, 4]
True False
[4, 10, 5, 2, 9]
[9, 2, 5, 10, 4]
[2, 4, 5, 9, 10]
[10, 9, 5, 4, 2]
30
True
karthi
100
3.89
8
0 True
1 karthi
2 100
3 3.89
4 8
1
3
['23', '11', '2001']
"""