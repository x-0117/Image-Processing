This repository contains four python files which can be used to perform various aspects of image processing.
1. Snip_it.py
2. Editor.py
3. Rectangular_selection.py
4. ASCII_art.py



# THE ORIGINAL IMAGES
![Forest](/Images/Original.jpeg)      
![Walter](/Images/Walter.JPG)
> The following images are with respect to these two


# SNIP IT
It is a GUI based application which resembles the magnetic lasso tool of photoshop i.e, one can use it to snip an image along the edges of any of the objects present inside the picture. The tool automatically detects the sharpest edge in it's vicinity and selects it.

## LIBRARIES REQUIRED :
 1. Numpy(`pip install numpy`)
 2. Scipy(`pip install scipy`)
 3. Pygame(`pip install pygame`)
 4. PIL or Pillow(`pip install --upgrade Pillow`)

## WORKING :
 - On running the program the user is prompted to provide the path to the targeted image.
 - After opening the user has to click to change the mode to selection mode(Shown by the circle on the upper left corner)
 - Once in selection mode the user has to move the mouse pointer close to the edges of the region to be selected. The edges will be automatically detected and selected (shown by red).
 - On clicking again the mode changes to the free-movement mode (The white circle changes to black) and the mouse pointer can be moved freely without selecting any part of the image.
 - This process has to be repeated again and again till the required region/regions get selected.
 - The selection does not necessarily have to be a closed polygon, as long as there is a red pixel to the right and left of the selected part. They may even be disconnected from one another, but please ensure they don't overlap.
 - On closing the window the selected part of the image is stored in a file called `<imageName>_cropped.png` as a transparent image in the same location as the original image file.

 ![Cropped image](/Images/Walter_transparent.png)

## FURTHER IMPROVEMENTS :
- The edges of the resulting image are not very sharp as the selection is not necessarily a closed polygon. That can be worked upon.



# EDITOR
It's a CLI tool to help the user produce different versions of the same image. The tool can be used to generate _Black and white_, _Sepia_, _Threshold_(Purely black and white), _Negative_ and much more...

![Black and White](/Images/Black_and_white.png) ![Sepia](/Images/Sepia.png) ![Negative](/Images/negative.png) ![Threshold](/Images/threshold.png)

## LIBRARIES REQUIRED :
1. Numpy(`pip install numpy`)
2. PIL or Pillow(`pip install --upgrade Pillow`)

## SYNTAX :
1. Black and White(syntax : `1`)
2. Negative(syntax : `2`)
3. Sepia(syntax : `3`)
4. Threshold(pure black and white)(syntax : `4 <threshold>`)
5. Coloured Monochrome(syntax : `5 <R>,<G>,<B>` (RGB values comma separated without space))
6. Coloured Threshold(syntax : `6 <R>,<G>,<B> <threshold>`)
- Make sure there's only *ONE* space wherever there is space in the syntax and no spaces around the commas(',')
- `<R>, <G>, <B>` refers to the red, green, blue values of the colour you want to choose. You may look that up on the internet.

## WORKING :
 - On running the program the user is prompted to provide the path to the targeted image.
 - Then the user has to specify the action using the syntax provided.
 - The edited image is saved in the same location as the original image with name `<imageName>_cropped.png`



# RECTANGULAR SELECTION
 To be honest, it is a rip-off of the `snipping tool` (or `grab` for mac users). It's a GUI based tool to crop a rectangular selection from an image.

## LIBRARIES REQUIRED :
 1. Numpy(`pip install numpy`)
 2. Pygame(`pip install pygame`)
 3. PIL or Pillow(`pip install --upgrade Pillow`)

## WORKING :
  - On running the program the user is prompted to provide the path to the targeted image.
  - After opening the user has to click to change the mode to selection mode(Shown by the circle on the upper left corner)
  - Once in selection mode the user has to drag the mouse pointer to another location in order to create a rectangolar selection.
  - On clicking again the mode changes to the free-movement mode (The white circle changes to black) and the rectangle becomes static.
  - On closing the window the selected part of the image is stored in a file called `<imageName>_cropped.png` in the same location as the original image file.
  - Please ensure that you make only one rectangular selection, else you won't get the desired results.



# ASCII ART
 As the name might suggest, it generates an ASCII art of the image in question. The targetted image should preferably have a lighter background.

## LIBRARIES REQUIRED :
 1. Numpy(`pip install numpy`)
 2. PIL or Pillow(`pip install --upgrade Pillow`)

## WORKING :
  - On running the program the user is prompted to provide the path to the targeted image.
  - Initially a smaller thumbnail sized version of the original image is created to ensure proper fit in the screen
  - The user has to provide a threshold(from 0 to 255, preferred range : 90 - 160) to affect the image.
  - The art is saved in a file called `<imageName> ASCII art.txt` in the same location as the original file and also displayed on the terminal screen.
  - The displayed text and the text stored in the file are printable character wise photographic negatives of each other. This has been done keeping in mind the standard dark colour of the terminal screen and lighter background of the text editors.

![ASCII terminal](/Images/Walter_ASCII.JPG)   ![ASCII notepad](/Images/Walter_text.JPG)

## CONTRIBUTIONS :
- Pull requests are welcome.
- For major changes, please open an issue first to discuss what you would like to change.
