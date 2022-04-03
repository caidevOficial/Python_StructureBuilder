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


from Modules.Auxiliars.formatter import capitalize_words as CW
from Modules.Auxiliars.stringbuilder import StringBuilder


class Parameter:
    __id_parameter: int = None
    __length_parameter: int = None
    __type_parameter: str = None
    __name_parameter: str = None
    __alias_parameter: str = None

    def __init__(self) -> None:
        pass

    # ?####### Start Properties: Getters #######

    @property
    def ID_Parameter(self) -> int:
        """[summary]\n
        Get the ID of the parameter.
        
        Returns:
            int: [The id of the actual parameter.]
        """
        return self.__id_parameter
    
    @property
    def Length_Parameter(self) -> int:
        """[summary]\n
        Get the length of the parameter.

        Returns:
            int: [The length of the parameter.]
        """
        return self.__length_parameter
    
    @property
    def Type_Parameter(self) -> str:
        """[summary]\n
        Get the type of the parameter.

        Returns:
            str: [The type of the parameter.]
        """
        return self.__type_parameter
    
    @property
    def Name_Parameter(self) -> str:
        """[summary]\n
        Get the name of the parameter.

        Returns:
            str: [The name of the parameter.]
        """
        return self.__name_parameter
    
    @property
    def Alias(self) -> str:
        """[summary]\n
        Get the alias of the parameter.

        Returns:
            str: [The alias of the parameter.]
        """
        return self.__alias_parameter
    
    # ?####### End Properties: Getters #######

    # ?####### Start Properties: Setters #######

    @ID_Parameter.setter
    def ID_Parameter(self, id_parameter: int) -> None:
        """[summary]\n
        Set the ID of the parameter.

        Args:
            id_parameter (int): [The id of the parameter.]
        """
        self.__id_parameter = id_parameter
    
    @Length_Parameter.setter
    def Length_Parameter(self, length_parameter: int) -> None:
        """[summary]\n
        Set the length of the parameter if is a integer value.

        Args:
            length_parameter (int): [The length of the parameter.]
        """
        self.__length_parameter = length_parameter
    
    @Type_Parameter.setter
    def Type_Parameter(self, type_parameter: str) -> None:
        """[summary]\n
        Set the type of the parameter.

        Args:
            type_parameter (str): [The type of the parameter.]
        """
        self.__type_parameter = type_parameter.lower()
    
    @Name_Parameter.setter
    def Name_Parameter(self, name_parameter: str) -> None:
        """[summary]\n
        Set the name of the parameter.

        Args:
            name_parameter (str): [The name of the parameter.]
        """
        self.__name_parameter = name_parameter.strip().lower()
   
    @Alias.setter
    def Alias(self, alias_parameter: str) -> None:
        """[summary]\n
        Set the alias of the parameter.

        Args:
            alias_parameter (str): [The alias of the parameter.]
        """
        alias = alias_parameter
        self.__alias_parameter = alias.capitalize()
    
    # ?####### End Properties: Setters #######

    # ?####### Start Methods #######

    def normalize_parameter(self, id_param: int, name_param: str, type_param: str, len_param: int) -> None:
        """[summary]\n
        Normalize the parameter.

        Args:
            id_param (int): [The id of the parameter.]
            name_param (str): [The name of the parameter.]
            type_param (str): [The type of the parameter.]
            len_param (int): [The length of the parameter.]
        """
        self.ID_Parameter = id_param
        self.Type_Parameter = type_param
        self.Length_Parameter = len_param
        self.Name_Parameter = name_param
        print(f'Name: {self.Name_Parameter}')
        self.Alias = self.Name_Parameter
        print(f'Alias: {self.Alias}')

    def lite_info(self):
        if self.Length_Parameter > 1:
            return f"Preview: {self.Type_Parameter} {self.Name_Parameter}[{self.Length_Parameter}];"
        else:
            return f"Preview: {self.Type_Parameter} {self.Name_Parameter};"

    def __str__(self) -> str:
        sb = StringBuilder()
        sb.AppendLine(f"ID: {self.ID_Parameter}")
        sb.AppendLine(f"Type: {self.Type_Parameter}")
        sb.AppendLine(f"Name: {self.Name_Parameter}")
        sb.AppendLine(f"Alias: {self.Alias}")
        if self.Length_Parameter > 1:
            sb.AppendLine(f"Length: {self.Length_Parameter}")
        return sb.__str__()
    
    # ?####### End Methods #######
