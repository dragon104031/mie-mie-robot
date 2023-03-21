@bot.command()
async def weather(ctx: commands.Context,*,city):
  url = "https://api.weatherapi.com/v1/current.json"
  params = {
    "key": "yourAPI",
    "q": city
  }
  async with aiohttp.ClientSession() as session:
     async with session.get(url, params=params) as res:
        data = await res.json()

        location = data["location"]["name"]
        temp_c = data["current"]["temp_c"]
        temp_f = data["current"]["temp_f"]
        humidity = data["current"]["humidity"]
        wind_kph = data["current"]["wind_kph"]
        wind_mph = data["current"]["wind_mph"]
        condition = data["current"]["condition"]["text"]
        image_url = "http:" + data["current"]["condition"]["icon"]

        embed = discord.Embed(title=f"{location}的天氣", description=f"The condition in `{location}` is `{condition}`")
        embed.add_field(name="Temperature", value=f"C: {temp_c} | F: {temp_f}" )
        embed.add_field(name="Humidity", value=f"{humidity}" )
        embed.add_field(name="Wind_speeds", value=f"KPH: {wind_kph} | MPH: {wind_mph}" )
        embed.set_thumbnail(url=image_url)
        await ctx.send(embed=embed)