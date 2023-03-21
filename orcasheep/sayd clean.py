@bot.command()
async def sayd(ctx,*,msg):
  user = ctx.author
  user1 = bot.get_user(500472439546052609)
  user2 = bot.get_user(547076362708451358)
  if user == user1:
    await ctx.message.delete()
    await ctx.send(msg)
  elif user == user2:
    await ctx.message.delete()
    await ctx.send(msg)
  else:
    await ctx.send(f'{ctx.message.author} 你無權使用這個指令')

@bot.command()
async def clean(ctx,num:int):
  user = ctx.author
  user1 = bot.get_user(500472439546052609)
  user2 = bot.get_user(547076362708451358)
  if user == user1:
    await ctx.channel.purge(limit=num+1)
  elif user == user2:
    await ctx.channel.purge(limit=num+1)
  else:
    await ctx.send(f'{ctx.message.author} 你無權使用這個指令')

eve = datetime.datetime.now().strftime('%Y-%m-%d %H %M %S')