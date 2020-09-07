list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four', 'five']

zipped = list(zip(list1, list2))
print(zipped)

unzipped = list(zip(*zipped))

print(unzipped)


for (l1, l2) in zip(list1, list2):
    print(l1)
    print(l2)

items = ['Apple', 'Orange', 'Banana']
counts = [3, 6, 4]
prices = [100, 40, 20]
sentences = []

for (item, count, price) in zip(items, counts, prices):
    item, count, price = str(item), str(count), str(price)
    sentence = 'I bought ' + count + ' ' + item + 's for ' + price + ' Rupees.'
    sentences.append(sentence)
print(sentences)
