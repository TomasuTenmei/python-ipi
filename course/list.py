def list_unique(value):

    tab_unique = []

    for item in value:

        if item not in tab_unique:
            
            tab_unique.append(item)

    return tab_unique

list = [1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9]
result = list_unique(list)
print(result)
