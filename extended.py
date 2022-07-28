def hypervolume(*lengths):
    i = iter(lengths)
    print(i)
    v = next(i)
    #print(v)
    for length in i:
        v *= length
    return v

print(hypervolume(2, 4))
#hypervolume(2, 4, 6)
#hypervolume(2, 4, 6, 8)

