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

from Modules.Entities_Mod.structure import Structure
from Modules.Auxiliars.data_collector import structure_name_col
from Modules.Auxiliars.data_collector import parameters_collector
from Modules.Auxiliars.data_collector import desktop_path
from Modules.Creators_Mod.creator_dot_h import CreatorDotH

# ?## Entites
myStructure = Structure()
builder_dot_h = CreatorDotH()
desktop = desktop_path()

# ?## Variables
sub_path = 'Files'

# ?## Creating structure
myStructure.Structure_Name = structure_name_col()
myStructure.normalize_structure_data()
myStructure = parameters_collector(myStructure)

# ?## Creating files
builder_dot_h.file_maker(desktop, sub_path , myStructure)
# TODO: Implement the builder_dot_c class
# builder_dot_c.file_maker(desktop, sub_path , myStructure)
