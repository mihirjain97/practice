names = ['Joe', 'John', 'Sushant', 'Krisha', 'Tanvi']

l = []

for person in names:
    l.append(person)
print(l)

print([person for person in names])

lst = []
for person in names:
    lst.append(person + ' dumped me.')
print(lst)

print([person + ' buddies foreever.' for person in names])
lst = []
movies_and_ratings = {'Interseller': 9, 'Brooklyn Nine': 8, 'Avengers': 10,
                      'Harry Potter': 9.5, 'F&F': 8, 'Sahoo': 2, 'Sadak2': 1, 'Mahavati': 3}

for movies in movies_and_ratings:
    if movies_and_ratings[movies] > 6:
        lst.append(movies)
print(lst)

print([movie for movie in movies_and_ratings if movies_and_ratings[movie] < 6])
