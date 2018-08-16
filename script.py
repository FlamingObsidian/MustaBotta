import discord
from discord.ext import commands
import random

bot=commands.Bot(command_prefix='.')

hates = ["maths","Elon Musk","American spelling","expanded universes","Disney","Ssolbergj","micromanaging herds of rowdy children","shaving","formal attire","Danes","charged chevrons","a lack of assets","American state flags","vacuum cleaners","the word \"independent\"","Avi","mobile keyboards","shopping","talking","the red underlines in MS Word","haircuts","Korean heart","artistic people",
"avatar changing","James","Wappenwiki colors","overcharging","covers at my local bookstore","Inkscape glitches","Iowan license plates","Spurdo Spärde","James's cadency system","peripheral vision playing tricks","when people misspell its / it's","bugs","the Finnish postal service","the name of Suomenusko","Russians","Germany","Finnish weather","tests that require googling words","societies with unspecified membership fees","people complaining about downvotes","the number of types of Lutheranism","zombies","blazoning","when I start a rant and noticing that the rantee is AFK","Rule 5",
"the phrase \"swiggity swooty\"","Russian heraldry","light","Cdreus","logos","Canada","75% of the new Star Wars characters","the US embassy in Helsinki","talented people","legs","British noble heraldry","the word Czechia","the Bézier Game","the animated logo of the Ministry of Foreign Affairs of Finland","loss","Iberian shields with diagonal sides","the word tabloid","the website of the Swedish royal family","the list of Russian leaders Lyylikki would bang","Artifexian, but can’t tell why","the Reddit comment section","the coat of arms of Kanepi, Estonia","the flaps the priests have around their necks","swimming pools",
"the official emblazon of the coat of arms of Norway","when my bookstore gives out -15% codes","claw monsters","Sodacan","when people claim sable could be a fur in certain jurisdictions","vexilloids","copper","purpure","the number of NYC polling stations","excitement","The pronunciation of “Guyana”","The Portuguese flag","non-Trinitarian Christians","A.C","proper","the College of Arms","the Lord Lyon of Arms","“family crests”","orange","trees","everything and everyone"]

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def hate(ctx)
    channel = ctx.message.channel
    await bot.send_message(channel, "I hate" + random.choice(hates))

@bot.event
async def on_message(message):
    channel = message.channel
    if message.author.id != '92635232607412224':
        if "purple" in message.content or "Purple" in message.content:
            await bot.send_message(channel, ">purple\n\n:nauseated_face:")
        elif "purpure" in message.content or "Purpure" in message.content:
            await bot.send_message(channel, ">purpure\n\n:nauseated_face:")

@bot.event
async def on_message(message):
    channel = message.channel
    if message.author.id == '92635232607412224' and 'like' in message.content:
        await bot.send_message(channel, "Not really, I don't actually like anything.")

@bot.command(pass_context=True)
async def nofun(ctx)
    channel = ctx.message.channel
    await bot.send_file(channel, "nofun.png")

@bot.command(pass_context=True)
async def nazis(ctx)
    channel = ctx.message.channel
    await bot.send_file(channel, "nazis.png")

bot.run('token here')
