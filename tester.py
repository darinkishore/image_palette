
# check to see if all five images have visually similar colors
import img_palette_gen
import sqlite3


def test_all_images():
    palette = img_palette_gen.main()
    conn = sqlite3.connect('images.db')
    c = conn.cursor()

    c.execute(f"SELECT * FROM images WHERE img_name = {palette[0]}")
    result = c.fetchone()
    h, s, v = result[1], result[2], result[3] # this gives us the values of h,s,v to compare to
    # make sure every image in palette is within 4% of the first image, except for value.
    for img in palette:
        c.execute(f"SELECT * FROM images WHERE img_name = {img}")
        result = c.fetchone()
        h2, s2, v2 = result[1], result[2], result[3]
        if abs(h - h2) > 0.04 or abs(s - s2) > 0.04:
            return False
    return True






