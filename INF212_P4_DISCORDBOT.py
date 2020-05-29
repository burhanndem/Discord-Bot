import discord

client = discord.Client()

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD')

channels = ["cmds", "genel"]
valid_users = ["Burhan//NewBaron//22#6767", "velevkinoname#6912", "Mamadou™#1193", "safa#7371","Griffin#1430"]
id = client.get_guild(659442099409780746)


@client.event
async def on_ready():
    global guild

    for guild in client.guilds:
        if guild.name == GUILD:
            print("BURDAAAAAYIIIIM :D")
            break

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) in channels:
            await channel.send(f"""ojjgeldiniiz {member.mention}""")
    await member.send(f'hoşgeldiin {member.name}! ')
    print(
        f'{member.name} de geldigine goree...''\n'
        'Logged in as' + " " + f'{member.name}'
    )

# @client.event
# async def on_guild_role_update(before, after):

@client.event
async def on_message(message):
    if str(message.channel) in channels and str(message.author) in valid_users:
        with open("greets.txt", 'r') as f:
            for word in f.read().split(" "):
                if message.content.count(word) > 0:
                    await message.channel.send("marabana maraba")
        with open("bad_words.txt", 'r') as f:
            for word in f.read().split(" "):
                if message.content.count(word) > 0:
                    await message.channel.send("hemen temizliyorum abijjiim")
                    await message.channel.purge(limit=2)
        if message.content == "!users":
            await message.channel.send(f"oda mevcudu: {guild.member_count}")
        elif message.content == "!help":
            embed = discord.Embed(title="bir takım şeyler", description="useful commands tarzında")
            embed.add_field(name="!hello", value="sa as")
            embed.add_field(name="!users", value="sınıf mevcudu")
            embed.add_field(name="!clear", value="temizlemece")
            embed.add_field(name="!beniöv", value="öv anam öv")
            await message.channel.send(content=None, embed=embed)
        elif message.content.startswith('++'):
            await message.channel.send("bence de")
        elif message.content.startswith('seni siksem iyi'):
            embed = discord.Embed(color=0xbe1919)
            embed.set_image(url="https://i.hizliresim.com/GB402Z.jpg")
            await message.channel.send(embed=embed)
        elif message.content.startswith('!lose'):
            await message.channel.send("Mahmut Safa BULAT 141024051"+"\n"+"Abdurrahman Cercis UYSAL 141024070"+"\n""Burhan DEMİRTAŞ 151024055 ")
        elif message.content == "!beniöv":
            await message.channel.send("gardaşım sen bitanesin gardaşım")
        elif message.content.startswith('!clear'):
            await message.channel.send('abi cöp varsa aliyim..') and await message.channel.purge()
        elif message.content.count("?") > 0:
            await message.channel.send("why not abi")
        with open("call.txt", 'r') as f:
            for word in f.read().split(" "):
                if message.content.count(word) > 0:
                    embed = discord.Embed(color=0xbe1919)
                    embed.set_image(url="https://cdn.discordapp.com/attachments/661256921671794726/715592560260939836/0fefb1d9874c71ae19e8bb3d64604b0d.png")
                    await message.channel.send(embed=embed)

client.run(TOKEN)
