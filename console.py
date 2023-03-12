#!/usr/bin/python3

import cmd
from models import storage
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""This is the console: the entry point of the AirBnB command line program"""


class HBNBCommand(cmd.Cmd):
    """this defines the HBNB class which inherits from the base_model"""
    prompt = "(hbnb) "
    __classes = {
        'BaseModel': BaseModel(),
        'User': User(),
        'State': State(),
        'Amenity': Amenity(),
        'Place': Place(),
        'Review': Review()
    }

    def do_quit(self, arg):
        """this stops and exits the program"""
        return True

    def do_help(self, *args):
        """displays help topics and usage syntax"""
        h_list = ['quit', 'help', 'EOF', 'all', 'destroy', 'create', 'show', 'update']
        h_info = f"Documented commands (type help <topic>):\n========================================\n{h_list}"
        h_quit = "This stops and exits the program"
        h_EOF = "This signifies an end of file - EOF"
        h_update = '[Usage]: update <class name> <id> <attribute name> "<attribute value>'

        h_topics = {'quit': h_quit, 'help': h_info, 'EOF': h_EOF, 'update': h_update} # please update as necessary

        if args[0] == "":
            print(h_info)
        elif args[0] not in h_topics.keys():
            print(f"No help for requested topic\n{h_info}")
        else:
            print(h_topics.get(args[0]))

    def do_EOF(self, arg):
        """implements the EOF scenario"""
        print('')
        return True

    def do_create(self, arg):
        argl = arg.split()
        if self.__is_class(argl):
            s = HBNBCommand.__classes.get(argl[0])
            print(s.id)
            s.save()

    def do_show(self, arg):
        storage.reload()
        argl = arg.split()
        if self.__is_class(argl):
            args = '.'.join(argl)
            all_objs = storage.all()
            if self.__is_instance(argl, all_objs):
                print(all_objs.get(args))

    def do_destroy(self, arg):
        """destroys an given instance and saves the change to file"""
        argl = arg.split()
        if self.__is_class(argl):
            args = '.'.join(argl)
            all_objs = storage.all()
            if self.__is_instance(argl, all_objs):
                all_objs.pop(args)
                storage.save()

    def do_all(self, arg):
        """display the string representation of all instances"""
        storage.reload()
        all_objs = storage.all()
        argl = arg.split()
        if argl and self.__is_class(argl):
            for obj in all_objs.keys():
                if re.search(f"^{argl[0]}*", obj): # refactor later; make into a function
                    print(all_objs.get(obj))
        elif not argl:
            for obj in all_objs.keys():
                print(all_objs.get(obj))

    def do_update(self, arg):
        """updates the instance with the given info and saves changes
        [Usage]: update <class name> <id> <attribute name> "<attribute value>"
        """
        # under construction
        argl = arg.split()
        if self.__is_class(argl):
            all_objs = storage.all()
            if self.__is_instance(argl, all_objs):
                args = '.'.join(argl[0:2])
                if not len(argl) >= 3:
                    print("** attribute name missing **")
                    return
                elif not len(argl) >= 4:
                    print("** value missing **")
                    return
                elif self.__is_writable(argl[2]):
                    obj = all_objs.get(args)
                    setattr(obj, argl[2], argl[3])
                    storage.save()

    def __is_class(self, arg):
        """returns True if a given class exists, else returns false"""
        if not arg: # checks if empty
            print("** class name missing **")
        elif arg[0] in HBNBCommand.__classes.keys():
            return True
        else:
            print("** class doesn't exist **")

    def __is_instance(self, id_class=[], al_obj={}):
        """returns true if a given instance exists, else returns false"""
        obj = ".".join(id_class[0:2])
        print(obj)
        if len(id_class) == 1:
            print("** instance id missing **")
        elif obj in al_obj.keys():
            return True
        else:
            print("** no instance found **")

    def __is_writable(self, arg):
        """returns True if a given attribute can be updated
        Read-Only attributes: id, created_at, updated_at
        """
        ROA = ['id', 'created_at', 'updated_at']
        if arg not in ROA:
            return True
        else:
            print("** attribute name is READ-ONLY")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
