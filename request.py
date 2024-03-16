from requests import Session,get


s =Session()
s.proxies={'http': 'socks5h://127.0.0.1:9050'}
s.proxies ={'https' : 'socks5h://127.0.0.1:9050'}
a=s.get('https://httpbin.org/ip')
response =get('https://httpbin.org/ip')
print(a.json())
print(response.json())
