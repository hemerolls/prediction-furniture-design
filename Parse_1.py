import requests
from bs4 import BeautifulSoup
import csv

cookies = {
    '__ddg1_': 'SbqzhEiS5w4CfPceXPPY',
    'cityads_user_type': 'new',
    'BITRIX_SM_REGION_ID': '1',
    '_ym_uid': '17141565663714594',
    '_ym_d': '1714156566',
    'tmr_lvid': 'dfedebec5ed15802eee886fe0bccd0e9',
    'tmr_lvidTS': '1714156566337',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    'g4c_x': '1',
    '_gid': 'GA1.2.1193359359.1714935196',
    'domain_sid': 'B6yWR0XuTOTTwmhfIeLJI%3A1714935197571',
    'PHPSESSID': '1176805a12e3eda0be1452d945faa396',
    'BITRIX_SM_cookie_available': 'available',
    'BITRIX_SM_REGION_TK_ID': '0',
    '_ym_visorc': 'b',
    '_ym_isad': '2',
    'adrdel': '1',
    'adrcid': 'AUnr7WUlZSnLUkLBbQLoiuA',
    'mindboxDeviceUUID': '14380643-6713-4214-ae93-b11b5a4c374c',
    'directCrm-session': '%7B%22deviceGuid%22%3A%2214380643-6713-4214-ae93-b11b5a4c374c%22%7D',
    'count_products': '108',
    'tmr_detect': '0%7C1715021461364',
    '_ga': 'GA1.2.120682631.1714156566',
    '_gat_UA-4410674-1': '1',
    '_ga_Z6QV7B92ES': 'GS1.1.1715021232.3.1.1715021466.56.0.0',
}

headers = {
    'authority': 'www.stolplit.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '__ddg1_=SbqzhEiS5w4CfPceXPPY; cityads_user_type=new; BITRIX_SM_REGION_ID=1; _ym_uid=17141565663714594; _ym_d=1714156566; tmr_lvid=dfedebec5ed15802eee886fe0bccd0e9; tmr_lvidTS=1714156566337; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; g4c_x=1; _gid=GA1.2.1193359359.1714935196; domain_sid=B6yWR0XuTOTTwmhfIeLJI%3A1714935197571; PHPSESSID=1176805a12e3eda0be1452d945faa396; BITRIX_SM_cookie_available=available; BITRIX_SM_REGION_TK_ID=0; _ym_visorc=b; _ym_isad=2; adrdel=1; adrcid=AUnr7WUlZSnLUkLBbQLoiuA; mindboxDeviceUUID=14380643-6713-4214-ae93-b11b5a4c374c; directCrm-session=%7B%22deviceGuid%22%3A%2214380643-6713-4214-ae93-b11b5a4c374c%22%7D; count_products=108; tmr_detect=0%7C1715021461364; _ga=GA1.2.120682631.1714156566; _gat_UA-4410674-1=1; _ga_Z6QV7B92ES=GS1.1.1715021232.3.1.1715021466.56.0.0',
    'referer': 'https://www.stolplit.ru/internet-magazin/katalog-mebeli/29-shkafy/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "YaBrowser";v="24.4", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36',
}
ii=3
#url=https://lazurit.com/catalog/kukhonnye-stoly/?page=2
for ii in range(3,6):
    response = requests.get(f"https://lazurit.com/catalog/kukhonnye-stoly/?page={ii}", cookies=cookies, headers=headers)
    src = response.text
    with open (f"tables{ii}.html","w",encoding="utf8") as file:
        file.write(src)
