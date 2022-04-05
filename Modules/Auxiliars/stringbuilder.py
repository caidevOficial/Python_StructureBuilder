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


from io import StringIO

class StringBuilder:
    _file_str: str = None
    _counter: int = None

    def __init__(self):
        self._file_str = StringIO()
    
    def __del__(self):
        """[summary]\n
        Delete the string builder.\n
        """
        self._file_str.close()
    
    def __len__(self):
        return len(self.String_Value)
    
    def __str__(self):
        return self._file_str.getvalue()
    
    def __int__(self):
        return int(self._file_str.getvalue())
    
    def __float__(self):
        return float(self._file_str.getvalue())
    
    def __iter__(self):
        self.Counter = 0
        return self
    
    def __next__(self):
        if self.Counter < self.Length_List:
            self.Counter += 1
            return self.String_Value.split('\n')[self.Counter - 1]
        else:
            raise StopIteration

    @property
    def Counter(self) -> int:
        """[summary]\n
        Get the counter of the string builder.\n
        Returns:
            [int]: [Counter of the string builder]\n
        """
        return self._counter
    
    @property
    def String_Value(self) -> str:
        """[summary]\n
        Get the string value of the string builder.\n
        Returns:
            [str]: [String value of the string builder]\n
        """
        return self._file_str.getvalue()
    
    @property
    def Length(self) -> int:
        """[summary]\n
        Get the length of the string builder.\n
        Returns:
            [int]: [Length of the string builder]\n
        """
        return self.__len__()

    @property
    def Length_List(self) -> list:
        """[summary]\n
        Get the amount of lines of the StringBuilder.\n
        Returns:
            [list]: [Amount of lines of the StringBuilder in a list]\n
        """
        return len(self.String_Value.split('\n'))
    
    @Counter.setter
    def Counter(self, value: int):
        """[summary]\n
        Set the counter of the string builder.\n
        Args:
            value (int): [Counter to be set]\n
        """
        self._counter = value

    def Append(self, text: str = None):
        """[summary]\n
        Append a text to the string builder in the same line.\n
        Args:
            text (str, optional): [Test to be appended]\n
        """
        if not text is None:
            self._file_str.write(text)
        else:
            self._file_str.write('')
    
    def AppendLine(self, text: str = None):
        """[summary]\n
        Append a text to the string builder in a new line.\n
        Args:
            text (str, optional): [Test to be appended]\n
        """
        if not text is None:
            self.Append(f'{text}\n')
        else:
            self.Append('\n')
    
    def Clear(self):
        """[summary]\n
        Clear the string builder.\n
        """
        self._file_str.close()
        self._file_str = StringIO()
