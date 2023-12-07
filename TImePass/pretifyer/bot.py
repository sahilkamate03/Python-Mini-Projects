import discord
from discord.ext import commands
import requests
import json
import datetime
import time
import random
import wikipedia

client = commands.Bot(command_prefix='$')


def developer(ctx):
    return ctx.author.id == 866933932222185492


class Utility(commands.Cog):

    @client.command()
    async def ping(self, ctx):
        start = time.perf_counter()
        message = await ctx.send("‎")
        end = time.perf_counter()
        duration = (end - start) * 1000
        embed = discord.Embed(
            title="__**Latency**__", colour=discord.Color.dark_gold(), timestamp=ctx.message.created_at)
        embed.add_field(name="Latency of bot :",
                        value=f"`{round(duration)} ms`")
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @client.command()
    async def dict(self, ctx, *, search):
        response = requests.get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{search}")
        data = json.loads(response.text)
        embed = discord.Embed(timestamp=ctx.message.created_at,
            title='Dictionary', description='Ask me any word meaning.', inline=False)
        embed.colour = 0xFFFFFF  # can be set in 'discord.Embed()' too
        # embed.set_image(url='' )
        embed.set_thumbnail(
            url='https://cdn.pixabay.com/photo/2014/03/25/16/34/owl-297413_960_720.png')
        embed.set_footer(
            text=f"Requested by {ctx.author} ", icon_url=ctx.author.avatar_url)
        # embed.set_author(
        #     name=ctx.author, url="https://discordapp.com", icon_url=ctx.author.avatar_url)
        try:
            embed.add_field(
                name=f"Word Not Found: {search}", value=data['title'], inline=False)
        except:
            pass

        try:
            embed.add_field(name="Word", value=data[0]['word'], inline=False)
            embed.add_field(name="Part of speech",
                            value=data[0]["meanings"][0]['partOfSpeech'], inline=False)
            embed.add_field(
                name="Origin", value=data[0]['origin'], inline=False)

            embed.add_field(
                name="Meaning 1", value=data[0]["meanings"][0]['definitions'][0]['definition'], inline=False)
            # embed.add_field(name="Synonyms", value=data[0][ "meanings"][0]['definitions'][0]['synonyms'])
            # embed.add_field(name="Antonyms", value=data[0][ "meanings"][0]['definitions'][0][''])
            embed.add_field(
                name="Example", value=data[0]["meanings"][0]['definitions'][0]['example'], inline=False)
        except:
            await ctx.send(f'No word found: {search}')

        try:
            embed.add_field(
                name="Meaning 2", value=data[0]["meanings"][0]['definitions'][1]['definition'], inline=False)
            embed.add_field(
                name="Example", value=data[0]["meanings"][0]['definitions'][1]['example'], inline=False)
        except:
            pass
        await ctx.send(embed=embed)

    @client.command()
    async def wiki(self, ctx,*,query):
        embed = discord.Embed(
            title="Wiki Summary", colour=discord.Color.dark_gold(), timestamp=ctx.message.created_at)
        summary=wikipedia.summary(query)
        first, second = summary[:len(summary)//2], summary[len(summary)//2:]
        embed.add_field(name=f"Summary of {query}",value=f"{first}")
        embed.add_field(name="‎",value=f"{second}")
        image=wikipedia.page(query).images
        embed.set_image(url=random.choice(image))
        info=wikipedia.page(query).url
        embed.set_footer(
            text=f"{info} \n Requested by {ctx.author} at {datetime.datetime.now()}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        
    @client.command(name='Translate',aliases=['trans','t'])
    async def traslate(self, ctx,*,query):
        response = requests.get(
            f"https://api.popcat.xyz/translate?to=en&text={query}")
        data = json.loads(response.text)
        embed = discord.Embed(
            title="__**Translate**__", colour=discord.Color.dark_gold(), timestamp=ctx.message.created_at)
        embed.add_field(name="from",value=query)
        embed.add_field(name="to",value=data[translated])
        await ctx.send(embed=embed)

