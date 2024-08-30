class console:
	def log(text):
		@staticmethod
		if "[obito red]" in text:
			print(red+text[11:])
		elif "[obito blue]" in text:
			print(sblue+text[12:])
		elif "[obito green]" in text:
			print(green+text[13:])
		elif "[obito black]" in text:
			print(black+text[13:])
		elif "[obito sspurp]" in text:
			print(sspurp+text[14:])
		elif "[obito orangefat]" in text:
			print(orangefat+text[17:])
		elif "[obito sblue]" in text:
			print(sblue+text[13:])
		elif "[obito swhite]" in text:
			print(swhite+text[14:])
		elif "[obito pink]" in text:
			print(pink+text[12:])
		elif "[obito white]" in text:
			print(white+text[13:])
		elif "[obito ssyellow]" in text:
			print(ssyellow+text[16:])
		elif "[obito ssbrown]" in text:
			print(ssbrown+text[15:])
		elif "[obito sbrown]" in text:
			print(sbrown+text[14:])
		elif "[obito syellow]" in text:
			print(syellow+text[15:])
		elif "[obito vyellow]" in text:
			print(vyellow+text[15:])
		elif "[obito Dyellow]" in text:
			print(Dyellow+text[15:])
		elif "[text$]" in text:
			print(text[7:])
#subscribe my channel please > https://t.me/pythonic1