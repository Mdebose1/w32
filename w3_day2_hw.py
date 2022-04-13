# Filter out all of the empty strings from the list below
places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']

def clear_whitespaces (places):
    result = []
    for w in places:
        # print(clear_whitespaces)
        result.append(w.replace(' ',""))
    # return result
        result = list(filter(clear_whitespaces, places))
    if result == places:
        return result
    else:
        print(clear_whitespaces(places))

        # print(result)





