from wand.image import Image as WandImage
from wand.color import Color as WandColor
import pathlib
from io import BytesIO

current_path = pathlib.Path(__file__).parent.resolve()


def wiggle(img: bytes) -> str:
    """
    Makes a wiggle gif effect from the image.
    Recommended to use smol images, cuz it'll take a long time for big images.
    """
    with WandImage(blob=BytesIO(img)) as im:
        crewmate = WandImage()
        frames = []
        for hm in range(-12, 12):
            if hm != 0:
                impostor = im.clone()
                impostor.background_color = WandColor('#36393f')
                impostor.wave(im.height / 32, im.width / (hm / 1.5))
                frames.append(impostor)
        frames.extend(frames[::-1])
        crewmate.sequence.extend(frames)
        save_path = f"{current_path}/temp/wiggle.gif"
        crewmate.save(filename=save_path)
        return save_path
