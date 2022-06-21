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

class ParserDotH(License_Manager, Credits_Manager, Common_Creator):
    def __init__(self):
        super().__init__()
        self.Filename = 'Parser.h'

    def _create_main_top_defines(self, s_builder: StringBuilder) -> None:
        super().create_main_top_defines('Parser', s_builder)
        
    def _create_main_bot_defines(self, s_builder: StringBuilder):
        super().create_main_bot_defines('Parser', s_builder)

    def create_top_defines(self, structure: Structure, s_builder: StringBuilder) -> None:
        self._create_main_top_defines(s_builder)
        super().create_top_defines(structure, s_builder)
        s_builder.AppendLine(f'#include "{structure.Final_Structure_Name}.h"\n')

    def parser_from_bin(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int parser_{structure.Alias}fromBinary(FILE *pFile, LinkedList *pArrayList{structure.Alias});')
        s_builder.AppendLine()

    def parser_from_text(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int parser_{structure.Alias}fromText(FILE *pFile, LinkedList *pArrayList{structure.Alias});')
        s_builder.AppendLine()

    def create_parser(self, path: str, sub_path: str, structure: Structure) -> None:
        if structure:
            s_builder = StringBuilder()
            # filename: str = "parser.h"
            try:
                self.create_license_header(s_builder)
                self.create_top_defines(structure, s_builder)
                self.create_credits(s_builder)
                self.parser_from_text(structure, s_builder)
                self.parser_from_bin(structure, s_builder)
                self._create_main_bot_defines(s_builder)

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