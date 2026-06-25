def sec_lar(lst):
    new_lst = list(set(lst))
    new_lst.sort(reverse=True)
    return new_lst[1]
print(sec_lar([1, 2, 3, 4]))