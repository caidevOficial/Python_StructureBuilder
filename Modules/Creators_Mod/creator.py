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
#

from abc import ABCMeta, abstractmethod
from Modules.Entities_Mod.parameter import Parameter
from Modules.Entities_Mod.structure import Structure
from Modules.Auxiliars.stringbuilder import StringBuilder

class Creator(metaclass=ABCMeta):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def create_imports(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the imports or 'Headers' of the file.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        pass

    @abstractmethod
    def create_builder_empty(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the empty builder of the file.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        pass
    
    @abstractmethod
    def create_builder_with_params(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the builder with parameters of the file.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        pass
    
    @abstractmethod
    def add_parameter_into_builder(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        """[summary]\n
        Adds the parameters into the builder.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            parameter (Parameter): [Parameter to add into the builder]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        pass

    @abstractmethod
    def add_parameter_to_builder(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Adds parameters data to the 'parameters' of the builder.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        pass

    @abstractmethod
    def show_one_entity(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the function that shows one entity.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        pass

    @abstractmethod
    def show_all_entities(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the function that shows all entities.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        pass

    @abstractmethod
    def create_basic_struct_functions(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the functions that create the basic structure of the file.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        pass

    @abstractmethod
    def create_getter(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the getter of the parameter.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            parameter (Parameter): [Parameter to get the data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        pass

    @abstractmethod
    def create_setter(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the setter of the parameter.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            parameter (Parameter): [Parameter to set the data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        pass
    
    @abstractmethod
    def create_comparer(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the comparer of the file.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            parameter (Parameter): [Parameter to compare the data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        pass

    @abstractmethod
    def create_getter_and_setter(self, structure: Structure, parameter: Parameter, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the getter and setter of the parameter.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            parameter (Parameter): [Parameter to get and set the data]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        pass

    @abstractmethod
    def create_delete_function(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the delete function of the file.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        pass

    @abstractmethod
    def create_file(self, path, s_builder: StringBuilder) -> bool:
        """[summary]\n
        Creates the file.\n
        Args:
            path (str): [Path to save the file]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        Returns:
            bool: [True if the file was created, False if not or error]
        """
        pass

    @abstractmethod
    def file_maker(self, path: str, structure: Structure) -> None:
        """[summary]\n
        Creates the file.\n
        Args:
            path (str): [Path of the file]
            structure (Structure): [Structure for check the parameters]
        """
        pass
