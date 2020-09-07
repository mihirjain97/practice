# String Manipulation
# examples = 'python, email, hack, rank, coding, key, value'
# print(examples)

# exam = examples.split(", ")

# print(exam)
# exam = ' and '.join(exam)

# print(exam)

# Tuples
# tuples = {1, 2, 3, 4, 5}
# credit_card1 = {12468854, 'CrediCard1', '11/20', '456'}
# credit_card2 = {45687892, 'CrediCard2', '12/20', '789'}
# credit_card3 = {45685566, 'CrediCard3', '01/21', '123'}
# credit = [credit_card1, credit_card2]
# credit.append(credit_card3)
# print(credit)

# person1 = ("Krisha", 18, "Dominos")
# person2 = ("Tanvi", 21, "Pasta")
# person3 = ("Mihir", 23, "Beer")

# people = [person1, person2, person3]


# for name, age, favfood in people:
#     # name, age, favfood = person
#     print(name)
#     print(age)
#     print(favfood)
#     print()


# Sets
listOfNumbers = [1, 2, 3, 3, 4, 4, 5, 5, 6, 7, 2, 8, 9, 10, "mihir", 'mihir']
print(listOfNumbers)
print()
no_duplicate_set = set(listOfNumbers)
no_duplicate_list = list(no_duplicate_set)
listOfNumbers = no_duplicate_list
print(no_duplicate_set)
print()
print(listOfNumbers)
print()

actionBooks = {'Harry Potter', 'Lord of the Rings', 'Hunger Games'}
mysteriousBooks = {'Harry Potter', 'Cindrella', 'Charlie'}

books = actionBooks.intersection(mysteriousBooks)

print(books)
