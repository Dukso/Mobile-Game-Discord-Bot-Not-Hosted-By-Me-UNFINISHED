import discord
from discord.ext import commands
import asyncio

print("Bot Online!")

PREFIX = '$'
CHANNEL_ID = 'OPTIONAL (sends a message when the Bot becomes online in the channel id)' #replace the channel ID
TIMEOUT = 30  # 2 minutes in seconds
WORLD_1_REACTION = '🔴'

intents = discord.Intents.default()
intents.messages = True
intents = discord.Intents.default()
intents.messages = True
intents.reactions = True  # Replace message_reactions with reactions
intents.message_content = True  # Enable message content intent
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Bot Online And Ready!\nType $MobileGame to start")
    else:
        print("Channel not found.")

@bot.event
async def on_message(message):
    if message.content.startswith(f'{PREFIX}Test'):
        await message.author.send('Success')
        await message.delete()

    await bot.process_commands(message)

@bot.command()
async def MobileGame(ctx):
    # Send the message with the options
    msg = await ctx.send("Pick a world\n"
                         "⚫ World 1\n"
                         "⚪ World 2\n"
                         "🔴 World 3\n"
                         "More Coming Soon")

    # React to the message with emojis
    emojis = ['⚫', '⚪', '🔴']
    for emoji in emojis:
        await msg.add_reaction(emoji)

    # Wait for reactions for 2 minutes
    await asyncio.sleep(TIMEOUT)

    # Get reactions after 2 minutes
    message = await ctx.channel.fetch_message(msg.id)
    reactions = message.reactions

    # Find the most reacted emoji
    most_reacted_emoji = max(reactions, key=lambda r: r.count)

    if most_reacted_emoji.emoji == WORLD_1_REACTION:
        await start_world_1(ctx)

async def start_world_1(ctx):
    # Send world 1 levels
    await ctx.send("Welcome to World 1!\nHere are the levels:")

    levels = [
        "Level 1\nWhich gate?\n🔴 +50 Troops\n🔵 A\n🟡 2X Frenzy (2:00)\n🟤Open Inventory",
        "Level 2\nWhich gate?\n🔴 +149 Troops\n🔵 +96 Troops\n🟡 +(Troops/2)\n🟤 Open Inventory",
        # Add more levels here...
    ]

    for level in levels:
        await ctx.send(level)

    # Send world 1 boss fight description
    boss_fight_desc = ("WORLD 1 BOSS\n\n"
                       "👺\n"
                       "Boss HP\n1000/1000\n\n"
                       "What Do We Do?\n"
                       "🔴 Attack\n🔵 Defend\n🟡 Befriend\n"
                       f"Troops: (Troops)")

    await ctx.send(boss_fight_desc)

# Run the bot with your token
bot.run('BOTTOKENHERE') #MAKE SURE TO KEEP THE '
