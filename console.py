#!/usr/bin/python3
"""contains the entry point of the command intepreter"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class definition"""
    prompt = "(hbnb)"
    __valid_classes = ['BaseModel']

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """do nothing"""
        pass

    def do_create(self, line):
        commands = line.split(" ")
        if commands[0] == "":
            print("** class name missing **")
        elif commands[0] not in self.__valid_classes:
            print("** class doesn't exist **")
        else:
            if commands[0] in self.__valid_classes:
                x = BaseModel()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
