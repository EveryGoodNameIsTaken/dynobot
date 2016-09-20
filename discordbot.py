import discord
import asyncio
import random
import string

client = discord.Client()

user_id = input("Before you go any further, what is your discord username and ID number? Enter it here, along with the hash (eg. Dynamo#1850):")
	
playlist = []	
players = []


@client.event
async def on_ready():
	print('Connected!')
	print('Username: ' + client.user.name)
	print('ID: ' + client.user.id)
	await asyncio.sleep(1)
	for server in client.servers:
		await client.send_message(server, 'Hello! My name is Dynobot! \nType !commands for a list of commands \nIf you have any questions, queries, or bug reports, go bother my creator, Dynamo#1850')

@client.event
async def on_message(message):
#Commands module
#List all the things the bot can do here.
	if message.content.startswith('!commands'):
		await client.send_message(message.channel, 'Here\'s what I can do.')
		await client.send_message(message.channel, '\!wisdom: Say a wise saying to inspire you!')
		await client.send_message(message.channel, '\!pasta: Shows you some pasta!')
		await client.send_message(message.channel, '\!disconnect: Only the person who is running me can disconnect me. This will ask them to.')
		await client.send_message(message.channel, '\!play (url): Plays something! This joins the voice channel you\'re in and will play something. Supports a bunch of sites, like youtube and soundcloud. Please wait until the song is done before you attempt to play another thing! I will ignore you if you try to play something while I\'m already playing something.')
	
#Wisdom Module
#To add more quotes, add them to the end of the wisdom list. Make sure there is a ',' at the end of every quote but the last.	
	if message.content.startswith('!wisdom'):
		wisdom_list = ['Religious suffering is, at one and the same time, the expression of real suffering and a protest against real suffering. Religion is the sigh of the oppressed creature, the heart of a heartless world, and the soul of soulless conditions. It is the opium of the people.', 
'Private property has made us so stupid and partial that an object is only ours when we have it, when it exists for us as capital',
'The proletarians have nothing to lose but their chains.',
'We communists are like seeds and the people are the soil. Wherever we go, we must unite with the people, take root and blossom among them.',
'You can become a Communist only when you enrich your mind with a knowledge of all the treasures created by mankind.',
'All over the world, wherever there are capitalists, freedom of the press means freedom to buy up newspapers, to buy writers, to bribe, buy and fake “public opinion” for the benefit of the bourgeoisie.']
		wisdom_said = random.randrange(0, len(wisdom_list))
		await client.send_message(message.channel, wisdom_list[wisdom_said])

	
	if message.content.startswith('!pasta'):
		await client.send_file(message.channel, '/home/sam/Discord Images/pasta.jpg')
		
	if message.content.startswith('!disconnect'):
		disconnecter = message.server.get_member_named(user_id)
		if message.author == disconnecter:
			await client.send_message(message.channel, 'Alright, later.')
			await client.close()
		else:
			await client.send_message(message.channel, 'You can\'t tell me what to do!')
	

#Youtube jams module

	if message.content.startswith('!play') and not client.voice_client_in(message.server):
		await client.join_voice_channel(message.author.voice.voice_channel)
		youtube_string = message.content
		youtube_string = str.split(youtube_string)
		voice = client.voice_client_in(message.server)
		player = await voice.create_ytdl_player(youtube_string[1])
		player.start()
		await client.send_message(message.channel, '**Now playing:** ' + player.title)
		await asyncio.sleep(player.duration)
		await voice.disconnect()


	if message.content.startswith('!stop'):
		voice = client.voice_client_in(message.server)
		await voice.disconnect()
		
	
#Identifier
	if any(x in message.content.lower() for x in ['fuck', 'shit', 'bitch', 'cunt', 'ass', 'emp', 'usa']):
		await client.send_message(message.channel, 'Hey! Watch your language!')
	if 'heswe' in message.content.lower():
		await client.send_file(message.channel, '/home/sam/Discord Images/heswe.jpg')
		
#Dice rolling
	if message.content.startswith('!roll'):
		try:
			d_position = message.content.find('d')
			amount_of_dice = abs(int(message.content[5:d_position]))
			if amount_of_dice > 99:
				amount_of_dice = 99
			sides_of_dice = abs(int(message.content[(d_position + 1):]))
			if sides_of_dice > 99:
				sides_of_dice = 99
			each_dice = 0
			dice_results = []
			while each_dice != amount_of_dice:
				dice_result = random.randrange(1, (sides_of_dice + 1))
				dice_results.append(dice_result)
				each_dice += 1
			sum_of_dice = sum(dice_results)
			await client.send_message(message.channel, dice_results)
			await client.send_message(message.channel, 'Sum: ' + str(sum_of_dice))
		except ValueError:
			await client.send_message(message.channel, "You haven't rolled correctly! The syntax is !roll XdX")
		
client.run('MjI2MTgyNDQ5OTEzMjY2MTc2.Crz4XQ.2jRSaMvik6TTD0zHB3Ju1sfWUmk')
