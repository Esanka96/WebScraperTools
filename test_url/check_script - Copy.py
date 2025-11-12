import requests
from bs4 import BeautifulSoup


def get_session(firstLink, secondLink):
    try:
        session = requests.session()

        firstHeaders = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            #"Cookie": "cck1=%7B%22cm%22%3Atrue%2C%22all1st%22%3Atrue%2C%22closed%22%3Afalse%7D; ppms_privacy_0b5594a8-b9c8-4cd6-aa25-5c578dcf91df={%22visitorId%22:%22d61bda36-0f53-49f9-8cee-3f9b68db62d6%22%2C%22domain%22:{%22normalized%22:%22eur-lex.europa.eu%22%2C%22isWildcard%22:false%2C%22pattern%22:%22eur-lex.europa.eu%22}%2C%22consents%22:{%22analytics%22:{%22status%22:1}}}; experimentalFeaturesActivated=false; _pk_id.0b5594a8-b9c8-4cd6-aa25-5c578dcf91df.5596=93e2ce268d80611b.1732721128.6.1762251612.1756358937.; _pk_ses.0b5594a8-b9c8-4cd6-aa25-5c578dcf91df.5596=*; dtCookie=v_4_srv_35_sn_7637AD71BA1AB635606E3D06243BF665_perc_100000_ol_0_mul_1_app-3A47d4c64c3b67ec69_0_rcs-3Acss_0; ELX_SESSIONID=ZGdOdi3NSDwcIeEULYBXFD9wz3hGZM2UfLeqxKTe5hOP0llnR36F!-263530540; aws-waf-token=43c9d142-0d08-4c46-934d-928d8d4aceb6:CgoAeThLWZtVAAAA:5DZ+MIly9BytTlhrZgudadKJ4t7PwyDChPn1aJWSuSZFfitbgPnfFCzKbV6omgXmXY1maG302nBkwL8Ayn4y+MVB8q5dN5nSKLejbX0NV72cPFn3yDs8SVvrxTeRdl0hxCU1FEiSVaJqT5eThOUhrWO+MPaT7fIAxjR/yHYeFNO1LyCq+RMXbLNuuTYdJHMYIX8gaQ==; AWSALB=rofACc41sP+trpgT2HngLAXWvUNhV7Gdg2h7jlV8dTZ9VHvJ+s+YcMiH5MLuD8QI5kmJEW2Xp21y5+zrzyWdn978zkDBnDhcLV/6l1J3KtysqTHccbOAfKMJawzm",
            "Host": "eur-lex.europa.eu",
            "Pragma": "no-cache",
            "Referer": "https://eur-lex.europa.eu/",
            "Sec-Ch-Ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        }

        session.get(firstLink, headers=firstHeaders)

        secondHeaders = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-encoding": "gzip, deflate, br, zstd",
            "Accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Cache-control": "no-cache",
            "Connection": "keep-alive",
            #"Cookie": "cck1=%7B%22cm%22%3Atrue%2C%22all1st%22%3Atrue%2C%22closed%22%3Afalse%7D; ppms_privacy_0b5594a8-b9c8-4cd6-aa25-5c578dcf91df={%22visitorId%22:%22d61bda36-0f53-49f9-8cee-3f9b68db62d6%22%2C%22domain%22:{%22normalized%22:%22eur-lex.europa.eu%22%2C%22isWildcard%22:false%2C%22pattern%22:%22eur-lex.europa.eu%22}%2C%22consents%22:{%22analytics%22:{%22status%22:1}}}; experimentalFeaturesActivated=false; _pk_id.0b5594a8-b9c8-4cd6-aa25-5c578dcf91df.5596=93e2ce268d80611b.1732721128.6.1762251612.1756358937.; _pk_ses.0b5594a8-b9c8-4cd6-aa25-5c578dcf91df.5596=*; dtCookie=v_4_srv_35_sn_7637AD71BA1AB635606E3D06243BF665_perc_100000_ol_0_mul_1_app-3A47d4c64c3b67ec69_0_rcs-3Acss_0; ELX_SESSIONID=ZGdOdi3NSDwcIeEULYBXFD9wz3hGZM2UfLeqxKTe5hOP0llnR36F!-263530540; AWSALB=rofACc41sP+trpgT2HngLAXWvUNhV7Gdg2h7jlV8dTZ9VHvJ+s+YcMiH5MLuD8QI5kmJEW2Xp21y5+zrzyWdn978zkDBnDhcLV/6l1J3KtysqTHccbOAfKMJawzm; aws-waf-token=43c9d142-0d08-4c46-934d-928d8d4aceb6:CgoAYR5Lon2bAAAA:eU96xDf2owMlcxt9HbaQMjC7Px5uSVgfIXo0ZM9r5V9PORso8yI015HlFEWPGNhRJNPEkcm4hGoY/laMSHoADDc+D0ua9ZvtKHV0S/0am7XWOxM35tu2KhuA/5vHeocz1iVErK7gnoo6lsHEBwe5f0k1L7o0CWJMyf41JCaZQaKNYV5e8gwE7NLeYq0qkZdK6VX3Rg==",
            "Host": "eur-lex.europa.eu",
            "Pragma": "no-cache",
            "Referer": "https://eur-lex.europa.eu/",
            "Sec-ch-ua": "\"Chromium\";v=\"142\", \"Google Chrome\";v=\"142\", \"Not_A Brand\";v=\"99\"",
            "Sec-ch-ua-mobile": "?0",
            "Sec-ch-ua-platform": "\"Windows\"",
            "Sec-fetch-dest": "document",
            "Sec-fetch-mode": "navigate",
            "Sec-fetch-site": "same-origin",
            "Upgrade-insecure-requests": "1",
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        }

        content=session.get(secondLink,headers=secondHeaders)
        soup = BeautifulSoup(content.content, "html.parser")

        print(soup)

    except requests.RequestException as e:
        print("Error fetching URL:", e)
        return None

firstLink = 'https://eur-lex.europa.eu/'
secondLink = "https://eur-lex.europa.eu/"

soup = get_session(firstLink, secondLink)
