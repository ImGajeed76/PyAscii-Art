from src.pyAsciiArt.PyAsciiArt import AsciiArt


def helloWorld():
    image_path = r"example_image.jpg"
    ascii_art = AsciiArt(image_path, divider=3.7, spacerX=4, spacerY=1,
                         ascii_chars_black_to_white=AsciiArt.simple_char_set)

    ascii_art.generatePixelArray()
    ascii_art.trimPixelColors()
    ascii_art.generateAsciiImage()
    ascii_art.writeToFile("image.txt")
