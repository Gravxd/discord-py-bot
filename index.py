import discord # import the discord libary
global prefix # set our prefix to be globally available throughout our code
prefix = '!' # set your prefix here
class MyClient(discord.Client):
    async def on_ready(self): # when the bot is in the 'ready' state
        print('Logged on as', self.user) # print to console with the bot's discord tag
    async def on_message(self, message): # when a message is sent
        if message.author == self.user: # if the author of that message is the bot itself, return (cancel)
            return 
        if message.content == prefix + 'ping': # if the message that was sent says !ping 
            await message.channel.send('pong') # then we reply with 'pong!'
        if message.content == prefix + 'help': # if the message that was sent says !help
            await message.channel.send('Contact a staff member for help!') # reply with 'contact a staff member for help!'
        if message.content == prefix + 'help': #if the message that was sent is !help
            print(message.author, 'has requested help!') # print to console that the user needs help
        print(message.author,':',message.content,'(','#',message.channel.name,')') # message logging / output = 'Grav#6969:Hi Github! (#general)'
        if message.content == prefix + 'embed': # if the message that is sent is !embed
            embed1 = discord.Embed(title="this is a title", description="this is a description!", color=0x00ff00) # build the embed
            await message.channel.send(embed = embed1) # send an embed with the listed characteristics 
        print('Operating in', client.guilds.size, 'servers!') # server count will display to terminal / console

client = MyClient() # Define the client variable  - We already defined MyClient() with 'class MyClient(discord.Client):'
client.run('tokenhere') # discord login (bot token) make one at https://discord.dev --> Applications --> Make New --> Bot
