def list_joiner(*lists_in_order):
    final_list = []
    for i in lists_in_order:
        final_list += i
    return final_list

print(list_joiner(list(range(10,21)),list(range(50,61))))