import discord
import os
import copy
import random
import asyncio

os.system('cls')

def read_token():
	with open('token.txt') as f:
		lines = f.readlines()
		return lines[0].strip()


def select_command(mystr):
	return mystr[1:].split()[0]



TOKEN = read_token()
client = discord.Client()



def get_board():
	with open('board.txt') as f:
		content = f.read()
	return content


def get_info():
	with open('info.txt') as f:
		info = f.read()
	return info


def random_capital(m):
	res = []
	res.append(m[0].lower())
	for char in m[1:]:
		n = random.randint(1,2)
		if n == 1:
			res.append(char.upper())
		else:
			res.append(char.lower())
	return "".join(res)

def random_pic():
	n = random.randint(1,9)
	return str(n)

def random_pic2():
	n = random.randint(1,8)
	return n

def random_pic3():
	n = random.randint(6,8)
	return n

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
	for guild in client.guilds:
		print(f'{client.user} is connected to {guild}')

flag = True
mock_john = False
mock_fei = False
mock_ks = False

@client.event
async def on_message(message):
	global flag
	global mock_john
	global mock_fei
	global mock_ks
	print(f'Server : {message.guild} || Channel: #{message.channel} || User : {message.author} said "{message.content}"')
	if str(message.author) == 'Pokécord#4503':
		with open('log.txt', 'a+') as f:
			f.write(f'Server : {message.guild} || Channel: #{message.channel} || User : {message.author} said "{message.content}"\n')

	if message.author == client.user:
		return
	
	###### guild exclusive commands ######
	if str(message.guild) == 'Impromtu study gang':
		if message.content.lower().find('mira') != -1:
			user = client.get_user(315529010132156416)
			if str(message.author) == 'mirainsight#6747':
				try:
					await user.send(file=discord.File(f'cutecat{random_pic()}.jpg'))
				except:
					await user.send(file=discord.File(f'cutecat2.gif'))
				await user.send('uhm Miraa uwu sorry to bother you')
				await user.send(f'but i\'m obligated to tell you that you\'ve mentioned your own name in #{message.channel}\n```{message.content}```')
			else:
				try:
					await user.send(file=discord.File(f'cutecat{random_pic()}.jpg'))
				except:
					await user.send(file=discord.File(f'cutecat2.gif'))
				await user.send('uhm Miraa uwu sorry to bother you')
				await user.send(f'but {message.author} mentioned your name #{message.channel}\n```{message.content}```')
			message.channel.send(file=discord.File('raino.png'))
			message.channel.send(f'<@{user}> has been notified')
	###### guild exclusive commands ######
	
	###### general commands #####
	if message.content == 'penguino':
		await message.channel.send(file=discord.File('penguino.png'))
		await message.channel.send('Have a nice day uwu :3')
	if message.content.find('angeri') != -1:
		await message.channel.send(file=discord.File('angeri.gif'))
		await message.channel.send(f'^ that\'s <@{message.author.id}> right now')
	if message.content == 'sed':
		await message.channel.send(file=discord.File('sad.jpg'))
	if message.content == 'yay':
		await message.channel.send(file=discord.File('yay.gif'))
		await message.channel.send(f'^ that\'s <@{message.author.id}> right now')
	if message.content.find('uwu') != -1:
		await message.channel.send(file=discord.File('raino.png'))
		await message.channel.send(f'^ that\'s <@{message.author.id}> right now')
	if message.content.find('pepega') != -1:
		await message.channel.send(file=discord.File('pepega.png'))
	if message.content.find('oh no') != -1:
		await message.channel.send(file=discord.File('pepelaugh.gif'))
	if message.content.find('awwww') != -1:
		try:
			await message.channel.send(file=discord.File(f'cutecat{random_pic()}.jpg'))
		except:
			await message.channel.send(file=discord.File(f'cutecat2.gif'))
	if message.content.find('idiot') != -1 or message.content.find('small brain') != -1:
		try:
			await message.channel.send(file=discord.File(f'smallbrain{random_pic2()}.jpg'))
		except:
			await message.channel.send(file=discord.File(f'smallbrain{random_pic3()}.png'))
	if message.content.find('yare') != -1:
		await message.channel.send(file=discord.File(f'yareyare.gif'))
	if message.content.find('confused') != -1:
		await message.channel.send(file=discord.File(f'confused.gif'))
	###### general commands #####


	###### user exclusive commands ######
	if str(message.author) == 'Trollorigins#5348':
		if message.content == '🍌':
			myid = '<@520132506532708352>'
			await message.channel.send(f'{myid} 不要害羞啦')
		if mock_ks:
			await message.channel.send(random_capital(message.content))
		if message.content == 'toggle mock john':
			mock_john = (not mock_john)
			if mock_john:
				print('mock_john toggled on')
				await message.channel.send('```mock_john toggled on```')
			else:
				print('mock_john toggled off')
				await message.channel.send('```mock_john toggled off```')
		if message.content == 'toggle mock fei':
			mock_fei = (not mock_fei)
			if mock_fei:
				print('mock_fei toggled on')
				await message.channel.send('```mock_fei toggled on```')
			else:
				print('mock_fei toggled off')
				await message.channel.send('```mock_fei toggled off```')
		if message.content == 'toggle mock ks':
			mock_ks = (not mock_ks)
			if mock_ks:
				print('mock_ks toggled on')
				await message.channel.send('```mock_ks toggled on```')
			else:
				print('mock_ks toggled off')
				await message.channel.send('```mock_ks toggled off```')
	if str(message.author) == 'John729#2455':
		if mock_john:
			await message.channel.send(file=discord.File('spongebob.jpg'))
			await message.channel.send(random_capital(message.content))
			await message.channel.send('diam 罢了 john')
		if message.content == 'toggle mock john':
			mock_john = (not mock_john)
			if mock_john:
				print('mock_john toggled on')
				await message.channel.send('```mock_john toggled on```')
			else:
				print('mock_john toggled off')
				await message.channel.send('```mock_john toggled off```')
		if message.content == 'toggle mock fei':
			mock_fei = (not mock_fei)
			if mock_fei:
				print('mock_fei toggled on')
				await message.channel.send('```mock_fei toggled on```')
			else:
				print('mock_fei toggled off')
				await message.channel.send('```mock_fei toggled off```')
	if str(message.author) == 'Fei#1782':
		if mock_fei:
			await message.channel.send(file=discord.File('spongebob.jpg'))
			await message.channel.send(random_capital(message.content))
	if message.content.find('heejin') != -1:
		user = client.get_user(292692870786187265)
		await user.send(f'user {message.author} has mentioned heejin in Server : {message.guild}, #{message.channel} \n```{message.content}```')
		print(f'message succesfully sent to {user.name}')
	if str(message.author) == 'NotMinami#1689':

		if message.content.startswith('>'):
			command = select_command(message.content)
			if command == 'close':
				await message.channel.send(file=discord.File('uwu.jpg'))
				await message.channel.send('Sorry to bother you uwu\ni\'ll go to sleep now :3')
				os.system('cls')
				print('Acme bot disconnected from server')
				await client.close()

		if message.content == 'toggle mock john':
			mock_john = (not mock_john)
			if mock_john:
				print('mock_john toggled on')
				await message.channel.send('```mock_john toggled on```')
			else:
				print('mock_john toggled off')
				await message.channel.send('```mock_john toggled off```')
		if message.content == 'toggle mock fei':
			mock_fei = (not mock_fei)
			if mock_fei:
				print('mock_fei toggled on')
				await message.channel.send('```mock_fei toggled on```')
			else:
				print('mock_fei toggled off')
				await message.channel.send('```mock_fei toggled off```')
		if message.content == 'toggle mock ks':
			mock_ks = (not mock_ks)
			if mock_ks:
				print('mock_ks toggled on')
				await message.channel.send('```mock_ks toggled on```')
			else:
				print('mock_ks toggled off')
				await message.channel.send('```mock_ks toggled off```')
	if str(message.author) == 'Pokécord#4503':
		try:
			for e in message.embeds:
				if not (e.description.find('Your') > -1):
					user = client.get_user(223691822440906752)
					await user.send(f'This pokemon has appeared in Server {message.guild} || Channel #{message.channel}')
					await user.send(file=discord.File(f'{e.url}'))
					await user.send('Here\'s a compliment on the house:')
					await user.send('```p!catch ```')
					await user.send('Go Get Em')
					user = client.get_user(223616371148193792)
					await user.send(f'This pokemon has appeared in Server {message.guild} || Channel #{message.channel}')
					await user.send(file=discord.File(f'{e.url}'))
					await user.send('Here\'s a compliment on the house:')
					await user.send('```p!catch ```')
					await user.send('Go Get Em')
		except:
			user = client.get_user(223691822440906752)
			await user.send(f'This pokemon has appeared in Server {message.guild} || Channel #{message.channel}')
			await user.send(file=discord.File(f'{e.url}'))
			await user.send('Here\'s a compliment on the house:')
			await user.send('```p!catch ```')
			await user.send('Go Get Em')
			user = client.get_user(223616371148193792)
			await user.send(f'This pokemon has appeared in Server {message.guild} || Channel #{message.channel}')
			await user.send(file=discord.File(f'{e.url}'))
			await user.send('Here\'s a compliment on the house:')
			await user.send('```p!catch ```')
			await user.send('Go Get Em')
	###### user exclusive commands ######
			
	### >commands ###
	if message.content.startswith('>'):
		command = select_command(message.content)
		if command == 'help':
			user = client.get_user(message.author.id)
			await user.send('```penguino\nangeri\nsed\nyay\nuwu\npepega\noh no\nawwww\nidiot\nyare\n<reversi```')
	### >commands ###

	###### command for reversi only ######
	if message.content.startswith('<'):
		command = select_command(message.content)
		if command == 'reversi':
			placeholder = ''
			game_board = [['empty' for x in range(8)] for y in range(8)]
			link_w = {}
			link_b = {}
			history = []
			bot_move = []
			winner = ''

			def print_board(board):
				os.remove('board.txt')
				with open('board.txt', 'a+') as f:
					for n, row in enumerate(board, 1):
						f.write(f'{n}|')
						for x in range(len(board)):
							if row[x] == 'empty':
								f.write(f'{" ":^3}|')
							elif row[x] == True:
								f.write(f'{"W":^3}|')
							elif row[x] == False:
								f.write(f'{"B":^3}|')
							else:
								f.write(f'{row[x]:^3}|')
						f.write('\n')
					for i in range(len(board)):
						f.write('   -')
					f.write('\n')
					f.write(' |')
					for char in 'abcdefgh':
						f.write(f'{char:^3}|')
					f.write('\n')
					count_points(f, game_board)
					f.write('\n')

			def reset_board(board=game_board):
				board = copy.deepcopy(game_board)
				board[3][3], board[3][4] = True, False
				board[4][3], board[4][4] = False, True
				return board

			def check_moves(g, turn):
				temp = copy.deepcopy(g)
				for m in range(8):
					for n in range(6):
						if g[m][n] == turn:
							if g[m][n+1] == (not turn):
								if g[m][n+2] == 'empty' or g[m][n+2] == '*':
									g[m][n+2] = '*'
									if turn == True:
										link_w[(m, n+2)].add((m, n+1))
									else:
										link_b[(m, n+2)].add((m, n+1))
					for n in range(7, 1, -1):
						if g[m][n] == turn:
							if g[m][n-1] == (not turn):
								if g[m][n-2] == 'empty' or g[m][n-2] == '*':
									g[m][n-2] = '*'
									if turn == True:
										link_w[(m, n-2)].add((m, n-1))
									else:
										link_b[(m, n-2)].add((m, n-1))
				for m in range(6):
					for n in range(8):
						if g[m][n] == turn:
							if g[m+1][n] == (not turn):
								if g[m+2][n] == 'empty' or g[m+2][n] == '*':
									g[m+2][n] = '*'
									if turn == True:
										link_w[(m+2, n)].add((m+1, n))
									else:
										link_b[(m+2, n)].add((m+1, n))
				for m in range(7, 1, -1):
					for n in range(8):
						if g[m][n] == turn:
							if g[m-1][n] == (not turn):
								if g[m-2][n] == 'empty' or g[m-2][n] == '*':
									g[m-2][n] = '*'
									if turn == True:
										link_w[(m-2, n)].add((m-1, n))
									else:
										link_b[(m-2, n)].add((m-1, n))
				for m in range(6):
					for n in range(6):
						if g[m][n] == turn:
							if g[m+1][n+1] == (not turn):
								if g[m+2][n+2] == 'empty' or g[m+2][n+2] == '*':
									g[m+2][n+2] = '*'
									if turn == True:
										link_w[(m+2, n+2)].add((m+1, n+1))
									else:
										link_b[(m+2, n+2)].add((m+1, n+1))
				for m in range(7, 1, -1):
					for n in range(6):
						if g[m][n] == turn:
							if g[m-1][n+1] == (not turn):
								if g[m-2][n+2] == 'empty' or g[m-2][n+2] == '*':
									g[m-2][n+2] = '*'
									if turn == True:
										link_w[(m-2, n+2)].add((m-1, n+1))
									else:
										link_b[(m-2, n+2)].add((m-1, n+1))
				for m in range(7, 1, -1):
					for n in range(7, 1, -1):
						if g[m][n] == turn:
							if g[m-1][n-1] == (not turn):
								if g[m-2][n-2] == 'empty' or g[m-2][n-2] == '*':
									g[m-2][n-2] = '*'
									if turn == True:
										link_w[(m-2, n-2)].add((m-1, n-1))
									else:
										link_b[(m-2, n-2)].add((m-1, n-1))
				for m in range(6):
					for n in range(7, 1, -1):
						if g[m][n] == turn:
							if g[m+1][n-1] == (not turn):
								if g[m+2][n-2] == 'empty' or g[m+2][n-2] == '*':
									g[m+2][n-2] = '*'
									if turn == True:
										link_w[(m+2, n-2)].add((m+1, n-1))
									else:
										link_b[(m+2, n-2)].add((m+1, n-1))
				if g == temp:
					return False

			def check_empty(g, x, y):
				if g[x][y] != '*':
					return False
				return True						

			async def move(g, turn, bot=None):
				if turn == True:
					player = 'W'
					temp = link_w
				else:
					player = 'B'
					temp = link_b
				flag = True
				while flag:
					if turn == bot:
						possible_move_bot(g)
						user_input = random.choice(bot_move)
					elif bot == None or turn == (not bot):
						def check_input(m):
							if turn == True:
								return m.author == message.author and len(m.content) == 2
							else:
								return m.author == message.author and len(m.content) == 2
						await message.channel.send(f"Player {player}, choose a tile: ")
						x = await client.wait_for('message', check=check_input)
						user_input = x.content
					else:
						await message.channel.send('wtf just happened?? (unknown error occured)')
					if len(user_input) != 2 or user_input[0] not in 'abcdefgh' or user_input[1] not in '12345678':
						await message.channel.send('invalid tile')
					else:
						index = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
						col = index[user_input[0]]
						row = int(user_input[1]) - 1
						if check_empty(g, row, col):
							history.append(user_input)
							g[row][col] = turn
							for i, j in temp[(row, col)]:
								g[i][j] = turn
							flag = False
						else:
							await message.channel.send('invalid tile (tile is not empty)')

			def possible_move_bot(g):
				index = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}
				for m in range(8):
					for n in range(8):
						if g[m][n] == '*':
							bot_move.append(index[n]+str(m+1))

			def clean_asterisk(g):
				for m in range(8):
					for n in range(8):
						if g[m][n] == '*':
							g[m][n] = 'empty'

			async def calculate_score(g):
				w_count = 0
				b_count = 0
				for m in range(8):
					for n in range(8):
						if g[m][n] == True:
							w_count += 1
						elif g[m][n] == False:
							b_count += 1
				await message.channel.send(f'Player W has {w_count} points')
				await message.channel.send(f'Player B has {b_count} points')
				if w_count > b_count:
					await message.channel.send('Player W wins!!')
				elif w_count < b_count:
					await message.channel.send('Player B wins!!')
				elif w_count == b_count:
					await message.channel.send('It\'s a tie!')
				else:
					await message.channel.send('wtf just happened?? (unknown error occured)')

			def initialize_dictionary(w, b):
				for m in range(8):
					for n in range(8):
						w[(m, n)] = set()
						b[(m, n)] = set()

			def moves_history():
				for x, tile in enumerate(history):
					if x % 2 == 0:
						print(f'Player B played {tile}')
					else:
						print(f'Player W played {tile}')

			def count_points(file, g):
				w_real = 0
				b_real = 0
				for m in range(8):
					for n in range(8):
						if g[m][n] == True:
							w_real += 1
						elif g[m][n] == False:
							b_real += 1
				file.write(f'Player W : {w_real:>2} ----- Player B : {b_real:>2}\n')

			async def choose_side():
				def check_see3(m):
					return m.author == message.author and len(m.content) == 1
				while True:
					await message.channel.send("Do you want to be player W or B: ")
					see3 = await client.wait_for('message', check=check_see3)
					if len(see3.content.strip()) != 1 or see3.content.upper() not in 'WB':
						await message.channel.send('invalid input')
					elif see3.content.upper() == 'W':
						return False
					elif see3.content.upper() == 'B':
						return True
					else:
						await message.channel.send('wtf did you do!??! (Please try again uwu :3)')

			async def move2(g, turn, player1, p2id):
				if turn == True:
					player = 'W'
					temp = link_w
				else:
					player = 'B'
					temp = link_b
				flag = True
				while flag:
					def check_input(m):
						if player1 == turn:
							return m.author == message.author and len(m.content) == 2
						else:
							return m.author.id == p2id and len(m.content) == 2
					await message.channel.send(f"Player {player}, choose a tile: ")
					x = await client.wait_for('message', check=check_input)
					user_input = x.content
					if len(user_input) != 2 or user_input[0] not in 'abcdefgh' or user_input[1] not in '12345678':
						await message.channel.send('invalid tile')
					else:
						index = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
						col = index[user_input[0]]
						row = int(user_input[1]) - 1
						if check_empty(g, row, col):
							history.append(user_input)
							g[row][col] = turn
							for i, j in temp[(row, col)]:
								g[i][j] = turn
							flag = False
						else:
							await message.channel.send('invalid tile (tile is not empty)')

			def check_see0(m):
				return m.author == message.author and len(m.content) == 1

			async def choose_opponent():
				def valid_user(m):
					return m.content[0:2] == '<@' and m.content[-1] == '>' and m.author == message.author
				await message.channel.send('```State your challenger```')
				challenger = await client.wait_for('message', check=valid_user)
				challengerid = int(challenger.content[3:-1])
				defenderid = message.author.id
				return defenderid, challengerid

			async def choose_sidep1():
				def valid_input(m):
					return m.content.upper() in 'WB' and m.author == message.author
				await message.channel.send(f'Choose W / B <@{message.author.id}>')
				side = await client.wait_for('message', check=valid_input)
				if side.content.upper() == 'B':
					return False
				elif side.content.upper() == 'W':
					return True
				else:
					await message.channel.send("wtf did you do?!? (Unknown error occured uwu)")
			### execution starts here
			see0 = ''
			while True:
				await message.channel.send("WELCOME TO REVERSI.PY")
				await message.channel.send("Enter 'A' to play Singleplayer\nEnter 'B' to play Multiplayer : ")
				see0 = await client.wait_for('message', check=check_see0)
				if len(see0.content.strip()) != 1 or see0.content.upper() not in 'AB':
					await message.channel.send('invalid input')
				elif see0.content.upper() == 'A' or see0.content.upper() == 'B':
					break
				else:
					await message.channel.send('wtf did you do!??! (Please try again uwu :3)')

			if see0.content.upper() == 'B':
				p1, p2 = await choose_opponent()
				p1side = await choose_sidep1()
				game_board = reset_board()
				current_player = False
				initialize_dictionary(link_w, link_b)
				while True:
					if check_moves(game_board, current_player) == False:
						break
					print_board(game_board)
					await message.channel.send(f"```{get_board()}```")
					await move2(game_board, current_player, p1side, p2)
					clean_asterisk(game_board)
					current_player = (not current_player)
					initialize_dictionary(link_w, link_b)
				bot = None
			elif see0.content.upper() == 'A':
				bot = await choose_side()
				game_board = reset_board()
				current_player = False
				initialize_dictionary(link_w, link_b)
				while True:
					if current_player == (not bot):
						if check_moves(game_board, current_player) == False:
							break
						print_board(game_board)
						await message.channel.send(f"```{get_board()}```")
						await move(game_board, current_player, bot)
						clean_asterisk(game_board)
						current_player = (not current_player)
						initialize_dictionary(link_w, link_b)
						bot_move = []
					elif current_player == bot:
						if check_moves(game_board, current_player) == False:
							break
						await move(game_board, current_player, bot)
						clean_asterisk(game_board)
						current_player = (not current_player)
						initialize_dictionary(link_w, link_b)
						bot_move = []
				placeholder = bot
			await calculate_score(game_board)
			### execution ends here


client.run(TOKEN)