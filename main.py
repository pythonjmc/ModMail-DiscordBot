import discord
from discord.ext import commands
from discord import Embed, Color
import asyncio
from discord import guild

bot = commands.Bot(command_prefix = '&', description = "Contactez moi par message privé pour signalez un probleme. Ne me contactez pas pour demander de l'aide.")

bot.help_command = None
bot.remove_command("help")


#Events
@bot.event
async def on_ready():
    print("Modmail is ready to work")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if str(message.channel.type) == 'private':
        modmail_channel = discord.utils.get(bot.get_all_channels(), name = "Your_channel_name")
        await modmail_channel.send(f"{message.author.mention}\n**{message.content}**")
    elif str(message.channel) == 'modmail-report' and message.content.startswith("<"):
        member_object = message.mentions[0]

        index = message.content.index(" ")
        string = message.content
        mod_message = string[index:]


        em = discord.Embed(title = f"{message.author}", color = 0x3498db)
        em.add_field(name="\u200B", value = f"{mod_message}")
        em.set_footer(text = f"Envoyé par {message.author}")
        em.set_thumbnail(url = message.author.avatar_url)
        await member_object.send(embed = em)
    else:
        await bot.process_commands(message)

#commands
@bot.command
@commands.has_any_role("Fondateur", "Administrateur", "Modérateur")
async def report(ctx, member : discord.Member, *, text):
    await member.send(text)

bot.run("token")
