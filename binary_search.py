def binary_search(a_list, a_value):
    lower = 0
    upper = len(a_list) - 1
    num_iterations = 1
    while lower <= upper:
        mid = (lower + upper) // 2
        if a_list[mid] == a_value:
            return True, num_iterations
        elif a_list[mid] < a_value:
            lower = a_list[mid]
        else:
            upper = a_list[mid]
        num_iterations += 1
    return False, num_iterations

def binary_search_recursive_aux(a_list, a_value, lower, upper):
    mid = (lower + upper)//2
    if lower > upper:
        return False
    if a_list[mid] == a_value:
        return True
    if a_list[mid] < a_value:
        return binary_search_recursive_aux(a_list, a_value, mid + 1, upper)
    return binary_search_recursive_aux(a_list, a_value, lower, mid - 1)

def binary_search_recursive(a_list, a_value):
    return binary_search_recursive_aux(a_list, a_value, 0, len(a_list) -1)
        

if __name__ == "__main__":
    my_list = [i for i in range(1,101, 2)]
    print(binary_search_recursive(my_list, 74))

    """
    Performs binary search on a list that is sorted from min to max
    : Input: a_list, the sorted list to be searched
    : Input: a_value, the value for which we are searching
    : Returns: True if a_value is in the list, False otherwise
    : Returns: num_iterations, the number of iterations required to perform the
    search
    """
