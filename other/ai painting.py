class Dropdown(nextcord.ui.Select):
  def __init__(self, message, images, user):
    self.message=message
    self.images=images
    self.user=user

    options=[
      nextcord.SelectOption(label="1"),
      nextcord.SelectOption(label="2"),
      nextcord.SelectOption(label="3"),
      nextcord.SelectOption(label="4"),
      nextcord.SelectOption(label="5"),
      nextcord.SelectOption(label="6"),
      nextcord.SelectOption(label="7"),
      nextcord.SelectOption(label="8"),
      nextcord.SelectOption(label="9"),
    ]
    super().__init__(
        placeholder="看其他作品!",
        min_values=1,
        max_values=1,
        options=options,
        )
  async def callback(self, interaction: nextcord.Interaction):
    if not int(self.user) == int(interaction.user.id):
      await interaction.response.send_message("You are not the author of this message!", ephemeral=True)
    selection = int(self.values[0])-1
    image = BytesIO(base64.decodebytes(self.images[selection].encode("utf-8")))
    return await self.message.edit(content="生成完畢,這幅畫生成自 **craiyon.com**",file=nextcord.File(image,"generatedImage.png"),view=DropdownView(self.message, self.images, self.user)) 

class DropdownView(nextcord.ui.View):
  def __init__(self,message,images,user):
    super().__init__()
    self.message=message
    self.images=images
    self.user=user
    self.add_item(Dropdown(self.message, self.images, self.user))

@bot.command()
async def generate(ctx:commands.Context,*,prompt:str):
    ETA = int(time.time() + 60)
    msg = await ctx.send(f"生成中,請稍後........ETA:<t:{ETA}:R>")
    async with aiohttp.request("POST", "https://backend.craiyon.com/generate", json={"prompt": prompt}) as resp:
      r = await resp.json()
      images = r['images']
      image = BytesIO(base64.decodebytes(images[0].encode("utf-8")))
      return await msg.edit(content="生成完畢,這幅畫生成自**craiyon.com**", file=nextcord.File(image,"generatedImage.png"),view=DropdownView(msg, images, ctx.author.id))