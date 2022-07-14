from email import message
import nextcord
from nextcord import Interaction, SlashOption, ChannelType
from nextcord.abc import GuildChannel
from nextcord.ext import commands
from config import *
import os
import wavelink


intents = nextcord.Intents.all()
client = commands.Bot()
testingServerID = 994219113994014770

@client.slash_command(name="reverser", description="reverses your message", guild_ids=[testingServerID])
async def repeat(interaction : Interaction, message:str):
    await interaction.response.send_message(f"You said '{message[::-1]}")

@client.slash_command(name="bitcounter", description="counts the number of characters in a string", guild_ids=[testingServerID])
async def repeat(interaction : Interaction, message:str):
    await interaction.response.send_message(len(message))

client.run(TOKEN)
