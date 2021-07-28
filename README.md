# Install

```
$ py -m pip install git+https://github.com/nirlep5252/epicbot-images
```

# Usage

### Memes:
```py
from epicbot_images import memes

# somewhere else
@bot.command()
async def drake(ctx, first, second):
    await ctx.reply(file=discord.File(await memes.drake(first, second)))
    # it's so easy to use
```

#### I won't be making docs for these, refer to the source code or ask in the support server if you have any questions

# Available meme templates

- `drake`, `disappointed`, `flex_tape`

# Links

## [Support](https://discord.gg/Zj7h8Fp) | [Invite EpicBot](https://epic-bot.com/invite) | [Vote EpicBot](https://epic-bot.com/vote)