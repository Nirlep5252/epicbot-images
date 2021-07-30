"""
Adds amazing filters to images.
"""

from PIL import Image, ImageFilter
from io import BytesIO
import pathlib

current_path = pathlib.Path(__file__).parent.resolve()


async def blur(image: bytes, radius: int = 2) -> str:
    """
    Blurs the image...
    """
    with Image.open(BytesIO(image)) as _e:
        e = _e.filter(ImageFilter.GaussianBlur(radius))
        save_path = f"{current_path}/temp/blur.png"
        e.save(save_path)
        return save_path
