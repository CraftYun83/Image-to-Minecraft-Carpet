# Image-to-Minecraft-Carpet
A Python script that will turn an image into a simplified image of Minecraft carpet colours.

I built this script in 3 hour at 10pm so it's really not optimized.

What the script is doing:

Storing the RGB values of every pixel inside an image onto a list  
Comparing each pixel to each colour of carpet (You can find the dictionary of each colour inside the main script)  
You can get the similarity level using this algorithm: `sqrt((r2-r1)^2+(g2-g1)^2+(b2-b1)^2)` (https://stackoverflow.com/a/9018153/17285943)  
The lower the number is, the closer the 2 RGB values are.  
It then gets the most similar RGB value and then saves it to a new list (`pix_as_carpet`)  
It then creates a new PIL image with the same dimensions as the original image, and then reapplies all the colours, except with the colours in `pix_as_carpet`  

I actually find this so cool, and I'm super proud of myself.
