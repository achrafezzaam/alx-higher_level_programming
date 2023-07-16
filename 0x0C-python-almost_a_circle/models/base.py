#!/usr/bin/python3
'''Define the Base class'''
import json
import csv


class Base:
    '''Create a Base object'''
    __nb_projects = 0

    def __init__(self, id=None):
        '''Instantiate the BAse object

        Args:
            id (int): The id of the instance
        '''
        if id is None:
            Base.__nb_projects += 1
            self.id = Base.__nb_projects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if (list_dictionaries is None) or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if (json_string is None) or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                l_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(l_dict))

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, encoding="utf-8") as f:
                save = f.read()
                save = cls.from_json_string(save)
                return [cls.create(**obj) for obj in save]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = "{}.csv".format(cls.__name__)
        rectangle = ['id', 'width', 'height', 'x', 'y']
        square = ['id', 'size', 'x', 'y']
        with open(filename, "w", newline="") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    csv_dict = csv.DictWriter(f, fieldnames=rectangle)
                else:
                    csv_dict = csv.DictWriter(f, fieldnames=square)
                csv_dict.writeheader()
                for elem in list_objs:
                    csv_dict.writerow(elem.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        filename = "{}.csv".format(cls.__name__)
        rectangle = ['id', 'width', 'height', 'x', 'y']
        square = ['id', 'size', 'x', 'y']
        try:
            with open(filename, encoding='utf-8') as f:
                save = csv.DictReader(f)
                save = [dict([key, int(val)] for key, val in elem.items())
                        for elem in save]
            return [cls.create(**elem) for elem in save]
        except IOError:
            return []
