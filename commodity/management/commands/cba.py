# coding: utf-8

import copy

a = [1, 2, 3, [4]]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)

a.append(5)
a[3].append(6)

print(a, b, c, d)

