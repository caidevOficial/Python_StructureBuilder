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


def capitalize_words(text: str) -> str:
    """[summary]\n
    Capitalize the words of the text.
    
    Args:
        text (str): [The text to be capitalized.]
    
    Returns:
        str: [The text with capitalized words.]
    """
    text = text.strip()
    return " ".join(word.capitalize() for word in text.split(' '))

def message_decor(func) -> None:
    """[summary]\n
    Decorator to show a message before and after the function.
    
    Args:
        func (function): [The function to be decorated.]
    """
    def wrapper(*args, **kwargs):
        symbols = ''.join(['#' for _ in range(len(*args))])
        print(symbols)
        func(*args)
        print(f'{symbols}\n')
    return wrapper

@message_decor
def print_message(message: str) -> None:
    """[summary]\n
    Prints a message.
    
    Args:
        message (str): [The message to be printed.]
    """
    print(message)
