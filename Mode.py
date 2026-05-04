'''
def mode(liist):
    unique_list = list(set(liist))
    frequencies = []
    for num in unique_list:
        frequencies.append(liist.count(num))
    #dict = dict(zip(frequencies, unique_list))
    #mode = dict.get(max(dict.keys()), 'there is no such value')
    mode = unique_list[frequencies.index(max(frequencies))]
    return unique_list, frequencies, mode
print(mode([12, 23, 45, 12, 12, 12, 12]))
'''
#Count 2 modes
def modes(liist):
    unique_list = list(set(liist))
    freq = []
    for num in unique_list:
        freq.append(liist.count(num))
    a = list(zip(unique_list, freq))
    max_freq = max(freq)
    mode = []
    for i, j in a:
        if j==max_freq:
            mode.append(i)
    return unique_list, freq, mode
print(modes([12, 23, 45, 12, 12, 12, 12, 45, 45, 45, 45, 45]))
            
    