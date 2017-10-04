
k = input('')

list_strings = []
list_return = []
value_one = "1"

if k >= 1 and k <=20:
    # value initial
    for i in range(k):
        list_strings.append("0")

    # add first combination
    first_value = ''.join(list_strings)
    list_return.append(first_value)

    #verify if already exits combination
    def has_combination(value):
        for x in range(len(list_return)):
            if list_return[x] == value:
                return True
        return False

    for z in range(len(list_strings)):
        if z != value_one:
            list_strings[z] = value_one
            value_string = ''.join(list_strings)
            list_return.append(value_string[::-1])
            list_strings[z] = "0"

    for z in range(len(list_strings)):
        if list_strings[z] == "0":
            if list_strings[z - 1] != value_one:
                list_strings[z] = value_one
                value_string = ''.join(list_strings)
                if has_combination(value_string[::-1]) == False:
                    list_return.append(value_string[::-1])

    for r in range(len(list_return)):
        print list_return[r]
