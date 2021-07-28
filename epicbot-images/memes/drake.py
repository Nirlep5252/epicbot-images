from PIL import Image, ImageDraw, ImageFont
from utils import wrap_text

font = ImageFont.truetype("assets/fonts/Roboto-Bold.ttf", size=30)

async def make_image(first, second) -> bytes:
    """
    Makes a drake meme image using the `first` and `second` strings.
    """
    _f = wrap_text(15, first)
    _s = wrap_text(15, second)
    with Image.open("assets/meme_templates/drake.png") as _t:
        t = _t.copy()
        draw = ImageDraw.Draw(t)
        draw.multiline_text(xy=(435, 150), text=_f, font=font, fill=(0, 0, 0), anchor='mm', align='center')
        draw.multiline_text(xy=(435, 435), text=_s, font=font, fill=(0, 0, 0), anchor='mm', align='center')
        return t.tobytes()