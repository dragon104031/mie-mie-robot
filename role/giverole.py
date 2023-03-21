@bot.command()
async def giverole(ctx, member: discord.Member):
    guild=bot.get_guild(1033696327848173618)
    role =guild.get_role(1033708753561862175)
    await member.add_roles(role)
    await ctx.send("已新增身分組")