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


def font(size: int = 30, fontname: str = 'Roboto-Bold'):
    return ImageFont.truetype(f"{current_path}/assets/fonts/{fontname}.ttf", size=size)


async def drake(first: str, second: str) -> str:
    """
    Makes a drake meme image using the `first` and `second` strings.
    """
    _f = wrap_text(15, first)
    _s = wrap_text(15, second)
    f = font()
    with Image.open(f"{current_path}/{templates}/drake.png") as _t:
        t = _t.copy()
        draw = ImageDraw.Draw(t)
        draw.multiline_text((435, 150), _f, (0, 0, 0), f, 'mm', align='center')
        draw.multiline_text((435, 435), _s, (0, 0, 0), f, 'mm', align='center')
        save_path = f"{current_path}/temp/drake.png"
        t.save(save_path)
        return save_path


async def disappointed(first: str, second: str) -> str:
    """
    Makes the disappointed meme image where the guy becomes excited but then gets disappointed again.
    """
    _f = wrap_text(20, first)
    _s = wrap_text(20, second)
    f = font()
    with Image.open(f"{current_path}/{templates}/disappointed.png") as _t:
        t = _t.copy()
        draw = ImageDraw.Draw(t)
        draw.multiline_text((250, 120), _f, (0, 0, 0), f, 'mm', align='center')
        draw.multiline_text((250, 400), _s, (0, 0, 0), f, 'mm', align='center')
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
    f = font()
    if username is not None:
        _u = wrap_text(25, username)
    with Image.open(f"{current_path}/{templates}/flex_tape.png") as _t:
        t = _t.copy()
        draw = ImageDraw.Draw(t)
        draw.multiline_text((490, 150), _f, (255, 255, 255), f, 'mm', align='center')
        draw.multiline_text((420, 500), _s, (255, 255, 255), f, 'mm', align='center')
        if username is not None:
            draw.multiline_text((200, 175), _u, (255, 255, 255), f, 'ms', align='center')
        save_path = f"{current_path}/temp/flex_tape.png"
        t.save(save_path)
        return save_path


async def bernie(text: str) -> str:
    """
    Makes the bernie meme, "I am once again asking for...".
    """
    _e = wrap_text(30, text)
    with Image.open(f"{current_path}/{templates}/bernie.png") as _t:
        t = _t.copy()
        draw = ImageDraw.Draw(t)
        draw.multiline_text((350, 670), _e, (255, 255, 255), font(40), 'ms', align='center')
        save_path = f"{current_path}/temp/bernie.png"
        t.save(save_path)
        return save_path


async def doge(first: str, second: str) -> str:
    """
    Makes the doge meme.
    """
    _f = wrap_text(20, first)
    _s = wrap_text(20, second)
    f = font()
    with Image.open(f"{current_path}/{templates}/doge.png") as _t:
        t = _t.copy()
        draw = ImageDraw.Draw(t)
        draw.multiline_text((150, 370), _f, (0, 0, 0), f, 'ms', align='center')
        draw.multiline_text((450, 370), _s, (0, 0, 0), f, 'ms', align='center')
        save_path = f"{current_path}/temp/doge.png"
        t.save(save_path)
        return save_path


async def panik(panic: str, kalm: str, panik_: str) -> str:
    """
    Panic... Kalm... PANIKK!!!
    """
    panic = wrap_text(15, panic)
    kalm = wrap_text(15, kalm)
    panik_ = wrap_text(15, panik_)
    f = font()
    with Image.open(f"{current_path}/{templates}/panik.png") as _t:
        t = _t.copy()
        draw = ImageDraw.Draw(t)
        draw.multiline_text((133, 133), panic, (0, 0, 0), f, 'mm', align='center')
        draw.multiline_text((133, 435), kalm, (0, 0, 0), f, 'mm', align='center')
        draw.multiline_text((133, 730), panik_, (0, 0, 0), f, 'mm', align='center')
        save_path = f"{current_path}/temp/panik.png"
        t.save(save_path)
        return save_path


# Denz lol (will try to add stuff.. but one for trial purposes)
async def my_heart(normal: str, slight_panic: str, ultra_panic: str) -> str:
    """
    My Heart when...
    """
    normal = wrap_text(15, normal)
    slight_panic = wrap_text(15, slight_panic)
    ultra_panic = wrap_text(15, ultra_panic)
    f = font(12)
    with Image.open(f"{current_path}/{templates}/my_heart.png") as _t:
        t = _t.copy()
        draw = ImageDraw.Draw(t)
        draw.multiline_text((69, 69), normal, (0, 0, 0), f, 'mm', align='center')
        draw.multiline_text((69, 144), slight_panic, (0, 0, 0), f, 'mm', align='center')
        draw.multiline_text((69, 212), ultra_panic, (0, 0, 0), f, 'mm', align='center')
        save_path = f"{current_path}/temp/my_heart.png"
        t.save(save_path)
        return save_path

# I will eat you >:3
# No u
