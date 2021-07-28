# Install

```
$ py -m pip install git+https://github.com/nirlep5252/epicbot-images
```

# Usage

```py
from epicbot-images.memes import drake

# in your bot
@bot.command()
async def drake(first, second):
    await ctx.reply(file=discord.File(await drake.make_image(first, second), filename='drake.png'))
```

# ey i didnt test this yet use at ur own risk 
## ~ norlap