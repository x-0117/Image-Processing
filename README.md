# Snip_It
"Snip_It" is a GUI based application which is similar to the snipping tool but one can use it to snip an image along the edges rather than just rectangular selections.

 LIBRARIES REQUIRED :
 1. Numpy
 2. Scipy
 3. Matplotlib
 4. Pygame

 WORKING :
 > On running the program the user is prompted to provide the path to the targeted image.
 > After opening the user has to click to change the mode to selection mode(Shown by the white opaque circle on the Left upper corner)
 > Once in selection mode the user has to move the mouse pointer close to the edges of the region to be selected. The edges will be automatically detected and selected (shown by red).
 > On clicking again the mode changes to the free-movement mode (The white circle changes to black) and the mouse pointer can be moved freely without selecting any part of the image.
 > This process has to be repeated again and again till the required region/regions get selected.
 > On closing the window the selected part of the image is displayed.

FURTHER IMPROVEMENTS :
> The resulting image is a bit distorted. The quality needs to be improved.
> The resulting image is just displayed on screen, rendering it useless for the future. The image data can be stored in files of jpeg or png formats

CONTRIBUTIONS :
> Pull requests are welcome.
> For major changes, please open an issue first to discuss what you would like to change.
