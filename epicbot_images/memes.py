from PIL import Image, ImageDraw, ImageFont
from .utils import wrap_text
import pathlib

templates = "assets/meme_templates"
current_path = pathlib.Path(__file__).parent.resolve()

async def drake(first, second) -> bytes:
    """
    Makes a drake meme image using the `first` and `second` strings.
    """
    _f = wrap_text(15, first)
    _s = wrap_text(15, second)
    with Image.open(f"{current_path}/{templates}/drake.png") as _t:
        font = ImageFont.truetype(f"{current_path}/assets/fonts/Roboto-Bold.ttf", size=30)
        t = _t.copy()
        draw = ImageDraw.Draw(t)
        draw.multiline_text(xy=(435, 150), text=_f, font=font, fill=(0, 0, 0), anchor='mm', align='center')
        draw.multiline_text(xy=(435, 435), text=_s, font=font, fill=(0, 0, 0), anchor='mm', align='center')
        return t.tobytes()