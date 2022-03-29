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


from Modules.Auxiliars.formatter import print_message as Print


def validate_answer(message: str, test_validate: str = None) -> bool:
    """[summary]\n
    Validate the answer of the user.
    
    Args:
        message (str): [The message to be shown to the user.]
        test_validate (str, optional): [The test to be validated.]
    
    Returns:
        bool: [True if the answer is 'y', False otherwise.]
    """
    Print(message)
    if test_validate:
        answer = test_validate
        print(f'Answer: {answer}')
    else:
        answer = input('Answer: ')
    return answer.lower() == 'y'
