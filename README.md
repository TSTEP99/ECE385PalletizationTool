# ECE385 Palletization Tool

- This is a ECE 385 helper tool that utilizes KMeans clustering to generate a pallete and utilize it to palletize the image.
- This program takes in four user inputs:
  - The first is the name of the png that you are trying to palletize. 
  - The second is the name of the palletized image with the new pallete colors. 
  - The third is the name of the file in which you want to save the corresponding indices into the pallete for each color in the image in row-major order. 
  - The fourth is the text file you want to store the actual colors in the pallete. 
  - The fifth is the number of colors you want in the pallete. 
- This tool requires <b>scikit-learn<\b>, <b>numpy<\b>, <b>matplotlib<\b> and <b>PIL<\b> to function and works with python up till 3.7 (confirmed).
- If you have any questions please contact me at tejag2@illinois.edu or avgupta3@illinois.edu
