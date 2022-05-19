import sqlite3


"""
img_palette_gen.py chooses 5 images that are used to generate a color palette.
"""
palette = []


def complimentary_palette(base_img):  # choose 5 images that are complimentary
    h, s, v = base_img[1:4]


def monochromatic_palette(base_img):  # choose 5 images that are monochromatic
    h, s, v = base_img[1:4]
    # Create a sql query to get all images that are within a certain range of the base image
    conn = sqlite3.connect('images.db')
    c = conn.cursor()
    c.execute(
        f"SELECT * FROM images WHERE ABS(images.saturation - {s}) < .03 "
        f"AND ABS(images.hue - {h}) < .01 ORDER BY RANDOM()")
    images = c.fetchall()
    if len(images) < 5:
        c.close()
        conn.close()
        monochromatic_palette(get_base_img())
    else:  # if there are 5 images, add them to the palette
        for img in images:
            palette.append(f'./archive/Images/{img[0]}')
        c.close()
        conn.close()


def get_choice(base_img, style):  # chooses what thing to run
        sel = style
        if sel == "m":
            monochromatic_palette(base_img)
        elif sel == "c":
            complimentary_palette(base_img)


def get_base_img():
    conn = sqlite3.connect('images.db')
    c = conn.cursor()
    c.execute("SELECT * FROM images ORDER BY RANDOM() LIMIT 20")  # selects a random image
    base_img = c.fetchone()  # gives a tuple of the image, with base[1,2,3] being h,s,v
    c.close()
    conn.close()
    return base_img


def main():  # open images.db and choose one random image
    base_img = get_base_img()
    # TODO : un-hardcode the monochromatic option
    get_choice(base_img, 'm') # chooses the type of palette and runs it
    thing_to_return = palette[0:5]
    palette.clear()
    return thing_to_return



if __name__ == "__main__":
    main()
