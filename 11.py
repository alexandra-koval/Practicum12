def ind_maxlist(a):
    if a == []:
        return None
    if len(a) == 1:
        return 0
    
    max_index_rest = ind_maxlist(a[1:])
    max_index_rest += 1
    
    if a[0] >= a[max_index_rest]:
        return 0
    else:
        return max_index_rest
