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
