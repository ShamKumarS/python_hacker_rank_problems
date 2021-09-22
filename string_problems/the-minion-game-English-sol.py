# def findKey(string, char, index, i):
#     start = string.find(char, index)
#     return string[start:start+i]


# def findWinner(stuart, kevin):
#     totalStPoint = sum(stuart.values())
#     totalKevPoint = sum(kevin.values())
#     if totalStPoint > totalKevPoint:
#         print("Stuart", totalStPoint)
#     elif totalStPoint < totalKevPoint:
#         print("Kevin", totalKevPoint)
#     else:
#         print("Draw")


# # def count_substring(string, sub_string):
# #     counter = 0
# #     substr_len = len(sub_string)
# #     str_len = len(string)
# #     # print(substr_len, str_len)
# #     for i in range(str_len):
# #         if string[i] == sub_string[0]:
# #             # print string[i:i+substr_len]
# #             if string[i:i+substr_len] == sub_string:
# #                 counter += 1
# #     return counter

# def minion_game(string):
#     kevin = {}
#     stuart = {}
#     length = len(string)
#     index = 0
#     for char, in string:
#         if char in ('A', 'E', 'I', 'O', 'U'):
#             for i in range(1, length-index+1):
#                 key = findKey(string, char, index, i)
#                 # value = count_substring(string, key)
#                 value = string.count(key, index)
#                 # kevin[key] = value
#                 if key in kevin:
#                     kevin[key] += 1
#                 else:
#                     kevin[key] = 1
#         else:
#             for i in range(1, length-index+1):
#                 key = findKey(string, char, index, i)
#                 # value = count_substring(string, key)
#                 value = string.count(key, index)
#                 # kevin[key] = value
#                 if key in stuart:
#                     stuart[key] += 1
#                 else:
#                     stuart[key] = 1
#         index += 1

#     findWinner(stuart, kevin)
#     # print(kevin, stuart)


# if __name__ == '__main__':
#     # s = input()
#     s = 'BANANA'
#     minion_game(s)


# Simplified Version....
def minion_game(s):
    vowels = 'AEIOU'
    length = len(s)
    kevin = 0
    stuart = 0
    for i in range(length):
        if s[i] in vowels:
            kevin += (length-i)
        else:
            stuart += (length-i)
    if stuart > kevin:
        print('Stuart', stuart)
    elif stuart < kevin:
        print('Kevin', kevin)
    else:
        print('Draw')
    # print(stuart, kevin)


if __name__ == '__main__':
    s = input()
    minion_game(s)
