#list comprehension
ls=list(range(10))
print(ls)
print()

even_ls=[]  #we are going put even elements in ls into even_ls

#normal way
print("normal way")
for _ in ls:
    if _%2==0:
        even_ls.append(_)
print("even_ls: ",even_ls)
print()

even_ls.clear()
print("even_ls is cleared. even_ls= ",even_ls)
print()

#list_comp way
#syntax: identifier = [local_variable for_loop(one or more) if_condition]
print("list comprehension way")
even_ls= [_ for _ in ls if _%2==0]
print("even_ls: ",even_ls)

"""
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

normal way
even_ls:  [0, 2, 4, 6, 8]

even_ls is cleared. even_ls=  []

list comprehension way
even_ls:  [0, 2, 4, 6, 8]
"""