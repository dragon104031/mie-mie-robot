@bot.listen()
async def on_raw_reaction_add(data):
  if str(data.emoji)=='<:fallguys:1086685759215501354>':
    guild=bot.get_guild(1033696327848173618)
    role =guild.get_role(1033712663710138408)
    await data.member.add_roles(role)
  elif str(data.emoji)=='<:identity:1086685994696331365>':
    guild=bot.get_guild(1033696327848173618)
    role =guild.get_role(1033712917956263936)
    await data.member.add_roles(role)
  elif str(data.emoji)=='<:roblox:1086685764273844375>':
    guild=bot.get_guild(1033696327848173618)
    role =guild.get_role(1035899577468985394)
    await data.member.add_roles(role)
  elif str(data.emoji)=='<:18:1086686599338786888>':
    guild=bot.get_guild(1033696327848173618)
    role =guild.get_role(1039134165158875217)
    await data.member.add_roles(role)
  elif str(data.emoji)=='<:agree:1086690767680065637>':
    guild=bot.get_guild(1033696327848173618)
    role =guild.get_role(1033708753561862175)
    await data.member.add_roles(role)

@bot.listen()
async def on_raw_reaction_remove(data):
  if str(data.emoji)=='<:fallguys:1086685759215501354>':
    guild=bot.get_guild(1033696327848173618)
    user=guild.get_member(data.user_id)
    role =guild.get_role(1033712663710138408)
    await user.remove_roles(role)
  elif str(data.emoji)=='<:identity:1086685994696331365>':
    guild=bot.get_guild(1033696327848173618)
    user=guild.get_member(data.user_id)
    role =guild.get_role(1033712917956263936)
    await user.remove_roles(role)
  elif str(data.emoji)=='<:roblox:1086685764273844375>':
    guild=bot.get_guild(1033696327848173618)
    user=guild.get_member(data.user_id)
    role =guild.get_role(1035899577468985394)
    await user.remove_roles(role)
  elif str(data.emoji)=='<:18:1086686599338786888>':
    guild=bot.get_guild(1033696327848173618)
    user=guild.get_member(data.user_id)
    role =guild.get_role(1039134165158875217)
    await user.remove_roles(role)
  elif str(data.emoji)=='<:agree:1086690767680065637>':
    guild=bot.get_guild(1033696327848173618)
    user=guild.get_member(data.user_id)
    role =guild.get_role(1033708753561862175)
    await user.remove_roles(role)