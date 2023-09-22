import requests
import json
import pandas as pd
import time
import random
import sys, os

key = input("Masukan Kata Kunci : ")

cookies = {
    '_gcl_au': '1.1.398061698.1694600533',
    'language': 'id',
    '_gid': 'GA1.3.507484886.1694600535',
    '_fbp': 'fb.2.1694600534942.2099159566',
    'SPC_SI': 'bzEAZQAAAABEdGhjcHJXaaoiFwAAAAAAanhGeU43a1Y=',
    'REC_T_ID': '6b28c763-521f-11ee-a772-d094667f97a7',
    'SPC_R_T_ID': 'j00wReRJLa9p7DfveHvnfP0EQT2JgPVFSJFGKN8VopPvG1Wpscb/Vop94xzt3l4VheOEqdXSAQ91kzxqjFpkUULBHcNREJ3vexBBXOV+R6BaIYS8Y8QbKjwwwD/4/fyr5IENPX3tqsmXWb2Qm9nqmDz2csWfce4IVx6dKr7Bn5E=',
    'SPC_R_T_IV': 'a2NTd3RpOTNFNGR6T3BLYg==',
    'SPC_T_ID': 'j00wReRJLa9p7DfveHvnfP0EQT2JgPVFSJFGKN8VopPvG1Wpscb/Vop94xzt3l4VheOEqdXSAQ91kzxqjFpkUULBHcNREJ3vexBBXOV+R6BaIYS8Y8QbKjwwwD/4/fyr5IENPX3tqsmXWb2Qm9nqmDz2csWfce4IVx6dKr7Bn5E=',
    'SPC_T_IV': 'a2NTd3RpOTNFNGR6T3BLYg==',
    'SPC_F': 'hgPqU7TZldHjgtbGsc7EnDtKPdzPdsqs',
    'AMP_TOKEN': '%24NOT_FOUND',
    '_ga': 'GA1.3.550974165.1694600535',
    'SPC_CLIENTID': 'aGdQcVU3VFpsZEhqlebzbjiomdnxbfjn',
    'SPC_EC': 'c0tMdWREalozeWo5czlVd3vUfmEyqXrTYUazhWPxLifWoTGmlX/Y2D6mk6w5kdoJq/0zVWub0weOoawpDcY1H4UdodlR8n5JHsNj/+qVaGsYIIcx3sF/XArjVyEEj4hn79GHSTKXtFdPkje/Wtq/7mPbjLSrwjqejgZXtz5GOno=',
    'SPC_ST': '.cTZERWkwamxJOHlyUTZTOLYhxiOBDuE4PQfmezqdS9O/K17gQ4eJcyVrqE/iAbyIEkSxh/QVX0ryZnuTSTVzCPUvTP2cOKS8uWP8V3P1KEU2+EcxEMaetyKzEnxDw+OC0H6NbvA+eI/dlZZNVJ4Qrl1WBOnXkJZHvrJ03Epuo+lDd7ybOhV34hx6M8VtfFfi8zEKQ4WMwNbq2cddRW/aog==',
    '_ga_SW6D8G0HXK': 'GS1.1.1694600538.1.1.1694600560.38.0.0',
    '_dc_gtm_UA-61904553-8': '1',
}

headers = {
    'authority': 'affiliate.shopee.co.id',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'affiliate-program-type': '1',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_gcl_au=1.1.398061698.1694600533; language=id; _gid=GA1.3.507484886.1694600535; _fbp=fb.2.1694600534942.2099159566; SPC_SI=bzEAZQAAAABEdGhjcHJXaaoiFwAAAAAAanhGeU43a1Y=; REC_T_ID=6b28c763-521f-11ee-a772-d094667f97a7; SPC_R_T_ID=j00wReRJLa9p7DfveHvnfP0EQT2JgPVFSJFGKN8VopPvG1Wpscb/Vop94xzt3l4VheOEqdXSAQ91kzxqjFpkUULBHcNREJ3vexBBXOV+R6BaIYS8Y8QbKjwwwD/4/fyr5IENPX3tqsmXWb2Qm9nqmDz2csWfce4IVx6dKr7Bn5E=; SPC_R_T_IV=a2NTd3RpOTNFNGR6T3BLYg==; SPC_T_ID=j00wReRJLa9p7DfveHvnfP0EQT2JgPVFSJFGKN8VopPvG1Wpscb/Vop94xzt3l4VheOEqdXSAQ91kzxqjFpkUULBHcNREJ3vexBBXOV+R6BaIYS8Y8QbKjwwwD/4/fyr5IENPX3tqsmXWb2Qm9nqmDz2csWfce4IVx6dKr7Bn5E=; SPC_T_IV=a2NTd3RpOTNFNGR6T3BLYg==; SPC_F=hgPqU7TZldHjgtbGsc7EnDtKPdzPdsqs; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.3.550974165.1694600535; SPC_CLIENTID=aGdQcVU3VFpsZEhqlebzbjiomdnxbfjn; SPC_EC=c0tMdWREalozeWo5czlVd3vUfmEyqXrTYUazhWPxLifWoTGmlX/Y2D6mk6w5kdoJq/0zVWub0weOoawpDcY1H4UdodlR8n5JHsNj/+qVaGsYIIcx3sF/XArjVyEEj4hn79GHSTKXtFdPkje/Wtq/7mPbjLSrwjqejgZXtz5GOno=; SPC_ST=.cTZERWkwamxJOHlyUTZTOLYhxiOBDuE4PQfmezqdS9O/K17gQ4eJcyVrqE/iAbyIEkSxh/QVX0ryZnuTSTVzCPUvTP2cOKS8uWP8V3P1KEU2+EcxEMaetyKzEnxDw+OC0H6NbvA+eI/dlZZNVJ4Qrl1WBOnXkJZHvrJ03Epuo+lDd7ybOhV34hx6M8VtfFfi8zEKQ4WMwNbq2cddRW/aog==; _ga_SW6D8G0HXK=GS1.1.1694600538.1.1.1694600560.38.0.0; _dc_gtm_UA-61904553-8=1',
    'csrf-token': 'ijpotS5v-eMjU_dW1IKhlDNRZl8OTAGRVvZ4',
    'referer': 'https://affiliate.shopee.co.id/offer/product_offer',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}




def get_products():
    products=[]
    offset = 0
    
    urlcc = f"https://affiliate.shopee.co.id/api/v3/offer/product/list?list_type=0&keyword={key}&sort_type=1&page_offset=0&page_limit=20&client_type=1"
    resc = requests.get(urlcc, cookies=cookies, headers=headers).json()
    tot = int(resc['data']['total_count'])
    pg = int(tot//20)
    print("Total Page : ", pg)
    pg = int(input("Input Jumlah Page yang akan di Scrap : "))
    
    for page in range (0, pg):
    #for page in range(0, 10): 
        
        url = f"https://affiliate.shopee.co.id/api/v3/offer/product/list?list_type=0&keyword={key}&sort_type=1&page_offset={offset}&page_limit=20&client_type=1"
        res = requests.get(url, cookies=cookies, headers=headers).json()
        
        b = 0
        while True:
            try:
                rows = res['data']['list']   
                time.sleep(random.randint(2, 5))
                print(page) 
                break
            except KeyError:
                print(f'percobaan ke {page} Error')
                ms = input("Lanjutkan Scraping ? ")
                if ms == "n":
                    return products
                time.sleep(random.randint(5, 10))
                b += 1
                print(page)
                
                            
        offset += 20
               
        for i in range(0, len(rows)):
            name            = rows[i]['batch_item_for_item_card_full']['name']            
            harga           = int(rows[i]['batch_item_for_item_card_full']['price'])/100000     
            toko            = rows[i]['batch_item_for_item_card_full']['shop_name']    
            rating_toko     = rows[i]['batch_item_for_item_card_full']['shop_rating']
            terjual         = rows[i]['batch_item_for_item_card_full']['historical_sold']            
            lokasi          = rows[i]['batch_item_for_item_card_full']['shop_location'] 
            rating          = rows[i]['batch_item_for_item_card_full']['item_rating']['rating_star']
            jlm_review      = rows[i]['batch_item_for_item_card_full']['item_rating']['rating_count'][0]
            bt_satu         = rows[i]['batch_item_for_item_card_full']['item_rating']['rating_count'][1]
            bt_dua          = rows[i]['batch_item_for_item_card_full']['item_rating']['rating_count'][2]
            bt_tiga         = rows[i]['batch_item_for_item_card_full']['item_rating']['rating_count'][3]
            bt_empat        = rows[i]['batch_item_for_item_card_full']['item_rating']['rating_count'][4]
            bt_lima         = rows[i]['batch_item_for_item_card_full']['item_rating']['rating_count'][5]
            komisi          = rows[i]['default_commission_rate']
            seller_komisi   = rows[i]['seller_commission_rate']
            link            = rows[i]['product_link']
            stok            = rows[i]['batch_item_for_item_card_full']['stock']
            products.append(
                (toko, lokasi, harga, rating_toko, rating, stok, terjual, jlm_review, bt_satu, bt_dua, bt_tiga, bt_empat, bt_lima, komisi, seller_komisi, link, name)
            )
                              
    return products

def get_dataframe(products):    
    return pd.DataFrame(products, columns=['Toko', 'Lokasi', 'Harga', 'Rating Toko', 'Rating Produk', 'Stok barang', 'Terjual', 'Jumlah Review', 'Bintang 1', 'Bintang 2', 'Bintang 3', 'Bintang 4', 'Bintang 5', 'Komisi', 'Komisi Seller', 'Link produk', 'Nama produk'])

def save_to_xlsx(df):
    subdir = sys.path[0]
    subdir = f'{subdir}/DataExcel/'
    df.to_excel(f'{subdir}{key}_{jlmrow}_shoopeaffiliate.xlsx', index=False)
    print(f'Data sudah disimpan di file "{key}_{jlmrow}_shoopeaffiliate.xlsx"')
    
if __name__ == '__main__':
    products = get_products()
    df = get_dataframe(products)
    print(df)
    jlmrow = len(df.axes[0])
    quit = input("Apakah Hasil Akan disimpan? Y/N : ")
    if  quit == "Y" or quit =="y":
        save_to_xlsx(df)
    exit()