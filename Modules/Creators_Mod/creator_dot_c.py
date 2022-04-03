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

from Modules.Auxiliars.stringbuilder import StringBuilder
from Modules.Creators_Mod.creator import Creator
from Modules.Entities_Mod.parameter import Parameter
from Modules.Entities_Mod.structure import Structure


class CreatorDotC(Creator):
    
    def __init__(self) -> None:
        super().__init__()
    
    def read_text_file(self, s_builder: StringBuilder, path: str) -> None:
        super().read_text_file(s_builder, path)
    
    def __check_char_param(self, structure: Structure) -> bool:
        if not structure is None:
            for i in range(1, len(structure.Parameters)):
                if structure.Parameters[i].Type_Parameter == 'char':
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
        s_builder.AppendLine(f'{structure.Final_Structure_Name}* {structure.Alias}_newEmpty(){{')
        s_builder.Append(f'\treturn ({structure.Final_Structure_Name}*) ')
        s_builder.AppendLine(f'calloc(sizeof({structure.Final_Structure_Name}), 1);\n}}\n')

    def add_parameter_into_builder(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the builder with parameters of the file.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            parameter (Parameter): [Parameter to write into the file]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        if parameter.Type_Parameter == 'char':
            s_builder.Append(f"{parameter.Type_Parameter}* {parameter.Name_Parameter}")
        else:
            s_builder.Append(f"{parameter.Type_Parameter} {parameter.Name_Parameter}")
        
        if structure.Parameters.index(parameter) != len(structure.Parameters) - 1:
            s_builder.Append(", ")
        else:
            s_builder.AppendLine("){")

    def add_parameter_to_builder(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Adds parameters to the builder of the file.h.\n

        Args:
            structure (Structure): [Structure to add the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        for i in range(1, len(structure.Parameters)):
            parameter = structure.Parameters[i]
            self.add_parameter_into_builder(structure, parameter, s_builder)

    # !### Verify this!
    def create_builder_with_params(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.Append(f'{structure.Final_Structure_Name}* {structure.Alias}_new(')
        self.add_parameter_to_builder(structure, s_builder)
        s_builder.AppendLine(f'\t{structure.Final_Structure_Name}* this = {structure.Alias}_newEmpty();')
        s_builder.AppendLine('\tif(this != NULL){')
        for i in range(1, len(structure.Parameters)):
            s_builder.AppendLine(f'\t\t{structure.Alias}_set{structure.Parameters[i].Alias}(this, {structure.Parameters[i].Name_Parameter});')
        s_builder.AppendLine('\t}\n\treturn this;\n}\n')

    def show_one_entity(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'void {structure.Alias}_show({structure.Final_Structure_Name}* this){{')
        for i in range(1, len(structure.Parameters)):
            s_builder.Append(f'\t{structure.Parameters[i].Type_Parameter} {structure.Parameters[i].Name_Parameter}')
            if structure.Parameters[i].Type_Parameter == 'char':
                s_builder.Append(f'[{structure.Parameters[i].Length_Parameter}]')
            s_builder.AppendLine(';')
        s_builder.AppendLine()
        
        for i in range(1, len(structure.Parameters)):
            if structure.Parameters[i].Type_Parameter == 'char':
                s_builder.Append(f'\t{structure.Alias}_get{structure.Parameters[i].Alias}')
                s_builder.AppendLine(f'(this, {structure.Parameters[i].Name_Parameter});')
            else:
                s_builder.Append(f'\t{structure.Alias}_get{structure.Parameters[i].Alias}')
                s_builder.AppendLine(f'(this, &{structure.Parameters[i].Name_Parameter});')
        s_builder.AppendLine()
        s_builder.AppendLine('\tif(this != NULL){')
        s_builder.Append('\t\tprintf("')
        
        for i in range(1, len(structure.Parameters)):
            if structure.Parameters[i].Type_Parameter == 'char':
                s_builder.Append(f'%s')
            elif structure.Parameters[i].Type_Parameter == 'int' or structure.Parameters[i].Type_Parameter == 'short':
                s_builder.Append(f'%d')
            elif structure.Parameters[i].Type_Parameter == 'long int':
                s_builder.Append(f'%ld')
            elif structure.Parameters[i].Type_Parameter == 'float':
                s_builder.Append(f'%f')
            
            if len(structure.Parameters) -1 != i:
                s_builder.Append('|')
            else:
                s_builder.Append(f'\\n"')
                for i in range(1, len(structure.Parameters)):
                    s_builder.Append(f', {structure.Parameters[i].Name_Parameter}')
                s_builder.AppendLine(');')
        s_builder.AppendLine('\t\tprintf("-\\n");\n\t}\n}\n')
    

    def show_all_entities(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'int {structure.Alias}_showAll(LinkedList* this, char* errorMessage){{')
        s_builder.AppendLine('\tint length;')
        s_builder.AppendLine('\tint isError = 1;')
        s_builder.AppendLine(f'\t{structure.Final_Structure_Name}* {structure.Structure_Name};')
        s_builder.AppendLine('\tlength = ll_len(this);')
        s_builder.AppendLine('\tif(length > 0){')
        s_builder.Append('\t\tprintf("')

        for i in range(1, len(structure.Parameters)):
            s_builder.Append(f'{structure.Parameters[i].Name_Parameter}')

            if len(structure.Parameters) -1 != i:
                s_builder.Append('|')
            else:
                s_builder.AppendLine('\\n");')
        s_builder.AppendLine('\t\tprintf("-\\n");')
        s_builder.AppendLine('\t\tfor(int i = 0; i < length; i++){')
        s_builder.AppendLine(f'\t\t\t{structure.Structure_Name} = ({structure.Final_Structure_Name}*) ll_get(this, i);')
        s_builder.AppendLine(f'\t\t\t{structure.Alias}_show({structure.Structure_Name});\n\t\t}}')
        s_builder.AppendLine('\t\tisError = 0;\n\t}')
        s_builder.AppendLine('\telse{')
        s_builder.AppendLine('\t\tprintf(errorMessage);\n\t}')
        s_builder.AppendLine('\treturn isError;\n}\n')
    
    def create_basic_struct_functions(self, structure: Structure, s_builder: StringBuilder) -> None:
        super().create_basic_struct_functions(structure, s_builder)

    def __create_comparer_with_char(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f"// For use in a sort function - Compare {structure.Structure_Name}->{parameter.Name_Parameter}")
        s_builder.AppendLine(f"int {structure.Alias}_compare{parameter.Alias}(void* this1, void* this2){{")
        s_builder.AppendLine("\tint anw;")
        # ?## First variable
        s_builder.AppendLine(f"\t{parameter.Type_Parameter} {parameter.Name_Parameter}1_1[{parameter.Length_Parameter}];")
        # ?## Second variable
        s_builder.AppendLine(f"\t{parameter.Type_Parameter} {parameter.Name_Parameter}2_2[{parameter.Length_Parameter}];\n")
        # ?## First getter
        s_builder.AppendLine(f"\t{structure.Alias}_get{parameter.Alias}(this1, {parameter.Name_Parameter}1_1);")
        # ?## Second getter
        s_builder.AppendLine(f"\t{structure.Alias}_get{parameter.Alias}(this2, {parameter.Name_Parameter}2_2);\n")
        s_builder.AppendLine(f"\tanw = strcmp({parameter.Name_Parameter}1_1, {parameter.Name_Parameter}2_2);")
        s_builder.AppendLine("\treturn anw;\n}\n")

    def __create_comparer_without_char(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f"// For use in a sort function - Compare {structure.Structure_Name}->{parameter.Name_Parameter}")
        s_builder.AppendLine(f"int {structure.Alias}_compare{parameter.Alias}(void* this1, void* this2){{")
        s_builder.AppendLine("\tint anw = 0;")
        # ?## First variable
        s_builder.AppendLine(f"\t{parameter.Type_Parameter} {parameter.Name_Parameter}1_1;")
        # ?## Second variable
        s_builder.AppendLine(f"\t{parameter.Type_Parameter} {parameter.Name_Parameter}2_2;\n")
        # ?## First getter
        s_builder.AppendLine(f"\t{structure.Alias}_get{parameter.Alias}(this1, &{parameter.Name_Parameter}1_1);")
        # ?## Second getter
        s_builder.AppendLine(f"\t{structure.Alias}_get{parameter.Alias}(this2, &{parameter.Name_Parameter}2_2);\n")
        s_builder.AppendLine(f"\tif({parameter.Name_Parameter}1_1 > {parameter.Name_Parameter}2_2){{")
        s_builder.AppendLine("\t\tanw = 1;\n\t}")
        s_builder.AppendLine(f"\telse if({parameter.Name_Parameter}1_1 < {parameter.Name_Parameter}2_2){{")
        s_builder.AppendLine("\t\tanw = -1;\n\t}")
        s_builder.AppendLine("\treturn anw;\n}\n")

    def create_comparer(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        if parameter.Type_Parameter == 'char':
            self.__create_comparer_with_char(structure, parameter, s_builder)
        elif parameter.Length_Parameter == 1:
            self.__create_comparer_without_char(structure, parameter, s_builder)
    
    def __create_comparers(self, structure: Structure, s_builder: StringBuilder) -> None:
        for i in range(1, len(structure.Parameters)):
            self.create_comparer(structure, structure.Parameters[i], s_builder)
    
    def __create_getters_char_function(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the getters taking in count that the parameter
        is char type.
        
        Args:
            structure (Structure): [Structure to retrieve the data]
            parameter (Parameter): [Parameter to retrieve its data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.Append(f'int {structure.Alias}_get{parameter.Alias}')
        s_builder.AppendLine(f'({structure.Final_Structure_Name}* this, {parameter.Type_Parameter}* {parameter.Name_Parameter}){{')
        s_builder.AppendLine('\tint isError = 1;')
        s_builder.AppendLine('\tif(this != NULL){')
        s_builder.AppendLine(f'\t\tstrcpy({parameter.Name_Parameter}, this->{parameter.Name_Parameter});')
        s_builder.AppendLine('\t\tisError = 0;\n\t}')
        s_builder.AppendLine('\treturn isError;\n}\n')
    

    def __create_getters_without_char_function(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the setters taking in count that the parameter
        is not char type.
        
        Args:
            structure (Structure): [Structure to retrieve the data]
            parameter (Parameter): [Parameter to retrieve its data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.Append(f'int {structure.Alias}_get{parameter.Alias}')
        s_builder.AppendLine(f'({structure.Final_Structure_Name}* this, {parameter.Type_Parameter}* {parameter.Name_Parameter}){{')
        s_builder.AppendLine('\tint isError = 1;')
        s_builder.AppendLine('\tif(this != NULL){')
        s_builder.AppendLine(f'\t\t*{parameter.Name_Parameter} = this->{parameter.Name_Parameter};')
        s_builder.AppendLine('\t\tisError = 0;\n\t}')
        s_builder.AppendLine('\treturn isError;\n}\n')

    def create_getter(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        if parameter.Type_Parameter == 'char':
            self.__create_getters_char_function(structure, parameter, s_builder)
        elif parameter.Length_Parameter == 1:
            self.__create_getters_without_char_function(structure, parameter, s_builder)
    
    def __create_getters(self, structure: Structure, s_builder: StringBuilder) -> None:
        for i in range(1, len(structure.Parameters)):
            self.create_getter(structure, structure.Parameters[i], s_builder)
    
    def __create_setters_without_char_function(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the setters taking in count that the parameter
        is not char type.
        
        Args:
            structure (Structure): [Structure to retrieve the data]
            parameter (Parameter): [Parameter to retrieve its data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.Append(f'int {structure.Alias}_set{parameter.Alias}')
        s_builder.AppendLine(f'({structure.Final_Structure_Name}* this, {parameter.Type_Parameter} {parameter.Name_Parameter}){{')
        s_builder.AppendLine('\tint isError = 1;')
        s_builder.AppendLine('\tif(this != NULL){')
        s_builder.AppendLine(f'\t\tthis->{parameter.Name_Parameter} = {parameter.Name_Parameter};')
        s_builder.AppendLine('\t\tisError = 0;\n\t}')
        s_builder.AppendLine('\treturn isError;\n}\n')

    def __create_setters_char_function(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the setters taking in count that the parameter
        is char type.
        
        Args:
            structure (Structure): [Structure to retrieve the data]
            parameter (Parameter): [Parameter to retrieve its data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.Append(f'int {structure.Alias}_set{parameter.Alias}')
        s_builder.AppendLine(f'({structure.Final_Structure_Name}* this, {parameter.Type_Parameter}* {parameter.Name_Parameter}){{')
        s_builder.AppendLine('\tint isError = 1;')
        s_builder.AppendLine('\tif(this != NULL){')
        s_builder.AppendLine(f'\t\tstrcpy(this->{parameter.Name_Parameter}, {parameter.Name_Parameter});')
        s_builder.AppendLine('\t\tisError = 0;\n\t}')
        s_builder.AppendLine('\treturn isError;\n}\n')
    
    def create_setter(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        if parameter.Type_Parameter == 'char':
            self.__create_setters_char_function(structure, parameter, s_builder)
        elif parameter.Length_Parameter == 1:
            self.__create_setters_without_char_function(structure, parameter, s_builder)
    
    def __create_setters(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the setters for all parameters, one for each parameter.

        Args:
            structure (Structure): [Structure to retrieve the data of the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        for i in range(1, len(structure.Parameters)):
            self.create_setter(structure, structure.Parameters[i], s_builder)
    
    def create_getter_and_setter(self, structure: Structure, s_builder: StringBuilder) -> None:
        if structure:
            s_builder.AppendLine(f'// ## {structure.Final_Structure_Name}: GETTERS')
            self.__create_getters(structure, s_builder)
            s_builder.AppendLine(f'// ## {structure.Final_Structure_Name}: SETTERS')
            self.__create_setters(structure, s_builder)
            s_builder.AppendLine(f'// ## {structure.Final_Structure_Name}: COMPARERS')
            self.__create_comparers(structure, s_builder)
    
    def create_destructor_function(self, structure: Structure, s_builder: StringBuilder) -> None:
        s_builder.AppendLine(f'// ## {structure.Final_Structure_Name}: DESTRUCTOR')
        s_builder.Append(f'void {structure.Alias}_delete')
        s_builder.AppendLine(f'({structure.Final_Structure_Name}* this){{')
        s_builder.AppendLine('\tif(this != NULL){')
        s_builder.AppendLine('\t\tfree(this);\n\t}')
        s_builder.AppendLine('}')

    def file_maker(self, path: str, sub_path: str, structure: Structure) -> None:
        if structure:
            s_builder = StringBuilder()
            filename: str = f"{structure.Final_Structure_Name}.c"

            try:
                self.read_text_file(s_builder, self.License)
                self.create_imports(structure, s_builder)
                self.read_text_file(s_builder, self.Credits)
                self.create_basic_struct_functions(structure, s_builder)
                self.create_getter_and_setter(structure, s_builder)
                self.create_destructor_function(structure, s_builder)

                self.create_dir(f'{path}/{sub_path}')

                if self.create_file(f'{path}/{sub_path}/{filename}', s_builder):
                    print(f"{filename} was created.")
                else:
                    print(f"{filename} wasn't created.")
            except Exception as e:
                print(e.args)
                print("Error in the creation of the file.")
