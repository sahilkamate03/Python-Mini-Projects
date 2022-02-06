import requests
import json
r=requests.get('https://codeforces.com/api/user.info?handles=Pravendra_235')
data=json.loads(r.text)
# print(data)
print(f"Status: {data['result'][0]}")
print(f"contribiution: ")
exit()

import discord
from discord.ext import commands
import random
import requests
import json
import datetime

client = commands.Bot(command_prefix='$')


class Social(commands.Cog):

    @client.command()
    async def insta(self, ctx, insta_id):
        '''
          Get info of abt any insta id
        '''
        response = requests.get(
            f"https://api.popcat.xyz/instagram?user={insta_id}")
        data = json.loads(response.text)
        try:
            feed=data['error']
        except:
            feed='clear'

        if feed == 'User not found!':
            embed = discord.Embed(
                title="__**User not found!!**__", colour=discord.Color.red(), timestamp=ctx.message.created_at)
            embed.add_field(name=insta_id, value='Please enter correct id', inline=False)
            await ctx.reply(embed=embed)
            await ctx.message.add_reaction('❌') 

        else:
            embed = discord.Embed(
                title="__**Insta Info**__", colour=discord.Color.purple(), timestamp=ctx.message.created_at)
            embed.set_thumbnail(
                url=data['profile_pic'])
            embed.add_field(name="User_Name", value=data['username'], inline=False)
            embed.add_field(name="Full Name", value=data['full_name'], inline=False)
            embed.add_field(name="Biography", value=data['biography'], inline=False)
            embed.add_field(name="Post", value=data['posts'], inline=False)
            embed.add_field(name="Reels", value=data['reels'], inline=False)
            embed.add_field(name="Follower", value=data['followers'], inline=False)
            embed.add_field(name="Following", value=data['following'], inline=False)
            embed.add_field(name="Private", value=data['private'], inline=False)
            embed.add_field(name="Verified", value=data['verified'], inline=False)
            embed.add_field(name="URL", value=f'https://www.instagram.com/{insta_id}/', inline=False)

            embed.set_footer(
                text=f"Requested by {ctx.author} ",icon_url=ctx.author.avatar_url)

            await ctx.reply(embed=embed)
            await ctx.message.add_reaction('👍') 

    @client.command() 
    async def reddit(self, ctx,search):
        '''
        get subreddit images just type subreddit
        '''
        response = requests.get(
            f"https://memes.blademaker.tv/api/{search}")
        data = json.loads(response.text)
        embed = discord.Embed(
            title='Reddit Page Image', description=data['image'], colour=0xFFFFFF, inline=True, timestamp=ctx.message.created_at)
        embed.set_image(url=data['image'])
        embed.set_footer(
            text=f"Requested by {ctx.author} ", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @client.command(aliases=['cf'])
    async def codeforces(self, ctx, codeforces_id):
        '''
          Get info of abt any codeforce account
        '''
        response = requests.get(
            f"https://codeforces.com/api/user.info?handles={codeforces_id}")
        data = json.loads(response.text)
        try:
            feed=data['status']
        except:
            feed='clear'

        if feed == 'FAILED':
            embed = discord.Embed(
                title="__**User not found!!**__", colour=discord.Color.red(), timestamp=ctx.message.created_at)
            embed.add_field(name=codeforces_id, value='Please enter correct id', inline=False)
            await ctx.reply(embed=embed)
            await ctx.message.add_reaction('❌') 

        else:
            embed = discord.Embed(
                title="__**CodeForces Info**__", colour=discord.Color.purple(), timestamp=ctx.message.created_at)
            embed.set_thumbnail(
                url=data['result'][0]['avatar'])
            embed.add_field(name="User_Name", value=codeforces_id, inline=False)
            embed.add_field(name="Full Name", value=data['result'][0]['firstName']+' '+data['result'][0]['lastName'], inline=False)
            embed.add_field(name="Location", value=data['result'][0]['city']+','+data['result'][0]['country'], inline=False)
            embed.add_field(name="Last Seen", value=str(datetime.timedelta(seconds=data['result'][0]['lastOnlineTimeSeconds'])), inline=False)
            embed.add_field(name="Friends", value=data['result'][0]['friendOfCount'], inline=False)
            embed.add_field(name="Contribution", value=data['result'][0]['contribution'], inline=False)
            embed.add_field(name="Organizarion", value=data['result'][0]['organization'], inline=False)
            embed.add_field(name="Current Rank", value=data['result'][0]['rank'], inline=False)
            embed.add_field(name="Max Rating", value=data['result'][0]['maxRating'], inline=False)
            embed.add_field(name="Max Rank", value=data['result'][0]['maxRank'], inline=False)
            embed.add_field(name="Account Created ", value=str(datetime.timedelta(seconds=data['result'][0]['registrationTimeSeconds'])), inline=False)
            
            embed.add_field(name="URL", value=f'https://codeforces.com/profile/{codeforces_id}/', inline=False)

            embed.set_footer(
                text=f"Requested by {ctx.author} ",icon_url=ctx.author.avatar_url)

            await ctx.reply(embed=embed)
            await ctx.message.add_reaction('👍')

def setup(client):
    client.add_cog(Social(client))