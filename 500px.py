#Author: Figen Güngör
#Year: 2013 
#Python version: 2.7


################ WHAT DOES THIS CODE DO? ##############################
#######################################################################
###############Download an image from 500px############################
#######################################################################

import urllib
link = raw_input("Enter the photo link: ")
name = raw_input("Enter a name for the photo: ")
f = urllib.urlopen(link)
pageResource = f.read()
pattern="{\"size\":2048,\"url\":"
start = pageResource.find(pattern)+20
end = pageResource.find("\"", start+2)
imgLink = pageResource[start:end]
imgLink=imgLink.replace("\\", "")          
urllib.urlretrieve(imgLink, name+".jpg")
print("Photo is successfully downloaded into the directory where your 500px.py file is.")
