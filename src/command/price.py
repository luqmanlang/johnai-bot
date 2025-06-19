import requests
from discord.ext import commands
from src.config import CMC_API_KEY, CMC_BASE_URL, HEADERS

@commands.command()
async def price(ctx, symbol: str):
    try:
        response = requests.get(f"{CMC_BASE_URL}/cryptocurrency/quotes/latest?symbol={symbol.upper()}", headers=HEADERS)
        data = response.json()
        coin = data['data'][symbol.upper()]
        price = coin['quote']['USD']['price']
        await ctx.send(f"💰 {symbol.upper()} is currently **${price:.2f}**")
    except Exception as e:
        await ctx.send("❌ Failed to fetch price. Check symbol or API status.")
        print(e)
