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
from Modules.Creators_Mod.Text.credits import Credits_Manager
from Modules.Entities_Mod.structure import Structure
from Modules.Creators_Mod.Text.license import License_Manager

class ControllerDotH(License_Manager, Credits_Manager, Common_Creator):
    
    def __init__(self):
        super().__init__()
        self.Filename = 'Controller.h'
    
    def _create_top_defines(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine('#include <string.h>')
        s_builder.AppendLine('#include <ctype.h>')
        return super().create_top_defines(structure, s_builder)

    def _create_main_top_defines(self, text: str, s_builder: StringBuilder) -> None:
        return super().create_main_top_defines(text, s_builder)
    
    def _create_main_bot_defines(self, text: str, s_builder: StringBuilder) -> None:
        return super().create_main_bot_defines(text, s_builder)

    def create_license_header(self, s_builder: StringBuilder) -> None:
        return super().create_license_header(s_builder)
    
    def create_credits(self, s_builder: StringBuilder) -> None:
        return super().create_credits(s_builder)
    
    def create_load_from_text(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_loadFromText(char* path, LinkedList* pArrayList{structure.Alias});')
    
    def create_load_from_bin(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_loadFromBinary(char* path, LinkedList* pArrayList{structure.Alias});')
    
    def create_list(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_List{structure.Alias}(LinkedList* pArrayList{structure.Alias});')
    
    def create_sort(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_sort{structure.Alias}(LinkedList* pArrayList{structure.Alias});')
    
    def create_modify(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_edit{structure.Alias}(LinkedList* pArrayList{structure.Alias});')
    
    def create_save_as_text(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_saveAsText(char* path, LinkedList* pArrayList{structure.Alias});')
    
    def create_save_as_bin(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_saveAsBinary(char* path, LinkedList* pArrayList{structure.Alias});')
    
    def create_add(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_add{structure.Alias}(LinkedList* pArrayList{structure.Alias});')
    
    def create_remove(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_remove{structure.Alias}(LinkedList* pArrayList{structure.Alias});')
    
    def create_obtain_id(self, s_builder: StringBuilder) -> None:
        s_builder.AppendLine('int obtainID(int* id);')
    
    def create_upgrade_id(self, s_builder: StringBuilder) -> None:
        s_builder.AppendLine('int upgradeID(int id);')
    
    def create_save_max_id(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int saveMaxID(FILE* pFile, char* path, LinkedList* pArrayList{structure.Alias});')
    
    def create_controller(self, path: str, sub_path: str, structure: Structure) -> None:
        if structure:
            s_builder = StringBuilder()
            
            try:
                self.create_license_header(s_builder)
                self._create_main_top_defines('controller', s_builder)
                self._create_top_defines(structure, s_builder)
                s_builder.AppendLine()
                self.create_credits(s_builder)
                s_builder.AppendLine('\n// CONTROLLER: Load')
                self.create_load_from_text(structure, s_builder)
                self.create_load_from_bin(structure, s_builder)
                s_builder.AppendLine('\n// CONTROLLER: List')
                self.create_list(structure, s_builder)
                s_builder.AppendLine('\n// CONTROLLER: Sort')
                self.create_sort(structure, s_builder)
                s_builder.AppendLine('\n// CONTROLLER: Modify')
                self.create_modify(structure, s_builder)
                s_builder.AppendLine('\n// CONTROLLER: Save')
                self.create_save_as_text(structure, s_builder)
                self.create_save_as_bin(structure, s_builder)
                self.create_add(structure, s_builder)
                s_builder.AppendLine('\n// CONTROLLER: Remove')
                self.create_remove(structure, s_builder)
                s_builder.AppendLine('\n// CONTROLLER: Auxiliars')
                self.create_obtain_id(s_builder)
                self.create_upgrade_id(s_builder)
                self.create_save_max_id(structure, s_builder)
                self._create_main_bot_defines('controller', s_builder)

                if super().create_file(f'{path}/{sub_path}/{self.Filename}', s_builder):
                    print_message(f'{self.Filename} was created successfully')
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