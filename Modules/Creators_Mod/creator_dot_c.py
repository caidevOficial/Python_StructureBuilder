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
from Modules.Creators_Mod.creator import Creator
from Modules.Auxiliars.stringbuilder import StringBuilder
from Modules.Entities_Mod.parameter import Parameter
from Modules.Entities_Mod.structure import Structure

class CreatorDotC(Creator):
    _FILENAME: str = 'Modules/Creators_Mod/license.txt'

    def __init__(self) -> None:
        super().__init__()
    
    def create_license_header(self, s_builder: StringBuilder) -> None:
        super().create_license_header(s_builder)
    
    def __check_char_param(self, structure: Structure) -> bool:
        if not structure is None:
            for parameter in structure.parameters:
                if parameter.Type_Parameter == 'char':
                    return True
        return False

    def create_imports(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine('#include <stdlib.h>')
        s_builder.AppendLine('#include <stdio.h>')

        if self.__check_char_param(structure):
            s_builder.AppendLine('#include <string.h>')
        s_builder.AppendLine('#include "LinkedList.h"')
        s_builder.AppendLine(f'#include "{structure.Final_Structure_Name}.h"\n')
    
    def create_builder_empty(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'{structure.Final_Structure_Name}* {structure.Final_Structure_Name}_newEmpty(){{')
        s_builder.Append(f'\treturn ({structure.Final_Structure_Name}*) ')
        s_builder.AppendLine(f'calloc(sizeof({structure.Final_Structure_Name}), 1);\n}}\n')

    def create_builder_with_params(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'{structure.Final_Structure_Name}* {structure.Final_Structure_Name}_newParametros(')
        for parameter in structure.parameters:
            s_builder.Append(f'\t{parameter.Type_Parameter} {parameter.Name_Parameter},')
        s_builder.AppendLine('\n\tint id)')
        s_builder.AppendLine(f'{{\n\t{structure.Final_Structure_Name}* this = {structure.Final_Structure_Name}_newEmpty();')
        for parameter in structure.parameters:
            s_builder.Append(f'\n\tthis->{parameter.Name_Parameter} = {parameter.Name_Parameter};')
        s_builder.AppendLine('\n\tthis->id = id;')
        s_builder.AppendLine('\n\treturn this;\n}}\n')

    def create_builder_parameters_list(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'{structure.Final_Structure_Name}* {structure.Alias}_new(')
        for parameter in structure.Parameters:
            if parameter.Length_Parameter == 1:
                s_builder.Append(f'{parameter.Type_Parameter} {parameter.Name_Parameter}')
            else:
                s_builder.Append(f'{parameter.Type_Parameter}* {parameter.Name_Parameter}')
            
            if len(structure.Parameters) -1 != structure.Parameters.index(parameter):
                s_builder.Append(', ')
            else:
                s_builder.AppendLine('){{')
        s_builder.AppendLine(f'\t{structure.Final_Structure_Name}* this = {structure.Alias}_newEmpty();')
        s_builder.AppendLine(f'\tif(this != NULL){{')

        for parameter in structure.Parameters:
            s_builder.AppendLine(f'\t\t{structure.Alias}_set{parameter.Alias}(this, {parameter.Name_Parameter});')
        s_builder.AppendLine('\t}}\n\treturn this;\n}}\n')
    
    def show_one_entity(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'void {structure.Alias}_showO({structure.Final_Structure_Name}* this){{')
        for parameter in structure.Parameters:
            s_builder.Append(f'\t{parameter.Type_Parameter} {parameter.Name_Parameter}')
            if parameter.Type_Parameter == 'char':
                s_builder.Append(f'[{parameter.Length_parameter}]')
            s_builder.AppendLine(';')
        s_builder.AppendLine()
        for parameter in structure.Parameters:
            if parameter.Type_Parameter == 'char':
                s_builder.AppendLine(f'\t{structure.Alias}_get{parameter.Alias}')
                s_builder.AppendLine(f'(this, {parameter.Name_Parameter});')
            else:
                s_builder.Append(f'\t{structure.Alias}_get{parameter.Alias}')
                s_builder.AppendLine(f'(this, &{parameter.Name_Parameter});')
        s_builder.AppendLine()
        s_builder.AppendLine(f'\tif(this != NULL){{')
        s_builder.Append(f'\t\tprintf("')
        for parameter in structure.Parameters:
            if parameter.Type_Parameter == 'char':
                s_builder.Append(f'%s')
            elif parameter.Type_Parameter == 'int' or parameter.Type_Parameter == 'short':
                s_builder.Append(f'%d')
            elif parameter.Type_Parameter == 'long int':
                s_builder.Append(f'%ld')
            elif parameter.Type_Parameter == 'float':
                s_builder.Append(f'%f')
            
            if len(structure.Parameters) -1 != structure.Parameters.index(parameter):
                s_builder.Append('|')
            else:
                s_builder.Append(f'\\n"')
                for parameter in structure.Parameters:
                    s_builder.Append(f', {parameter.Name_Parameter}')
                s_builder.AppendLine(');')
        s_builder.AppendLine(f'\t\tprintf("-\\n");\n\t}}\n}}\n')
    

    def show_all_entities(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'void {structure.Alias}_showAll(LinkedList* this, char* errorMessage){{')
        s_builder.AppendLine(f'\tint length;')
        s_builder.AppendLine(f'\tint isError = 1;')
        s_builder.AppendLine(f'\t{structure.Final_Structure_Name}* {structure.Structure_Name};')
        s_builder.AppendLine(f'\tlength = ll_len(this);')
        s_builder.AppendLine(f'\tif(length > 0){{')
        s_builder.AppendLine(f'\t\tprintf("')

        for parameter in structure.Parameters:
            s_builder.Append(f'{parameter.Name_Parameter}')

            if len(structure.Parameters) -1 != structure.Parameters.index(parameter):
                s_builder.Append('|')
            else:
                s_builder.AppendLine(f'\\n");')
        s_builder.AppendLine(f'\t\tprintf("-\\n");')
        s_builder.AppendLine(f'\t\tfor(int i = 0; i < length; i++){{')
        s_builder.AppendLine(f'\t\t\t{structure.Structure_Name} = ({structure.Final_Structure_Name}*) ll_get(this, i);')
        s_builder.AppendLine(f'\t\t\t{structure.Alias}_show({structure.Structure_Name});\n\t\t')
        s_builder.AppendLine(f'\t\tisError = 0;\n\t}}')
        s_builder.AppendLine(f'\telse{{')
        s_builder.AppendLine(f'\t\tprintf(errorMessage);\n\t}}')
        s_builder.AppendLine(f'\treturn isError;')
    
    def create_basic_struct_functions(self, structure: Structure, s_builder: StringBuilder) -> None:
        if not structure is None:
            self.create_license_header(s_builder)
            self.create_imports(structure, s_builder)
            s_builder.AppendLine(f'// ## {structure.Final_Structure_Name}: CONSTRUCTORS')
            # *# Empty Builder
            self.create_builder_empty(structure, s_builder)
            # *# Builder with parameters
            self.create_builder_with_params(structure, s_builder)
            s_builder.AppendLine(f'// ## {structure.Final_Structure_Name}: SHOW & SHOW ALL.')
            # *# Show one entity
            self.show_one_entity(structure, s_builder)
            # *# Show all entities
            self.show_all_entities(structure, s_builder)

        # TODO: Implement create comparer with char

