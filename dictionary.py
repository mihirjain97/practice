from collections import OrderedDict
groceries = {'bananas': 5, 'oranges': 4}

print(groceries.get('hello'))


contacts = {
    'Manav': {'phone': '+91-12333-45666', 'email': 'manav@webmail.com'},
    'Deepak': {'phone': '+91-78999-12333', 'email': 'deepak@webmail.com'},
    'Mehul': {'phone': '+91-45666-78999', 'email': 'mehul@webmail.com'},
}

print(contacts['Manav'])


sentence = "I love my name because its my name and the name I love the most is Mihir I I I I name I love Mihir because"

list1 = sentence.split()
word_count = {}
for i in list1:
    if(word_count.get('I') == None):
        word_count = {'I': 0}
    if(i == 'I'):
        word_count['I'] = word_count['I']+1
    if(word_count.get('love') == None):
        word_count.update({'love': 0})
    if(i == 'love'):
        word_count['love'] = word_count['love']+1
    if(word_count.get('my') == None):
        word_count['my'] = 0
    if(i == 'my'):
        word_count['my'] = word_count['my']+1
    if(word_count.get('because') == None):
        word_count.update({'because': 0})
    if(i == 'because'):
        word_count['because'] = word_count['because']+1
    if(word_count.get('name') == None):
        word_count.update({'name': 0})
    if(i == 'name'):
        word_count['name'] = word_count['name']+1
    if(word_count.get('Mihir') == None):
        word_count.update({'Mihir': 0})
    if(i == 'Mihir'):
        word_count['Mihir'] = word_count['Mihir']+1
# word_count.popitem()
# word_count.popitem()
print(word_count)

print(dict(sorted(list(word_count.items()))))
