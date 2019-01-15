import requests


def get_iplocation():
    url='http://restapi.amap.com/v3/ip?ip=113.105.125.178&key=5fb61aaf02e17d15f5f5922debcfbc02&output=JSON'
    r=requests.get(url)
    #获取rectangle的values
    #print(r.json()['rectangle'])
    landt=[]
    gps_list=r.json()['rectangle'].split(';')
    for i in range(len(gps_list)):
        element=gps_list[i].split(',')
        for j in range(len(element)):
            #print(element[j])
            landt.append(element[j])
        #print(element)
    #print(landt)
    return landt
    #print(gps_list)

get_iplocation()