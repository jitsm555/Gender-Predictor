'''
This class is responsible for loading files data in memory, This data will be containing gender types.
a.Male
b.Female
c.Unisex
'''
import csv
import os

source_file = 'data/gender_type.csv'


def get_name_list():
    # print('Get the male and female list name')
    name_dict = get_data_from_csv()

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
    return names


def get_data_from_csv():
    # Convert csv data to dictionary

    path = os.path.abspath(__file__)
    dir_path = os.path.dirname(path) + '/'

    names = dict()
    with open(dir_path + '/' + source_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            names[row['name']] = [int(row['male_count']), int(row['female_count'])]
    return names


if __name__ == "__main__":
    print(get_name_list())
