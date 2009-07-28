#!/bin/bash
#
# Builds changes in documentation and copies to gh-pages branch.
# 
# LICENSE:
#    This file is part of pyy.
#    
#    pyy is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#    
#    pyy is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#    
#    You should have received a copy of the GNU Lesser General
#    Public License along with pyy. If not, see
#    <http://www.gnu.org/licenses/>.

echo "WARNING: This script must be run from the root folder of the project!"
echo "         You must also already be tracking the gh-pages branch. Run"
echo "           git checkout -t -b gh-pages origin/gh-pages"
echo "         if you are not."
echo ""
echo "Press [ENTER] if both of these conditions have been satisfied. Otherwise"
echo "  [CTRL]+C to cease execution."
read

#Create temporary directory
TEMP_DIR=$(mktemp -d)

#Build all documentation into temporary folder
sphinx-build -a docs/ $TEMP_DIR

#Switch to gh-pages
git checkout gh-pages

#Delete current documentation
rm -rf *

#Move documentation from temporary folder to branch root
mv $TEMP_DIR/* .

#Show changed files and prompt for action
git status
echo ""
echo "Please review changes before commit/push."
