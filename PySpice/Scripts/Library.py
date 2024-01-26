####################################################################################################
#
# PySpice - A Spice Package for Python
# Copyright (C) 2021 Fabrice Salvaire
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
####################################################################################################

####################################################################################################

from pathlib import Path
import argparse
import os

####################################################################################################

import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

####################################################################################################

from PySpice.Spice.Library import SpiceLibrary

####################################################################################################

def main() -> None:

    parser = argparse.ArgumentParser(description='Manage Spice library')

    parser.add_argument('library_path', metavar='LibraryPath', type=str,
                        help='Spice library root path')

    parser.add_argument('--scan',
                        default=False, action='store_true',
                        help='Scan library')

    parser.add_argument('--delete-yaml',
                        default=False, action='store_true',
                        help='WARNING: Delete YAML Files')

    parser.add_argument('--add-category',
                        type=str,
                        help='Add a category')

    parser.add_argument('--category',
                        type=str,
                        default=None,
                        help='specify the category')

    parser.add_argument('--add-library',
                        type=str,
                        help='Add a library')

    parser.add_argument('--show-categories',
                        default=False, action='store_true',
                        help='Show categories')

    args = parser.parse_args()

    ##############################################

    library_path = Path(args.library_path).resolve()
    print(f"Library is {library_path}")

    spice_library = SpiceLibrary(library_path, scan=args.scan)

    if args.delete_yaml:
        rc = input('Confirm deletion (y/n): ')
        if rc.lower() == 'y':
            spice_library.delete_yaml()

    if args.show_categories:
        print(spice_library.list_categories())

    if args.add_category:
        spice_library.category_path(args.add_category)

    if args.add_library:
        if args.category is None:
            print("A category is required")
