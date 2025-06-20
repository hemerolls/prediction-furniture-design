import requests
import csv
from pydantic import BaseModel

class Item(BaseModel):
    id:int
    url:str
    categoryType:str
    name:str
    rating:float
    category_path:str


class It(BaseModel):
    items:list[Item]



def create_csv():
    with open("wb_data.csv",mode="w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'detail_page_url', 'categoryType','name', 'rating', 'category_path'])
def save_csv(it):
    with open("wb_data.csv",mode="a",newline="") as file:
        writer = csv.writer(file)
        for product in it.items:
            writer.writerow([items.id,items.url,items.categoryType,items.name,items.rating,items.items])
cookies = {
    '_ym_uid': '171312542779173604',
    '_ym_d': '1713125427',
    'analytic_id': '1713125427518576',
    'current_location_id': '277',
    'current_city': '711',
    'current_location_data': 'a%3A4%3A%7Bs%3A5%3A%22chain%22%3Ba%3A3%3A%7Bi%3A0%3Bi%3A2%3Bi%3A1%3Bi%3A270%3Bi%3A2%3Bi%3A277%3B%7Ds%3A4%3A%22name%22%3Bs%3A14%3A%22%D0%A9%D0%B5%D0%BB%D0%BA%D0%BE%D0%B2%D0%BE%22%3Bs%3A9%3A%22full_name%22%3Bs%3A71%3A%22%D0%A9%D0%B5%D0%BB%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D1%80-%D0%BD%2C%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%2C%20%D0%A9%D0%B5%D0%BB%D0%BA%D0%BE%D0%B2%D0%BE%22%3Bs%3A11%3A%22location_id%22%3Bi%3A277%3B%7D',
    'BITRIX_SM_SALE_UID': '2380675475',
    'BITRIX_SM_SALE_UID': '2380675475',
    'rrpvid': '400880708331375',
    'rcuid': '661c3834a0146f38cc113781',
    '_gcl_au': '1.1.483016679.1713125430',
    'amlitude_samp': '1510933423',
    '_ga': 'GA1.1.1646253238.1713125430',
    'tmr_lvid': '436f82f08dc00b2a185b63b29d553852',
    'tmr_lvidTS': '1713125430565',
    '__exponea_etc__': '5ad6b775-b2fd-4a94-801a-d946fe9e8122',
    'adtech_uid': 'cd6d7a7c-025f-4b5b-9ec5-b10b8b9f9b64%3Ahoff.ru',
    'top100_id': 't1.7498786.500530686.1713125431048',
    'flocktory-uuid': '85cdbb4d-864c-4e5e-9296-6332d5c4ee80-3',
    '_ct': '1800000000321395468',
    '_ct_client_global_id': 'a46159a7-5bda-541e-8a63-6b1223fdf6b1',
    'uxs_uid': '0f14cb80-fa9b-11ee-a490-9189f59de522',
    'adid': '171415826727322',
    'adrcid': 'AIJCeF2JJQLTWFqUDSdRV6g',
    'last_visit': '1714924334802%3A%3A1714935134802',
    '__USER_ID_COOKIE_NAME__': '171726157465656',
    'advcake_track_id': 'edf105e9-9f18-6d83-bf51-c708c2f3e276',
    'adrcid': 'AOdvu3u_Gb3wRiukU2Xlpbw',
    'BITRIX_SM_ab_test_multi': '%7B%227710124%22%3A%22A%22%2C%227710127%22%3A%22A%22%2C%227710128%22%3A%22B%22%2C%227710129%22%3A%22B%22%2C%227710131%22%3A%22B%22%2C%228116774%22%3A%22%22%2C%228423545%22%3A%22B%22%2C%228522979%22%3A%22A%22%2C%228880741%22%3A%22%22%2C%228897565%22%3A%22C%22%2C%228941487%22%3A%22%22%2C%228965847%22%3A%22A%22%2C%228983931%22%3A%22B%22%2C%229203635%22%3A%22B%22%2C%229310713%22%3A%22A%22%2C%229335295%22%3A%22%22%2C%229336583%22%3A%22A%22%2C%229336665%22%3A%22B%22%2C%229357055%22%3A%22B%22%2C%229406411%22%3A%22A%22%2C%229419263%22%3A%22A%22%2C%229427155%22%3A%22A%22%2C%229428117%22%3A%22A%22%2C%229457513%22%3A%22B%22%2C%229466567%22%3A%22A%22%2C%229476107%22%3A%22B%22%2C%229510127%22%3A%22B%22%2C%229565733%22%3A%22B%22%2C%229565743%22%3A%22A%22%2C%229692643%22%3A%22B%22%2C%229714289%22%3A%22A%22%2C%229737159%22%3A%22A%22%2C%229740171%22%3A%22B%22%2C%229778761%22%3A%22A%22%2C%229810557%22%3A%22A%22%2C%229830639%22%3A%22B%22%2C%229830641%22%3A%22B%22%2C%229842187%22%3A%22A%22%2C%229878381%22%3A%22B%22%2C%229879555%22%3A%22%22%2C%229884541%22%3A%22A%22%2C%229920633%22%3A%22A%22%2C%229955949%22%3A%22B%22%2C%229965231%22%3A%22A%22%2C%229973537%22%3A%22A%22%2C%229973705%22%3A%22B%22%2C%229976787%22%3A%22A%22%2C%229993227%22%3A%22B%22%2C%2210000341%22%3A%22B%22%2C%2210021689%22%3A%22B%22%2C%2210021981%22%3A%22A%22%2C%2210044939%22%3A%22B%22%2C%2210047871%22%3A%22C%22%2C%2210048189%22%3A%22A%22%2C%2210050173%22%3A%22B%22%2C%2210051495%22%3A%22B%22%2C%2210072191%22%3A%22D%22%2C%2210097915%22%3A%22B%22%2C%2210098021%22%3A%22B%22%2C%2210106837%22%3A%22B%22%2C%2210109755%22%3A%22A%22%2C%2210110989%22%3A%22A%22%7D',
    'current_city_name': 'Ð©ÐµÐ»ÐºÐ¾Ð²Ð¾',
    'st_uid': '3db70555e2ce4aba077e86b51533',
    'advcake_session_id': '91977c3e-c9a2-a390-d423-357b78300130',
    'acs_3': '%7B%22hash%22%3A%22ae20ebda0c76a160feca%22%2C%22nextSyncTime%22%3A1719262376639%2C%22syncLog%22%3A%7B%22224%22%3A1719175976639%2C%221228%22%3A1719175976639%2C%221230%22%3A1719175976639%7D%7D',
    'qrator_jsr': 'v2.0.1719276024.950.5d7bcc0eal0FLueS|gTV7D2Tw8IXcQ9No|0wSz1cCDYOD+zYSO1iFHj12/1wd31EErV7PtRrQ8Niz6D6KMp0QGAQnrmD76Nc/ASbj58M1pHOqKWViCGJiYsA==-C0bwu1iucY3iVNB1CPECCBsmP18=-00',
    'qrator_jsid2': 'v2.0.1719276024.950.5d7bcc0eal0FLueS|gTk11CCARxhFz1qC|AE5falnQxMS7l3df7vTUJ7kuVg86n53A+k9dYoRlxmdPWIY8ySb3aEEI9ZLVeB93WihgP59tH8lj3pbpchgzQbheNTLHmr9iA0cjL3KFnjbu6kVyU6JbWCfuii5jc6ni7D7VabFnBgw/f7iumgolOQ==-iKfDqmYyVzXn2o808f56FIDh334=',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'PHPSESSID': '5obtvfc8rovtnp5gajrb5ovin6',
    '__exponea_time2__': '0.07243514060974121',
    'session': '1',
    '_sp_ses.6c0f': '*',
    'cted': 'modId%3Dbl52shes%3Bclient_id%3D1646253238.1713125430%3Bya_client_id%3D171312542779173604',
    '_ct_ids': 'bl52shes%3A45153%3A516037757',
    '_ct_session_id': '516037757',
    '_ct_site_id': '45153',
    'adrdel': '1719276030177',
    'domain_sid': 'XcTAxEQZcF3zHStdAak8M%3A1719276030208',
    '_spx': 'eyJpZCI6IjljN2E5MjhhLWYzYTctNDU4Ni1iMTg3LTAwNzMzMDAxMjM0ZSIsInNvdXJjZSI6IiIsImZpeGVkIjp7InN0YWNrIjpbMCwwXX19',
    'advcake_track_url': '%3D20240624aY0e7v8OKq9NddlyICMyjlfFvnChSkxIv6qPWrXoA%2BGknAXI%2BqsuNxPUX3VjkwfCPIbFVWDtMVxy2nvSyTMao7iVbOprsREWjsbFyGPg33KcUez7%2F6fD%2BSwKL3NC3qipUIJ3F6W%2BVFuQUWf9VXCd6eWjHv8hy4B2ePSgFvbthZKE6qz8rrDdo%2FoudBnvcPWZuG7zq5qP6%2Bw5qDrjlvaNgiOWuFp%2BdoUBFojEpMDAtzLt6IcCkYCtIrS2PwGk6tefhq8Mo3ISjaJysaVu46soHNpsKbJ%2Fc6srFeSS1%2BFpGWHbC%2FCCGx51W3ZDA%2Byu9CPkVMyJ6e83MT0uuLESV8NtWTgZ3pttLS4B0x1aC80obzyWtk1vOyZDoZ9B0CaAM%2FCP3wo%2BurhFQ328GhG9si7kpad063flRKQKZv0dVuDBLXMsvml%2B4DWHcE3%2BFmp%2BwVtXonjV%2FD0m9BrnV4YriIcNNxlf2g%2FyaHbwDvuQZZ6qQryXPPARNZcuZf9zXAowlEnUdOUfCBkciOHgKL99IyTRzbv2AO6OcjuXonoRZEZ9Uf7U%2Buj%2FqLtF4D%2F2HZAh2VHf2vYbYzFVgCHaZZXpq7Mw9VE4V4xF1qAlBoqJ45eOCuHfW2Qg3HMrPr3Zf5OJ7iv6smTC3b0KxWLdwO9%2BltYwfrnnwL56BpApgefX9Xmvhuk5PhFFho9vc9JV5QoxfYQFs9rw4MtRBYEJWTSmiXonxlSYro4rty9ndkdAYwvKtR2JKfdxTHl%2F%2Bq9MysOn7sPQEH980FuzvBWgpA03FLv1Cyh3a1in30P7M%2BgBIOxOGx%2BL3z8l0s2Ck0NKjEsCke59JtDOdXFZkk4anHviNupxuy7KSZhJ9T1Ye2swtaRoTu6dwLtyKAj7BClmyhpVWDSy%2BsWAz2yT7lFRWzpbrrAkmDn2zVj1xigyi4YJFNkrVJaoxk2Ldgde6xHIpYTxaaqsBrUApZQMSMVLWZjOFSgmqPZHXaULZfuZcOxVZBdiPPQYPGGzDmN2KyHW7h%2B2GpC1ywyWSsl1xy%2BSb1F%2Fl7yK%2BWHWBQdOK3hzXW1u0j2Lf9OBjleuqEJ2Tsw0rsNpWJ4qZrEijlS966yDoYYSVCeLR3Es0ETfPm20Euf3Zq7zrRcW%2Bje3BINx%2FfKLqzRxEqDRPpz8SSnexZpxtAcbkbMzeCBJ8npTKxgUZqCg2Yz39otV%2FF7zEfdh1OI%3D',
    'AMP_1fb6bd33a0': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJ3cUgzbkJxSW0wTDczcEdiOHd0QVEyJTIyJTJDJTIyc2Vzc2lvbklkJTIyJTNBMTcxOTI3NjAyOTcwNiUyQyUyMm9wdE91dCUyMiUzQWZhbHNlJTJDJTIybGFzdEV2ZW50VGltZSUyMiUzQTE3MTkyNzYwNTU3MTglMkMlMjJsYXN0RXZlbnRJZCUyMiUzQTE1OCUyQyUyMnBhZ2VDb3VudGVyJTIyJTNBMCU3RA==',
    'call_s': '%3C!%3E%7B%22bl52shes%22%3A%5B1719277855%2C516037757%2C%7B%22202048%22%3A%22621811%22%2C%22202051%22%3A%22621810%22%2C%22202056%22%3A%22621806%22%2C%22202093%22%3A%22621767%22%2C%22202141%22%3A%22621824%22%2C%22202142%22%3A%22621825%22%2C%22202143%22%3A%22874354%22%2C%22202144%22%3A%22621827%22%2C%22202145%22%3A%22621830%22%2C%22202150%22%3A%22621833%22%2C%22202152%22%3A%22621834%22%2C%22202153%22%3A%22621835%22%2C%22202154%22%3A%22621836%22%2C%22202155%22%3A%22621837%22%2C%22202288%22%3A%22622296%22%2C%22202306%22%3A%22622317%22%2C%22202326%22%3A%22622338%22%2C%22202331%22%3A%22622356%22%2C%22202336%22%3A%22622363%22%2C%22202338%22%3A%22873833%22%2C%22202370%22%3A%22624647%22%2C%22202371%22%3A%22624648%22%2C%22202372%22%3A%22624649%22%2C%22202373%22%3A%22624659%22%2C%22202374%22%3A%22624660%22%2C%22202387%22%3A%22879788%22%2C%22202389%22%3A%22624687%22%2C%22202399%22%3A%22624697%22%2C%22202405%22%3A%22624713%22%2C%22202406%22%3A%22961567%22%2C%22202407%22%3A%22624715%22%2C%22202408%22%3A%22624716%22%2C%22202411%22%3A%22624719%22%2C%22202412%22%3A%22879787%22%2C%22202418%22%3A%22624727%22%2C%22202419%22%3A%22624728%22%2C%22202420%22%3A%22624732%22%2C%22202421%22%3A%22624733%22%2C%22202422%22%3A%22624734%22%2C%22202423%22%3A%22624735%22%2C%22202445%22%3A%22961566%22%2C%22202473%22%3A%22962326%22%2C%22202479%22%3A%22961584%22%2C%22202480%22%3A%22962327%22%2C%22202482%22%3A%22624800%22%2C%22202483%22%3A%22624802%22%2C%22202484%22%3A%22624799%22%2C%22202547%22%3A%22624923%22%2C%22202558%22%3A%22624943%22%2C%22202690%22%3A%22857459%22%2C%22202725%22%3A%22625546%22%2C%22202832%22%3A%22625877%22%2C%22202833%22%3A%22625879%22%2C%22202834%22%3A%22625881%22%2C%22202835%22%3A%22625882%22%2C%22202837%22%3A%22625884%22%2C%22202838%22%3A%22625885%22%2C%22203958%22%3A%22628846%22%7D%5D%2C%22d%22%3A2%7D%3C!%3E',
    'tmr_detect': '0%7C1719276057943',
    '_sp_id.6c0f': '2dda7359-752a-4cac-814c-de2746029f85.1713125430.21.1719276074.1719196652.39aaef15-6fba-4415-b63b-8222962ad045.3475561d-8b36-4a7d-9c32-e2b84318023a.d0e4db93-3ba6-4a15-bd1d-b455e4995ce5.1719276029026.36',
    '_ga_444YM4BF0J': 'GS1.1.1719276029.21.1.1719276075.14.0.0',
    't3_sid_7498786': 's1.126082103.1719276029767.1719276075842.21.12',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru,en;q=0.9',
    # 'cookie': '_ym_uid=171312542779173604; _ym_d=1713125427; analytic_id=1713125427518576; current_location_id=277; current_city=711; current_location_data=a%3A4%3A%7Bs%3A5%3A%22chain%22%3Ba%3A3%3A%7Bi%3A0%3Bi%3A2%3Bi%3A1%3Bi%3A270%3Bi%3A2%3Bi%3A277%3B%7Ds%3A4%3A%22name%22%3Bs%3A14%3A%22%D0%A9%D0%B5%D0%BB%D0%BA%D0%BE%D0%B2%D0%BE%22%3Bs%3A9%3A%22full_name%22%3Bs%3A71%3A%22%D0%A9%D0%B5%D0%BB%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D1%80-%D0%BD%2C%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%2C%20%D0%A9%D0%B5%D0%BB%D0%BA%D0%BE%D0%B2%D0%BE%22%3Bs%3A11%3A%22location_id%22%3Bi%3A277%3B%7D; BITRIX_SM_SALE_UID=2380675475; BITRIX_SM_SALE_UID=2380675475; rrpvid=400880708331375; rcuid=661c3834a0146f38cc113781; _gcl_au=1.1.483016679.1713125430; amlitude_samp=1510933423; _ga=GA1.1.1646253238.1713125430; tmr_lvid=436f82f08dc00b2a185b63b29d553852; tmr_lvidTS=1713125430565; __exponea_etc__=5ad6b775-b2fd-4a94-801a-d946fe9e8122; adtech_uid=cd6d7a7c-025f-4b5b-9ec5-b10b8b9f9b64%3Ahoff.ru; top100_id=t1.7498786.500530686.1713125431048; flocktory-uuid=85cdbb4d-864c-4e5e-9296-6332d5c4ee80-3; _ct=1800000000321395468; _ct_client_global_id=a46159a7-5bda-541e-8a63-6b1223fdf6b1; uxs_uid=0f14cb80-fa9b-11ee-a490-9189f59de522; adid=171415826727322; adrcid=AIJCeF2JJQLTWFqUDSdRV6g; last_visit=1714924334802%3A%3A1714935134802; __USER_ID_COOKIE_NAME__=171726157465656; advcake_track_id=edf105e9-9f18-6d83-bf51-c708c2f3e276; adrcid=AOdvu3u_Gb3wRiukU2Xlpbw; BITRIX_SM_ab_test_multi=%7B%227710124%22%3A%22A%22%2C%227710127%22%3A%22A%22%2C%227710128%22%3A%22B%22%2C%227710129%22%3A%22B%22%2C%227710131%22%3A%22B%22%2C%228116774%22%3A%22%22%2C%228423545%22%3A%22B%22%2C%228522979%22%3A%22A%22%2C%228880741%22%3A%22%22%2C%228897565%22%3A%22C%22%2C%228941487%22%3A%22%22%2C%228965847%22%3A%22A%22%2C%228983931%22%3A%22B%22%2C%229203635%22%3A%22B%22%2C%229310713%22%3A%22A%22%2C%229335295%22%3A%22%22%2C%229336583%22%3A%22A%22%2C%229336665%22%3A%22B%22%2C%229357055%22%3A%22B%22%2C%229406411%22%3A%22A%22%2C%229419263%22%3A%22A%22%2C%229427155%22%3A%22A%22%2C%229428117%22%3A%22A%22%2C%229457513%22%3A%22B%22%2C%229466567%22%3A%22A%22%2C%229476107%22%3A%22B%22%2C%229510127%22%3A%22B%22%2C%229565733%22%3A%22B%22%2C%229565743%22%3A%22A%22%2C%229692643%22%3A%22B%22%2C%229714289%22%3A%22A%22%2C%229737159%22%3A%22A%22%2C%229740171%22%3A%22B%22%2C%229778761%22%3A%22A%22%2C%229810557%22%3A%22A%22%2C%229830639%22%3A%22B%22%2C%229830641%22%3A%22B%22%2C%229842187%22%3A%22A%22%2C%229878381%22%3A%22B%22%2C%229879555%22%3A%22%22%2C%229884541%22%3A%22A%22%2C%229920633%22%3A%22A%22%2C%229955949%22%3A%22B%22%2C%229965231%22%3A%22A%22%2C%229973537%22%3A%22A%22%2C%229973705%22%3A%22B%22%2C%229976787%22%3A%22A%22%2C%229993227%22%3A%22B%22%2C%2210000341%22%3A%22B%22%2C%2210021689%22%3A%22B%22%2C%2210021981%22%3A%22A%22%2C%2210044939%22%3A%22B%22%2C%2210047871%22%3A%22C%22%2C%2210048189%22%3A%22A%22%2C%2210050173%22%3A%22B%22%2C%2210051495%22%3A%22B%22%2C%2210072191%22%3A%22D%22%2C%2210097915%22%3A%22B%22%2C%2210098021%22%3A%22B%22%2C%2210106837%22%3A%22B%22%2C%2210109755%22%3A%22A%22%2C%2210110989%22%3A%22A%22%7D; current_city_name=Ð©ÐµÐ»ÐºÐ¾Ð²Ð¾; st_uid=3db70555e2ce4aba077e86b51533; advcake_session_id=91977c3e-c9a2-a390-d423-357b78300130; acs_3=%7B%22hash%22%3A%22ae20ebda0c76a160feca%22%2C%22nextSyncTime%22%3A1719262376639%2C%22syncLog%22%3A%7B%22224%22%3A1719175976639%2C%221228%22%3A1719175976639%2C%221230%22%3A1719175976639%7D%7D; qrator_jsr=v2.0.1719276024.950.5d7bcc0eal0FLueS|gTV7D2Tw8IXcQ9No|0wSz1cCDYOD+zYSO1iFHj12/1wd31EErV7PtRrQ8Niz6D6KMp0QGAQnrmD76Nc/ASbj58M1pHOqKWViCGJiYsA==-C0bwu1iucY3iVNB1CPECCBsmP18=-00; qrator_jsid2=v2.0.1719276024.950.5d7bcc0eal0FLueS|gTk11CCARxhFz1qC|AE5falnQxMS7l3df7vTUJ7kuVg86n53A+k9dYoRlxmdPWIY8ySb3aEEI9ZLVeB93WihgP59tH8lj3pbpchgzQbheNTLHmr9iA0cjL3KFnjbu6kVyU6JbWCfuii5jc6ni7D7VabFnBgw/f7iumgolOQ==-iKfDqmYyVzXn2o808f56FIDh334=; _ym_isad=2; _ym_visorc=b; PHPSESSID=5obtvfc8rovtnp5gajrb5ovin6; __exponea_time2__=0.07243514060974121; session=1; _sp_ses.6c0f=*; cted=modId%3Dbl52shes%3Bclient_id%3D1646253238.1713125430%3Bya_client_id%3D171312542779173604; _ct_ids=bl52shes%3A45153%3A516037757; _ct_session_id=516037757; _ct_site_id=45153; adrdel=1719276030177; domain_sid=XcTAxEQZcF3zHStdAak8M%3A1719276030208; _spx=eyJpZCI6IjljN2E5MjhhLWYzYTctNDU4Ni1iMTg3LTAwNzMzMDAxMjM0ZSIsInNvdXJjZSI6IiIsImZpeGVkIjp7InN0YWNrIjpbMCwwXX19; advcake_track_url=%3D20240624aY0e7v8OKq9NddlyICMyjlfFvnChSkxIv6qPWrXoA%2BGknAXI%2BqsuNxPUX3VjkwfCPIbFVWDtMVxy2nvSyTMao7iVbOprsREWjsbFyGPg33KcUez7%2F6fD%2BSwKL3NC3qipUIJ3F6W%2BVFuQUWf9VXCd6eWjHv8hy4B2ePSgFvbthZKE6qz8rrDdo%2FoudBnvcPWZuG7zq5qP6%2Bw5qDrjlvaNgiOWuFp%2BdoUBFojEpMDAtzLt6IcCkYCtIrS2PwGk6tefhq8Mo3ISjaJysaVu46soHNpsKbJ%2Fc6srFeSS1%2BFpGWHbC%2FCCGx51W3ZDA%2Byu9CPkVMyJ6e83MT0uuLESV8NtWTgZ3pttLS4B0x1aC80obzyWtk1vOyZDoZ9B0CaAM%2FCP3wo%2BurhFQ328GhG9si7kpad063flRKQKZv0dVuDBLXMsvml%2B4DWHcE3%2BFmp%2BwVtXonjV%2FD0m9BrnV4YriIcNNxlf2g%2FyaHbwDvuQZZ6qQryXPPARNZcuZf9zXAowlEnUdOUfCBkciOHgKL99IyTRzbv2AO6OcjuXonoRZEZ9Uf7U%2Buj%2FqLtF4D%2F2HZAh2VHf2vYbYzFVgCHaZZXpq7Mw9VE4V4xF1qAlBoqJ45eOCuHfW2Qg3HMrPr3Zf5OJ7iv6smTC3b0KxWLdwO9%2BltYwfrnnwL56BpApgefX9Xmvhuk5PhFFho9vc9JV5QoxfYQFs9rw4MtRBYEJWTSmiXonxlSYro4rty9ndkdAYwvKtR2JKfdxTHl%2F%2Bq9MysOn7sPQEH980FuzvBWgpA03FLv1Cyh3a1in30P7M%2BgBIOxOGx%2BL3z8l0s2Ck0NKjEsCke59JtDOdXFZkk4anHviNupxuy7KSZhJ9T1Ye2swtaRoTu6dwLtyKAj7BClmyhpVWDSy%2BsWAz2yT7lFRWzpbrrAkmDn2zVj1xigyi4YJFNkrVJaoxk2Ldgde6xHIpYTxaaqsBrUApZQMSMVLWZjOFSgmqPZHXaULZfuZcOxVZBdiPPQYPGGzDmN2KyHW7h%2B2GpC1ywyWSsl1xy%2BSb1F%2Fl7yK%2BWHWBQdOK3hzXW1u0j2Lf9OBjleuqEJ2Tsw0rsNpWJ4qZrEijlS966yDoYYSVCeLR3Es0ETfPm20Euf3Zq7zrRcW%2Bje3BINx%2FfKLqzRxEqDRPpz8SSnexZpxtAcbkbMzeCBJ8npTKxgUZqCg2Yz39otV%2FF7zEfdh1OI%3D; AMP_1fb6bd33a0=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJ3cUgzbkJxSW0wTDczcEdiOHd0QVEyJTIyJTJDJTIyc2Vzc2lvbklkJTIyJTNBMTcxOTI3NjAyOTcwNiUyQyUyMm9wdE91dCUyMiUzQWZhbHNlJTJDJTIybGFzdEV2ZW50VGltZSUyMiUzQTE3MTkyNzYwNTU3MTglMkMlMjJsYXN0RXZlbnRJZCUyMiUzQTE1OCUyQyUyMnBhZ2VDb3VudGVyJTIyJTNBMCU3RA==; call_s=%3C!%3E%7B%22bl52shes%22%3A%5B1719277855%2C516037757%2C%7B%22202048%22%3A%22621811%22%2C%22202051%22%3A%22621810%22%2C%22202056%22%3A%22621806%22%2C%22202093%22%3A%22621767%22%2C%22202141%22%3A%22621824%22%2C%22202142%22%3A%22621825%22%2C%22202143%22%3A%22874354%22%2C%22202144%22%3A%22621827%22%2C%22202145%22%3A%22621830%22%2C%22202150%22%3A%22621833%22%2C%22202152%22%3A%22621834%22%2C%22202153%22%3A%22621835%22%2C%22202154%22%3A%22621836%22%2C%22202155%22%3A%22621837%22%2C%22202288%22%3A%22622296%22%2C%22202306%22%3A%22622317%22%2C%22202326%22%3A%22622338%22%2C%22202331%22%3A%22622356%22%2C%22202336%22%3A%22622363%22%2C%22202338%22%3A%22873833%22%2C%22202370%22%3A%22624647%22%2C%22202371%22%3A%22624648%22%2C%22202372%22%3A%22624649%22%2C%22202373%22%3A%22624659%22%2C%22202374%22%3A%22624660%22%2C%22202387%22%3A%22879788%22%2C%22202389%22%3A%22624687%22%2C%22202399%22%3A%22624697%22%2C%22202405%22%3A%22624713%22%2C%22202406%22%3A%22961567%22%2C%22202407%22%3A%22624715%22%2C%22202408%22%3A%22624716%22%2C%22202411%22%3A%22624719%22%2C%22202412%22%3A%22879787%22%2C%22202418%22%3A%22624727%22%2C%22202419%22%3A%22624728%22%2C%22202420%22%3A%22624732%22%2C%22202421%22%3A%22624733%22%2C%22202422%22%3A%22624734%22%2C%22202423%22%3A%22624735%22%2C%22202445%22%3A%22961566%22%2C%22202473%22%3A%22962326%22%2C%22202479%22%3A%22961584%22%2C%22202480%22%3A%22962327%22%2C%22202482%22%3A%22624800%22%2C%22202483%22%3A%22624802%22%2C%22202484%22%3A%22624799%22%2C%22202547%22%3A%22624923%22%2C%22202558%22%3A%22624943%22%2C%22202690%22%3A%22857459%22%2C%22202725%22%3A%22625546%22%2C%22202832%22%3A%22625877%22%2C%22202833%22%3A%22625879%22%2C%22202834%22%3A%22625881%22%2C%22202835%22%3A%22625882%22%2C%22202837%22%3A%22625884%22%2C%22202838%22%3A%22625885%22%2C%22203958%22%3A%22628846%22%7D%5D%2C%22d%22%3A2%7D%3C!%3E; tmr_detect=0%7C1719276057943; _sp_id.6c0f=2dda7359-752a-4cac-814c-de2746029f85.1713125430.21.1719276074.1719196652.39aaef15-6fba-4415-b63b-8222962ad045.3475561d-8b36-4a7d-9c32-e2b84318023a.d0e4db93-3ba6-4a15-bd1d-b455e4995ce5.1719276029026.36; _ga_444YM4BF0J=GS1.1.1719276029.21.1.1719276075.14.0.0; t3_sid_7498786=s1.126082103.1719276029767.1719276075842.21.12',
    'priority': 'u=1, i',
    'referer': 'https://hoff.ru/catalog/komody/',
    'sec-ch-ua': '"Chromium";v="124", "YaBrowser";v="24.6", "Not-A.Brand";v="99", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'category_id': '3403',
    'limit': '30',
    'offset': '0',
    'showCount': 'true',
    'type': 'product_list',
    'redesignFilters': 'false',
}

response = requests.get('https://hoff.ru/vue/catalog/section/', params=params, cookies=cookies, headers=headers)


required_keys = {'id', 'detail_page_url', 'categoryType', 'name', 'rating', 'prices', 'category_path','image','image_small'}
data = ['id', 'detail_page_url', 'categoryType', 'name', 'rating','pricenew','priceold', 'category_path','image','image_small']
     #Добавьте другие строки данных, если необходимо

with open("dressers.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(data)
print(response.status_code)

for j in range(30*0,30*56,30):
    params = {
    'category_id': '3403',
    'limit': '30',
    'offset': str(j), 
    'showCount': 'true',
    'type': 'product_list',}
    response = requests.get('https://hoff.ru/vue/catalog/section/', params=params, cookies=cookies, headers=headers)
    R=response.json()['data']['items']
    with open("dressers.csv",mode="a",newline="") as file:
        writer = csv.writer(file)
        for i in range(0,30):
            if all(key in R[i] for key in required_keys):
                 writer.writerow([R[i]['id'], R[i]['detail_page_url'], R[i]['categoryType'], R[i]['name'], R[i]['rating'], R[i]['prices']['new'], R[i]['prices']['old'], R[i]['category_path'],R[i]['image'],R[i]['image_small'] ])


### 'category_id': '1314' - стулья, 









