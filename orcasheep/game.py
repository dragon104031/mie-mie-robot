@bot.command()
async def game(ctx):
    embed=discord.Embed(title="以下是虎鯨有玩的遊戲", color=0x2160f2)
    embed.set_thumbnail(
      url=
"https://cdn-icons-png.flaticon.com/512/2780/2780137.png"
  )
    embed.add_field(name="神界god field", value="固定房號:1107", inline=False)
    embed.add_field(name="第五人格", value="ID:17993843", inline=False)
    embed.add_field(name="傳說對決", value="遊戲名:虎鯨咩咩", inline=True)
    embed.add_field(name="神魔之塔", value="遊戲名:虎鯨咩咩", inline=True)
    embed.add_field(name="哈利波特：魔法覺醒", value="遊戲名:虎鯨咩咩", inline=True)
    embed.add_field(name="糖豆人fallguys", value="ID:YT_虎鯨咩咩orcasheep", inline=True)
    embed.add_field(name="一起來拼軌", value="此遊戲不能加好友", inline=True)
    embed.add_field(name="你畫我猜", value="此遊戲不能加好友", inline=True)
    embed.add_field(name="Roblox", value="遊戲名:orcasheep", inline=True)
    embed.add_field(name="pokemon unite", value="id:H63H8K8", inline=True)
    embed.add_field(name="tetr.io",   value="id:orcasheep", inline=True)
    embed.set_footer(text="別再問虎鯨有玩什麼遊戲了")
    await ctx.send(embed=embed)