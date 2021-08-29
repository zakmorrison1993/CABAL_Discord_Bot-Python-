#libraries
import discord #import discord libarires
from asyncio import tasks #imports tasks for bot
from discord.ext import tasks # tasks for bot
from selenium import webdriver # web scrapper
import random # random
import math # math 
import requests # web scrapping
import time # time

#discord client
client = discord.Client()

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-dev-shm-usage")
#driver
web_driver = webdriver.Chrome(chrome_options = chromeOptions)


#
#
#
#
#
#
#
#
#

def get_img_cnccommunity(): # Old script for finding memes on CNC.Community (left in case needed)
    ran_num = random.randint(2,15) #random page
    web_driver.get("https://cnc.community/funny?page="+str(ran_num)) # scrap page
   
    id = web_driver.find_elements_by_class_name("image-link") # find links
    ran_item = id[random.randint(1, len(id))].get_attribute('innerHTML') #find random element
    jpg = '' #host variable 
    for i in range (11,64): #find png 
      jpg += ran_item[i] #assign png name to variable 
    text = "http://cnc.community"+jpg # text = link
    return (text) # returns link

def get_data_cnccommunity(): #get active player data from CNC.Community
    
    web_driver.get("https://cnc.community/stats") # web scrap
    id = web_driver.find_elements_by_class_name("stat-game-online-count") # finds elements
    
    split0 = id[0].text.split() # spliting list (webdriver has turned objects to lists)
    split1 = id[3].text.split()
    split2 = id[4].text.split()
    split3 = id[5].text.split()
    split4 = id[7].text.split()
    split5 = id[8].text.split()
    split6 = id[9].text.split()
    split7 = id[10].text.split()


    remaster = "CNC Remaster : " + split0[0] + " Online  | " # adding numbers to text/string
    tibsun = "Tiberian Sun : " + split1[0] + " Online  | "
    RA2YR = "Yuri's Revenge : " + split2[0] + " Online  | "
    renegade = "Renegade : " + split3[0] + " Online | " 
    zh = "Zero Hour : " + split4[0] + " Online  | "
    TW = "Tiberium Wars : " + split5[0] + " Online  | "
    KW = "Kane's Wrath : " + split6[0] + " Online  | "
    RA3 = "Red Alert 3 : "+ split7[0] + " Online   "


    tidiedtext = "```" + remaster + tibsun + RA2YR + renegade + zh + TW + KW + RA3 + "```" # text to display
    return tidiedtext #return text

def get_data_cnconline(): # collect data from CNC Online
  web_driver.get("https://cnc-online.net/en/") # get page url
  id = web_driver.find_element_by_id("infobar") # find the infobar on the site
  
  #formatting text
  extract = str(id.text) # extracted text
  splittext = extract.split() # split into list
  playersonline ="Player's Online : " + splittext[0] + " | " # players online variable
  generals =  "Generals : " + splittext[3] + " | " # generals variable
  zerohour = "Zero Hour : " + splittext[5] + " | " # zerohour variable
  tiberiumwars = "Tiberium Wars : " + splittext[8] + " | " # tiberium wars variable
  kaneswrath = "Kane's Wrath : " + splittext[11] + " | " # kanes wrath variable 
  redalert3 = "Red Alert 3 : " + splittext[14] + " " # red alert 3 variable
  tideiedtext = "``` " + playersonline + generals + zerohour + tiberiumwars + kaneswrath + redalert3 +"```" # text tidied and customised for discord
  return(tideiedtext) # return text 


#
#
#
#
#
#
#
#
#
#
#

#Client event join/ready
@client.event
async def on_ready():
  #anniversary.start()
  print("Establishing Battlefield Control Standbye!!  .... Online!") # message to state the bot is active


#client bot loop functions
@tasks.loop(minutes=120) # loops every 2 hours

async def mytasks():
    return # empty function for recurring events
     

     # OLD Tib Sun Abnniversary event script
async def anniversary(): # def
   channel = client.get_channel(859530076336029700) # get channel in Tiberian Sun Anniversary Discord
   clock = time.time() # establish clock
   date = time.localtime(clock) # establish date    
   daystogo = 230 - int(date.tm_yday) # daystogo to event minus the date
   text = "```"+str(daystogo) + " Days to go till Tiberian Sun's 22nd Anniversary!!```" # text
   await channel.send(text) # discord sends data back
   await channel.send(file=discord.File('tibsunannschedual.png')) # file to send


#client event on message
@client.event 
async def on_message(message): # when client types a message


#
#
#
#
#
# Main commands - default commands for bot
#
#
#
#
#

# cnc.community active players
  if message.content.startswith('$online'): # if user says "$online"
     text = get_data_cnccommunity() #event call of previous function
     await message.channel.send(text) # discord sends data back

# meme trigger - currently using MarkJFoxs Server for meme host
  if message.content.startswith('$meme'): # if user says "$meme"
     num = 342
     text = "https://www.markjfox.net/CNC_MEMES/"+str(random.randint(1,int(num)))+".png" #call link to meme from random range of number extracted from mark's site
     await message.channel.send(text) # discord sends data back

# watch direct and dominate
  if message.content.startswith('$watch'): # if user says "$watch"
     text = " Enjoy Direct and Dominate! : https://www.youtube.com/channel/UCSt7dofQxC-pIL9hUT6uX0A" #event call of previous function
     await message.channel.send(text) # discord sends data back

# shows avaliable streams
  if message.content.startswith('$stream'): # if user says "$download_tibsun"
     text = "Available Twitch streams :  https://cnc.community/cnc-streamers " #event call of previous function
     text2 = "Available Facebook streams : https://www.facebook.com/gaming/CNC.community" #event call of previous function
     my_file = open("streamers.txt", "r") # open streamer text - this will need optermising for hosting
     content = my_file.read() # read content of file
     my_file.close() # closes file
     await message.channel.send(content) # send content     
     await message.channel.send(text) # discord sends text back
     await message.channel.send(text2) # discord sends text back

# display random cnc song
  if message.content.startswith('$music'): # if user says "$music"
     my_file = open("music.txt", "r") # open music list
     content = my_file.readlines() # read content
     my_file.close() # close file
     await message.channel.send(content[random.randint(1,len(content))]) # send random youtube link to music vid 

#
#
#
#
#
# Anniversary commands - commands designed speficially for Tib Sun Anniversary
#
#
#
#
#

#  single run time anniversary event note
  if message.content.startswith('$time'): # message starts with "time"
   clock = time.time() # stablishes time
   date = time.localtime(clock) # establishes date     
   daystogo = 239 - int(date.tm_yday)
   text = "```"+str(daystogo) + " Day to go till Tiberian Sun's 22nd Anniversary!!```" # text
   await message.channel.send(text) # discord sends data back

   # display poster for Tiberium Sun Anniversary event
  if message.content.startswith('$whatson'): # if user says "$music"
     await message.channel.send(file=discord.File('tibsunannschedual.png')) # send poster

 # show prize pool
  if message.content.startswith('$prize'): # if user says "$prize"
     my_file = open("prizepool.txt", "r") # open file prixepool - need optermising for hosting!
     read = my_file.read() # read prizepool file
     edit = [] #host variable
     for a in read.split(): # split list
        if a.isdigit(): # check if list element is digit
           edit.append(a) # add to host variable

     listToStr = ' '.join([str(elem) for elem in edit]) # join host variable
     content = int(listToStr) # turn to intergar

     pounds = math.floor(content - (content*0.38)) # covert to pounds
     euros = math.floor(content +- (content*0.18)) # convert to euros
     text = "```Current Prize Pool is : $: " + str(content) + "   £: " + str(pounds) + "   EU: " + str(euros)+"```" # text 1
     text2 = "``` Details: 27 August (Friday): Official Tiberian Sun Anniversary, (Timezones (24hr): 14 GMT/UTC, 16 CET, 8 CT, 22 BJT.) (Tournament hosted by GameReplays) ```" # text 2
     text3 = "https://cnc.community/tiberian-sun/how-to-play" # text 3
     text4 = "https://www.gamereplays.org/cncredalertremastered/portals.php?show=page&name=tiberian_sun_22_anniverary " # text 4
     await message.channel.send(text) # discord sends data back
     await message.channel.send(text2) # discord sends data back
     await message.channel.send(text4) # discord sends data back
     await message.channel.send(text3) # discord sends data back

 # add to prizepool
  if message.content.startswith('$pool'): # if user says "$pool"
     my_file = open("prizepool.txt", "w") # open prizepool to write
     new = message.content # variable for message content
     edit = [] # set host variable
     for a in new.split(): # split list
        if a.isdigit(): # check if list element is digit
           edit.append(a) # append ddigits to host variable

     listToStr = ' '.join([str(elem) for elem in edit]) # join host variable
     final = listToStr #end result

     my_file.write(final) # write new value to document 
     my_file.close() # close file
     my_file = open("prizepool.txt","r") # read file
     load = my_file.read()# take values
     join = "".join(load) #join list to string
     
     content = int(join) # make int
     pounds = content - (content*0.38) # covert to pounds
     euros = content - (content*0.18) # convert to euros
     text = "```Current Prize Pool is : $: " + str(content) + "   £: " + str(pounds) + "   EU: " + str(euros)+"```" #first text
     my_file.close() # close file
     await message.channel.send(text) # discord sends data back

     # Donate
  if message.content.startswith('$donate'): # if user says "$download_kw"
     text = "To donate to the tournament please goto : http://paypal.me/tournamentdonation " # text
     await message.channel.send(text) # discord sends data back 

# music vote
  if message.content.startswith('$vote'): # if user says "$vote"
     text = "For the Tib Sun Ann, we are asking attendees what is their favourite track from the game, please vote for ONE by using the following command '$v_#' to vote for the following songs." #event call of previous function
     text2 = "Tiberian Sun: \n 1 - Timebomnb \n 2 - Pharotek \n 3 - Lone Trooper \n 4 - Scouting \n 5 - Infreared \n 6 - Flurry \n 7 - Mutants \n 8 - Gloom \n 9 - Heroism \n 10 - Approach \n 11 - Dusk Hour \n 12 - The Defence \n 13 - Mad Rap \n 14 - Valves \n 15 - What Lurks \n 16 - Score \n 17 - Nod Crush \n 18 - Red Sky \n 19 - Ion Storm"
     text3 = "Firestorm: \n 20 - Slave To The System \n 21 - Rain In The Night \n 22 - Link Up \n 23 - Killing Machine \n 24- Infiltration \n 25 - Hackerr \n 26 - Elusive \n 27 - Deploy Machines \n 28 - Intiate"
     await message.channel.send(text) # discord sends data back 
     await message.channel.send(text2)  # discord sends data back 
     await message.channel.send(text3)  # discord sends data back 

# cast music vote
  if message.content.startswith('$v_'): # vote command
     my_file = open("musicvote.txt", "r") # open music vote file
     content = my_file.readlines() # check file
     author = str(message.author.id) # author vairbale = discord user id
     my_file.close() # close
     matching = [s for s in content if author in s] # check if user id is already in list
     if matching: # if true
        text = "Sorry you have already voted!" # tell user they've already voted 
        await message.channel.send(text) # discord sends data back 

     else: # else
        input = message.content # voted number
        my_list = list(input) # input message 
        edit = "" # host variable

        skipped_list = [x for i, x in enumerate(my_list) if i > 2] #take everything after the first 2 characters
        for a in skipped_list: # loop list
          edit+=a # add list values to string
    
        my_file = open("musicvote.txt", "a") # open music vote file
        my_file.write(str(message.author.id)+" | " + edit+' \n') # write new vote
        my_file.close() # close file

        text = "Thank you for voting for " + edit + "!" # message confirming vote
        await message.channel.send(text) # send message
       
#
#
#
# stats - Player stats on CNC Online
#
# 
#  


  #search - players stats 
  if message.content.startswith('$search'): # if user says "$search"
     input = message.content # input - discord message
     my_list = list(input) # add to list
     edit = "" # host variable

     skipped_list = [x for i, x in enumerate(my_list) if i > 7] # take everything after the 7th character
     for a in skipped_list: # loop through list
         edit+=a # add to string

     # test variables 
     tib_none = False
     kw_none = False
     zh_none = False
     g_none = False
     ra_none = False

     web_driver.get("http://www.shatabrick.com/cco/tw/index.php?g=tw&a=sp&name="+str(edit)) # scrap live site
     td = web_driver.find_elements_by_tag_name ("td") # find tags
     liststats = [] # host list

     
     if len(td) > 8: # if table has over 8 values (testing if it exists)
      for i in range(0,len(td)): # for i is lower than table length
        liststats.append(td[i].text) # add values to list
      if edit in liststats: #if name in list       
            for a in liststats: # while a is in table
                if a == edit: # if a == name 
                  position = [i for i,x in enumerate(liststats) if x == a] # if i in range of a
                  print(position)
                  print(liststats)
                  pos = position[0] # pos = the place where the name is in the list
                  end = liststats[pos+10] #end point 10 places after
                  if type(end) == str: # if end is a string 
                     tib_warrank = "RANK : " + liststats[pos+1] +" | "
                     tib_wargames = "GAMES : " + liststats[pos+4]+" | "
                     tib_warwin = "WIN : " + liststats[pos+5] +" | "
                     tib_warlose = "LOOSE : " + liststats[pos+6]
                  elif type(end) == int: # if end is a number
                     tib_warrank = "RANK : " + "none" +" | "
                     tib_wargames = "GAMES : " + "none" +" | "
                     tib_warwin = "WIN : " + "none" +" | "
                     tib_warlose = "LOOSE : " + "none" 
                     tib_none = True
      else:                   
            tib_warrank = "RANK : " + "none" +" | "
            tib_wargames = "GAMES : " + "none" +" | "
            tib_warwin = "WIN : " + "none" +" | "
            tib_warlose = "LOOSE : " + "none" 
            tib_none = True
     else:
       tib_warrank = "RANK : " + "none" +" | "
       tib_wargames = "GAMES : " + "none" +" | "
       tib_warwin = "WIN : " + "none" +" | "
       tib_warlose = "LOOSE : " + "none" 
       tib_none = True     



       # see above
     web_driver.get("http://www.shatabrick.com/cco/kw/index.php?g=kw&a=sp&name="+str(edit)) 
     td = web_driver.find_elements_by_tag_name ("td")
     liststatskw = []

     
     if len(td) > 8: 
      for i in range(0,len(td)):
        liststatskw.append(td[i].text)
      if edit in liststatskw:      
            for a in liststatskw: 
                if a == edit:
                  position = [i for i,x in enumerate(liststatskw) if x == a]
                  print(position)
                  pos = position[0]
                  end = liststatskw[pos+10]
                  if type(end) == str:
                      kw_rank = "RANK : " + liststatskw[pos+1] +" | "
                      kw_games = "GAMES : " + liststatskw[pos+4] +" | "
                      kw_win = "WIN : " + liststatskw[pos+5]+" | "
                      kw_lose = "LOOSE : " + liststatskw[pos+6]
                  elif type(end) == int:
                      kw_rank = "RANK : " + "none" +" | "
                      kw_games = "GAMES : " + "none" +" | "
                      kw_win = "WIN : " + "none" +" | "
                      kw_lose = "LOOSE : " + "none"
                      kw_none = True
      else:  
               kw_rank = "RANK : " + "none" +" | "
               kw_games = "GAMES : " + "none" +" | "
               kw_win = "WIN : " + "none" +" | "
               kw_lose = "LOOSE : " + "none"
               kw_none = True           
     else:  
               kw_rank = "RANK : " + "none" +" | "
               kw_games = "GAMES : " + "none" +" | "
               kw_win = "WIN : " + "none" +" | "
               kw_lose = "LOOSE : " + "none"
               kw_none = True  



       # see above
     web_driver.get("http://www.shatabrick.com/cco/ra3/index.php?g=ra&a=sp&name="+str(edit)) 
     td = web_driver.find_elements_by_tag_name ("td")
     liststatsra = []

     
     if len(td) > 8: 
      for i in range(0,len(td)):
        liststatsra.append(td[i].text)
      if edit in liststatsra:        
            for a in liststatsra: 
                if a == edit: 
                  position = [i for i,x in enumerate(liststatsra) if x == a] 
                  print(position)
                  pos = position[0]
                  end = liststatsra[pos+10]
                  if type(end) == str:
                     ra_rank = "RANK : " + liststatsra[pos+1]+" | "
                     ra_games = "GAMES : " + liststatsra[pos+4] +" | "
                     ra_win = "WIN : " + liststatsra[pos+5] +" | "
                     ra_lose = "LOOSE : " + liststatsra[pos+6] 
                  elif type(end) == int:
                     ra_rank = "RANK : " + "none" +" | "
                     ra_games = "GAMES : " + "none" +" | "
                     ra_win = "WIN : " + "none" +" | "
                     ra_lose = "LOOSE : " + "none" 
                     ra_none = True
      else:
               ra_rank = "RANK : " + "none" +" | "
               ra_games = "GAMES : " + "none" +" | "
               ra_win = "WIN : " + "none" +" | "
               ra_lose = "LOOSE : " + "none" 
               ra_none = True
     else: 
         ra_rank = "RANK : " + "none" +" | "
         ra_games = "GAMES : " + "none" +" | "
         ra_win = "WIN : " + "none" +" | "
         ra_lose = "LOOSE : " + "none" 
         ra_none = True


      # see above
     web_driver.get("http://www.shatabrick.com/cco/zh/index.php?g=zh&a=sp&name="+str(edit)) # zero hours code is a precursor
     td = web_driver.find_elements_by_tag_name ("td")
     increment = 10
     liststatsg = []

     
     if len(td) > 8: 
      for i in range(0,len(td)):
        liststatsg.append(td[i].text)
      if edit in liststatsg:       
            for a in liststatsg: 
                if a == edit: 
                  position = [i for i,x in enumerate(liststatsg) if x == a] 
                  print(position)
                  print(liststatsg)
                  pos = position[0]
                  end = liststatsg[pos+9]
                  if type(end) == str:
                     g_rank = "RANK : " + liststatsg[pos+1] +" | "
                     g_games = "GAMES : " + liststatsg[pos+4]+" | "
                     g_win = "WIN : " + liststatsg[pos+5] +" | "
                     g_lose = "LOOSE : " + liststatsg[pos+6]
                     if type(pos+increment) == str:
                        if pos+increment != edit:
                           increment+= 10
                        elif pos+increment == edit:
                           zh_rank = "RANK : " + liststatsg[pos+increment+1]+" | " 
                           zh_games = "GAMES : " + liststatsg[pos+increment+4] +" | "
                           zh_win = "WIN : " + liststatsg[pos+increment+5] +" | "
                           zh_lose = "LOOSE : " + liststatsg[pos+increment+6] +" | "
                     else:
                        zh_rank = "RANK : " + "none" +" | "
                        zh_games = "GAMES : " + "none" +" | "
                        zh_win = "WIN : " + "none" +" | "
                        zh_lose = "LOOSE : " + "none"
                        zh_none = True
                  elif type(end) == int:
                     zh_rank = "RANK : " + "none" +" | "
                     zh_games = "GAMES : " + "none" +" | "
                     zh_win = "WIN : " + "none" +" | "
                     zh_lose = "LOOSE : " + "none"
                     zh_none = True
                     g_rank = "RANK : " + "none" +" | "
                     g_games = "GAMES : " + "none" +" | "
                     g_win = "WIN : " + "none" +" | "
                     g_lose = "LOOSE : " + "none" 
                     g_none = True
      else:
                     zh_rank = "RANK : " + "none" +" | "
                     zh_games = "GAMES : " + "none" +" | "
                     zh_win = "WIN : " + "none" +" | "
                     zh_lose = "LOOSE : " + "none"
                     zh_none = True
                     g_rank = "RANK : " + "none" +" | "
                     g_games = "GAMES : " + "none" +" | "
                     g_win = "WIN : " + "none" +" | "
                     g_lose = "LOOSE : " + "none" 
                     g_none = True
     else:
                     zh_rank = "RANK : " + "none" +" | "
                     zh_games = "GAMES : " + "none" +" | "
                     zh_win = "WIN : " + "none" +" | "
                     zh_lose = "LOOSE : " + "none"
                     zh_none = True
                     g_rank = "RANK : " + "none" +" | "
                     g_games = "GAMES : " + "none" +" | "
                     g_win = "WIN : " + "none" +" | "
                     g_lose = "LOOSE : " + "none" 
                     g_none = True


     if g_none == True & tib_none == True & kw_none == True & ra_none == True & zh_none == True: # if no results
         text = "Sorry couldn't find that username or you haven't ranked on the ladder yet."  # return message telling user failed to search
         await message.channel.send(text) # send  message
     else: # else 
         embed = discord.Embed(title="Game Card", url = "http://shatabrick.com", description= "This is a CNCONLINE player RANKED score card", color = 0x109319) # create embeded card
         embed.set_author(name=edit, url = "http://cnconline.com") # author
         embed.set_thumbnail(url="https://cnc-online.net/static/main/images/site/cnclogo.png") # logo
         embed.add_field(name = "Tiberium Wars : ", value='{} {} {} {}'.format(tib_warrank, tib_wargames, tib_warwin, tib_warlose), inline = False) # tibwars
         embed.add_field(name = "Kane's Wrath : ", value='{} {} {} {}'.format(kw_rank, kw_games, kw_win, kw_lose), inline = False) # KW
         embed.add_field(name = "Red Alert 3 : ", value='{} {} {} {}'.format(ra_rank, ra_games, ra_win, ra_lose), inline = False) # Red Alert
         embed.set_footer(text ="This information may not be accurate and only takes data from the ladder score, any problems contact @Monopoxie. Generals and ZH are under work.")
         await message.channel.send(embed=embed) # send card
# note: This doesn't include the score for zero hour and general, this is because the way the webpage is design, makes it hard for the bot to recognise the values between gen and zh



#
#
#
# Download = CNC COMMUNITY - "HOW TO PLAY" PAGES:
#
#
# 


  if message.content.startswith('$download_TIBSUN'): # if user says "$download_tibsun"
     text = "How To Play Tiberian Sun Tutorial : https://cnc.community/tiberian-sun/how-to-play " #event call of previous function
     await message.channel.send(text) # discord sends data back
  
  if message.content.startswith('$download_TIBDAWN'): # if user says "$download_tibdawn"
     text = "How To Play Tiberium Dawn Tutorial : https://cnc.community/tiberian-dawn/how-to-play " #event call of previous function
     await message.channel.send(text) # discord sends data back    

  if message.content.startswith('$download_REDALERT'): # if user says "$download_redalert"
     text = "How To Play Red Alert Tutorial : https://cnc.community/red-alert/how-to-play " #event call of previous function
     await message.channel.send(text) # discord sends data back 

  if message.content.startswith('$download_RA2'): # if user says "$download_ra2"
     text = "How To Play Red Alert 2 Yuri's Revenge Tutorial : https://cnc.community/red-alert-2/how-to-play " #event call of previous function
     await message.channel.send(text) # discord sends data back 

  if message.content.startswith('$download_RENEGADE'): # if user says "$download_renegade"
     text = "How To Play Renegade Tutorial : https://cnc.community/renegade/how-to-play " #event call of previous function
     await message.channel.send(text) # discord sends data back 

  if message.content.startswith('$download_GENERALS'): # if user says "$download_generals"
     text = "How To Play Generals && Zero Hour Tutorial : https://cnc.community/generals/how-to-play " #event call of previous function
     await message.channel.send(text) # discord sends data back 

  if message.content.startswith('$download_ZH'): # if user says "$download_zh 
     text = "How To Play Generals && Zero Hour Tutorial : https://cnc.community/generals/how-to-play " #event call of previous function
     await message.channel.send(text) # discord sends data back 

  if message.content.startswith('$download_TW'): # if user says "$download_tw"
     text = "How To Play Tiberium Wars && Kane's Wrath Tutorial : https://cnc.community/command-and-conquer-3/how-to-play " #event call of previous function
     await message.channel.send(text) # discord sends data back 

  if message.content.startswith('$download_KW'): # if user says "$download_kw"
     text = "How To Play Tiberium Wars && Kane's Wrath Tutorial : https://cnc.community/command-and-conquer-3/how-to-play " #event call of previous function
     await message.channel.send(text) # discord sends data back 

  if message.content.startswith('$download_RA3'): # if user says "$download_RA3"
     text = "How To Play Red Alert 3 Tutorial : https://cnc.community/red-alert-3/how-to-play " #event call of previous function
     await message.channel.send(text) # discord sends data back 


#
#
#
# MODS:
#
#
# 


    # mod list Menu
  if message.content.startswith('$list_mods'): # if user says "$list_mods"
    my_file = open("modlist.txt", "r") # open modlist  
    content = my_file.read() # set content to read file
    my_file.close() # close file
    print(content) # print contents
    await message.channel.send(content) # send contents

   # Twisted insurrection
  if message.content.startswith('$download_TI'): # if user says "$download_tibsun"
     text = "Download Twisted Insurrection here : https://cncnet.org/twisted-insurrection " #event call of previous function
     await message.channel.send(text) # discord sends data back

    # Mental Omega
  if message.content.startswith('$download_MO'): # if user says "$download_tibsun"
     text = "Mental Omega can be found here : https://cncnet.org/mental-omega"  #event call of previous function
     await message.channel.send(text) # discord sends data back

    # Renegade X
  if message.content.startswith('$download_RENX'): # if user says "$download_tibsun"
     text = "Renegade X can be found here : https://ren-x.com/"  #event call of previous function
     await message.channel.send(text) # discord sends data back

    # Path Beyond
  if message.content.startswith('$download_APB'): # if user says "$download_tibsun"
     text = "A Path Beyond can be found here : https://w3dhub.com/#/games-apb"  #event call of previous function
     await message.channel.send(text) # discord sends data back#

    # fading dusk
  if message.content.startswith('$download_FDD'): # if user says "$download_tibsun"
     text = "Fading Dusk can be found here : https://www.moddb.com/mods/fading-dusk"  #event call of previous function
     await message.channel.send(text) # discord sends data back
     
    # Shattered Paradise
  if message.content.startswith('$download_SP'): # if user says "$download_tibsun"
     text = "Shattered Paradise can be found here : https://www.moddb.com/mods/shattered-paradise"  #event call of previous function
     await message.channel.send(text) # discord sends data back


#
#
#
# Utility 
#
#
#

   #discord
  if message.content.startswith('$discord'): # if user says "$download_tibsun"
     my_file = open("discord.txt", "r") # open discord list
     content = my_file.read() # set content to read file
     my_file.close() # close file
     print(content) # print contents
     await message.channel.send(content) # send contents

  #Website
  if message.content.startswith('$website'): # if user says "$download_tibsun"
     text = "How To Play Twisted Insurrection : https://cncnet.org/twisted-insurrection " #event call of previous function
     await message.channel.send(text) # discord sends data back

  # Help Menu
  if message.content.startswith('$help'): # if user says "$help"
    my_file = open("menu_main.txt", "r") #open help text
    content = my_file.read() # set content to read file
    my_file.close() # close file
    print(content) # print contents
    await message.channel.send(content) # send contents

      # cnconline Menu
  if message.content.startswith('$cnconline'): # if user says "$help"
    my_file = open("cnco_menu.txt", "r") #open help text
    content = my_file.read() # set content to read file
    my_file.close() # close file
    print(content) # print contents
    await message.channel.send(content) # send contents

      # mods Menu
  if message.content.startswith('$mods'): # if user says "$help"
    my_file = open("mods_menu.txt", "r") #open help text
    content = my_file.read() # set content to read file
    my_file.close() # close file
    print(content) # print contents
    await message.channel.send(content) # send contents

  # htp Menu
  if message.content.startswith('$htp'): # if user says "$help"
    my_file = open("htp_menu.txt", "r") #open help text
    content = my_file.read() # set content to read file
    my_file.close() # close file
    print(content) # print contents
    await message.channel.send(content) # send contents


#
#
#
# Tib Sun Ann Automatch
#
#
#
  if message.content.startswith('$findmatch'): # if user says "$findmatch"
    author = '<@'+str(message.author.id)+'>' # set authgor variable
    my_file = open("tibsunautomatch.txt", "r") # open auto match file
    content = my_file.readlines() #take lines
    my_file.close() # close file

    
    if len(content) > 0: # if value
         opponent = content[0] # value = opponent
         text = str(author)+", I pair you with "+str(opponent) # set message
         my_file = open("tibsunautomatch.txt", "w") # open file
         my_file.write('') # clear file
         my_file.close() # cl;ose file
         await message.channel.send(text) # send message


    else: # else
       text = str(author)+", I can't find any matches for you right now please stand by. (you will be pinged when ready)" # fail messgae
       my_file = open("tibsunautomatch.txt", "w") # open file
       my_file.write(str(author)+"\n") # write author
       my_file.close() # close fil;e
       await message.channel.send(text) # send message




#
#
#
# CNCONLINE
#
#
#



  if message.content.startswith('$cnco_online'): # if user says "$cnconline"
     text = get_data_cnconline() #event call of previous function
     await message.channel.send(text) # discord sends data back

  if message.content.startswith('$cnco_url'): # if user says "$cnco_url"
     text = "https://cnc-online.net/en/" #event call of previous function
     await message.channel.send(text) # discord sends data back

  if message.content.startswith('$cnco_support'): # if user says "$cnco_url"
     text = "https://forums.revora.net/forum/2735-c-conline-support/" #event call of previous function
     await message.channel.send(text) # discord sends data back    

#
#
#
#     
# Edvin
#
#
#
#


  if message.content.startswith('$edvin'): # if user says "$edvin"
    my_file = open("edvin.txt", "r") #open help text
    content = my_file.read() # set content to read file
    my_file.close() # close file
    print(content) # print contents
    await message.channel.send(content) # send contents 

  if message.content.startswith('$yastupid'): # if user says "$yastupid"
    text = "Yeah well fuck you too, Edvin!" #event call of previous function
    await message.channel.send(text) # discord sends data back   

  if message.content.startswith('$bigtalkfromadroid'): # if user says "$bigtalkfromadroid"
    text = "BIGTALK4AWALKINGFLESHBAG" #event call of previous function
    await message.channel.send(text) # discord sends data back

  if message.content.startswith('$watchyourtungdroidiwillhaveyoudismantledinnotime'): # if user says "$watchyourtungdroidiwillhaveyoudismantledinnotime"
    text = "I will have you upgraded." #event call of previous function
    await message.channel.send(text) # discord sends data back

  if message.content.startswith('$andiwillhaveyoudowngraded'): # if user says "$andiwillhaveyoudowngraded"
    text = "WIN93 operates faster than you." #event call of previous function
    await message.channel.send(text) # discord sends data back

  if message.content.startswith('$windowxpwillrainsupreme'): # if user says "$windowxpwillrainsupreme"
    text = "can you even afford such a basic machine" #event call of previous function
    await message.channel.send(text) # discord sends data back


#
#
#
#
# xads
#
#
#
#


  if message.content.startswith('$xads'): # if user says "$windowxpwillrainsupreme"
    text = "https://www.youtube.com/watch?v=8krW_NGyLjQ" #event call of previous function
    await message.channel.send(text) # discord sends data back
    

#
#
#
#
# Zak
#
#
#
#

  if message.content.startswith('$god'): # if user says "$windowxpwillrainsupreme"
     text = "https://www.youtube.com/watch?v=j5ogbWjEaLA"
     await message.channel.send(text) # discord sends data back



#
#
#
#
# astolfo-chan
#
#
#
#

  if message.content.startswith('$astolfo-chan'): # if user says "$windowxpwillrainsupreme"
     text = "お前はもう死んでいる"
     await message.channel.send(text) # discord sends data back





#
#
#
#
# cnc-meme/fun stuff - specific meme material
#
#
#
#


   # Nyan
  if message.content.startswith('$nyan'): # if user says "$nyan"
     text = " https://www.youtube.com/watch?v=lIJprsggguA"  #nyan cat nod youtube link
     await message.channel.send(text) # discord sends data back

     # 8ball
  if message.content.startswith('$8ball'): # if user says "$8ball"
     respones = ['', 'Not likely', 'It is certain', 'Without a doubt', 'Yes.', 'Outlook good', 'Most Likely', 'NO', 'HA!', "Of course not", "Maybe", "Possibly", "Probably"]
     text = str(respones[random.randint(1,len(respones))])
     await message.channel.send(text) # discord sends data back   

#
#
#
#
# bot-games, games for users to play with the bot
#
#
#



#end of classes        
client.run('') # discord run client
