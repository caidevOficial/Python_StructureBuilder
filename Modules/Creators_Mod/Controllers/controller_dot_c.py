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

class ControllerDotC(License_Manager, Credits_Manager, Common_Creator):

    def __init__(self):
        super().__init__()
        self.Filename = 'Controller.c'
    
    def _create_top_defines(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine('#include <string.h>')
        s_builder.AppendLine('#include <ctype.h>')
        s_builder.AppendLine('#include "Parser.h"')
        s_builder.AppendLine(f'#include "{self.Filename.replace(".c", ".h")}"')
        s_builder.AppendLine(f'#include "{structure.Final_Structure_Name}.h"\n')
        return super().create_top_defines(structure, s_builder)

    def _create_main_top_defines(self, text: str, s_builder: StringBuilder) -> None:
        return super().create_main_top_defines(text, s_builder)
    
    def _create_main_bot_defines(self, text: str, s_builder: StringBuilder) -> None:
        return super().create_main_bot_defines(text, s_builder)

    def create_license_header(self, s_builder: StringBuilder) -> None:
        return super().create_license_header(s_builder)
    
    def create_get_higher_ID(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int {structure.Alias}_get_higher_ID({structure.Alias}* this, int* id){{')
        s_builder.AppendLine('\tint success = -1;')
        s_builder.AppendLine('\tif(this != NULL){')
        s_builder.AppendLine(f'\t\t{structure.Alias}_getID(this, id);')
        s_builder.AppendLine('\t\tsuccess = 0;')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\treturn success;')
        s_builder.AppendLine('}')

    def create_save_max_id_as_text(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int saveAsText_maxID(FILE* pFile, LinkedList* pArrayList{structure.Alias}, int* maxID){{')
        s_builder.AppendLine(f'\t{structure.Final_Structure_Name}* {structure.Alias};')
        s_builder.AppendLine('\tint ID;')
        s_builder.AppendLine('\tint len_LL;')
        s_builder.AppendLine('\tint success = 0;')
        s_builder.AppendLine('\tint biggerID;')
        s_builder.AppendLine('\tint flag = 0;')
        s_builder.AppendLine(f'\tif(pFile != NULL && pArrayList{structure.Alias} != NULL){{')
        s_builder.AppendLine(f'\t\tlen_LL = ll_len(pArrayList{structure.Alias});')
        s_builder.AppendLine('\t\tfor(int = 0; i<len_ll; i++){')
        s_builder.AppendLine(f'\t\t\t{structure.Alias} = ll_get(pArrayList{structure.Alias}, i);')
        s_builder.AppendLine(f'\t\t\t{structure.Alias}_getHigherID({structure.Alias}, &ID);')
        s_builder.AppendLine('\t\t\tif(!flag || ID > biggerID){')
        s_builder.AppendLine('\t\t\t\tbiggerID = ID;')
        s_builder.AppendLine('\t\t\t\tflag = 1;')
        s_builder.AppendLine('\t\t\t}')
        s_builder.AppendLine('\t\t\tsuccess = 1;')
        s_builder.AppendLine('\t\t}')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\t*maxID = biggerID;')
        s_builder.AppendLine('\treturn success;')
        s_builder.AppendLine('\t}')

    def create_save_as_text_maxID(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_saveAsTextMaxID(FILE* pFile, char* path, LinkedList* pArrayList{structure.Alias}){{')
        s_builder.AppendLine('\tint success = 0;')
        s_builder.AppendLine('\tint maxID;')
        s_builder.AppendLine(f'\tif(pFile != NULL && saveAsText_maxID(pFile, pArrayList{structure.Alias}, &maxID)){{')
        s_builder.AppendLine('\t\tsuccess = 1;')
        s_builder.AppendLine('\t\tfprintf(pFile, "%d\n", maxID+1);')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\treturn success;')
        s_builder.AppendLine('}')

    def create_obtain_id(self, s_builder: StringBuilder) -> None:
        s_builder.AppendLine('int obtainID(int* id){')
        s_builder.AppendLine('\tint success = 0;')
        s_builder.AppendLine('\tint newID;')
        s_builder.AppendLine('\tFILE* pFile;')
        s_builder.AppendLine('\tpFile = fopen("lastID.txt", "r");')
        s_builder.AppendLine('\tif(pFile != NULL){')
        s_builder.AppendLine('\t\tfscanf(pFile, "%d\n", &newID);')
        s_builder.AppendLine('\t\t*id = newID;')
        s_builder.AppendLine('\t\tfclose(pFile);')
        s_builder.AppendLine('\t\tsuccess = 1;')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\treturn success;')
        s_builder.AppendLine('}')
    
    def create_upgrade_id(self, s_builder: StringBuilder) -> None:
        s_builder.AppendLine('int upgradeID(int id){')
        s_builder.AppendLine('\tint success = 0;')
        s_builder.AppendLine('\tFILE* pFile;')
        s_builder.AppendLine('\tpFile = fopen("lastID.txt", "w");')
        s_builder.AppendLine('\tif(pFile != NULL){')
        s_builder.AppendLine('\t\tfprintf(pFile, "%d\n", nextID);')
        s_builder.AppendLine('\t\tfclose(pFile);')
        s_builder.AppendLine('\t\tsuccess = 1;')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\treturn success;')
        s_builder.AppendLine('}')

    def create_save_max_id():
        pass

    def create_load_from_text(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_loadFromText(char* path, LinkedList* pArrayList{structure.Alias}){{')
        s_builder.AppendLine('\tFILE* pFile;')
        s_builder.AppendLine('\tFILE* pFile2;')
        s_builder.AppendLine('\tint success = 0;\n')
        s_builder.AppendLine('\tpFile = fopen(path, "r");')
        s_builder.AppendLine('\tpFile2 = fopen("lastID.txt", "w");')
        s_builder.AppendLine('\tif(pFile != NULL){')
        s_builder.AppendLine(f'\t\tparser_{structure.Alias}FromText(pFile, pArrayList{structure.Alias});')
        s_builder.AppendLine('\t\tfclose(pFile);')
        s_builder.AppendLine('\t\tsuccess = 1;')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\tif(controller_saveAsTextMaxID(pFile2, "maxID.txt", pArrayList{structure.Alias}){')
        s_builder.AppendLine('\t\tfclose(pFile2);')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\treturn success;')
        s_builder.AppendLine('}')
    
    def create_load_from_bin(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_loadFromBinary(char* path, LinkedList* pArrayList{structure.Alias}){{')
        s_builder.AppendLine('\tFILE* pFile;')
        s_builder.AppendLine('\tFILE* pFile2;')
        s_builder.AppendLine('\tint success = 0;\n')
        s_builder.AppendLine('\tpFile = fopen(path, "rb");')
        s_builder.AppendLine('\tpFile2 = fopen("lastID.txt", "w");')
        s_builder.AppendLine('\tif(pFile != NULL){')
        s_builder.AppendLine(f'\t\tparser_{structure.Alias}FromBinary(pFile, pArrayList{structure.Alias});')
        s_builder.AppendLine('\t\tfclose(pFile);')
        s_builder.AppendLine('\t\tsuccess = 1;')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\tif(controller_saveAsTextMaxID(pFile2, "maxID.txt", pArrayList{structure.Alias}){')
        s_builder.AppendLine('\t\tfclose(pFile2);')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\treturn success;')
        s_builder.AppendLine('}')

    def create_list():
        pass

    def create_sort():
        pass

    def create_modify():
        pass

    def create_save_as_text_csv():
        pass

    def create_save_as_text(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_saveAsText(char* path, LinkedList* pArrayList{structure.Alias}){{')
        s_builder.AppendLine('\tint success = 0;')
        s_builder.AppendLine('\tFILE* pFile = fopen(path, "w");')
        s_builder.AppendLine(f'\tif(pFile != NULL && saveAsTextFormat_CSV(pFile, pArrayList{structure.Alias})){{')
        s_builder.AppendLine('\t\tsuccess = 1;')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\tfclose(pFile);')
        s_builder.AppendLine(f'\tll_clear(pArrayList{structure.Alias});')
        s_builder.AppendLine('\treturn success;')
        s_builder.AppendLine('}')

    def create_save_as_bin(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_saveAsBinary(char* path, LinkedList* pArrayList{structure.Alias}){{')
        s_builder.AppendLine('\tint success = 0;')
        s_builder.AppendLine(f'\t{structure.Final_Structure_Name}* {structure.Alias};')
        s_builder.AppendLine('\tFILE* pFile;')
        s_builder.AppendLine(f'\tif(pArrayList{structure.Alias} != NULL){{')
        s_builder.AppendLine('\t\tpFile = fopen(path, "wb");')
        s_builder.AppendLine(f'\t\tfor(int i = 0; i < ll_len(pArrayList{structure.Alias}); i++){{')
        s_builder.AppendLine(f'\t\t\t{structure.Alias} = ({structure.Final_Structure_Name}*) ll_get(pArrayList{structure.Alias}, i);')
        s_builder.AppendLine(f'\t\t\tfwrite({structure.Alias}, sizeof({structure.Final_Structure_Name}), 1, pFile);')
        s_builder.AppendLine('\t\t}')
        s_builder.AppendLine('\t\tfclose(pFile);')
        s_builder.AppendLine(f'\t\tll_clear(pArrayList{structure.Alias});')
        s_builder.AppendLine('\t\tsuccess = 1;')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\treturn success;')
        s_builder.AppendLine('}')


    def create_add(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int controller_add{structure.Alias}(LinkedList* pArrayList{structure.Alias}){{')
        s_builder.AppendLine(f'\t{structure.Final_Structure_Name}* {structure.Alias};')
        s_builder.AppendLine(f'\t{structure.Alias} = {structure.Alias}_newEmpty();')
        s_builder.AppendLine('\tint success = 0;')
        s_builder.AppendLine('\tint idForUse;')
        self._create_parameters(structure, s_builder)
        s_builder.AppendLine(f'\tif(pArrayList{structure.Alias} != NULL){{')
        s_builder.AppendLine('\t\tobtainID(&idForUse);')
        s_builder.AppendLine('\t\tprinf("[BOT]: El alta se asignara con el ID: %d\n", idForUse);')
        # TODO: Create the get data function for each parameter
        # ? Code here

        # TODO: Create structure setAllInfo function
        # ? Code here
        # LIKE: KnightZodiac_setAllInfo(pKnightZodiac, &idForUse, nameKnightZodiac, constellationName, armorType, level, cosmosLevel);
         
        s_builder.AppendLine(f't\t\tll_add(pArrayList{structure.Alias}, {structure.Alias});')
        s_builder.AppendLine('\t\t\tupgradeID(idForUse);')
        s_builder.AppendLine('\t\t\tsuccess = 1;')
        s_builder.AppendLine('\t\t}')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\treturn success;')
        s_builder.AppendLine('}')

    




    def create_controller(self, path: str, sub_path: str, structure: Structure) -> None:
        if structure:
            s_builder = StringBuilder()
            
            try:
                self.create_license_header(s_builder)
                self._create_main_top_defines('controller', s_builder)
                self._create_top_defines(structure, s_builder)
                s_builder.AppendLine()
                self.create_credits(s_builder)

                s_builder.AppendLine('\n// CONTROLLER: Auxiliars')
                #* Done
                self.create_get_higher_ID(structure, s_builder)
                self.create_save_max_id_as_text(structure, s_builder)
                self.create_save_as_text_maxID(structure, s_builder)
                self.create_obtain_id(s_builder)
                self.create_upgrade_id(s_builder)
                #! TODO
                self.create_save_max_id(structure, s_builder)
                

                #* Done
                s_builder.AppendLine('\n// CONTROLLER: Load')
                self.create_load_from_text(structure, s_builder)
                self.create_load_from_bin(structure, s_builder)

                #! TODO
                s_builder.AppendLine('\n// CONTROLLER: List')
                self.create_list(structure, s_builder)

                #! TODO
                s_builder.AppendLine('\n// CONTROLLER: Sort')
                self.create_sort(structure, s_builder)

                #! TODO
                s_builder.AppendLine('\n// CONTROLLER: Modify')
                self.create_modify(structure, s_builder)

                #* Done
                s_builder.AppendLine('\n// CONTROLLER: Save')
                self.create_save_as_text(structure, s_builder)
                self.create_save_as_bin(structure, s_builder)
                #! TODO
                self.create_add(structure, s_builder)

                #! TODO
                s_builder.AppendLine('\n// CONTROLLER: Remove')
                self.create_remove(structure, s_builder)

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