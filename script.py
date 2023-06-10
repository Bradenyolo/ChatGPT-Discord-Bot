import discord
from discord.ext import commands
import openai
import time

try:
    prefix = "/"

    permissions = discord.Permissions(3072)

    openai.api_key = "hey bro you sneaking up on my chatgpt api key? 😏"

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix=prefix, intents=intents, permissions=permissions)

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user.name} ({bot.user.id})")

    @bot.event
    async def on_message(message):
        if not message.author.bot:
            await bot.process_commands(message)

    @bot.command()
    async def chatgpt(ctx, *, message):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": message}],
            max_tokens=2000,
            temperature=0.7,
            n=1,
            stop=None
        )
        assistant_message = response.choices[0].message
        assistant_text = assistant_message["content"]
        
        embed = discord.Embed(description=assistant_text)
        embed.set_footer(text="Generated by ChatGPT")

        await ctx.send(embed=embed)
        # await ctx.send(assistant_text)
        print(f"ChatGPT responded: \n{assistant_text}")
    bot.run("ayo what are u doing with my code bruh?! dont leak my token to the internet!!!")
except Exception as e:
    print("The bot encountered an error. Review this error:", e)
    time.sleep(60)
