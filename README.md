# TerminalPortrait

## Description
A personal project (so the namings are not serious). Use string to make image. Inspired by the logo when opening msfconsole. (I knew later that this is called ascii art)
Try with example.txt, open with Notepad, zoom out to 20% or 30%.

## Usage
cd to the directory of terminalportrait-MODEL_PRODUCTION.py  
    $ python terminalportrait-MODEL_PRODUCTION.py -i *input_file* -o *output_file* -l *level* -d *density* -c *contrast_factor*
- -i *input_file* : Precise the input image file. Needs absolute path. Needs to be quoted. Needs to precise the filename.  
e.g.: "D:\pictures\input_image.jpg". Can use either backslash or slash. It is recommanded that the width shall be under 500px.  
- -o *output_file* : Precise the output text file. Needs absolute path. Needs to be quoted. Needs to precise the filename.  
e.g.: "D:\docs\output.txt". Can use either backslash or slash.
- -l *level* : Set the ink level. In other words, use how many differents characters. Must be an integer within 3 to 14. If the level is 3, then the output text will be composed of "@", "o" and ":".
- -d *density* : Set the ink density. In other words, how many time each character will be repeated. Must be an integer. It is suggested to be 2 or 3. If the density is 2, then the output text will be like: "@@%%MMoo"...
- -c *contrast_factor*: Optional argument, set the contrast factor. Must be float. The script runs better if the input image has more contrast.  

Real example:  
    `$ python terminalportrait-MODEL_PRODUCTION.py -i "D:\input.jfif" -o "D:/output.txt" -l 14 -d 2 -c 2  `

## Explanation
Scripts are in src. Order of developpement: PROTOTYPE, TEST_TYPE, MODEL_PRODUCTION.  
PROTOTYPE is the "core" script.  
Based on PROTOTYPE, I created TEST_TYPE which is restructured and cleaner.  
Based on TEST_TYPE, I added features and created MODEL_PRODUCTION, which is the final version.  
  
Technically the project is not complicate. It consists of:
- Read image.  
- Adjust contrast level.
- Transform to numpy array.  
- Transform to grayscale.  
- Each pixel corresponds to a RGB color value. According to the value, determine which character will be use. For depper color, use characters like "@", "M". For lighter color, use characters like ";", ".".  
- Output to text.


------------------------------
(wow it's already three years later... in another city)
parameters that work well:
- "python3 terminalportrait-DUMMYSYSTEM.py -i ../data/i_love_kirino_copy.jpg -o ../out/i_love_kirino_copy.docx -l special2 -d 1 -c 1.01 -r 375"  
  with font size 3, linespacing 0.6, output canva is landscape A3
