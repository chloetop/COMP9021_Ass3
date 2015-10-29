# Sublime Text 3 for OS X
# Copyright (c) 2015 Subramanya Vajiraya
# 
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
# 
# Written by Subramanya Vajiraya (z5081713) COMP9021

python display_tree.py tree_1.txt
diff tree_1.tex Test_files/tree_1.tex 
python display_tree.py -grow up tree_2.txt 
diff tree_2.tex Test_files/tree_2.tex
python display_tree.py -nodestyle circle tree_3.txt
diff tree_3.tex Test_files/tree_3.tex
python display_tree.py -grow left -nodestyle ellipse tree_4.txt 
diff tree_4.tex Test_files/tree_4.tex
python display_tree.py -grow down -nodestyle rectangle tree_5.txt
diff tree_5.tex Test_files/tree_5.tex
python display_tree.py tree_6.txt
diff tree_6.tex Test_files/tree_6.tex

python3 display_tree.py wrong_1.txt
python3 display_tree.py wrong_2.txt
python3 display_tree.py wrong_3.txt
python3 display_tree.py wrong_4.txt
