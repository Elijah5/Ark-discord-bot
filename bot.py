import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import json
import os
import re
import time
import discord.utils
from ahk import AHK

ahk = AHK()

#---Prefix Dict---#
defaultPrefix = '$'
prefixDict = {}


#---Get Prefix---#
async def get_pre(bot, message):
    ###Create a dict entry if there isnt one###
    if len(prefixDict) > 0:
        guildID = str(next(iter(prefixDict)))
        return prefixDict[guildID]

        try:
            dictRead = open("prefixDict.json", "r")
            dictRead.read(dictFile)
            print(guildID + "This Guild already has an entry")
            dictRead.close()

        except:
            dictRead = open("prefixDict.json", "r")
            dictRead.read(dictFile)
            dictRead.close()
            print("This Guild has no entry... Appending the default prefix")
            dictWrite = open("prefixDict.json", "w")
            dictWrite.write(dictFile)

            dictWrite.close()

###If there is no server set prefix, return defaultPrefix###
    else:
        return [defaultPrefix]


#---Discord.py Def---#
bot = commands.Bot(command_prefix=get_pre)


#---Print When Ready---#
@bot.event
async def on_ready():
    print("-----------------------------------------------")
    print("Bot Is Online!")
    print("-----------------------------------------------")
    await bot.change_presence(activity=discord.Game(name='$help'))


#---Ping delay test---#
@bot.command()
async def ping(ctx):
    latency = (bot.latency)
    msLatency = latency * 1000
    strLatency = str(msLatency)
    roundLatency = strLatency[0:5]
    await ctx.send("Pong! `(" + roundLatency + " ms)`")


#---Set Prefix---#
@bot.command()
@has_permissions(administrator=True)
async def prefix(ctx, prefix):
    if len(prefix) > 3:
        await ctx.send(
            "Usage: \n ```>prefix <prefix> \n Note: prefix can take 3 characters only.```"
        )
    else:
        setPrefix = prefix
        guildID = str(ctx.guild.id)
        prefixDict[guildID] = [setPrefix, defaultPrefix]
        await ctx.send("Prefix set to `" + setPrefix + ("` \n `") + setPrefix +
                       ("help`"))

        dictFile = json.dumps(prefixDict)
        f = open("prefixDict.json", "w")
        f.write(dictFile)
        f.close()


@bot.command()
async def clayton(ctx):
    claytonid = '<@479374887450836992>'
    await ctx.send("Shut up Clayton " + claytonid)

@bot.command()
@commands.has_role('Ark')
async def servercycle(ctx):
    await ctx.send("```Please make sure the server is offline before running this command \n \n" + "If the server is offline, type confirm in the next 15 seconds \n \n GIVE THE SERVER UP TO 15min TO BOOT AND WAIT 5min INBETWEEN COMMANDS```")

    def check(m):
        return m.content == 'confirm'

    await bot.wait_for('message', timeout=15.0, check=check)
    await ctx.send("Confirmed")
    serverStart = True

    if serverStart == True:
        ahk.click(634, 485)
        time.sleep(5)
        ahk.click(634, 485)
        time.sleep(10)
        ahk.click(780, 405)
        time.sleep(75)
        ahk.click(772, 390)
        time.sleep(5)
        serverStart = False


#---Stop Bot Command---#
@bot.command()
async def stop(ctx):
    ###Only Allow Authorized Users to Stop the Bot###
    if ctx.message.author.id == (
            420437587413434369) or ctx.message.author.id == (
                547092292121657344):
        await ctx.send("Stopping!")
        exit()
    ###If Not Authorized, Let Them Know!###
    else:
        await ctx.send("You are not authorized to use stop!")


#---Discord Bot API Token---#
bot.run("")
