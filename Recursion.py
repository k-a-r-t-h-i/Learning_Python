# recursion- a function calls itself

def sum_of_list_using_recursion(L, output=0):       #here output is initialized to 0
    if len(L)>0:
        output+=L[0]
        L.pop(0)
        return sum_of_list_using_recursion(L,output)
    else:
        return output

print(sum_of_list_using_recursion([1,2,3,4,5,6,7,8,9]))

"""
Output:
45
"""