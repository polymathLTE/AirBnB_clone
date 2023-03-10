#!/usr/bin/python3

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """this defines the HBNB class which inherits from the base_model"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """this stops and exits the program"""
        return True

    def do_help(self, arg, *args):
        """displays short tutorial"""
        h_info = "Documented commands (type help <topic>):\n========================================\nEOF\t\thelp\t\tquit"
        h_quit = "This stops and exits the program"
        # work in progress, please review
        print(args)
        if len(args) < 1 or len(args) > 2:
            print(f'[Usage]: help\nhelp <command>\nsee commands list below\n{h_info}')
        if len(args) == 0:
            print(h_info)
        elif args[0] == 'quit':
            print(h_quit)

    def do_EOF(self, arg):
        """implements the EOF scenario"""
        print('')
        return True

    def do_create(self, *args):
        classes = ['BaseModel()', 'mo']
        if len(args) <= 0:
            print("** class name missing **")
        if args[0] in classes:
            s = BaseModel()
            print(s.id)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
