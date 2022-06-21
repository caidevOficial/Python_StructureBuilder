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

from Modules.Auxiliars.formatter import print_message
from Modules.Auxiliars.stringbuilder import StringBuilder
from Modules.Creators_Mod.Common.common_creator import Common_Creator
from Modules.Entities_Mod.structure import Structure


class LinkedListC(Common_Creator):

    def __init__(self):
        super().__init__()
        self.Filename = 'LinkedList.c'
    
    def create_linkedlist_file(self, path: str, sub_path: str, structure: Structure) -> None:
        if structure:
            try:
                s_builder = StringBuilder()
                # filename: str = "LinkedList.c"
                
                self.create_LL_C(structure, s_builder)

                if super().create_file(f'{path}/{sub_path}/{self.Filename}', s_builder):
                    print_message(f"{self.Filename} was created.")
                else:
                    print_message(f"{self.Filename} wasn't created.")
            except Exception as e:
                print_message(
                    e.args,
                    "Error in the creation of the file."
                )
                raise e
        else:
            print_message('Error: Structure is empty')