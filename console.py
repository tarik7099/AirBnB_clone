#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

import cmd
import json


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    MY_CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Place': Place,
        'Amentiy': Amenity,
        'Review': Review
    }

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in self.MY_CLASSES:
            print("** class doesn't exist **")
            return

        new_instance = self.MY_CLASSES[class_name]()
        new_instance.save()
        print(new_instance.id)
        storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in self.MY_CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects_dict = storage.all()
        key = "{}.{}".format(class_name, args[1])
        obj = objects_dict.get(key)
        if not obj:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.MY_CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects_dict = storage.all()
        key = "{}.{}".format(class_name, args[1])
        obj = objects_dict.get(key)
        if not obj:
            print("** no instance found **")
        else:
            del objects_dict[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representations of instances."""
        objects_dict = storage.all()
        if not arg:
            print([str(obj) for obj in objects_dict.values()])
        else:
            class_name = arg.split()[0]
            if class_name not in self.MY_CLASSES:
                print("** class doesn't exist **")
                return
            filtered_objects = []
            for key, obj in objects_dict.items():
                if key.split('.')[0] == class_name:
                    filtered_objects.append(str(obj))
                    print(filtered_objects)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.MY_CLASSES:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects_dict = storage.all()
        key = "{}.{}".format(class_name, args[1])
        obj = objects_dict.get(key)
        if not obj:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_value = args[3]
        setattr(obj, attr_name, attr_value)
        storage.save()

    def do_help(self, arg):
        """To get help on a command, type help <topic>.
        """
        return super().do_help(arg)

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program."""
        print("")
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
