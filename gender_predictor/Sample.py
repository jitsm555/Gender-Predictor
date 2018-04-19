dictionary = dict()

name = 'jitesh'
gender = 1
count = 50

print(dictionary)

if name not in dictionary:
    dictionary[name] = [0, 0]

dictionary[name][gender] = dictionary[name][gender] + count

name = 'jitesh'
gender = 0
count = 20
dictionary[name][gender] = dictionary[name][gender] + count

print(dictionary)

for key, value in dictionary.items():
    print(key)
    print(value[0])



