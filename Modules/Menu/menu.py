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
#

from Modules.Data_Validator_Mod.data_validator import validate_answer as VA

def __print_options() -> None:
    """[summary]\n
    Print the options.
    """
    print('Possible types of parameters:')
    print("1. int\n2. float\n3. char\n4. long int\n5. short\n")
    

def __select_menu_option() -> int:
    """[summary]\n
    Select the menu option.
    
    Returns:
        int: [The menu option.]
    """
    __print_options()
    return int(input("Choose a number corresponding to the types listed above: "))

def menu_of_types() -> str:
    """[summary]\n
    Show the menu of types.
    
    Returns:
        str: [The menu of types.]
    """
    confirm = False
    options = {1:'int', 2:'float', 3:'char', 4:'long int', 5:'short'}
    option_selected = __select_menu_option()
    while not confirm:
        while not option_selected in options:
            print('Error, invalid option selected. Please, Try Again.')
            option_selected = __select_menu_option()
        confirm = VA('Are you sure you want to use the type (y/n)?: ')
    return options[option_selected]