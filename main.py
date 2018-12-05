import requests
import time
from bs4 import BeautifulSoup

first =  True
days_left_array = []

first_channel_subs = None
second_channel_subs = None

#search

first_channel_name = "pewdiepie"
second_channel_name = "t-series"

search_url1 = "https://www.youtube.com/results?sp=EgIQAg%253D%253D&search_query="+first_channel_name
search_url2 = "https://www.youtube.com/results?sp=EgIQAg%253D%253D&search_query="+second_channel_name
soup1 = BeautifulSoup(requests.get(search_url1,headers={"User-Agent":"Mozilla/5.0"}).text, "lxml").find("button", attrs={"class":"yt-uix-button yt-uix-button-size-default yt-uix-button-subscribe-unbranded yt-uix-button-has-icon no-icon-markup yt-uix-subscription-button yt-can-buffer yt-uix-servicelink vve-check"})

first_channel_userid = soup1.get("data-channel-external-id")

soup2 = BeautifulSoup(requests.get(search_url2,headers={"User-Agent":"Mozilla/5.0"}).text, "lxml").find("button", attrs={"class":"yt-uix-button yt-uix-button-size-default yt-uix-button-subscribe-unbranded yt-uix-button-has-icon no-icon-markup yt-uix-subscription-button yt-can-buffer yt-uix-servicelink vve-check"})
second_channel_userid = soup2.get("data-channel-external-id")
#second_channel_name =

#or
#direct channel url
##
##first_channel_youtube = "https://www.youtube.com/user/first_channel"
##soup = BeautifulSoup(requests.get(first_channel_youtube).text, "lxml")
##second_channel_youtube = "https://www.youtube.com/user/second_channel" 
##soup2 = BeautifulSoup(requests.get(second_channel_youtube).text, "lxml")
##
##first_channel_userid = soup.find("link", attrs={"rel":"canonical"}).get("href").split("/")[-1]
##second_channel_userid = soup2.find("link", attrs={"rel":"canonical"}).get("href").split("/")[-1]

#print(first_channel_userid,second_channel_userid)

time1 = time.time()
while True:
    try:
        first_channel_url = "https://bastet.socialblade.com/youtube/lookup?query="+first_channel_userid#UC-lHJZR3Gqxm24_Vd_AJ5Yw"
        second_channel_url = "https://bastet.socialblade.com/youtube/lookup?query="+second_channel_userid#UCq-Fj5jknLsUf-MWSy4_brA"
        
        first_channel_subs_old = first_channel_subs
        second_channel_subs_old = second_channel_subs
        
        first_channel_subs = int(requests.get(first_channel_url).text)
        second_channel_subs = int(requests.get(second_channel_url).text)

        if first_channel_subs_old != None:
            first_channel_gains = first_channel_subs - first_channel_subs_old
        else:
            first_channel_gains = 0
        if second_channel_subs_old != None:
            second_channel_gains = second_channel_subs - second_channel_subs_old
        else:
            second_channel_gains = 0
        if not first:
            old_difference = difference
        else:
            old_difference = abs(first_channel_subs-second_channel_subs)
        difference = abs(first_channel_subs-second_channel_subs)
        change = old_difference-difference
        time2 = time.time()
        time_delta = time2-time1
        subs_per_second = change/time_delta
        try:
            days_left = (difference/subs_per_second)/86400
            if days_left > 0:
                days_left_array.append(days_left)
        except:
            days_left = 999999999999
        avg_value = 0
        for value in days_left_array:
            avg_value += value
        try:
            avg_value = avg_value/(len(days_left_array))
        except:
            avg_value = 999999999999
            
        print("Subs Per Second:",subs_per_second)
        print(first_channel_name.title(),"Subs:",first_channel_subs)
        print(second_channel_name.title(),"Subs:",second_channel_subs)
        print(first_channel_name.title(),"Gains:",first_channel_gains)
        print(second_channel_name.title(),"Gains:",second_channel_gains)
        print("Difference:",difference)
        print("Change:",change)
        print("Days Left:",days_left)
        print("Days Left (Avg):",avg_value)
        print("-----------------------------")
        first = False
        time1 = time.time()
        time.sleep(1)
    except:
        pass


