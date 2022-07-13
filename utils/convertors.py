def group_list(custom_list, size=4):
    grouped_list = []
    for i in range(0, len(custom_list), size):
        grouped_list.append(custom_list[i:i + size])
    return grouped_list
