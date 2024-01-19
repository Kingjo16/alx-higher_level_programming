#!/usr/bin/python3
"""Define a base Model class that will reperesent a base."""
import json
import csv


class Base:
    """Represent a Base Model."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base with id set to None."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a Json.dumps to list dic."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write a JSOON on the list obj."""
        located_file = cls.__name__ + ".json"
        with open(located_file, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dicts = [m.to_dictionary() for m in list_objs]
                jsonfile.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return a Json.loads to list dic."""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Write a cls dic on the list obj."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a class list fromthe Json string."""
        located_name = str(cls.__name__) + ".json"
        try:
            with open(located_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write a CSV to the lis of obj to the file."""
        located_name = cls.__name__ + ".csv"
        with open(located_name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
    @classmethod
    def load_from_file_csv(cls):
        """Return a class list withan instantaind from a CSV."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
