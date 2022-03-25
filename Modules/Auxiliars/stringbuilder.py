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

from io import StringIO

class StringBuilder:
    _file_str = None

    def __init__(self):
        self._file_str = StringIO()

    def Append(self, text: str):
        """[summary]\n
        Append a text to the string builder in the same line.\n
        Args:
            text (str): [Test to be appended]\n
        """
        self._file_str.write(text)
    
    def AppendLine(self, text: str):
        """[summary]\n
        Append a text to the string builder in a new line.\n
        Args:
            text (str): [Test to be appended]\n
        """
        self.Append(f'{text}\n')
    
    def Clear(self):
        """[summary]\n
        Clear the string builder.\n
        """
        self._file_str.close()
        self._file_str = StringIO()
    
    def __del__(self):
        """[summary]\n
        Delete the string builder.\n
        """
        self._file_str.close()
    
    def __exit__(self, exc_type, exc_value, traceback):
        self._file_str.close()
        self._file_str = None
        return False
    
    def __repr__(self):
        return self._file_str.getvalue()
    
    def __len__(self):
        return len(self._file_str.getvalue())
    

    def __str__(self):
        return self._file_str.getvalue()
