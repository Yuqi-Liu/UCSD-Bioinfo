def pattern_count(text = [], pattern = []):
    count = 0
    length = len(text) - len(pattern)
    length_p = len(pattern)
    for i in range(length + 1):
        for j in range(length_p):
            if text[i + j] != pattern[j]:
                count -= 1
                break
        count += 1
    return count