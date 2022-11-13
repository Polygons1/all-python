import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return


        if message.content == "!pcodes-sites":
            await message.channel.send("Using: google.com - https://www.google.com/search?q=roblox+promo+codes&oq=roblox+promo&aqs=chrome.0.0i512j69i57j0i512l8.10096j0j7&sourceid=chrome&ie=UTF-8")
            await message.channel.send(u"\u2800")
            for url in ["https://www.vg247.com/roblox-promo-codes", "https://progameguides.com/roblox/roblox-promo-codes-list/", "https://www.pcgamesn.com/roblox/promo-codes-redeem", "https://www.rockpapershotgun.com/roblox-promo-codes"]:
                await message.channel.send(u"\u2800")
                await message.channel.send(f"{url}")
        if message.content == "!clear":
            for times in range(100):
                await message.channel.send(u"\u2800")


client = MyClient()
client.run('OTc0OTQwNDc5NjAwODY5NDE3.Giq-9F.5PQLyChQpyX6_rDQ-u8pCixbsOXJ-w3vwMocNU')