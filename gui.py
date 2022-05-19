import PIL
import PySimpleGUI as sg
import img_palette_gen
import os.path
import PIL.Image
import io
import base64

"""
This program displays the image palette in a GUI after generating it in img_palette_gen.py
"""


def convert_to_bytes(file_or_bytes, resize=None):
    """
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (Union[str, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    Credit: PySimpleGUI's sample code.
    """
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception as e:
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)

    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height / cur_height, new_width / cur_width)
        img = img.resize((int(cur_width * scale), int(cur_height * scale)), PIL.Image.ANTIALIAS)
    with io.BytesIO() as bio:
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()


def main():
    sg.theme('Dark Amber')

    # Define the layout of the GUI
    row_1 = [[sg.Text('Generate a palette of Monochromatic colors.', font="Helvetica", expand_y=True, expand_x=True)]]

    row_2 = [[sg.Column([[sg.Image(key='img1', s=(100,100), expand_x=True, expand_y=True)]]),
              sg.Column([[sg.Image(key='img2', s=(100,100), expand_x=True, expand_y=True)]]),
              sg.Column([[sg.Image(key='img3', s=(100,100), expand_x=True, expand_y=True)]]),
              sg.Column([[sg.Image(key='img4', s=(100,100), expand_x=True, expand_y=True)]])]]

    row_3 = [[sg.Ok(button_text='Generate', size=(30, 1), font=("Helvetica", 25))],
             [sg.Exit(size=(30, 1), font=("Helvetica", 25))]]

    layout = [[row_1], [row_2], [row_3]]

    # Create the window to display the palette.
    window = sg.Window('Image Palette Generator', layout, resizable=True,
                       return_keyboard_events=True)

    # Run the event loop
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        # if generate is pressed
        if event == 'Generate':
            # Generate a new palette
            palette = img_palette_gen.main()
            byte_palette = []
            for img in palette:
                byte_palette.append(convert_to_bytes(img))
            # Update the images in the GUI
            window['img1'].update(data=byte_palette[0])
            window['img2'].update(data=byte_palette[1])
            window['img3'].update(data=byte_palette[2])
            window['img4'].update(data=byte_palette[3])

    # Close and Exit.
    window.close()


if __name__ == '__main__':
    main()
