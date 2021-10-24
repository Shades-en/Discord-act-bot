import datetime as dt
import discord
from discord import guild
from discord.activity import Spotify
from discord.ext import commands
from discord.flags import Intents
from datetime import datetime 


intents=discord.Intents.all()
token="ODYyNzE2MDI5MTgzNTkwNDUw.YOcY6Q.aqScrYDIDkMPJStzyGky1fPi92Q"
client = commands.Bot(command_prefix=".",intents=intents)

@client.event
async def on_ready():
    print("bot is ready")

@client.command()
async def active(ctx,member:discord.Member):
    current=member.activities
    active=["ActivityType.playing","ActivityType.listening"]
    y=[]
    for i in active:
        z=y
        y=[x.name for x in current if str(x.type)==i] 
        u=[[x.title,x.artist] for x in current if str(x.type)=="ActivityType.listening"]
    
    print(f"Playing~ \n{', '.join(z)}") if z!=[] else print("Playing~ None")
    print("\n")
    print(f"Listening~ {', '.join(y)}") if y!=[] else print("Listening~ None")
    if u!=[]:
        print(f"song ~ {u[0][0]} \nartist ~ {u[0][1]}")
    
@client.command()
async def players(ctx,*,game):
    members=ctx.guild.members
    n=0
    member_list=["names"]
    for member in members:
        if member.bot is False:
            for activity in member.activities:
                if str(activity.type)!="ActivityType.custom" and game.upper()==activity.name.upper():
                    n+=1
                    print(f"{n}. {member.name}")
                    member_list.append(member.name)
    if n==0:
        print("No person found with the activity mentioneed")

    print("To invite them use (invite @mention) or (invite all)")

    channel=ctx.channel
    def check(m):
            return m.content and m.channel == channel

    msg=await client.wait_for("message",check=check)
    print(msg.created_at)

    if msg.content.lower()=="invite all":
        for member in members:
            for name in member_list:
                if member.name==name:
                    await member.send(f"{ctx.author} has invited you to play {game}")
        print("invite sent!")

    else:
        for i in msg.mentions:
            await i.send(f"{ctx.author} has invited you to play {game}")
        print("invite sent!")


@client.command()  
async def duration(ctx,member:discord.Member):
    current=member.activities
    for activity in current:
        if str(activity.type)!="ActivityType.custom":
            x1=str(datetime.now(dt.timezone.utc))
            x=datetime.fromisoformat(x1[:-6])
            y=(activity.start)
            if y!=None:
                print(activity.name,f"~ {x-y}")
    

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        print("Member Not Found")

            

           



            


    


client.run(token)
