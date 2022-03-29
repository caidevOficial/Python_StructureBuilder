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

from Modules.Data_Validator_Mod.data_validator import validate_answer as VA

def __print_options() -> None:
    """[summary]\n
    Print the options.
    """
    print('\nPossible types of parameters:')
    print("1. int\n2. float\n3. char\n4. long int\n5. short\n")
    

def __select_menu_option(selected: int = None) -> int:
    """[summary]\n
    Select the menu option.

    Args:
        selected (int, optional): [The selected option.]
    
    Returns:
        int: [The menu option.]
    """
    __print_options()
    if selected:
        print(f'\nChoose a number corresponding to the types listed above: {selected}')
        return selected
    return int(input("\nChoose a number corresponding to the types listed above: "))

def menu_of_types(selected: int = None) -> str:
    """[summary]\n
    Select the type of parameter.
    
    Args:
        selected (int, optional): [The selected option.]

    Returns:
        str: [The type of parameter.]
    """
    option_test = None
    confirm = False
    options = {1:'int', 2:'float', 3:'char', 4:'long int', 5:'short'}
    while not confirm:
        option_selected = __select_menu_option(selected)
        while not option_selected in options:
            print('Error, invalid option selected. Please, Try Again.\n')
            option_selected = __select_menu_option()
        if selected:
            option_test = 'y'
        confirm = VA('Are you sure you want to use the type (y/n)?: ', option_test)
    return options[option_selected]
