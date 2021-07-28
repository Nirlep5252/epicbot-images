"""
All of these functions save the images in the temp directory and return the path to that.

So you can not only use this in your Discord bot, but also any website made using a python backend,
or any other python application you might have.

Feel free to contribute any new image templates/code improvements in my stupid package lmao :3
"""

from PIL import Image, ImageDraw, ImageFont
from .utils import wrap_text
import pathlib

templates = "assets/meme_templates"
current_path = pathlib.Path(__file__).parent.resolve()
font = ImageFont.truetype(f"{current_path}/assets/fonts/Roboto-Bold.ttf", size=30)

async def drake(first: str, second: str) -> str:
    """
    Makes a drake meme image using the `first` and `second` strings.
    """
    _f = wrap_text(15, first)
    _s = wrap_text(15, second)
    with Image.open(f"{current_path}/{templates}/drake.png") as _t:
        t = _t.copy()
        draw = ImageDraw.Draw(t)
        draw.multiline_text((435, 150), _f, (0, 0, 0), font, 'mm', align='center')
        draw.multiline_text((435, 435), _s, (0, 0, 0), font, 'mm', align='center')
        save_path = f"{current_path}/temp/drake.png"
        t.save(save_path)
        return save_path

async def disappointed(first: str, second: str) -> str:
    """
    Makes the disappointed meme image where the guy becomes excited but then gets disappointed again.
    """
    _f = wrap_text(20, first)
    _s = wrap_text(20, second)
    with Image.open(f"{current_path}/{templates}/disappointed.png") as _t:
        t = _t.copy()
        draw = ImageDraw.Draw(t)
        draw.multiline_text((250, 120), _f, (0, 0, 0), font, 'mm', align='center')
        draw.multiline_text((250, 400), _s, (0, 0, 0), font, 'mm', align='center')
        save_path = f"{current_path}/temp/disappointed.png"
        t.save(save_path)
        return save_path

async def flex_tape(first: str, second: str, username: str = None) -> str:
    """
    Makes the flex tape meme.
    Put's the username as the flex tape guy if given, else leaves it empty.
    """
    _f = wrap_text(15, first)
    _s = wrap_text(15, second)
    _u = wrap_text(25, username)
    with Image.open(f"{current_path}/{templates}/flex_tape.png") as _t:
        t = _t.copy()
        draw = ImageDraw.Draw(t)
        draw.multiline_text((490, 150), _f, (255, 255, 255), font, 'mm', align='center')
        draw.multiline_text((420, 500), _s, (255, 255, 255), font, 'mm', align='center')
        if username is not None:
            draw.multiline_text((200, 175), _u, (255, 255, 255), font, 'ms', align='center')
        save_path = f"{current_path}/temp/flex_tape.png"
        t.save(save_path)
        return save_path

# I will eat you >:3