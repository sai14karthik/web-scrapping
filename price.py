import smtplib

from bs4 import BeautifulSoup

import requests



url="https://www.flipkart.com/lotto-vertigo-blk-running-shoes-men-7/p/itmf3xxvza78vmyg?pid=SHOEVQTQGNXX5HZG&lid=LSTSHOEVQTQGNXX5HZGGDI2D0&marketplace=FLIPKART&store=osp%2Fcil%2F1cu&srno=b_1_2&otracker=clp_omu_Top%2BDeals%2Bon%2BFashion_2_3.dealCard.OMU_fashion-rd-jan23-sale-store_fashion-rd-jan23-sale-store_GNMJC5NSLZ2K_3&otracker1=clp_omu_PINNED_neo%2Fmerchandising_Top%2BDeals%2Bon%2BFashion_NA_dealCard_cc_2_NA_view-all_3&fm=neo%2Fmerchandising&iid=en_ZeGteErASz%2FNKM2vcflHONM6lRPky5a%2Fi%2BCiV2g70JdUekwslXlBmpEmlW7BOnIuTPr4uNSmrcpxwO0e3az80g%3D%3D&ppt=browse&ppn=browse&ssid=afr5ymi6fms74yrk1674106562130"

r=requests.get(url)

soup=BeautifulSoup(r.content,'html.parser')



price=soup.find('div',class_="_30jeq3")
print("VERTIGO BLK RUNNING SHOES For MEN 7 Running Shoes For Men  (Black)")
print("Todays price")
print(price.text)

