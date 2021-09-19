def count_substring(string, sub_string):
    counter = 0
    substr_len = len(sub_string)
    str_len = len(string)
    # print(substr_len, str_len)
    for i in range(str_len):
        if string[i] == sub_string[0]:
            # print string[i:i+substr_len]
            if string[i:i+substr_len] == sub_string:
                counter += 1
    return counter


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print(count)
