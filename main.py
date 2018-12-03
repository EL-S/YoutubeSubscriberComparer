import requests
import time

first =  True
days_left_array = []

time1 = time.time()
while True:
    try:
        pewdiepie_url = "https://bastet.socialblade.com/youtube/lookup?query=UC-lHJZR3Gqxm24_Vd_AJ5Yw"
        tseries_url = "https://bastet.socialblade.com/youtube/lookup?query=UCq-Fj5jknLsUf-MWSy4_brA"

        pewdiepie_subs = int(requests.get(pewdiepie_url).text)
        tseries_subs = int(requests.get(tseries_url).text)
        if not first:
            old_difference = difference
        else:
            old_difference = abs(pewdiepie_subs-tseries_subs)
        difference = abs(pewdiepie_subs-tseries_subs)
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
        print("Difference:",difference)
        print("Change:",change)
        print("Days Left:",days_left)
        print("Days Left (Avg):",avg_value)
        print("-----------------------------")
        first = False
        time1 = time.time()
        time.sleep(600)
    except:
        pass

