# Slow
from ast import stmt
import timeit
timeit.timeit(stmt='''for i in range(10000):t.append(i)''', setup='t=[]', number=10000)

# timeit.timeit(stmt='''
#     for i in range(10000):
#         t.append(i)''', setup='t=[]', number=10000)

# Faster
timeit.timeit(stmt='''for i in range(10000):l(i)''', setup='t=[]; l=t.append', number=10000)

# Faster still
timeit.timeit(stmt='t = [i for i in range(10000)]', number=10000)