# Install

```shell
$ pip install epicbot-images
```

# Usage

### Memes:
```py
from epicbot_images import memes

# for a discord bot
@bot.command()
async def drake(ctx, first, second):
    await ctx.reply(file=discord.File(memes.drake(first, second)))
    # it's so easy to use
```
### Effects:
```py
from epicbot_images import effects

@bot.command()
async def blur(ctx, user: discord.User):
    await ctx.reply(file=discord.File(effects.blur(await user.avatar.read())))
    # 1 line go brr
```

### Advanced Usage (recommended):
```py
from epicbot_images import effects 
from functools import partial

@bot.command()
async def wiggle(ctx, user: discord.User):
    await ctx.reply(file=discord.File(
        await bot.loop.run_in_executor(None, partial(effects.wiggle, img=await user.avatar.read()))
    ))
```

#### I won't be making docs for these, refer to the source code or ask in the support server if you have any questions

## Meme templates
- `drake`, `disappointed`, `flex_tape`, `bernie`, `panik`, `doge`, `my_heart`
## Effects
- `blur`, `flip`, `rotate`, `enhance`, `ascii`, `blend`, `wiggle`

# Links
## [Support](https://discord.gg/Zj7h8Fp) | [Invite EpicBot](https://epic-bot.com/invite) | [Vote EpicBot](https://epic-bot.com/vote)
