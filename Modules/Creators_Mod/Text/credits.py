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
from Modules.Creators_Mod.Common.common_creator import Common_Creator

class Credits_Manager(Common_Creator):

    def __init__(self):
        pass
    
    @property
    def Credits(self) -> str:
        """[summary]\n
        Gets the License path.\n
        Returns:
            str: [The path where the License is]
        """
        return super().Credits
    
    def create_credits(self, s_builder: StringBuilder) -> None:
        """[summary]\n
        Writes in the file The credits.\n
        Args:
            s_builder (StringBuilder): [StringBuilder to write the data of the file]
        """
        super().read_text_file(s_builder, self.Credits)
    