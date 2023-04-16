import discord
from discord.ext import commands
from discord.utils import sleep_until
import datetime

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=None, intents=intents)

bot_token = "YOUR_BOT_TOKEN"
channel_id_1 = 5646544654654 # replace with ur first channel id 
channel_id_2 = 6449849848947 # replace with ur second channel id
channel_id_3 = 4654654654654654 # replace with ur third channel id 

#logs and timeout role
timeout_role = "ROLE_NAME" # create a timeout role and disable all permission for it in every category 
logss = "logs_channel_name" # create a logs channel and it will post logs there :)


@bot.event
async def on_message(message):
    print(message.content)
    if message.channel.id == channel_id_1 or message.channel.id == channel_id_2 or message.channel.id == channel_id_3:
        bans = ["discord.gg", "discord.com", ".gg/", "tiktok.com", "youtube.com", "twitter.com", "instagram.com"]
        content = message.content.lower()
        for lines in bans:
            if lines in content:
                await message.delete()

                bot_role = discord.utils.get(message.guild.roles, name=timeout_role)
                if bot_role:
                    await message.author.add_roles(bot_role)
                    embed = discord.Embed(title="Damn",
                                        description="Some nigga tried to send discord server invite link, dont worry our anti raid has detected that shit.")
                    await message.channel.send(embed=embed)
                    log_channel = discord.utils.get(message.guild.channels, name=logss)
                    embed = discord.Embed(
                        title='Some nigga got timed out',
                        description=f'<@{message.author.id}> got timed out for weeks for saying `{content}`'
                    )
                    await log_channel.send(embed=embed)
                    await sleep_until(datetime.datetime.now() + datetime.timedelta(seconds=604800))
                    await message.author.remove_roles(bot_role)
                    print(message.author.name)
    if message.channel.id == channel_id_1 or message.channel.id == channel_id_2 or message.channel.id == channel_id_3:
        if len(message.mentions) > 2:
                await message.delete()
                bot_role = discord.utils.get(message.guild.roles, name=timeout_role)
                if bot_role:
                    await message.author.add_roles(bot_role)
                    embed = discord.Embed(
                        title="Oops!",
                        description="Some dumbass tried to mass ping, If you have received any pings ignore it."
                    )
                    await message.channel.send(embed=embed)
                    log_channel = discord.utils.get(message.guild.channels, name=logss)
                    embed = discord.Embed(
                            title="Looks like fat bitches get timedout",
                            description=f"<@{message.author.id}> got timed out for `trying to mass ping everyone.`"
                    )
                    await log_channel.send(embed=embed)
                    await sleep_until(datetime.datetime.now() + datetime.timedelta(seconds=604800))
                    await message.author.remove_roles(bot_role)
                    print(message.author.name)


bot.run(bot_token)
