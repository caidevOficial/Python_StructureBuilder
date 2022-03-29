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


class CreatorDotH(Creator):
    
    _FILENAME: str = 'Modules/Creators_Mod/license.txt'

    def __init__(self):
        pass
    
    def create_license_header(self, s_builder: StringBuilder) -> None:
        """[summary]\n
        Writes in the file a license MIT-type.\n
        Args:
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        with open(self._FILENAME, 'r') as license_file:
            for line in license_file:
                s_builder.Append(line)
            s_builder.AppendLine('\n')
    
    def create_imports(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the imports or 'Headers' of the file.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.AppendLine(f"#ifndef {structure.Final_Structure_Name.upper()}_H_INCLUDED")
        s_builder.AppendLine(f"#define {structure.Final_Structure_Name.upper()}_H_INCLUDED")
        s_builder.AppendLine("#include \"LinkedList.h\"")
    
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
        # for parameter in structure.Parameters:
        #     self.add_parameter_into_builder(structure, parameter, s_builder)
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
        self.create_imports(structure, s_builder)
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
        s_builder.Append(f"{structure.Final_Structure_Name}* {structure.Alias}_new(")
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
        s_builder.AppendLine(f"// ## {structure.Final_Structure_Name}: CONSTRUCTORS.")
        # ?# Empty builder
        self.create_builder_empty(structure, s_builder)

        # ?# Builder with params.
        self.create_builder_with_params(structure, s_builder)

        s_builder.AppendLine(f"// ## {structure.Final_Structure_Name}: SHOW & SHOW_ALL.")
        # ?# Show one
        self.show_one_entity(structure, s_builder)

        # ?# Show All
        self.show_all_entities(structure, s_builder)
    
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
        s_builder.AppendLine(f"\n// ## {structure.Final_Structure_Name}: GETTERS");

        for i in range(1, len(structure.Parameters)):
            parameter = structure.Parameters[i]
            self.create_getter(structure, parameter, s_builder)
        s_builder.AppendLine()

        s_builder.AppendLine(f"// ## {structure.Final_Structure_Name}: SETTERS");
        for i in range(1, len(structure.Parameters)):
            parameter = structure.Parameters[i]
            self.create_setter(structure, parameter, s_builder)
        s_builder.AppendLine()

        s_builder.AppendLine(f"// ## {structure.Final_Structure_Name}: COMPARERS");
        for i in range(1, len(structure.Parameters)):
            parameter = structure.Parameters[i]
            self.create_comparer(structure, parameter, s_builder)
        s_builder.AppendLine()
    
    def create_delete_function(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the delete function of the structure.\n
        Args:
            structure (Structure): [Structure for check the data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.AppendLine(f"// ## {structure.Final_Structure_Name}: DELETE")
        s_builder.AppendLine(f"void {structure.Alias}_delete({structure.Final_Structure_Name}* this);")

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
                file.write(s_builder.__str__())
                print(f"File {path.split('/')[-1]} was created.")
                print(f'in Path: {path}')
                return True
        except:
            return False

    def create_dir(self, path):
        """[summary]\n
        Creates the directory.\n
        Args:
            path (str): [Path to the directory]
        """
        try:
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Directory {path} was created.")
        except Exception as e:
            print(f'Error creating Path: {e}')

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
            self.create_license_header(s_builder)
            self.create_structure(structure, s_builder)
            s_builder.AppendLine("// # CREDITS TO:")
            s_builder.AppendLine("// ## Advanced Improvement And develop in Python: FacuFalcone - CaidevOficial.")
            s_builder.AppendLine("// ## Follow me on -> github.com/CaidevOficial\n")

            self.create_basic_struct_functions(structure, s_builder)
            self.create_getter_and_setter(structure, s_builder)
            self.create_delete_function(structure, s_builder)

            s_builder.AppendLine(f"\n#endif /* {structure.Final_Structure_Name.upper()}_H_INCLUDED */")

            self.create_dir(f'{path}/{sub_path}')

            if self.create_file(f'{path}/{sub_path}/{filename}', s_builder):
                print(f"{filename} was created.")
            else:
                print(f"{filename} wasn't created.")

        except Exception as e:
            print(e.args)
            print("Error in the creation of the file.")
