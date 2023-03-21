@bot.event
async def on_member_join(member):
    print(f"{member}join!")
    channel=bot.get_channel(1084499683839332362)
    embed=discord.Embed(title=f"{member}歡迎光臨虎鯨咩咩dc群！", color=0x2160f2)
    embed.set_footer(text="記得領身分組!")
    await channel.send(embed=embed)
    

@bot.event
async def on_member_remove(member):
    print(f"{member}leave!")
    channel = bot.get_channel(1084500185025101915)
    await channel.send(f"{member}對於您的離開,我們非常遺憾")