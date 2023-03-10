#!/usr/bin/python3

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """this defines the HBNB class which inherits from the base_model"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """this stops and exits the program"""
        return True

    def do_help(self, *args):
        """displays short tutorial"""
        h_list = ['quit', 'help'] # please update with necessary help topics
        h_info = f"Documented commands (type help <topic>):\n========================================\n{h_list}"
        h_quit = "This stops and exits the program"

        h_topics = {'quit': h_quit, 'help': h_info} # please uodate with necessary help topics

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

    def do_create(self, *args):
        classes = {'BaseModel': BaseModel()}
        if args[0] == "":
            print("** class name missing **")
        elif args[0] in classes.keys():
            s = classes.get(args[0])
            print(s.id)
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
