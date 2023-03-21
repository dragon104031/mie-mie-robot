@bot.command()
async def join(ctx):
    
    
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if ctx.author.voice == None:
        await ctx.send("我不在任何一個語音頻道裡")
    elif voice == None:
        voiceChannel = ctx.author.voice.channel
        await voiceChannel.connect()
    else:
         channel = ctx.message.author.voice.channel
         await ctx.send(f"機器咩咩已連接語音頻道{channel}")
        
@bot.command()
async def leave(ctx):
    
    
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice == None:
        await ctx.send("機器咩咩並未連接語音頻道")
    else:
        await voice.disconnect()
        channel =  ctx.message.author.voice.channel
        await ctx.send(f"機器咩咩已離開語音頻道{channel}")