def frequent_words(k, text = []):
    frequent_patterns = set()
    length = len(text) - k
    count = []
    for i in range(length + 1):
        pattern = text[i: i + k]
        result = pattern_count(text, pattern)
        count.append(result)
    max_count = max(count)
    for i in range(length):
        if count[i] == max_count:
            string = ''.join(text[i: i+k])
            frequent_patterns.add(string)
    return frequent_patterns