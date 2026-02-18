import discord
from discord.ext import commands
from discord import app_commands
import datetime

LOG_KANAL_ID = 1471654919034638447  # log kanal ID

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

GUILD_ID = 1471123727776350350
OTOROL_ID = 1471161213131165718


@bot.event
async def on_ready():
    guild = discord.Object(id=GUILD_ID)
    bot.tree.copy_global_to(guild=guild)
    await bot.tree.sync(guild=guild)
    print(f'Bot aktif: {bot.user}')

# HOŞGELDİN

@bot.event
async def on_member_join(member):
    # hoşgeldin mesajı
    kanal = member.guild.system_channel
    if kanal:
        await kanal.send(f"Hoşgeldin {member.mention}! 🎉")

    # otorol
    rol = member.guild.get_role(OTOROL_ID)
    if rol:
        await member.add_roles(rol)

# OTOMATİK CEVAPLAR
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if content.startswith("sa"):
        await message.channel.send(f"as {message.author.mention}")

    elif content.startswith("aferin"):
        await message.channel.send("miyav :3")

    elif content.startswith("günaydın") or content.startswith("gunaydin"):
        await message.channel.send(f"günaydın {message.author.mention}")

# MESAJ SİL
@bot.tree.command(name="sil", description="Mesaj siler")
@app_commands.describe(miktar="Silinecek mesaj sayısı")
async def sil(interaction: discord.Interaction, miktar: int):
    await interaction.channel.purge(limit=miktar)
    await interaction.response.send_message(f"{miktar} mesaj silindi.", ephemeral=True)

# KICK
@bot.tree.command(name="kick", description="Kullanıcıyı sunucudan atar")
async def kick(interaction: discord.Interaction, uye: discord.Member):
    await uye.kick()
    await interaction.response.send_message(f"{uye} sunucudan atıldı.")

    log = bot.get_channel(LOG_KANAL_ID)
    if log:
        await log.send(f"👢 {uye} kicklendi | Yetkili: {interaction.user}")

# BAN
@bot.tree.command(name="ban", description="Kullanıcıyı banlar")
async def ban(interaction: discord.Interaction, uye: discord.Member):
    await uye.ban()
    await interaction.response.send_message(f"{uye} banlandı.")

    log = bot.get_channel(LOG_KANAL_ID)
    if log:
        await log.send(f"🔨 {uye} banlandı | Yetkili: {interaction.user}")

# MUTE
@bot.tree.command(name="mute", description="Kullanıcıyı süreli susturur")
@app_commands.describe(dakika="Susturma süresi (dakika)")
async def mute(interaction: discord.Interaction, uye: discord.Member, dakika: int):
    sure = datetime.timedelta(minutes=dakika)
    await uye.timeout(sure)
    await interaction.response.send_message(f"{uye.mention} {dakika} dakika susturuldu.")

    log = bot.get_channel(LOG_KANAL_ID)
    if log:
        await log.send(f"🔇 {uye} {dakika} dakika mute aldı | Yetkili: {interaction.user}")

# KANAL KİLİTLE
@bot.tree.command(name="kilitle", description="Kanalı kilitler")
async def kilitle(interaction: discord.Interaction):
    await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=False)
    await interaction.response.send_message("Kanal kilitlendi.")

# KANAL AÇ
@bot.tree.command(name="ac", description="Kanalı açar")
async def ac(interaction: discord.Interaction):
    await interaction.channel.set_permissions(interaction.guild.default_role, send_messages=True)
    await interaction.response.send_message("Kanal açıldı.")

# EĞLENCE KOMUTLARI

import random

@bot.tree.command(name="zar", description="1-6 arası zar atar")
async def zar(interaction: discord.Interaction):
    sonuc = random.randint(1, 6)
    await interaction.response.send_message(f"🎲 Zar sonucu: **{sonuc}**")

@bot.tree.command(name="8ball", description="Soru sor, cevap versin")
async def eightball(interaction: discord.Interaction, soru: str):
    import random

    cevaplar = [
        "Evet",
        "Hayır",
        "Büyük ihtimalle",
        "Şu an belli değil",
        "Kesinlikle",
        "Tekrar dene"
    ]

    cevap = random.choice(cevaplar)

    await interaction.response.send_message(
        f"❓ Sorulan soru: {soru}\n🔮 Cevap: {cevap}"
    )

@bot.tree.command(name="saka", description="Rastgele şaka yapar")
async def saka(interaction: discord.Interaction):
    import random

    sakalar = [
        "Arkadaş: 5 dakikaya geliyorum. Tarihçiler: Hangi 5 dakika?",
        "Telefon şarjı %1 olunca insanın bütün hayat kararları değişiyor.",
        "Alarmı erteleye erteleye artık alarm bana güvenmiyor.",
        "Bugün erken yatacağım dedim, internet güldü.",
        "Cüzdanım o kadar sessiz ki içinde meditasyon yapılıyor.",
        "Ben diyetteyim ama yemekler beni bırakmıyor.",
        "Uyku düzenim yok, uyku bana misafir geliyor.",
        "Motivasyonum var ama çalışmaya gelmedi.",
        "Param yok ama harcama isteğim CEO seviyesinde.",
        "Plan yapıyorum, hayat 'bakalım' diyor.",
        "Telefonu elimden bıraksam hayatım düzelecek ama elim bırakmıyor.",
        "Ben sorun değilim, internet yavaş.",
        "Ders çalışmaya başladığım an bütün ev ilginç gelmeye başlıyor.",
        "İnsan bazen hiçbir şey yapmadan yorulabiliyormuş, test edildi.",
        "Haftaya başlıyorum dediğim şeyler efsane oldu.",
        "Uyku: gel. Sorumluluklar: hayır.",
        "Markete sadece ekmek almaya girip 300 lira bırakmak modern çağ olayıdır.",
        "Kafamda kurduğum senaryolar Netflix bütçesini geçer.",
        "Bugün çok üretken olacağım dedim, sonra oturdum.",
        "Telefonu sessize alıyorum, hayat da beni sessize alıyor.",
        "Ben zengin olacağım ama ekonomi spoiler veriyor.",
        "İnternet kesilince hayatın ne kadar boş olduğunu fark etmek.",
        "Diyet yarın başlar, yarın da yarın başlar.",
        "Planım var ama uygulama kısmı beta sürüm.",
        "İnsan bazen hiçbir şey yapmadan da mola vermek ister.",
        "Uyumadan önce telefonu bırakacağım dedim, telefon bırakmadı.",
        "Sabah erken kalkacağım diyen gece versiyonuma güvenim yok.",
        "Ben değilim, pazartesi suçlu.",
        "Bir şey yapmaya niyetlenince koltuk 'otur konuşalım' diyor.",
        "Hayat zor değil, sadece sürekli güncelleme geliyor."
    ]

    await interaction.response.send_message(random.choice(sakalar))
    
@bot.tree.command(name="slot", description="Slot makinesi çevirir")
async def slot(interaction: discord.Interaction):
    import random
    import asyncio

    semboller = ["🍒", "🍋", "🍉", "⭐", "💎"]

    await interaction.response.send_message("🎰 Dönüyor...")
    mesaj = await interaction.original_response()

    # animasyon (fake dönüş)
    for _ in range(5):
        fake = [random.choice(semboller) for _ in range(3)]
        await mesaj.edit(content="🎰 " + " | ".join(fake))
        await asyncio.sleep(0.5)

    # gerçek sonuç
    sonuc = [random.choice(semboller) for _ in range(3)]
    sonuc_yazi = " | ".join(sonuc)

    if sonuc[0] == sonuc[1] == sonuc[2]:
        final = f"🎰 {sonuc_yazi}\nJACKPOT! Büyük kazandın!"
    elif sonuc[0] == sonuc[1] or sonuc[1] == sonuc[2] or sonuc[0] == sonuc[2]:
        final = f"🎰 {sonuc_yazi}\nKüçük kazanç!"
    else:
        final = f"🎰 {sonuc_yazi}\nBu sefer olmadı."

    await mesaj.edit(content=final)

class TKMView(discord.ui.View):
    def __init__(self, player1, player2):
        super().__init__(timeout=60)
        self.player1 = player1
        self.player2 = player2
        self.choices = {}

    async def check_winner(self, interaction):
     if len(self.choices) == 2:
            p1 = self.choices[self.player1]
            p2 = self.choices[self.player2]

            if p1 == p2:
                sonuc = "Berabere!"
            elif (p1 == "Taş" and p2 == "Makas") or \
                 (p1 == "Kağıt" and p2 == "Taş") or \
                 (p1 == "Makas" and p2 == "Kağıt"):
                sonuc = f"Kazanan: {self.player1.mention}"
            else:
                sonuc = f"Kazanan: {self.player2.mention}"

            await interaction.message.edit(
                content=f"{self.player1.mention}: {p1}\n{self.player2.mention}: {p2}\n\n{sonuc}",
                view=None
            )

    @discord.ui.button(label="Taş", style=discord.ButtonStyle.primary)
    async def tas(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user not in [self.player1, self.player2]:
            await interaction.response.send_message("Bu oyunda değilsin.", ephemeral=True)
            return
        self.choices[interaction.user] = "Taş"
        await interaction.response.defer()
        await self.check_winner(interaction)

    @discord.ui.button(label="Kağıt", style=discord.ButtonStyle.success)
    async def kagit(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user not in [self.player1, self.player2]:
            await interaction.response.send_message("Bu oyunda değilsin.", ephemeral=True)
            return
        self.choices[interaction.user] = "Kağıt"
        await interaction.response.defer()
        await self.check_winner(interaction)

    @discord.ui.button(label="Makas", style=discord.ButtonStyle.danger)
    async def makas(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user not in [self.player1, self.player2]:
            await interaction.response.send_message("Bu oyunda değilsin.", ephemeral=True)
            return
        self.choices[interaction.user] = "Makas"
        await interaction.response.defer()
        await self.check_winner(interaction)


@bot.tree.command(name="tkm", description="Bir kullanıcıyla taş kağıt makas oynarsın")
async def tkm(interaction: discord.Interaction, rakip: discord.Member):
    view = TKMView(interaction.user, rakip)
    await interaction.response.send_message(
        f"{interaction.user.mention} vs {rakip.mention}\nSeçimlerinizi yapın!",
        view=view
    )


import os
bot.run(os.getenv("TOKEN"))
