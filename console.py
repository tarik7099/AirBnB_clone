#!/usr/bin/python3
"""Command interpreter module"""

import cmd
import json
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print("")
        return True

    def emptyline(self):
        pass

    def do_help(self, arg):
        """Help command"""
        super().do_help(arg)

    def do_create(self, arg):
        """Create command"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show command"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy command"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """All command"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            print([str(obj) for key, obj in objects.items() if key.split('.')[0] == args[0]])

    def do_update(self, arg):
        """Update command"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objects[key], args[2], args[3])
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
