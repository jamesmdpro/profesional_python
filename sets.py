# eliminador de repetidos forma 1
"""
def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    random_list = [1, 1, 2, 3, 2, 4]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()

    """
# eliminador de repetidos " en esta caso lo que utilizo el la propiedad de set y listo"
"""
list = [1, 1, 2, 3, 2, 4]
print(set(list))

"""

list = {1, 1, 2, 3, 2, 4}
list2 = {1, 1, 2, 3, 2, 4}
list3 = list | list2 
print(list3)

