#! /user/bin/env python3.4

# Problem 1
def find(pattern):
    with open('sequence.txt', 'r') as sequence:
        seq = sequence.read()
    match_list = []
    match = ''
    for i in range(0, len(seq) - len(pattern)):
        for j in range(0, len(pattern)):
            if pattern[j] == seq[i + j] or pattern[j] == 'X':
                match += seq[i + j]
            else:
                match = ''
                break
        if match != '':
            match_list.append(int(match))
    return match_list


# #problem 2
def getStreakProduct(sequence, maxSize, product):
    match_list = []
    match = ''
    test_product = product
    for i in range(0, len(sequence)-maxSize+2):
        for j in range(0, maxSize):
            k = i+j
            if int(sequence[k]) * int(sequence[k+1]) < product:
                match += sequence[k]
                product /= int(sequence[k])
            elif int(sequence[k]) * int(sequence[k+1]) == product:
                match += sequence[k] + sequence[k+1]
                break
            elif int(sequence[k]) * int(sequence[k+1]) > product:
                match = ''
                break
        if match != '':
            match_list.append(int(match))
            match = ''
        product = test_product
    return match_list


# #problem 3
def writePyramids(filePath, baseSize, count, char):
    with open(filePath, 'w') as myFile:
        mid = int(baseSize / 2)
        left = mid
        right = mid
        times = count - 1
        for k in range(0, int(baseSize / 2) + 1):
            for i in range(0, count):
                for j in range(0, baseSize):
                    if left <= j <= right:
                        myFile.write(char)
                    else:
                        myFile.write(' ')
                if times:
                    myFile.write(' ')
                    times -= 1
                else:
                    times = count - 1
            left -= 1
            right += 1
            myFile.write('\n')
    return


# problem 4
def getStreaks(sequence, letters):
    match_list = []
    match = []
    i = 1
    while i < len(sequence):
        if sequence[i-1] != sequence[i]:
            match.append(sequence[0:i])
            sequence = sequence[i:]
            i = 1
        else:
            i += 1
    match.append(sequence)
    for i in range(0, len(match)):
        test = match[i]
        if test[0] in letters:
            match_list.append(test)
    return match_list


# problem 5
def findNames(nameList, part, name):
    match_list = []
    for i in range(0, len(nameList)):
        first, last = nameList[i].split(' ')
        if part == 'F':
            if name.lower() == first.lower():
                match_list.append(nameList[i])
        elif part == 'L':
            if name.lower() == last.lower():
                match_list.append(nameList[i])
        else:
            if name.lower() in nameList[i].lower():
                match_list.append(nameList[i])
    return match_list

# problem 6
def convertToBoolean(num, size):
    if not isinstance(num, int):
        return []
    else:
        result = []
        while num != 0:
            if num % 2 == 1:
                result.append(1)
            else:
                result.append(0)
            num = int(num/2)
        result.reverse()
        for i in range(0, len(result)):
            if result[i] == 1:
                result[i] = "True"
            else:
                result[i] = "False"
        if size > len(result):
            for i in range(1, size - len(result)+1):
                result.insert(0, "False")
        return result

# problem 7
def convertToInteger(boolList):
    result = 0
    if isinstance(boolList, list) and check(boolList) and boolList != []:
        for i in range(0, len(boolList)):
            if boolList[i]:
                result += 2 ** (len(boolList) - 1 - i)
        return result
    else:
        return None

def check(list):
    for i in range(0, len(list)):
        if not isinstance(list[i], bool):
            return False
    return True


if __name__ == "__main__":

    writePyramids('test3.txt', 13, 6, 'X')
    # result = find("154X")
    # string = "1547896154321687984"
    # result = getStreakProduct(string, 3, 20)
    # sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
    # result = getStreaks(sequence, "K")
    # names = ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
    # result = findNames(names, 'FL', 'chen')
    # result = convertToBoolean('f', 5)
    # bList = [False, False, True, False, False, True]
    # result = convertToInteger(bList)
    # print(result)
