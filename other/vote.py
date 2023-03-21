@bot.command()
async def vote(ctx, *, message):
  user = ctx.author
  user1 = bot.get_user(500472439546052609)
  user2 = bot.get_user(547076362708451358)
  if user == user1:
        await ctx.message.delete()
        embed = discord.Embed(title=f"{message}", description="", color=0x2160f2)
        embed.set_thumbnail(url=ctx.author.avatar)
        embed.set_footer(text="請投下神聖的一票")
        msg = await ctx.send(embed=embed)
  
        
        await msg.add_reaction('✅')
        await msg.add_reaction('❎')

  elif user == user2:
        await ctx.message.delete()
        embed = discord.Embed(title=f"{message}", description="", color=0x2160f2)
        embed.set_thumbnail(url=ctx.author.avatar)
        embed.set_footer(text="請投下神聖的一票")
        msg = await ctx.send(embed=embed)
  
        
        await msg.add_reaction('✅')
        await msg.add_reaction('❎')
  else:
    await ctx.send(f'{ctx.message.author} 你無權使用這個指令')