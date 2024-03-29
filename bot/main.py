#! venv/bin/python3
"""a little bot for send paom at One houre to Discord Chanell
"""
import logging
from json import loads
from typing import AnyStr, Dict

from discord.ext import commands
from discord import Intents
from requests import get

TOKEN="TOKEN"

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)


logger = logging.getLogger("discord")

logging.basicConfig(level=logging.INFO)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)


def get_random_poem_from_ganjoor() -> Dict:
    content = get("http://c.ganjoor.net/beyt-json.php").content
    json_poem = loads(content)

    m1 = json_poem["m1"]
    m2 = json_poem["m2"]
    return {"m1": m1, "m2": m2, "شاعر": json_poem["poet"]}


def send_poem_for_user() -> AnyStr:
    poem_poet = get_random_poem_from_ganjoor()

    return f"{poem_poet['m1']} // {poem_poet['m2']}\n" f"{poem_poet['شاعر']}\n"


@bot.hybrid_command()
async def poem(ctx):
    await ctx.send(send_poem_for_user())


if __name__ == "__main__":
    bot.run(TOKEN)
