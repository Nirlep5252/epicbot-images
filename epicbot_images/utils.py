from textwrap import TextWrapper
from PIL.Image import Image


def wrap_text(width, text) -> str:
    """
    Making it so that the text doesn't flow outside the image by adding a bunch of `\n`s.
    """
    wrapper = TextWrapper(width=width)
    t = ""
    _t_list = wrapper.wrap(text=text)
    for _t in _t_list:
        t += f"{_t}\n"
    return t

def resize_image(image: Image, new_width: int = 100) -> Image:
    """
    Resizes the mother fucking image.
    """
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def convert_image_to_grayscale(image: Image) -> Image:
    """
    Makes the image same as my life.
    """
    return image.convert("L")

# this utilizes your mo-
# :flint:
