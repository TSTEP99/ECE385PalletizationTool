# ECE385PalletizationTool

This is a ECE 385 helper tool that utilizes KMeans clustering to generate a pallete and utilize it to palletize the image.
This program takes in four user inputs. The first is the name of the png that you are trying to palletize. The second is the where
you want to save the palletized image with the new pallete colors. The third is where you want to save the corresponding indices into the
pallete for each color in the image in row-major order. The fourth the text file you want to store the actual colors in the pallete. The fifth
is the number of colors you want in the pallete. This tool requires both scikit-learn and numpy to function and works with python 3.6. If you
have any questions please contact me at tejag2@illinois.edu.
