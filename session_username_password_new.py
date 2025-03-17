import requests
from bs4 import BeautifulSoup
import cloudscraper

#new_session = cloudscraper.create_scraper()

new_session = requests.session()

url = 'https://www.futuribles.com/en/'
headers1 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,da;q=0.8",
    "Cache-Control": "no-cache",
    #"Cookie": "disable_cache_on_first_load=true; wp-wpml_current_language=en; _pk_id.1.7e77=bab599d550c2d61f.1741807133.; _pk_ses.1.7e77=1; cf_clearance=bd4JDBepEhvTGxmDNqn25cH_6ieLkMs5hbzT1pmuRcU-1741807158-1.2.1.1-ZIQRccIv1qg0iKPUE0tbDUn25eNqyyigsFA_GCkfbFv_wK_O7fG1A7.r16o2dU_gCDyilQg6F8Bew61Yzw.oKN2HpnWdAq4Xyb7ksokqFO3dr0NHgb3KlIpCEqlZvVMuymVULJ_pkHsAbv4HXFa98UL5vY_NW2u94M_kXP_eYUEs8vHhHpEf_QH9cZVWPNVm_zJHs0F8_O698_YarqIW0mi5WIt2dMWa6QMGyUJqh_DzEMmVEKXBKGzkacTULK34gC3aQaTOsgv_sWRpqeSvmgi.ogxYmyX_xPRG9jWi7Dfv_v7Tl6Kk78mJFClQppdyfr4MWIB4fDWPTdwvcvf6JGcsAo.EQ.i9nKpKCsyAAgk; axeptio_authorized_vendors=%2Cgmaps%2CYoutube%2Ctheconversation%2Cspotify%2Capplemusic%2Csoundcloud%2Cyoutube%2C; axeptio_all_vendors=%2Cgmaps%2CYoutube%2Ctheconversation%2Cspotify%2Capplemusic%2Csoundcloud%2Cyoutube%2C; axeptio_cookies={%22$$token%22:%22ry2ah7jxnw5tivbqkvlis%22%2C%22$$date%22:%222025-03-12T19:19:00.770Z%22%2C%22$$cookiesVersion%22:{%22name%22:%22futurible%20dev-fr%22%2C%22identifier%22:%2262d944c58776485f930eae3e%22}%2C%22gmaps%22:true%2C%22Youtube%22:true%2C%22theconversation%22:true%2C%22spotify%22:true%2C%22applemusic%22:true%2C%22soundcloud%22:true%2C%22youtube%22:true%2C%22$$completed%22:true}",
    "Pragma": "no-cache",
    "Priority": "u=0, i",
    "Sec-CH-UA": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
new_session.get(url,headers=headers1)

headers2 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,da;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "288",
    "Content-Type": "application/x-www-form-urlencoded",
    #"Cookie": "SERVERID=sso05; SERVERID161275=ssoha|Z9He1|Z9He1",
    "Host": "sso.qiota.com",
    "Origin": "https://connexion.futuribles.com",
    "Pragma": "no-cache",
    "Referer": "https://connexion.futuribles.com/",
    "Sec-CH-UA": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
post_url='https://sso.qiota.com/api/v1/login'
data = {
    "email": "bd-scm@elsevier.com",
    "password": "Ye2qaMME",
    "response_type": "code",
    "client_id": "62b5ae865e720",
    "scope": "email",
    "redirect_uri": "https://www.futuribles.com/connect-success",
    "error_uri": "https://connexion.futuribles.com/",
    "referer": "7dkINtxf9Q",
    "uri_referer": "https://www.futuribles.com/en/"
}
new_session.post(post_url,data=data,headers=headers2)

url3 = "https://sso.qiota.com/api/v1/authorize?response_type=code&client_id=62b5ae865e720&scope=email&redirect_uri=https://www.futuribles.com/connect-success&error_uri=https://connexion.futuribles.com/&referer=7dkINtxf9Q&uri_referer=https://www.futuribles.com/en/"
headers3 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,da;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    #"Cookie": "SERVERID=sso05; PHPSESSID=9mole6l076q7u9v2upadjampc9; SERVERID161275=ssoha|Z9He8|Z9He1",
    "Host": "sso.qiota.com",
    "Pragma": "no-cache",
    "Referer": "https://connexion.futuribles.com/",
    "Sec-CH-UA": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}
response = new_session.get(url3,headers=headers3)

print(response.cookies)

# url4 = "https://www.futuribles.com/connect-success?code=def5020046f83cf432cb4766f208208a31c26b931a4094fbf8c4013cc1a68cfef60e095c04844e1c6ed9e0ba531981fee2d4f2994c97995654d3b00dba7d480d93c1c5b7641c8aae29b0bb53bb6f427cacc59d7b9aa9ce17947579151476e10d5da9239e93d4db92d5064691a51afc54a880e23b4a36c36526952356717f3284f17a2ff6f2c33923e1c696d21cc7a4790df3bf8854b79f5595f95fd97c55b7edb82ec85631d54dc7f6f99328750944491c58116c13132865cbb4b916c06f05d46f955c68c9e689d8d5aba94bc9f71380a029be34fb1e8bcccc98c5da3e292bf9ca5ef9061e06347cea81a15e87888c717ea0dfcec212963e734888f61a93a4592dab8ebccc5e691cf9ede3dbeaafa6608389f2698e13992ffaf1b3d8b65a446b9a6f5ce07ebfdb2a772b357bb059c2a77804b7e5c409c0449679ade58b930506d8ab003894f3c9ba539982f57309fdea763b3db6180e997e38f145e28cbab85d3cd482affae43b99d91fdf0f30ebde68b4741b0cf97b771d240fd94773bf6c82&uri_referer=https://www.futuribles.com/en/&uri_referer=https://www.futuribles.com/en/"
# headers4 = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-US,en;q=0.9,da;q=0.8",
#     "Cache-Control": "no-cache",
#     #"Cookie": "disable_cache_on_first_load=true; wp-wpml_current_language=en; _pk_id.1.7e77=bab599d550c2d61f.1741807133.; _pk_ses.1.7e77=1; cf_clearance=bd4JDBepEhvTGxmDNqn25cH_6ieLkMs5hbzT1pmuRcU-1741807158-1.2.1.1-ZIQRccIv1qg0iKPUE0tbDUn25eNqyyigsFA_GCkfbFv_wK_O7fG1A7.r16o2dU_gCDyilQg6F8Bew61Yzw.oKN2HpnWdAq4Xyb7ksokqFO3dr0NHgb3KlIpCEqlZvVMuymVULJ_pkHsAbv4HXFa98UL5vY_NW2u94M_kXP_eYUEs8vHhHpEf_QH9cZVWPNVm_zJHs0F8_O698_YarqIW0mi5WIt2dMWa6QMGyUJqh_DzEMmVEKXBKGzkacTULK34gC3aQaTOsgv_sWRpqeSvmgi.ogxYmyX_xPRG9jWi7Dfv_v7Tl6Kk78mJFClQppdyfr4MWIB4fDWPTdwvcvf6JGcsAo.EQ.i9nKpKCsyAAgk; axeptio_authorized_vendors=%2Cgmaps%2CYoutube%2Ctheconversation%2Cspotify%2Capplemusic%2Csoundcloud%2Cyoutube%2C; axeptio_all_vendors=%2Cgmaps%2CYoutube%2Ctheconversation%2Cspotify%2Capplemusic%2Csoundcloud%2Cyoutube%2C; axeptio_cookies={%22$$token%22:%22ry2ah7jxnw5tivbqkvlis%22%2C%22$$date%22:%222025-03-12T19:19:00.770Z%22%2C%22$$cookiesVersion%22:{%22name%22:%22futurible%20dev-fr%22%2C%22identifier%22:%2262d944c58776485f930eae3e%22}%2C%22gmaps%22:true%2C%22Youtube%22:true%2C%22theconversation%22:true%2C%22spotify%22:true%2C%22applemusic%22:true%2C%22soundcloud%22:true%2C%22youtube%22:true%2C%22$$completed%22:true}",
#     "Pragma": "no-cache",
#     "Priority": "u=0, i",
#     "Referer": "https://connexion.futuribles.com/",
#     "Sec-CH-UA": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
#     "Sec-CH-UA-Mobile": "?0",
#     "Sec-CH-UA-Platform": '"Windows"',
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "cross-site",
#     "Sec-Fetch-User": "?1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
# }
# new_session.get(url4,headers=headers4)
#
# new_response=new_session.get('https://www.futuribles.com/en/')
# soup=BeautifulSoup(new_response.content,'html.parser')
# print(soup)

