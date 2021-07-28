# Install

```
$ py -m pip install git+https://github.com/nirlep5252/epicbot-images
```

# Usage

```py
from epicbot_images import memes

# in your bot
@bot.command()
async def drake(ctx, first, second):
    await ctx.reply(file=discord.File(await memes.drake(first, second), filename='drake.png'))
```

# ey i didnt test this yet use at ur own risk 
## ~ norlap