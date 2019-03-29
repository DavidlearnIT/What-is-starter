def get_cimi(n):
    if n<0:
        return -1
    elif n<2:
        return 1  
    else:
        return n*get_cimi(n-1)
print(get_cimi(5))