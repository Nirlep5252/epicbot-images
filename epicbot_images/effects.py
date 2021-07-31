"""
Adds amazing filters to images.
"""

from PIL import Image, ImageFilter, ImageEnhance
from io import BytesIO
from .utils import resize_image, convert_image_to_grayscale
import pathlib

current_path = pathlib.Path(__file__).parent.resolve()
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


async def blur(image: bytes, radius: int = 2) -> str:
    """
    Blurs the image.
    This might crash if the radius is too big, just like your mom.
    """
    with Image.open(BytesIO(image)) as _e:
        e = _e.filter(ImageFilter.GaussianBlur(radius))
        save_path = f"{current_path}/temp/blur.png"
        e.save(save_path)
        return save_path


async def flip(image: bytes, horizontal: bool = True, vertical: bool = False) -> str:
    """
    Flips the image.

    By default it will flip it horizontally, but you can make it flip veritically or both.
    """
    with Image.open(BytesIO(image)) as e:
        if horizontal:
            e = e.transpose(Image.FLIP_LEFT_RIGHT)
        if vertical:
            e = e.transpose(Image.FLIP_TOP_BOTTOM)
        save_path = f"{current_path}/temp/flip.png"
        e.save(save_path)
        return save_path


async def rotate(image: bytes, degrees: int = 90) -> str:
    """
    Rotates your cute face UwU!~
    """
    with Image.open(BytesIO(image)) as e:
        e = e.rotate(degrees)
        save_path = f"{current_path}/temp/rotate.png"
        e.save(save_path)
        return save_path


async def enhance(image: bytes, **options) -> str:
    """
    Enhances the image based on the options.
    """
    with Image.open(BytesIO(image)) as e:
        if 'contrast' in options:
            contrast = ImageEnhance.Contrast(e)
            e = contrast.enhance(options['contrast'])
        if 'color' in options:
            color = ImageEnhance.Color(e)
            e = color.enhance(options['color'])
        if 'brightness' in options:
            brightness = ImageEnhance.Brightness(e)
            e = brightness.enhance(options['brightness'])
        if 'sharpness' in options:
            sharpness = ImageEnhance.Sharpness(e)
            e = sharpness.enhance(options['sharpness'])
        save_path = f"{current_path}/temp/enhance.png"
        e.save(save_path)
        return save_path


async def ascii(image: bytes, width: int = 50) -> str:
    """
    Converts your image to ascii. Pretty dope.
    """
    with Image.open(BytesIO(image)) as e:
        e = convert_image_to_grayscale(resize_image(e, width))
        pixels = e.getdata()
        chars = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
        return "\n".join([chars[index: (index + width)] for index in range(0, len(chars), width)])
