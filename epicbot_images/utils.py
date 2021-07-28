from textwrap import TextWrapper

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