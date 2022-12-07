# TerminalPortrait

## Description
A personal project (so the naming is not serious). Use string to make image. Inspired by the logo when opening msfconsole.


## Usage
cd to the directory of terminalportrait-MODEL_PRODUCTION.py
    $ python terminalportrait-MODEL_PRODUCTION.py -i *input_file* -o *output_file* -l *level* -d *density* -c *contrast_factor*
- -i *input_file* : Precise the input image file. Needs absolute path. Needs to be quoted. Needs to precise the filename.  
e.g.: "D:\pictures\input_image.jpg". Can use either backslash or slash.
- -o *output_file* : Precise the output text file. Needs absolute path. Needs to be quoted. Needs to precise the filename.  
e.g.: "D:\docs\output.txt". Can use either backslash or slash.
- -l *level* : Set the ink level. In other words, use how many differents characters. Must be an integer within 3 to 14. If the level is 3, then the output text will be composed of "@", "o" and ":".
- -d *density* : Set the ink density. In other words, how many time each character will be repeated. Must be an integer. It is suggested to be 2 or 3. If the density is 2, then the output text will be like: "@@%%MMoo"...
- -c *contrast_factor*: Optional argument, set the contrast factor. Must be float. The script runs better if the input image has more contrast.  

Real example:  
    $ python terminalportrait-MODEL_PRODUCTION.py -i "D:\input.jfif" -o "D:/output.txt" -l 14 -d 2 -c 2  

## Explanation
Scripts are in src. Order of developpement: PROTOTYPE, TEST_TYPE, MODEL_PRODUCTION.  
PROTOTYPE is the "core" script. Based on PROTOTYPE, I added features in TEST_TYPE and MODEL_PRODUCTION. MODEL_PRODUCTION is the final version.  
Technically the project is not complicate. It consists of:  
- Read image.  
- Adjust contrast level.
- Transform to numpy array.  
- Transform to grayscale.  
- Each pixel corresponds to a RGB color value. According to the value, determine which character will be use. For depper color, use characters like "@", "M". For lighter color, use characters like ";", ".".  
- Output to text.