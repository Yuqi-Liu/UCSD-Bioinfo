def reverse_complement(string = []):
    length = len(string)
    complement = []
    for i in range(length):
        if string[i] == 'A':
            complement.append('T')
        if string[i] == 'C':
            complement.append('G')
        if string[i] == 'T':
            complement.append('A')
        if string[i] == 'G':
            complement.append('C')
    reverse_complement_str = "".join(complement[::-1])
    return reverse_complement_str