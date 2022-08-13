#from ast import arg
#from asyncore import file_dispatcher
#from http import client
#from unicodedata import name
#from turtle import color
#from turtle import title
#from subprocess import _TXT
#from tokenize import Token
from discord.ext import commands
import os 
import discord
from dotenv import load_dotenv

load_dotenv()


bot=commands.Bot(command_prefix='!')

#use !help



#hackers ignore this because this is modified version of help
bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed=discord.Embed(
        title='Bot Commands',
        description='Some basic info about all the commands and how to use it',
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url='https://avatars.githubusercontent.com/u/70646122?v=4')
    
    embed.add_field(
        name='!nmap',
        value='Used for port scanning just type !nmap with ip address which u want for ex !nmap 127.0.0.1',
        inline=False
    )
    embed.add_field(
        name='!amass',
        value='The OWASP Amass Project performs network mapping of attack surfaces and external asset discovery using open source information gathering and active reconnaissance techniques. For ex !amass example.com',
        inline=False
    )
    embed.add_field(
        name='!subfinder',
        value='Subfinder is a subdomain discovery tool that discovers valid subdomains for websites by using passive online source for ex. !subfinder target.com',
        inline=False
    )

    await ctx.send(embed=embed)
    
# https://www.youtube.com/watch?v=XzcJ4p0R6NY&t=8s used for making help noice




@bot.command()
async def info(ctx):
    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

@bot.command()
async def nmap(ctx,arg):
    '''
    Used for port scanning just type !nmap with ip address which u want for ex !nmap 127.0.0.1
    '''
    #os_level_command_for_nmap = os.popen("nmap -sV "+arg+" -oN prety.txt")
    os_level_command_for_nmap = subprocess.run(["nmap","-sV","-oN","nmap.txt",f"{arg}"],capture_output=True)

   # output = os_level_command_for_nmap.read()
    await ctx.send("Your result:- \n")
    await ctx.send(file=discord.File("prety.txt"))
#thanks vikran 

@bot.command()
async def amass(ctx,arg):
    '''
    The OWASP Amass Project performs network mapping of attack surfaces and external asset discovery using open source information gathering and active reconnaissance techniques.
    For ex : !amass example.com
 
    '''
    #os_level_command_for_amass=os.popen("amass enum -v -src -ip -brute -min-for-recursive 2 -share -d "+arg+" -oA amass_result.txt" )
    os_level_command_for_amass=subprocess.run(["amass","enum","-v","-src","-ip","-brute","-min-for-recursive","2","-share","-d",f"{arg}","-oA","amass_result.txt"],capture_output=True)
    #output = os_level_command_for_amass.read()
    await ctx.send("Your result:- \n")
    await ctx.send(file=discord.File("amass_result.txt.txt"))

@bot.command()
async def subfinder(ctx,arg):
    os_level_command_for_subfinder=os.popen("subfinder -d "+arg+" -o subfinder.txt")
    output = os_level_command_for_subfinder.read()
    await ctx.send("Your result:- \n")
    await ctx.send(file=discord.File("subfinder.txt"))
   
@bot.command()
async def superscript(ctx,arg):
    #if u want to use this then uncomment
    os_level_command_for_superscript=os.popen("./super.sh "+arg+"")
    output=os_level_command_for_superscript.read()
    await ctx.send("I am still working on this feature ")
    await ctx.send("Your result:- \n")
    await ctx.send("Here comes the subdomains file")
    await ctx.send(file=discord.File("subdomains.txt"))
    await ctx.send("Here comes waybackurls file")
    await ctx.send(file=discord.File("waybackurls.txt"))
    await ctx.send("Your httpx file ")
    await ctx.send(file=discord.File("httpx.txt"))
    await ctx.send(file=discord.File("ip.txt"))
    await ctx.send(file=discord.File("nmap.txt"))
    
   # await ctx.send(file=discord.File("nmap.txt"))
#send hosts.txt , subdomains.txt , waybackurls.txt , nmap.txt , httpx.txt


    
#@bot.command()
#async def amass(ctx,arg):

bot.run(os.getenv('TOKEN'))
