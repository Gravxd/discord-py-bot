import discord
global prefix 
prefix = '!' # set your prefix here
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        if message.author == self.user:
            return 
        if message.content == prefix + 'ping':
            await message.channel.send('pong')
        if message.content == prefix + 'help':
            await message.channel.send('Contact a staff member for help!')
        if message.content == prefix + 'help':
            print(message.author, 'has requested help!')
        print(message.author,':',message.content,'(',message.channel.name,')')
        if message.content == prefix + 'embed':
            embed1 = discord.Embed(title="this is a title", description="this is a description!", color=0x00ff00)
            await message.channel.send(embed = embed1)
        

client = MyClient()
client.run('tokenhere')
