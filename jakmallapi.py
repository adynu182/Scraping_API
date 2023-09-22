import requests
import json
import pandas as pd
import sys, os

cari = input("Masukan Kata Kunci : ")

headers = {
    'authority': 'www.jakmall.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'S-VOC=eyJpdiI6IjdhVTZGM1hFTCtlTTBGNEI2VVJWNWc9PSIsInZhbHVlIjoiMDcwXC9wYUVKSFNYUXZNYlBxY2xVS0E9PSIsIm1hYyI6ImRlZmMxYmRhNzNmMTBiMmE1MDE0NWM4M2QyMTQ0ZTE1NzQ5M2YzZTAyZmQ2ZWFhZTUxMjkxNzA4M2E5YTdiMjgifQ%3D%3D; _gid=GA1.2.1786263480.1692963822; _fbp=fb.1.1692963822520.1581822758; _tt_enable_cookie=1; _ttp=MH5vqtdJVamPy7dE32eTbfMhHst; _hjFirstSeen=1; _hjIncludedInSessionSample_226234=0; _hjSession_226234=eyJpZCI6IjY4OTk4Y2Q0LTM2MTAtNGEyYi1iNzU5LTg5MzM4YmMzMGE2NCIsImNyZWF0ZWQiOjE2OTI5NjM4MjM0MTgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; twk_idm_key=VTx_bdIqJi9A9sBQTxjkI; _hjSessionUser_226234=eyJpZCI6IjNlMDkwZmJhLTRmMjEtNTkwNi1iYmViLWRkYTZmZjM0ZWE2ZiIsImNyZWF0ZWQiOjE2OTI5NjM4MjMzOTUsImV4aXN0aW5nIjp0cnVlfQ==; AWSALB=xiVRBjKwq/KhydkrRktLtJgEjIJUxocQsZKO8xXyt6Ci8MN2bgfeL77Lw/3v+5BwdsX5cDhLPVPlrCN8jbKY4Uos/oI+R5OTiABNKgHqB+KDyjFcPYrvRyTIQee8; AWSALBCORS=xiVRBjKwq/KhydkrRktLtJgEjIJUxocQsZKO8xXyt6Ci8MN2bgfeL77Lw/3v+5BwdsX5cDhLPVPlrCN8jbKY4Uos/oI+R5OTiABNKgHqB+KDyjFcPYrvRyTIQee8; XSRF-TOKEN=eyJpdiI6IlNyVXNcL2UxUkQ5TkE1c3VEU0s5dDFBPT0iLCJ2YWx1ZSI6ImFUV09RQXNkQk9cL25aazFsR0ZZeW4xblVlK21Ec3ZQblpZZnVZSzMrVFlxT0lkQ1BlQXVhbnFXTVVIdXI3QWdhIiwibWFjIjoiNzUwYjg1ZmQ5MTk0MjI1ZGNmYmIzNDNlOTM3NTQ1M2JmZjkxMDUxYTdkZGZiZTVhNjFmZmY1YmEwM2JjODJmYiJ9; jsi=eyJpdiI6Im9Jb2xWUXpITmJuUjBpbkdSRTA0RXc9PSIsInZhbHVlIjoiYkhjeEtGYnBvOFM2bkxGXC91YVNuRmV3aGdDY2RScnpPMjJPNjg2Um44Z3Myd2Y0UTAybHQzZXFsdUQ3RFc4N3IiLCJtYWMiOiI4MjJlZTI2MTA3YTIzZThkNDVjZmY3YmQ0Y2ZjYzJmNTUyY2VlYjA5YTBkMWUyODAyNzA5NDUyYjc0YTY2MDBjIn0%3D; _gat_UA-66644090-1=1; TawkConnectionTime=0; twk_uuid_5dc3e523e4c2fa4b6bda7115=%7B%22uuid%22%3A%221.70gbKM4OEN4jYjjCV5lofYpYCyheXC9tMiwpLOSHwCWb7yE0MHZehTK3t09sBhBxqSiFEb8XZqneZG1GjBnIhO7PVrf1wiqtGQOYpbpT5ak8FZofHAQc%22%2C%22version%22%3A3%2C%22domain%22%3A%22jakmall.com%22%2C%22ts%22%3A1692963894920%7D; _ga=GA1.2.649133720.1692963822; _ga_XX88006F73=GS1.1.1692963822.1.1.1692963914.0.0.0',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-csrf-token': 'TZfGQJByhSHKdauKabFCsSjd3Q9tT1kUPj8Vpsfr',
    'x-requested-with': 'XMLHttpRequest',
}


    

def get_products(): 
    urlc = f"https://www.jakmall.com/search?q={cari}&sort=popular&page=1"
    resc = requests.get(urlc, headers=headers).json()
    pg = resc['pagination']
    
    t = int(pg['total']) % 60
    tot = int(pg['total']) // 60
    if t > 0 :
        tot +=1
        
    print("Total Page : ", tot)
    tot = int(input("Input Jumlah Page yang akan di Scrap : "))

    products=[]
    for page in range(1, tot+1):
        url = f"https://www.jakmall.com/search?q={cari}&sort=popular&page={page}"
        res = requests.get(url, headers=headers).json()
        rows = res['products']
        
        for i in range(0, len(rows)):
            name = rows[i]['name']
            harga = rows[i]['sku'][0]['normal_price']
            rating = rows[i]['rating']
            store = rows[i]['store']['name']
            terjual = rows[i]['sold']
            review = rows[i]['review_count']
            link = rows[i]['url']
            lokasi = rows[i]['warehouse']['display_city']
            products.append(
                (name, harga, rating, store, terjual, review, link, lokasi)
            )
                
    return products

def get_dataframe(products):    
    return pd.DataFrame(products, columns=['Nama produk', 'Harga', 'Rating', 'Toko', 'Terjual', 'Jml Review', 'Link Produk', 'Lokasi'])

def save_to_xlsx(df):
    subdir = sys.path[0]
    try:
        subdir = subdir.replace('\\','/') 
        os.mkdir(f'{subdir}/DataExcel/') 
    except FileExistsError:  
        subdir = f'{subdir}/DataExcel/'
    df.to_excel(f'{subdir}{cari}_{jlmrow}_jakmall.xlsx', index=False)
    print(f'Data sudah disimpan di file "{cari}_{jlmrow}_jakmall.xlsx"')
    
if __name__ == '__main__':
    products = get_products()
    df = get_dataframe(products)
    print(df)
    jlmrow = len(df.axes[0])
    quit = input("Apakah Hasil Akan disimpan? Y/N : ")
    if  quit == "Y" or quit =="y":
        save_to_xlsx(df)
    exit()