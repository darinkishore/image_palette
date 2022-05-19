# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
from PIL import Image
import csv
from colorthief import ColorThief
from colormap import rgb2hsv, hsv2rgb


def get_dominant_color(image):
    """
    Returns the dominant color in the image.
    """
    thief = ColorThief(image)
    color = thief.get_color(1)  # get rgb tuples of primary colors in img
    return rgb2hsv(color[0], color[1], color[2], normalised=False) # convert them to hex



def main():
    """
    This function creates a csv file with the dominant colors of the images in the folder.
    HSV is used to simplify finding complimentary colors.
    """
    with open('images.csv', 'w') as csvfile:
        imgwriter = csv.writer(csvfile, delimiter=',')  # Create a csv writer object
        imgwriter.writerow(['image', 'hue', 'saturation', 'value'])  # Write the header.
        # json = []
        for file in os.listdir('./archive/Images/'):
            color = get_dominant_color(f'./archive/Images/{file}')  # Get the colors
            imgwriter.writerow([file, color[0], color[1], color[2]])  # Write the row
            # json.append({'image': file, 'color': hsv2rgb(color[0], color[1], color[2])})
            print(f'{file} done')

        # print(json)
    # Dominant colors have been written to the images.csv file.


if __name__ == '__main__':
    main()
