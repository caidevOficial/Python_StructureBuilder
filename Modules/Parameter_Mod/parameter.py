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

from Modules.Auxiliars.formatter import capitalize_words as CW

class Parameter:
    __id_parameter: int = None
    __length_parameter: int = None
    __type_parameter: str = None
    __name_parameter: str = None
    __alias_parameter: str = None

    def __init__(self) -> None:
        pass

    @property
    def ID_Parameter(self) -> int:
        """[summary]\n
        Get the ID of the parameter.
        
        Returns:
            int: [The id of the actual parameter.]
        """
        return self.__id_parameter
    
    @ID_Parameter.setter
    def ID_Parameter(self, id_parameter: int) -> None:
        """[summary]\n
        Set the ID of the parameter.

        Args:
            id_parameter (int): [The id of the parameter.]
        """
        self.__id_parameter = id_parameter
    
    @property
    def Length_Parameter(self) -> int:
        """[summary]\n
        Get the length of the parameter.

        Returns:
            int: [The length of the parameter.]
        """
        return self.__length_parameter
    
    @Length_Parameter.setter
    def Length_Parameter(self, length_parameter: int) -> None:
        """[summary]\n
        Set the length of the parameter if is a integer value.

        Args:
            length_parameter (int): [The length of the parameter.]
        """
        self.__length_parameter = length_parameter
    
    @property
    def Type_Parameter(self) -> str:
        """[summary]\n
        Get the type of the parameter.

        Returns:
            str: [The type of the parameter.]
        """
        return self.__type_parameter
    
    @Type_Parameter.setter
    def Type_Parameter(self, type_parameter: str) -> None:
        """[summary]\n
        Set the type of the parameter.

        Args:
            type_parameter (str): [The type of the parameter.]
        """
        self.__type_parameter = type_parameter.lower()
    
    @property
    def Name_Parameter(self) -> str:
        """[summary]\n
        Get the name of the parameter.

        Returns:
            str: [The name of the parameter.]
        """
        return self.__name_parameter
    
    @Name_Parameter.setter
    def Name_Parameter(self, name_parameter: str) -> None:
        """[summary]\n
        Set the name of the parameter.

        Args:
            name_parameter (str): [The name of the parameter.]
        """
        self.__name_parameter = CW(name_parameter)
   
    @property
    def Alias_Parameter(self) -> str:
        """[summary]\n
        Get the alias of the parameter.

        Returns:
            str: [The alias of the parameter.]
        """
        return self.__alias_parameter
    
    @Alias_Parameter.setter
    def Alias_Parameter(self, alias_parameter: str) -> None:
        """[summary]\n
        Set the alias of the parameter.

        Args:
            alias_parameter (str): [The alias of the parameter.]
        """
        self.__alias_parameter = alias_parameter.capitalize()
    
    def __str__(self) -> str:
        return f""""
        ID: {self.ID_Parameter}
        Name: {self.Name_Parameter}
        Alias: {self.Alias_Parameter}
        Type: {self.Type_Parameter}
        Length: {self.Length_Parameter}
        """
