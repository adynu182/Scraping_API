import requests
import pandas as pd
import math
import time
import random
import sys, os

cari = input("Masukan Kata Kunci : ")


headers= {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Cache-Control' : 'no-cache'
        }

url = f"https://www.blibli.com/backend/search/products?sort=&page=1&start=0&searchTerm={cari}&intent=true&merchantSearch=true&multiCategory=true&customUrl=&&channelId=web&showFacet=false&userIdentifier=657116261.U.7936267998746352.1693789735&isMobileBCA=false"

base = 'https://www.blibli.com'

req = requests.get(url, headers=headers).json()

def get_urls():
    tot_pg = int(req['data']['paging']['total_page'])
    print("Total Page : ", tot_pg)
    jlmpg = int(input("Input Jumlah Page yang akan di Scrap : "))
    urls = []
    for i in range(1, jlmpg+1):
        url = 'https://www.blibli.com/backend/search/products?sort=&page={}&start={}&searchTerm={}&intent=true&merchantSearch=true&multiCategory=true&customUrl=&&channelId=web&showFacet=false&userIdentifier=657116261.U.7936267998746352.1693789735&isMobileBCA=false'.format(i, (i-1)*40, cari)
        urls.append(url)
    return urls


def scrape(url):
    req = requests.get(url, headers=headers).json()
    rows = req['data']['products']
    
    produk_all = []
    for i in range(0, len(rows)):
        toko = rows[i]['merchantName']
        lokasi = rows[i]['location']
        nama_produk = rows[i]['name']
        
        # harga = rows[i]['price']['priceDisplay']
        harga = rows[i]['price']['priceDisplay'][2:]
        harga = int(harga.replace('.',''))
        
        diskon = rows[i]['price']['discount']    
        
        # if "soldRangeCount" in rows[i]:
            # item_sold = int(rows[i]['soldRangeCount']['en'])
        # else:
            # item_sold = 0
            
        try:
            item_sold = int(rows[i]['soldRangeCount']['en'])
        except KeyError:
            item_sold = 0
        except ValueError:
            item_sold = item_sold.replace(',','.')
        
        rating = rows[i]['review']['absoluteRating']
        li= rows[i]['url']
        link = base + li
        produk_all.append(
            (toko, lokasi, nama_produk, harga, diskon, item_sold, rating, link)
        )
    return produk_all


def data_frame(data):
    df = pd.DataFrame(data, columns=['nama toko',
                      'lokasi', 'Nama Barang', 'Harga', 'Diskon', 'Terjual', 'Rating', 'Link'])
    return df


def save_to_xlsx(df):
    subdir = sys.path[0]
    try:
        subdir = subdir.replace('\\','/') 
        os.mkdir(f'{subdir}/DataExcel/') 
    except FileExistsError:  
        subdir = f'{subdir}/DataExcel/'
    df.to_excel(f'{subdir}{cari}_{jlmrow}_blibliapi.xlsx', index=False)
    print(f'Data sudah disimpan di file "{cari}_{jlmrow}_blibli.xlsx"')


if __name__ == '__main__':
    urls = get_urls()
    semua_produk = []
    for i in range(0, len(urls)):
        produk = scrape(urls[i])
        # time.sleep(random.randint(2, 9))
        print(i)
        semua_produk.extend(produk)

    df = data_frame(semua_produk)
    print(df)
    jlmrow = len(df.axes[0])
    quit = input("Apakah Hasil Akan disimpan? Y/N : ")
    if  quit == "Y" or quit =="y":
        save_to_xlsx(df)
    exit()
