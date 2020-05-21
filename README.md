# ECE385 Palletization Tool

- This is a ECE 385 helper tool that utilizes KMeans clustering to generate a pallete and utilize it to palletize the image.
- This program takes in five user inputs:
  - The first is the name of the png that you are trying to palletize (say like img.png is the image but you should just input img). 
  - The second is the name of the palletized image with the new pallete colors (say you want to name it img_final, so you input that). 
  - The third is the name of the file in which you want to save the corresponding indices into the pallete for each color in the image in row-major order (something like img_indices). 
  - The fourth is the text file you want to store the actual colors in the pallete (something like img_palette). 
  - The fifth is the number of colors you want in the pallete (a number say like 24 or 16). 
- This tool requires **scikit-learn**, **numpy**, **matplotlib** and **PIL** to function and works with python up till 3.7 (confirmed).
- A video tutorial can be viewed here: https://www.youtube.com/watch?v=5r1jbdgiNRg
- If you have any questions please contact me at tejag2@illinois.edu or avgupta3@illinois.edu
