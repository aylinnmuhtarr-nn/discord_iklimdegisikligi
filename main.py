import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
#1
@bot.command()
async def iklim_değişikliğinin_sebebleri(ctx):
    await ctx.send("""*İklim değişikliğinin başlıca sebepleri şunlardır*:
        • Fosil yakıtların kullanılması
        • Fabrika ve araçlardan çıkan gazlar
        • Ormanların yok edilmesi
        • Tarım ve hayvancılık faaliyetleri""")

#2
@bot.command()
async def cevre_kirliligi_türleri(ctx):
    await ctx.send ("""*Çevre kirliliği türleri*:
        • Hava kirliliği
        • Su kirliliği 
        • Toprak kirliliği
        • Plastik atıklar
        • Kimyasal maddeler""")
 #3   
@bot.command()
async def iklim_değişikliğinin_karsisini_almak(ctx):
    await ctx.send("""Çevre Kirliliğinin karşısını almak
        • Yenilenebilir enerji kullanmak
        • Ağaç dikmek
        • Plastik kullanımını azaltmak
        • Toplu taşıma kullanmak 
        • Enerji tasarrufu yapmak""")
#4
@bot.command()
async def kuresel_sorunlar(ctx):
    await ctx.send("""*Küresel Sorunlar:*"
        • İklim değişikliği
        • Küresel ısınma
        • Su kıtlığı
        • Biyoçeşitliliğin azalması
        • Deniz seviyesinin yükselmesi""")
#5
@bot.command()
async def kuresel_isinma(ctx):
    await ctx.send("""*Küresel Isınma Nedir?*
        • Atmosferdeki sera gazlarının artması sonucu 
        • Dünya’nın ortalama sıcaklığının yükselmesidir.""")
    
@bot.command()
async def dunya_durumu (ctx):
    await ctx.send(
        "🌍 Dünyanın şuanki durumu:\n"
        "Sıcaklık: 🔥🔥🔥⚪⚪\n"
        "Su: 💧💧💧⚪⚪\n"
        "Doğa: 🌳🌳⚪⚪⚪"
    )


@bot.command()
async def iklim_test(ctx):
    await ctx.send(" Plastik kullanıyor musun? (evet / hayır)")

    def check(m):
        return m.author == ctx.author

    cevap = await bot.wait_for("message", check=check)

    if cevap.content.lower() == "evet":
        await ctx.send("❌ Mümkünse azaltmaya çalış.")
    else:
        await ctx.send("✅ Harika! Böyle devam et.")

@bot.event
async def on_message(message):
    
    if message.author.bot:
        return

    
    if not message.content.startswith("*"):
        await message.channel.send(
            " Böyle bir komut bulunamadı.\n"
            " *Not*! : Mesajın başına * işaretini yazmayı unutmuş olabilirsiniz."
        )

    # Diğer komutların çalışması için gerekli
    await bot.process_commands(message)

bot.run("")