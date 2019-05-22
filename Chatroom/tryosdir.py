import os
imgname="wtf.jpg"
destination="kamu"
if not os.path.exists(destination):
	os.mkdir(destination)

completeName = os.path.join(destination, imgname)
print completeName