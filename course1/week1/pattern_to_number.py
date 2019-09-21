def symbol_to_number(symbol):
    if symbol == 'A':
        return 0
    if symbol == 'C':
        return 1
    if symbol == 'G':
        return 2
    if symbol == 'T':
        return 3

def pattern_to_number(pattern = []):
    length_p = len(pattern)
    if length_p == 0:
        return 0
    symbol = pattern[length_p - 1]
    prefix = pattern[0:length_p - 1]
    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)
   

