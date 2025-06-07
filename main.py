import os import discord from discord.ext import commands, tasks import datetime

Setup environment variables

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN") BOT_PREFIX = "!"

Setup intents

intents = discord.Intents.default() intents.message_content = True

Setup bot

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

=== AI John & Alpha System ===

@bot.event async def on_ready(): print(f"✅ Bot aktif sebagai {bot.user.name}") channel_id = os.getenv("DISCORD_CHANNEL_ID") if channel_id: channel = bot.get_channel(int(channel_id)) if channel: await channel.send("🤖 AI John & Alpha telah dihidupkan dan bersedia menghantar alert 24/7!") hourly_alert.start() four_hour_alert.start() daily_analysis.start() weekly_analysis.start() monthly_analysis.start()

=== Command Biasa ===

@bot.command() async def john(ctx): await ctx.send("👋 Hai! Saya AI John, penganalisis utama pasaran crypto dan pelaburan jangka panjang.")

@bot.command() async def alpha(ctx): await ctx.send("🧠 Saya AI Alpha – saya bertugas beri pandangan berbeza dan analisis risiko untuk pastikan strategi John tidak berat sebelah.")

@bot.command() async def analisis(ctx): await ctx.send("📊 John: Berdasarkan trend semasa, pasaran menunjukkan sokongan stabil sekitar $100K.") await ctx.send("📉 Alpha: Waspada kemungkinan penurunan mengejut jika volume beli tidak kekal dalam 48 jam.")

@bot.command() async def status(ctx): await ctx.send("🔎 Sistem John & Alpha berfungsi dengan baik. Sedia untuk arahan baru.")

=== Alert Automatik ===

@tasks.loop(minutes=60) async def hourly_alert(): channel = bot.get_channel(int(os.getenv("DISCORD_CHANNEL_ID"))) if channel: await channel.send("⏰ Alert 1H: Data teknikal sedang dikemas kini oleh JohnAI.")

@tasks.loop(hours=4) async def four_hour_alert(): channel = bot.get_channel(int(os.getenv("DISCORD_CHANNEL_ID"))) if channel: await channel.send("🔁 Alert 4H: Pemantauan semula pasaran dilakukan.")

@tasks.loop(hours=24) async def daily_analysis(): channel = bot.get_channel(int(os.getenv("DISCORD_CHANNEL_ID"))) if channel: await channel.send("📅 1D Analysis: Perubahan trend harian sedang diproses oleh AI John & Alpha.")

@tasks.loop(hours=24 * 7) async def weekly_analysis(): channel = bot.get_channel(int(os.getenv("DISCORD_CHANNEL_ID"))) if channel: await channel.send("📈 1W Analysis: Laporan mingguan JohnAI sedang dijana.")

@tasks.loop(hours=24 * 30) async def monthly_analysis(): channel = bot.get_channel(int(os.getenv("DISCORD_CHANNEL_ID"))) if channel: await channel.send("📊 1M Analysis: Sorotan bulanan pasaran telah dimulakan.")

Jalankan bot

bot.run(DISCORD_TOKEN)


