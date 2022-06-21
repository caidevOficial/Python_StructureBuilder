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
from Modules.Entities_Mod.structure import Structure


class Common_Creator:
    _CREDITS: str = 'Docs/credits.txt'
    _LICENSE: str = 'Docs/license.txt'
    __LL_C: str = 'Docs/LL_C.txt'
    __LL_H: str = 'Docs/LL_H.txt'
    __FILENAME: str = ''

    def __init__(self):
        pass

    @property
    def Credits(self) -> str:
        """[summary]\n
        Gets the Credits path.\n
        Returns:
            str: [The path where the Credits is]
        """
        return self._CREDITS
    
    @property
    def License(self) -> str:
        """[summary]\n
        Gets the License path.\n
        Returns:
            str: [The path where the License is]
        """
        return self._LICENSE
    
    @property
    def LL_H(self) -> str:
        """[summary]\n
        Gets the LL_H path.\n
        Returns:
            str: [The path where the LL_H is]
        """
        return self.__LL_H
    
    @property
    def LL_C(self) -> str:
        """[summary]\n
        Gets the LL_C path.\n
        Returns:
            str: [The path where the LL_C is]
        """
        return self.__LL_C

    @property
    def Filename(self) -> str:
        """[summary]\n
        Gets the Filename.\n
        Returns:
            str: [The name of the file]
        """
        return self.__FILENAME
    
    @Filename.setter
    def Filename(self, value: str) -> None:
        """[summary]\n
        Sets the Filename.\n
        Args:
            value (str): [The name of the file]
        """
        self.__FILENAME = value

    def create_top_defines(self, structure: Structure, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the imports or 'Headers' of the file.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.AppendLine('#include <stdlib.h>')
        s_builder.AppendLine('#include <stdio.h>')
        s_builder.AppendLine('#include "LinkedList.h"')

    def read_text_file(self, s_builder: StringBuilder, path: str) -> None:
        """[summary]\n
        Creates the Credits or License.\n
        Args:
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
            path (str): [Path to the file]
        """
        with open(path, 'r', encoding="utf8") as text_file:
            for line in text_file:
                s_builder.Append(line)
            s_builder.AppendLine('\n')
    
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
                print(f"File {path.split('/')[-1]} was created.")
                print(f'in Path: {path}')
                s_builder.Clear()
                return True
        except Exception as e:
            print_message(e.args)
            raise e
    
    def create_main_top_defines(self, text: str, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the imports or 'Headers' of the file.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.AppendLine(f"#ifndef {text.upper()}_H_INCLUDED")
        s_builder.AppendLine(f"#define {text.upper()}_H_INCLUDED\n")
    
    def create_main_bot_defines(self, text: str, s_builder: StringBuilder) -> None:
        """[summary]\n
        Creates the imports or 'Headers' of the file.\n
        Args:
            structure (Structure): [Structure for check the parameters]
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        s_builder.AppendLine(f"\n#endif /* {text.upper()}_H_INCLUDED */")
    
    def create_LL_H(self, s_builder: StringBuilder) -> None:
        self.read_text_file(s_builder, self.License)
        self.read_text_file(s_builder, self.Credits)
        self.read_text_file(s_builder, self.LL_H)
    
    def create_LL_C(self, structure: Structure, s_builder: StringBuilder) -> None:
        self.read_text_file(s_builder, self.License)
        self.read_text_file(s_builder, self.LL_C)
        s_builder.String_Value = s_builder.String_Value.replace('StructureName', f'{structure.Alias}')