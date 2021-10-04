from telethon import TelegramClient
from time import sleep

########################VARIAVEIS########
api_id = #######
api_hash = '################################'


client = TelegramClient('anon', api_id, api_hash)

channels = ['']   ##########NOME DOS CANAIS PARA SPAMAR


links = ['']     ###############Links para mandar no spam

#####definindo a função do bot

def bot():  
	############Definindo um loop
	while True:
		try:
			for link in links:
				for channel in channels:
					client.loop.run_until_complete(client.send_message(channel,link))
		#######Tratando erros com uma espera
		except:
			print('AGUARDE')
			sleep(300)
with client:
    client.loop.run_until_complete(bot())

