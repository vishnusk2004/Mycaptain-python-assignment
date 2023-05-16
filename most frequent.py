def most_frequent(name):
    new_name = {}
    for char in name:
        if char not in new_name:
            new_name[char] = 1
        else:
            new_name[char] += 1
    sorted_dict = sorted(new_name.items(), key=lambda x: x[1], reverse=True)
    for item in sorted_dict:
        print(item[0], '=', item[1], end=' ')


string = input(" Please enter a string: ")
most_frequent(string)
