#начало задания 1:

men = ("""Eddard Stark
Robb Stark
Jaime Lannister
Tyrion Lannister
Joffrey Baratheon
Robert Baratheon
Viserys Targaryen
Jon Snow""").split('\n')

women = ("""Catelyn Stark
Sansa Stark
Cersei Lannister
Daenerys Targaryen""").split('\n')

print(men, women)

#ответ: ['Eddard Stark', 'Robb Stark', 'Jaime Lannister', 'Tyrion Lannister', 'Joffrey Baratheon', 'Robert Baratheon', 'Viserys Targaryen', 'Jon Snow']
# ['Catelyn Stark', 'Sansa Stark', 'Cersei Lannister', 'Daenerys Targaryen']

#начало задания 2:

all = men + women
def firstsecond(all):
    all.sort()
    second = []
    for i in range(1, len(all), 2):
        second.append(all[i])
    return second

print(firstsecond(all))

#ответ: ['Cersei Lannister', 'Eddard Stark', 'Joffrey Baratheon', 'Robb Stark', 'Sansa Stark', 'Viserys Targaryen']

#начало задания 3:

def surname(test):
    surname = test.split(' ')[1]
    return surname

def pairscheck(all):
    pairs = {}
    for i in range(len(all)):
        one = all[i]
        for i in range (len(all)):
            if all[i] == one:
                continue
            two = all[i]
            if surname(one) == surname(two):
                pairs[f'{one} and {two}'] = 1
            else:
                pairs[f'{one} and {two}'] = 0
    return pairs

print(pairscheck(all))

#ответ (не буду выводить по всем, просто покажу что выдает все пары и правильно определяет однофамильцев):
# {'Catelyn Stark and Cersei Lannister': 0,
# 'Catelyn Stark and Daenerys Targaryen': 0,
# 'Catelyn Stark and Eddard Stark': 1,
# 'Catelyn Stark and Jaime Lannister': 0,
# 'Catelyn Stark and Joffrey Baratheon': 0,
# 'Catelyn Stark and Jon Snow': 0,
# 'Catelyn Stark and Robb Stark': 1,
# 'Catelyn Stark and Robert Baratheon': 0,
# 'Catelyn Stark and Sansa Stark': 1,
# 'Catelyn Stark and Tyrion Lannister': 0,
# 'Catelyn Stark and Viserys Targaryen': 0,
# 'Cersei Lannister and Catelyn Stark': 0,
# 'Cersei Lannister and Daenerys Targaryen': 0,
# 'Cersei Lannister and Eddard Stark': 0,
# 'Cersei Lannister and Jaime Lannister': 1,
# 'Cersei Lannister and Joffrey Baratheon': 0,
# 'Cersei Lannister and Jon Snow': 0,
# 'Cersei Lannister and Robb Stark': 0,
# 'Cersei Lannister and Robert Baratheon': 0,
# 'Cersei Lannister and Sansa Stark': 0,
# 'Cersei Lannister and Tyrion Lannister': 1,
# 'Cersei Lannister and Viserys Targaryen': 0,

#начало задания 4:

def families(all):
    families = {}
    for i in range(len(all)):
        family = surname(all[i])
        if not family in families.keys():
            families[family] = []
            for i in range(len(all)):
                person = surname(all[i])
                if person == family:
                    families[family].append(all[i])
    return families

print(families(all))

#ответ: {'Stark': ['Catelyn Stark', 'Eddard Stark', 'Robb Stark', 'Sansa Stark'],
# 'Lannister': ['Cersei Lannister', 'Jaime Lannister', 'Tyrion Lannister'],
# 'Targaryen': ['Daenerys Targaryen', 'Viserys Targaryen'],
# 'Baratheon': ['Joffrey Baratheon', 'Robert Baratheon'],
# 'Snow': ['Jon Snow']}

#начало задания 5:

def size(families):
    for key in families.keys():
        print(f'{key}: {len(families[key])}')

size(families(all))

#ответ: Stark: 4
#Lannister: 3
#Targaryen: 2
#Baratheon: 2
#Snow: 1