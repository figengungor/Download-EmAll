#Author: Figen Güngör
#Year: 14.02.2014  --- finished at 03:57 a.m.
#Python version: 2.7
#Code Songs: Spotify Top 100 Songs 


################ WHAT DOES THIS CODE DO? ##############################
#######################################################################
#########Saves opengameart sounds in one search page################### 
#####(tested by selecting music category and cc0 license(public)) #####
#######################################################################

import urllib
import os

#creates a directory for sounds if not exist
if not os.path.exists('C:/opengameart'):
    os.makedirs('C:/opengameart')

#changes current directory, sounds will be saved here.
os.chdir('C:/opengameart')

#get user input
link = raw_input("Enter url: ")

#opens url and read it
f = urllib.urlopen(link)
pageResource = f.read()

#pattern for sounds in opengameart
pattern="data-mp3-url='http://opengameart.org/sites/default/files/"
start=0
while(pageResource.find(pattern)!=-1):
    try:
        start = pageResource.find(pattern)+14
        end = pageResource.find("\'", start+2)
        soundLink = pageResource[start:end]
        name = pageResource[start+len(pattern)-14:end]
        name = name.replace("%20", "_") 
        pageResource = pageResource[end:]
        urllib.urlretrieve(soundLink, name)
    except:
        pass
    
