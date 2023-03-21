@bot.command()
@commands.has_permissions(manage_guild=True)
async def open_tickets(ctx:commands.Context):
  await ctx.message.delete()
  embed = nextcord.Embed(title ="有時本咩會不在,可以用這個,會有管理員協助唷！（當然我在的話也可以用）", description="此功能用途包含檢舉騷擾,提供意見等等....（請各位盡量不要直接私訊管理員）" , color = 0x2160f2 )
  embed.set_thumbnail(url="https://yt3.googleusercontent.com/vS1pFquZ8l0UNUwdUg-fxI4AUoznqnibjS62tJcO1WZKc9Ps2vEfm6cF9vL0p9b0-EDQjmx2_w=s176-c-k-c0x00ffffff-no-rj")
  await ctx.send(embed=embed, view=CreateTicket())
  
class CreateTicket(nextcord.ui.View):
  def __init__(self):
      super().__init__(timeout=None)
      self.value=None

  @nextcord.ui.button(
    label="🛂呼叫管理員", style=nextcord.ButtonStyle.blurple, custom_id="Create_Ticket:blurple"
  )
  async def create_ticket(self, button: nextcord.ui.button, interaction: nextcord.Interaction):
    msg=await interaction.response.send_message("正在創建客服單....", ephemeral=True)
    overwrites = {
    interaction.guild.default_role:nextcord.PermissionOverwrite(read_messages=False),
    interaction.guild.me: nextcord.PermissionOverwrite(read_messages=True),
    interaction.user: nextcord.PermissionOverwrite(read_messages=True)
   
    }
    channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-ticket", overwrites=overwrites)
    await msg.edit(f"已創建客服單! {channel.mention}")
    embed = nextcord.Embed(title="歡迎使用客服單", description=f"{interaction.user.mention} 請等待管理員進來為你服務", color=0x2160f2)
    await channel.send(embed=embed, view=TicketSettings())

class TicketSettings(nextcord.ui.View):
  def __init__(self):
      super().__init__(timeout=None)
      self.value=None
  @nextcord.ui.button(
    label="❎按此結束私訊", style=nextcord.ButtonStyle.red, custom_id="ticket_settings:red")
  async def close_ticket(self, button: nextcord.ui.button, interaction: nextcord.Interaction):
    await interaction.response.send_message("客服單已關閉",ephemeral=True)
    await interaction.channel.delete()
