import requests
import argparse

liste = list()

nesne = argparse.ArgumentParser(description = "alt domain kontrol uyguglaması")
nesne.add_argument("-d","--dosya", help = "dosya yolunu ve adını belirtiniz" , required = True)
args = nesne.parse_args()

with open(args.dosya , "r" , encoding = "utf-8") as file:

	for i in file:

		if not i.startswith("http" or "https"):

			i = "http://" + i 

			i = i.replace("\n" , "")

		liste.append(i)

for i in liste:

	response = requests.get(i)
	print("site adı : {}			http kodu : {}  cookiler : {}".format(i,response.status_code,response.cookies))
