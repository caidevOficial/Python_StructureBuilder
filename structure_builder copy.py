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

from Modules.Creators_Mod.Parsers.parser_dot_h import ParserDotH
from Modules.Entities_Mod.structure import Structure
from Modules.Entities_Mod.parameter import Parameter
from Modules.Auxiliars.data_collector import structure_name_col
from Modules.Auxiliars.data_collector import parameters_collector
from Modules.Auxiliars.data_collector import desktop_path
from Modules.Creators_Mod.Structure.creator_dot_c import CreatorDotC
from Modules.Creators_Mod.Structure.creator_dot_h import CreatorDotH
from Modules.Creators_Mod.Parsers.parser_dot_c import ParserDotC
from Modules.Auxiliars.formatter import print_message


# ?## Entites
myStructure = Structure()
builder_dot_h = CreatorDotH()
builder_dot_c = CreatorDotC()
builder_parser_c = ParserDotC()
builder_parser_h = ParserDotH()
parameter = Parameter()
desktop = desktop_path()

# ?## Variables for the directory to save the files
sub_path = 'test_Py_StructureBuilder_Files'

try:
    # ?## Creating structure
    myStructure.Structure_Name = 'ferrocarril'
    myStructure.normalize_structure_data()
    # myStructure = parameters_collector(myStructure)

    # Add parameters
    parameter = Parameter()
    parameter.ID_Parameter = 1
    parameter.Name_Parameter = 'empresa'
    parameter.Alias = 'Empresa'
    parameter.Type_Parameter = 'char'
    parameter.Length_Parameter = 20
    myStructure.add_parameter(parameter)

    parameter = Parameter()
    parameter.ID_Parameter = 2
    parameter.Name_Parameter = 'pasajeros'
    parameter.Alias = 'Pasajeros'
    parameter.Type_Parameter = 'short'
    parameter.Length_Parameter = 1
    myStructure.add_parameter(parameter)

    parameter = Parameter()
    parameter.ID_Parameter = 3
    parameter.Name_Parameter = 'velocidad'
    parameter.Alias = 'Velocidad'
    parameter.Type_Parameter = 'float'
    parameter.Length_Parameter = 1
    myStructure.add_parameter(parameter)

    parameter = Parameter()
    parameter.ID_Parameter = 4
    parameter.Name_Parameter = 'ramal'
    parameter.Alias = 'Ramal'
    parameter.Type_Parameter = 'char'
    parameter.Length_Parameter = 15
    myStructure.add_parameter(parameter)
    

    # ?## Creating files
    builder_dot_h.file_maker(desktop, sub_path , myStructure)
    builder_dot_c.file_maker(desktop, sub_path , myStructure)
    builder_parser_c.create_parser(desktop, sub_path , myStructure)
    builder_parser_h.create_parser(desktop, sub_path , myStructure)

except Exception as e:
    print_message(
        'Exeption found:', 
        f'Details ----> {e}'
    )
