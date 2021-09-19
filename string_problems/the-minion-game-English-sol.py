def findKey(string, char, index, i):
    start = string.find(char, index)
    return string[start:start+i]
     
def findWinner(stuart, kevin):
    totalStPoint = sum(stuart.values())
    totalKevPoint = sum(kevin.values())
    if totalStPoint > totalKevPoint:
        print("Stuart", totalStPoint)
    elif totalStPoint < totalKevPoint:
        print("Kevin", totalKevPoint)
    else:
        print("Draw")
   
    
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

def minion_game(string):
    kevin = {}
    stuart = {}
    length = len(string)
    index = 0
    for char, in string:
        if char in ('A', 'E', 'I', 'O', 'U'):
            for i in range(1, length-index+1):
                key = findKey(string, char, index, i)
                value = count_substring(string, key)
                # value = string.count(key)
                kevin[key] = value
        else:
            for i in range(1, length-index+1):
                key = findKey(string, char, index, i)
                value = count_substring(string, key)
                # value = string.count(key)
                stuart[key] = value
        index +=1
               
    findWinner(stuart, kevin)
    # print(kevin, stuart)
    # print(vowel, consonant)
    
    
    
    

if __name__ == '__main__':
    s = input()
    minion_game(s)