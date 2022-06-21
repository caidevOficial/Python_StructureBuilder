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

class ParserDotC(License_Manager, Credits_Manager, Common_Creator):

    def __init__(self):
        super().__init__()
        self.Filename = 'Parser.c'

    def create_top_defines(self, structure: Structure, s_builder: StringBuilder) -> None:
        super().create_top_defines(structure, s_builder)
        s_builder.AppendLine(f'#include "{self.Filename.replace(".c", ".h")}"')
        s_builder.AppendLine(f'#include "{structure.Final_Structure_Name}.h"\n')
    
    def parser_from_bin(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int parser_{structure.Alias}fromBinary(FILE *pFile, LinkedList *pArrayList{structure.Alias}){{')
        s_builder.AppendLine(f'\t{structure.Final_Structure_Name}* {structure.Alias};')
        s_builder.AppendLine('\tint success = 0;')
        s_builder.AppendLine('\tif(pFile != NULL){')
        s_builder.AppendLine('\t\twhile(!feof(pFile)){')
        s_builder.AppendLine(f'\t\t\t{structure.Alias} = {structure.Alias}_newEmpty();')
        s_builder.AppendLine(f'\t\t\tif(fread({structure.Alias}, sizeof({structure.Final_Structure_Name}), 1, pFile)){{')
        s_builder.AppendLine(f'\t\t\t\tll_add(pArrayList{structure.Alias}, {structure.Alias});')
        s_builder.AppendLine('\t\t\t}')
        s_builder.AppendLine('\t\t}')
        s_builder.AppendLine('\t\tsuccess = 1;')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\treturn success;')
        s_builder.AppendLine('}')
    
    def _create_params_from_structure(self, structure: Structure, s_builder: StringBuilder) -> None:
        for index in range(1, len(structure.Parameters)):
            s_builder.AppendLine(f'\tchar aux_{structure.Parameters[index].Name_Parameter}[128];')
        s_builder.AppendLine()

    def _create_regex(self, structure: Structure, s_builder: StringBuilder) -> None:
        for index in range(1, len(structure.Parameters)-1):
            s_builder.Append('%[^,],')
        s_builder.Append('%[^\\n]\\n"')

    def _create_param_part(self, structure: Structure, s_builder: StringBuilder) -> None:
        for index in range(1, len(structure.Parameters)):
            s_builder.Append(f', aux_{structure.Parameters[index].Name_Parameter}')
        s_builder.AppendLine(');')

    def _create_fscanf(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.Append('fscanf(pFile, "')
        self._create_regex(structure, s_builder)
        self._create_param_part(structure, s_builder)

    def parser_from_text(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int parser_{structure.Alias}fromText(FILE *pFile, LinkedList *pArrayList{structure.Alias}){{')
        s_builder.AppendLine(f'\t{structure.Final_Structure_Name}* {structure.Alias};')
        s_builder.AppendLine('\tint success = 0;')
        s_builder.AppendLine('\tint firstElement = 1;')
        
        self._create_params_from_structure(structure, s_builder)

        s_builder.AppendLine('\tif(pFile != NULL){')
        s_builder.AppendLine('\t\twhile(!feof(pFile)){')
        s_builder.AppendLine('\t\t\tif(firstElement){')
        s_builder.Append('\t\t\t\t')
        self._create_fscanf(structure, s_builder)

        s_builder.AppendLine(f'\t\t\t\tfirstElement = !firstElement;')
        s_builder.AppendLine('\t\t\t}')

        s_builder.Append('\t\t\t')
        self._create_fscanf(structure, s_builder)
        s_builder.Append(f'\t\t\t{structure.Alias} = {structure.Alias}_newParam(')
        
        for index in range(1, len(structure.Parameters)-1):
            s_builder.Append(f'aux_{structure.Parameters[index].Name_Parameter}, ')
        s_builder.Append(f'aux_{structure.Parameters[len(structure.Parameters)-1].Name_Parameter});\n')

        s_builder.AppendLine(f'\t\t\tif({structure.Final_Structure_Name} != NULL){{')
        s_builder.AppendLine(f'\t\t\t\tll_add(pArrayList{structure.Alias}, {structure.Alias});')
        s_builder.AppendLine('\t\t\t\tsuccess = 1;')
        s_builder.AppendLine('\t\t\t}')
        s_builder.AppendLine('\t\t}')
        s_builder.AppendLine('\t}')
        s_builder.AppendLine('\treturn success;')
        s_builder.AppendLine('}\n')

    def create_file(self, path: str, s_builder: StringBuilder) -> bool:
        """[summary]\n
        Creates the file.h.\n
        Args:
            path (str): [Path to the file]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
            
        Returns:
            bool: [True if the file was created, False if not]
        """
        try:
            with open(path, 'w') as file:
                for line in s_builder:
                    print(line, file=file)
                print_message(
                    f"File {path.split('/')[-1]} was created.",
                    f'in Path: {path}'
                )
                s_builder.Clear()
                return True
        except Exception as e:
            print_message(e.args)
            raise e

    def create_parser(self, path: str, sub_path: str, structure: Structure) -> None:
        if structure:
            s_builder = StringBuilder()
            # filename: str = "parser.c"
            try:
                self.create_license_header(s_builder)
                self.create_top_defines(structure, s_builder)
                self.create_credits(s_builder)
                self.parser_from_text(structure, s_builder)
                self.parser_from_bin(structure, s_builder)

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
