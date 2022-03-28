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

from Modules.Entities_Mod.parameter import Parameter

class Structure:
    __structure_name: str = None
    __final_structure_name: str = None
    __alias_short_name: str = None
    __parameters: list = None

    def __init__(self, struct_name: str = None) -> None:
        """[summary]\n
        Initialize the structure.
        
        Args:
            struct_name (str): [The name of the structure.]
        """
        self.Parameters = [Parameter]
        self.Structure_Name = struct_name

    # ?####### Start Properties: Getters #######
    @property
    def Structure_Name(self) -> str:
        """[summary]\n
        Get the name of the structure.
        
        Returns:
            str: [The name of the structure.]
        """
        return self.__structure_name
    
    @property
    def Final_Structure_Name(self) -> str:
        """[summary]\n
        Get the final name of the structure.
        
        Returns:
            str: [The final name of the structure.]
        """
        return self.__final_structure_name
    
    @property
    def Alias(self) -> str:
        """[summary]\n
        Get the alias short name of the structure.
        
        Returns:
            str: [The alias short name of the structure.]
        """
        return self.__alias_short_name
    
    @property
    def Parameters(self) -> list:
        """[summary]\n
        Get the parameters of the structure.
        
        Returns:
            list: [The parameters of the structure.]
        """
        return self.__parameters
    
    @property
    def Len_Parameters_List(self) -> int:
        """[summary]\n
        Get the length of the parameters list.
        
        Returns:
            int: [The length of the parameters list.]
        """
        return len(self.Parameters)
    
    # ?####### End Properties: Getters #######

    # ?####### Start Properties: Setters #######

    @Structure_Name.setter
    def Structure_Name(self, struct_name: str) -> None:
        """[summary]\n
        Set the name of the structure.
        
        Args:
            struct_name (str): [The name of the structure.]
        """
        self.__structure_name = struct_name.capitalize() if struct_name else None
    
    @Final_Structure_Name.setter
    def Final_Structure_Name(self, final_struct_name: str) -> None:
        """[summary]\n
        Set the final name of the structure.
        
        Args:
            final_struct_name (str): [The final name of the structure.]
        """
        self.__final_structure_name = f's{final_struct_name}' if final_struct_name else None
    
    @Alias.setter
    def Alias(self, alias_short_name: str) -> None:
        """[summary]\n
        Set the alias short name of the structure.
        
        Args:
            alias_short_name (str): [The alias short name of the structure.]
        """
        self.__alias_short_name = alias_short_name.capitalize() if alias_short_name else None
    
    @Parameters.setter
    def Parameters(self, parameters: list) -> None:
        """[summary]\n
        Set the parameters of the structure.
        
        Args:
            parameters (list): [The parameters to set.]
        """
        self.__parameters = parameters if parameters else None
    
    # ?####### End Properties: Setters #######

    # ?####### Start Methods #######

    def add_parameter(self, parameter: Parameter) -> None:
        """[summary]\n
        Add a parameter to the structure.
        
        Args:
            parameter (PARAM): [The parameter to add.]
        """
        self.__parameters.append(parameter)

    def normalize_structure_data(self):
        self.Alias = self.Structure_Name
        self.Final_Structure_Name = self.Alias

    def __str__(self) -> str:
        """[summary]\n
        Return the structure as a string.
        
        Returns:
            str: [The structure info as a string.]
        """
        data = '########################'
        data += f'{self.Structure_Name}\n'
        for parameter in self.Parameters:
            data += f'\t{parameter}\n'
        data += '########################\n'
        return f'{data}'

    # ?####### End Methods #######
