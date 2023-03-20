# A2L Variable Extractor
 A python script to extract specific variables from an A2L file.

This is currently a rudimentary script to extract the CHARACTERISTIC, 
MEASUREMENT and AXIS_PTS variable information from an A2L file used in the automotive industry.
It outputs a text file with the variable ID, description and address, each delimited with a "|".

This program was created to be used with an import script that labels the variable addresses
in Ghidra.

It has currently only been tested with a Simos18 A2L.

How to use:
Paste your A2L in the same folder as this script.
Open the code in an editor and change the name of the input file to that of your A2L.
Run the script.
"output.txt" will be generated with your variables.

Future improvements:
A2L name will be an input text field and not hard-coded.
An .exe with a GUI where you can select your A2L in the file explorer.
