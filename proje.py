inp1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

lst = list()
def flatten(x):
    y = x.copy()
    for i in list(y):
        if type(i) is list:
            flatten(i)
        else:
            lst.append(i)
flatten(inp1)
print(lst)

inp2 = [[1, 2], [3, 4], [5, 6, 7]]
def lst_reverse(x):
    return [i[::-1] for i in x[::-1]]
print(lst_reverse(inp2))
