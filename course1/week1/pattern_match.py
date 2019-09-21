def pattern_match(pattern = [], genome = []):
    length_p = len(pattern)
    length_g = len(genome)
    length = length_g - length_p + 1
    result = []
    flag = True
    for i in range(length):
        if genome[i] == pattern[0]:
            for j in range(length_p):
                if genome[i + j] != pattern[j]:
                    flag = False
            if flag:
                result.append(i)
            else:
                flag = True
    return result
