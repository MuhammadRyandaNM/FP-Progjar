def sendImg(self,source,destination, filename):
		if not os.path.exists(destination):
			os.mkdir(destination)
		if not os.path.exists(source):
			os.mkdir(source)
		sourceName = os.path.join(source, filename)
		destinationName = os.path.join(destination, filename)

		fp = open(sourceName, "rb")
		pckg = fp.read()
		sizeSent = 0
		fp.close()
		fp = open(destinationName, "wb+")
		fp.write(pckg)
		fp.close()