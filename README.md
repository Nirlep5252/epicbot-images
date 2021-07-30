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
    await ctx.reply(file=discord.File(await memes.drake(first, second)))
    # it's so easy to use
```
### Filters:
```py
from epicbot_images import effects

@bot.command()
async def blur(ctx, user: discord.User):
    await ctx.reply(file=discord.File(await effects.blur(await user.avatar.read())))
    # 1 line go brr
```

#### I won't be making docs for these, refer to the source code or ask in the support server if you have any questions

## Meme templates
- `drake`, `disappointed`, `flex_tape`, `bernie`, `panik`, `doge`, `my_heart`
## Effects
- `blur`, `flip`, `rotate`, `enhance`

# Links
## [Support](https://discord.gg/Zj7h8Fp) | [Invite EpicBot](https://epic-bot.com/invite) | [Vote EpicBot](https://epic-bot.com/vote)