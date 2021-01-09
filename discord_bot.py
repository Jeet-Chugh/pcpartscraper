import discord
from pcpartscraper.scraper import Part,Query

client = discord.Client()

@client.event
async def on_ready():
    print('PC Part Bot has started Running......'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:  return
    elif message.content.startswith(('pc.link','pc.search','pc.find','pc.part')):
        try:
            if message.content.startswith(('pc.link','pc.part')):
                part_url = message.content.replace('pc.link ','').replace('pc.part ','')
                if not part_url.startswith('/product/'):
                    part_url = part_url.replace('https://','').replace('www.','')
                    part_url = part_url.replace('pcpartpicker.com','')
                part = Part(part_url)
            elif message.content.startswith(('pc.search','pc.find')):
                search_term = message.content.replace('pc.search ','').replace('pc.find ','')
                part = Query(search_term+'+-OEM',2,1,True)
                try:
                    if part[0].type() == 'CPU' and len(part) == 2:
                        part = part[1]
                    else:  part = part[0]
                except:  part == None
            if part == None:
                await message.channel.send("Uh-Oh! No Parts Matched your URL. Type pc.help if you need more information.")
                return
            await message.channel.send("__Name: '{}'__".format(part.name()))
            await message.channel.send("**Category:** '{}'".format(part.type()))
            if part.price() != None:
                await message.channel.send("**Price: ${}**".format(str(part.price())))
            elif part.rating() != None:
                await message.channel.send("**Rating:** {}/5".format(part.rating()))
            try:
                await message.channel.send("__Top Review:__\n*{}*".format(part.reviews(1)[0]))
            except:
                await message.channel.send("**No Reviews Found**")
            await message.channel.send(embed=discord.Embed(title='pcpartpicker.com Link',url=part.url(),description='View {} on pcpartpicker.com'.format(part.name())))
            if part.amazon_link() != None:
                await message.channel.send(embed=discord.Embed(title='Amazon Link',url=part.amazon_link(),description='Buy {} on Amazon.com'.format(part.name())))
            await message.channel.send("__Advanced Specifications:__")
            advanced_info = part.advanced_specs()
            for key in advanced_info:
                await message.channel.send("**{}**: *{}*".format(key,advanced_info[key]))
            await message.channel.send("Search for {} Complete!".format(part.name()))
        except:
            await message.channel.send('**Part Error: Stopping Search**')
            return
    elif message.content.startswith('pc.help'):
        await message.channel.send("__Help Menu:__")
        await message.channel.send("**All Bot Commands:** 'pc.commands'")
        await message.channel.send("**Credits:** 'pc.credits'")
        await message.channel.send("**License/Code:** 'pc.code'")
        return

    elif message.content.startswith('pc.commands'):
        await message.channel.send("Commands:")
        await message.channel.send("**pc.** is the universal prefix for referencing PC Part Bot. You can not change the prefix.")
        await message.channel.send("**'pc.search'** or **'pc.find'** = Search for a Part with keywords\nExample: **'pc.search ryzen 5'** would return info on a search for a ryzen 5")
        await message.channel.send("**'pc.link'** or **'pc.part'** = Search for a Part with a pcpartpicker.com URL\nExample: **'pc.link pcpartpicker.com/product/id/part_name'** would return info on that part")
        await message.channel.send("Remember: **'pc.search'** and **'pc.find'** are the same commands. **'pc.link'** and **'pc.part'** are also the same command.")
        await message.channel.send("**'pc.help'** brings up the Help Menu. Within the help menu, you can type **'pc.commands','pc.code', or 'pc.credits'** to get more information.")

    elif message.content.startswith('pc.credits'):
        await message.channel.send("**Author: Jeet Chugh**")
        await message.channel.send("Programming Language: Python 3")
        await message.channel.send("GitHub Link: ||https://github.com/Jeet-Chugh/pcpartscraper||")
        await message.channel.send("I also Created the Python Package which searches for PC Parts: ")
        await message.channel.send("I have all rights to my code under the MIT License")
        await message.channel.send("Please Submit any issues to the github repository. This Bot is Open-Source")

    elif message.content.startswith('pc.code'):
        await message.channel.send(embed=discord.Embed(title='GitHub Repository',url='https://github.com/Jeet-Chugh/pcpartscraper',description='View the pcpartscraper Python Module.'))

client.run('token')
