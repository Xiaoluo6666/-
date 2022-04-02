


from codeop import bot


bot = bot.Bot(command_prefix='[')

@bot.event
async def on_ready():
   print(">> Bot is online <<")

bot.run('OTUyODk4NTYzNjg2NDI0NTk2.Yi8t8Q.VXF81ckI-MFvl0xbE2xTrIOWVEU')