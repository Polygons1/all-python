import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!normal':
        	await message.channel.send(":foot:")




client = MyClient()
client.run("MTAxNTY0Nzk1ODY4OTEyMDI3OA.G5zYQS.D4R2XjN948X5kk323Niyfgt8AkNXjiu-n8On3Q")