#!/usr/bin/env python3
"""Class Console"""

import cmd
from datetime import datetime, date, time
from models.base_model import BaseModel, storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB Console"""

    airbnb_models = {"BaseModel": BaseModel, "User": User, "Place": Place,
                     "State": State, "City": City,
                     "Amenity": Amenity, Review: "Review"}
    prompt = "(hbnb) "

    def do_quit(self, command):
        """Quit command line"""
        return True

    def do_EOF(self, command):
        """Quit command line"""
        return True

    def emptyline(self):
        """Repeat prompt"""
        pass

    def do_create(self, command):
        """This method crea new objet type BaseMo"""

        command_split = command.split()
        name_object = command_split[0]
        if len(command) == 0 or command is None:
            print("** class name missing **")
        elif command not in self.airbnb_models:
            print("** class doesn't exist **")
        else:
            new_instance = self.airbnb_models[name_object]()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, command):
        """Prints the string representation of an instance"""
        split_command = command.split()
        if len(split_command) == 0:
            print("** class name missing **")
            return
        elif split_command[0] not in self.airbnb_models:
            print("** class doesn't exist **")
            return
        elif len(split_command) == 1:
            print("** instance id missing **")
            return
        elif len(split_command) == 2:
            all_dict_json = storage.all()
            key_dict = "{}.{}".format(split_command[0], split_command[1])
            try:
                print("[{}] ({}) {}".format(split_command[0], split_command[1],
                                            all_dict_json[key_dict]))
            except:
                print("** no instance found **")

    def do_destroy(self, command):
        """Delete an instance based on the class name and id"""
        split_command = command.split()
        if len(split_command) == 0:
            print("** class name missing **")
            return
        elif split_command[0] not in self.airbnb_models:
            print("** class doesn't exist **")
            return
        elif len(split_command) == 1:
            print("** instance id missing **")
            return
        elif len(split_command) == 2:
            all_dict_json = storage.all()
            key_dict = "{}.{}".format(split_command[0], split_command[1])
            try:
                all_dict_json.pop(key_dict)
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, command=""):
        """Prints string representation of all instances"""
        instances = storage.all()
        if not command:
            print(instances)
        else:
            if command not in self.airbnb_models:
                print("** class doesn't exist **")
                return
            else:
                allItemsModel = []
                name_object = self.airbnb_models[command]
                for key, value in instances.items():
                    if command in key:
                        allItemsModel.append(name_object(**value).__str__())
                print(allItemsModel)

    def do_update(self, command):
        """Actualiza an instance based on the class name and id"""
        split_command = command.split()
        if not command:
            print("** class name missing **")
            return
        elif split_command[0] not in self.airbnb_models:
            print("** class doesn't exist **")
            return
        elif len(split_command) == 1:
            print("** instance id missing **")
            return
        elif len(split_command) == 2:
            print("** attribute name missing **")
            return
        elif len(split_command) == 3:
            print("** value missing **")
            return
        else:
            all_dict = storage.all()
            key_dict = "{}.{}".format(split_command[0], split_command[1])
            if key_dict not in all_dict:
                print("** no instance found **")
                return
            else:
                k_upd = split_command[2]
                v_upd = split_command[3]
                object_n = split_command[0]
                name_object = self.airbnb_models[object_n]
                all_dict[key_dict].update({k_upd: v_upd.replace('"', '')})
                new_instance = name_object(**all_dict[key_dict])
                new_instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
