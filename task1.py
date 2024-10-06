print('Write down some integeres for S and T set, \n note |S| <= |T|')

hash_table_S = [int(it) for it in input().split()]
hash_table_T = [int(it) for it in input().split()]

def task():
    T = dict()
    for i in hash_table_T:
        T.setdefault(i, 0)
        T[i] += 1

    for j in hash_table_S:
        T.setdefault(j, 0)
        T[j] -= 1
        if T[j] < 0:
            return (False)
    return (True)

print (task())
        