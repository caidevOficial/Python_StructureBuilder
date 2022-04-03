# GNU GENERAL PUBLIC LICENSE
# Version 3, 29 June 2007
# 
# Copyright (C) 2022 <FacuFalcone - CaidevOficial>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os

from Modules.Auxiliars.formatter import print_message
from Modules.Auxiliars.stringbuilder import StringBuilder
from Modules.Data_Validator_Mod.data_validator import validate_answer
from Modules.Entities_Mod.parameter import Parameter
from Modules.Entities_Mod.structure import Structure
from Modules.Menu.menu import menu_of_types


def structure_name_col()-> str:
    """
    Gets the name of the structure.
    """
    sb = StringBuilder()
    validated = False
    while not validated:
        print("Through this program you'll be asked many times for yes or no.")
        print("At those times enter 'y' for yes and 'n' for no.")
        print("Nothing will be saved if you close the program at a random time.")
        print("The saving will only procced after the 'LAST CONFIRMATION' Question.")
        print("(An 's' will be added at the beginning of the structure name) so.. \n")
        print("Write the name of the Structure: ")
        sb.Append(input().strip())
        validated =  validate_answer('Are you sure? [y/n]: ')
    return sb.__str__()

def param_name_col(structure_name: str, order: int) -> str:
    """
    Gets the name of the parameter.
    """
    sb = StringBuilder()
    validated = False
    while not validated:
        print_message(f"Write the name of the {order}° parameter for {structure_name}: ")
        # print(f"Write the name of the parameter for {structure_name}: ")
        sb.Append(input().strip())
        validated =  validate_answer('Are you sure? [y/n]: ')
    return sb.__str__()

def param_type_col(order: int, param_name: str) -> str:
    """
    Gets the type of the parameter.
    """
    sb = StringBuilder()
    print_message(f"Write the type of the {order}° parameter [{param_name}]: ")
    sb.Append(menu_of_types())
    return sb.__str__()

def param_len_col(param_name: str, order: int) -> int:
    """
    Gets the length of the parameter.
    """
    sb = StringBuilder()
    validated = False
    while not validated:
        print_message(f"Write the length for the {order}° parameter [{param_name}]: ")
        sb.Append(input().strip())
        validated =  validate_answer('Are you sure? [y/n]: ')
    return int(sb)

def param_amount_col(structure_name: str) -> int:
    """
    Gets the amount of parameters for the structure.
    """
    sb = StringBuilder()
    validated = False
    while not validated:
        print_message(f"Write the amount of parameters for {structure_name}: ")
        sb.Append(input().strip())
        validated =  validate_answer('Are you sure? [y/n]: ')
    return sb.__int__()

def parameters_collector(structure: Structure) -> Structure:
    """[summary]\n
    Collects the parameters of the structure.
    Args:
        structure (Structure): [The structure to collect the parameters.]
    """
    amount_param = param_amount_col(structure.Structure_Name)
    for i in range(amount_param):
        param = Parameter()
        print_message(f"\nParameter {i+1} of {amount_param}")
        param_name = param_name_col(structure.Structure_Name, i+1)
        param_type = param_type_col(param_name, i+1)
        param_len = param_len_col(param_name, i+1) if param_type == 'char' else 1
        param.normalize_parameter(i+1, param_name, param_type, param_len)
        structure.add_parameter(param)
    return structure

def desktop_path() -> str:
    """[summary]\n
    Gets the desktop path.
    Returns:
        str: [The desktop path.]
    """
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    return desktop
