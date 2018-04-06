'''
This class is responsible for loading files data in memory, This data will be containing gender types.
a.Male
b.Female
c.Unisex
'''
import os
import csv


def get_name_list():
    # print('Get the male and female list name')
    name_dict = extract_name_dict()

    male_names = list()
    female_names = list()

    # print('Sorting Names')
    for name in name_dict:
        counts = name_dict[name]
        tuple = (name, counts[0], counts[1])
        if counts[0] > counts[1]:
            male_names.append(tuple)
        elif counts[1] > counts[0]:
            female_names.append(tuple)

    names = (male_names, female_names)
    # print('%d male names loaded, %d female names loaded' % (len(names[0]), len(names[1])))
    return names


def extract_name_dict():
    file_list = os.listdir(os.getcwd() + "/names")
    names = dict()
    gender_map = {'M': 0, 'F': 1}
    for filename in file_list:
        file = open(os.getcwd() + "/names/" + filename, 'r')
        print("Final File :" + file.name)
        rows = csv.reader(file, delimiter=',')
        for row in rows:
            name = row[0].upper()
            gender = gender_map[row[1]]
            count = int(row[2])
            if name not in names:
                names[name] = [0, 0]
            names[name][gender] = names[name][gender] + count

        file.close()
    print(names)
    # print('\tImported %s' % file.name)
    return names


if __name__ == "__main__":
    print(get_name_list())
