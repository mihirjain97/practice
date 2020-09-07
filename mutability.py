# Mutable
# -lists
# -dictionaries
# -OrderedDictionaries

list_1 = [1, 2, 3, 4, 5]
list_1.append((6, 7, 8))
print(list_1.append(9))

# d={()}

# immutable
# -tuples
#-ints,floats, boolean

t = (1, 2, 3, [4, 5, 6])
t[3][1] = 7
print(t)
