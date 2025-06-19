import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import requests
from config import DISCORD_TOKEN, CHANNEL_ID, CMC_BASE_URL, HEADERS
from commands.ping import ping
from src.commands.price import price

load_dotenv()
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

bot.add_command(ping)
bot.add_command(price)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    await bot.get_channel(CHANNEL_ID).send("🚀 Crypto Analysis Bot is online!")
    crypto_analysis_loop.start()

@tasks.loop(minutes=60)
async def crypto_analysis_loop():
    try:
        channel = bot.get_channel(CHANNEL_ID)
        response = requests.get(f"{CMC_BASE_URL}/cryptocurrency/listings/latest?limit=10", headers=HEADERS)
        data = response.json()
        message = "\n**📊 Top 10 Crypto Update (Hourly)**\n\n"
        for coin in data['data']:
            symbol = coin['symbol']
            price = float(coin['quote']['USD']['price'])
            change = coin['quote']['USD']['percent_change_24h']
            emoji = "📈" if change > 0 else "📉"
            message += f"{emoji} **{symbol}**: ${price:.2f} ({change:.2f}%)\n"
        await channel.send(message)
    except Exception as e:
        print(f"Error in analysis loop: {e}")

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
