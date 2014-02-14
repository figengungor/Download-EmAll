#Author: Figen Güngör
#Year: 2013
#Python version: 3.2
#Code Song: The Upsetter by Jack Johnson


################ WHAT DOES THIS CODE DO? ##############################
#######################################################################
#########Saves a range of comics on xkcd webpage to user's computer.###
#######################################################################

import urllib.request
import os
import time

xkcd = "http://xkcd.com"

#creates a directory for images if not exist
if not os.path.exists('C:/xkcd'):
    os.makedirs('C:/xkcd')

#changes current directory, images will be saved here.
os.chdir('C:/xkcd')

# returns page content
def get_page_content(link):
    path = urllib.request.urlopen(link)
    page = path.read().decode("utf-8")
    return page
#test and see the page content if you desire
#print(get_page_content(xkcd))

#finds and returns image's url and name
def find_image_link(page):
    comic = page.find('<div id="comic">')
    image = page.find('<img src=', comic)
    start= page.find('"', image)
    end = page.find('"', start+1)
    image = page[start+1 : end]
    # 29 letters of directory path where all the comics are kept
    #<img src=" ###http://imgs.xkcd.com/comics/### barrel_cropped_(1).jpg"
    name = page[start+29: end-4]
    return name,image
#test and see the url and name of the image on following link
#print(find_image_link(get_page_content("http://xkcd.com/100")))

#finally saves the image to current directory
def copy_image_to_computer(link, name):
    urllib.request.urlretrieve(link, name+".jpg")

#Takes range input from user
print("Please specify xkcd comics range as you wish.") 
start=int(input("Enter start number: "))
end=int(input("Enter end number: "))

#to learn how long it takes to save images from webpage to computer
start_time=time.time()

for x in range(start,end+1):
    name, link = find_image_link(get_page_content(xkcd+"/"+str(x)))
    #if the image already exists, no need to copy again.
    if name+".jpg" not in os.listdir('C:/xkcd'):
        copy_image_to_computer(link,name)
    x+=1

#code ends here, so calculates the passed time in seconds
end_time = time.time()-start_time
print("Comics between "+str(start)+" and "+str(end)+" are saved to C:/xkcd in "+str(int(end_time))+" seconds")
