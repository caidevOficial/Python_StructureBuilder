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
from Modules.Creators_Mod.Structure.creator import Creator
from Modules.Entities_Mod.parameter import Parameter
from Modules.Entities_Mod.structure import Structure


class CreatorDotH(Creator, Common_Creator):

    def __init__(self):
        pass
    
    def read_text_file(self, s_builder: StringBuilder, path: str) -> None:
        super().read_text_file(s_builder, path)
    
    def create_top_defines(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the imports or 'Headers' of the file.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        super().create_main_top_defines(structure.Final_Structure_Name, s_builder)
        s_builder.AppendLine('#include "LinkedList.h"')
    
    def create_bot_defines(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the imports or 'Headers' of the file.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        super().create_main_bot_defines(structure.Final_Structure_Name, s_builder)
    
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
            s_builder.AppendLine(");\n")

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

    def create_structure(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the structure of the file.h.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        self.create_top_defines(structure, s_builder)
        s_builder.AppendLine("\ntypedef struct{")
        for i in range(1, len(structure.Parameters)):
            parameter = structure.Parameters[i]
            if parameter.Type_Parameter == 'char':
                s_builder.AppendLine(f"\t{parameter.Type_Parameter} {parameter.Name_Parameter}[{parameter.Length_Parameter}];")
            else:
                s_builder.AppendLine(f"\t{parameter.Type_Parameter} {parameter.Name_Parameter};")
        s_builder.AppendLine(f"}}{structure.Final_Structure_Name};\n")
    
    def create_builder_empty(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the empty builder of the file.h.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.AppendLine(f"{structure.Final_Structure_Name}* {structure.Alias}_newEmpty();")
    
    def create_builder_with_params(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the builder with parameters of the file.h.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.Append(f"{structure.Final_Structure_Name}* {structure.Alias}_newParam(")
        self.add_parameter_to_builder(structure, s_builder)
    
    def show_one_entity(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the show one entity of the file.h.\n
        Args:
            structure (Structure): [Structure for check the data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.AppendLine(f'void {structure.Alias}_show({structure.Final_Structure_Name}* this);')
    
    def show_all_entities(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the function that show all entities of structures.
        Args:
            structure (Structure): [Structure for check the data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.AppendLine(f'int {structure.Alias}_showAll(LinkedList* this, char* errorMesage);')
    
    def create_basic_struct_functions(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the basic functions such as Constructors, Show and ShowAll.

        Args:
            structure (Structure): [Structure for check the data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        super().create_basic_struct_functions(structure, s_builder)
    
    def create_getter(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the getter of the structure.\n
        Args:
            structure (Structure): [Structure for check the data]
            parameter (Parameter): [Parameter to write into the file]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.Append(f"int {structure.Alias}_get{parameter.Alias}")
        s_builder.AppendLine(f"({structure.Final_Structure_Name}* this, {parameter.Type_Parameter}* {parameter.Name_Parameter});")
    
    def create_setter(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the setter of the structure.\n
        Args:
            structure (Structure): [Structure for check the data]
            parameter (Parameter): [Parameter to make its setter]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.Append(f"int {structure.Alias}_set{parameter.Alias}")
        if parameter.Type_Parameter == 'char':
            s_builder.AppendLine(f"({structure.Final_Structure_Name}* this, {parameter.Type_Parameter}* {parameter.Name_Parameter});")
        else:
            s_builder.AppendLine(f"({structure.Final_Structure_Name}* this, {parameter.Type_Parameter} {parameter.Name_Parameter});")
    
    def create_comparer(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the comparer of the structure.\n
        Args:
            structure (Structure): [Structure for check the data]
            parameter (Parameter): [Parameter to make its comparer]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.AppendLine(f"int {structure.Alias}_compare{parameter.Alias}(void* this1, void* this2);")
    
    def create_getter_and_setter(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the getter and setter of the structure.\n
        Args:
            structure (Structure): [Structure for check the data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.AppendLine(f"\n// ## {structure.Final_Structure_Name}: GETTERS")

        for i in range(1, len(structure.Parameters)):
            parameter = structure.Parameters[i]
            self.create_getter(structure, parameter, s_builder)
        s_builder.AppendLine()

        s_builder.AppendLine(f"// ## {structure.Final_Structure_Name}: SETTERS")
        for i in range(1, len(structure.Parameters)):
            parameter = structure.Parameters[i]
            self.create_setter(structure, parameter, s_builder)
        s_builder.AppendLine()

        s_builder.AppendLine(f"// ## {structure.Final_Structure_Name}: COMPARERS")
        for i in range(1, len(structure.Parameters)):
            parameter = structure.Parameters[i]
            self.create_comparer(structure, parameter, s_builder)
        s_builder.AppendLine()
    
    def create_destructor_function(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the delete function of the structure.\n
        Args:
            structure (Structure): [Structure for check the data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.AppendLine(f"// ## {structure.Final_Structure_Name}: DELETE")
        s_builder.AppendLine(f"void {structure.Alias}_delete({structure.Final_Structure_Name}* this);")

    def file_maker(self, path: str, sub_path: str, structure: Structure) -> None:
        """[summary]\n
        Creates the file.h.\n
        Args:
            path (str): [Path of the file]
            structure (Structure): [Structure for check the data]
        """
        s_builder = StringBuilder()
        filename: str = f"{structure.Final_Structure_Name}.h"
        try:
            self.read_text_file(s_builder, self.License)
            self.create_structure(structure, s_builder)
            self.read_text_file(s_builder, self.Credits)
            self.create_basic_struct_functions(structure, s_builder)
            self.create_getter_and_setter(structure, s_builder)
            self.create_destructor_function(structure, s_builder)
            self.create_bot_defines(structure, s_builder)
            # s_builder.AppendLine(f"\n#endif /* {structure.Final_Structure_Name.upper()}_H_INCLUDED */")

            self.create_dir(f'{path}/{sub_path}')
            if self.create_file(f'{path}/{sub_path}/{filename}', s_builder):
                print_message(f"{filename} was created.")
            else:
                print_message(f"{filename} wasn't created.")

        except Exception as e:
            print_message(
                e.args,
                "Error in the creation of the file."
            )
            raise e
