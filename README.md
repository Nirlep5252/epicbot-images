# Install

```
$ pip install epicbot-images
```

# Usage

### Memes:
```py
from epicbot_images import memes


# somewhere else
# this example is for discord bots,
# but `memes.drake()` returns a path to the final image output,
# you can use this in any python app you want, not limited to discord bots.
@bot.command()
async def drake(ctx, first, second):
    await ctx.reply(file=discord.File(await memes.drake(first, second)))
    # it's so easy to use
```

#### I won't be making docs for these, refer to the source code or ask in the support server if you have any questions

# Available meme templates

- `drake`, `disappointed`, `flex_tape`, `bernie`, `panik`, `doge`, `my_heart`

# Links

## [Support](https://discord.gg/Zj7h8Fp) | [Invite EpicBot](https://epic-bot.com/invite) | [Vote EpicBot](https://epic-bot.com/vote)