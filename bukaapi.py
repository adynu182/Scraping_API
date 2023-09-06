import requests
import pandas as pd

cari = input("Masukan Kata Kunci : ")
url = 'https://api.bukalapak.com/multistrategy-products'


token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImFjY291bnRzLmp3dC5hY2Nlc3MtdG9rZW4iLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmJ1a2FsYXBhay5jb20vIiwic3ViIjoiMjMxZDRhODY5MDVmMGYyNjJjNWUwM2ZjIiwiYXVkIjpbImh0dHBzOi8vYWNjb3VudHMuYnVrYWxhcGFrLmNvbSIsImh0dHBzOi8vYXBpLmJ1a2FsYXBhay5jb20iLCJodHRwczovL2FwaS5zZXJ2ZXJtaXRyYS5jb20iXSwiZXhwIjoxNjkzNzU3MTczLCJuYmYiOjE2OTM3NDQzOTMsImlhdCI6MTY5Mzc0NDM5MywianRpIjoiZmQzbG9TamJlaTdMQndtRXdiZmhHUSIsImNsaWVudF9pZCI6IjIzMWQ0YTg2OTA1ZjBmMjYyYzVlMDNmYyIsInNjb3BlIjoicHVibGljIn0.X3QoFPaa5P1ApaiMGyl7KbZ2bOs_meM6ugLQH5KQKkGCXlyhbUY92g4y5OLuHjGadpoCKHeM3Dq_VzDZU9jdwmqj4qPBOFLvfAsNVAUQYDpPiIPEfCKXf120TB716_6NS3GwczYWvBRWtQtfG3baK6FnnR8Qo6JGkqcp7LN0NRyJ8m4imoab7Ff_LU1Wm0lsypWRQo2_AjYxElr0DzevPbBRJ2s97iXdR6YU2WmGXffc9i5qKqOCrfOMAj86nArMW5sqmIO3-_BgqFW-V_Gn7GMTkkW9QK1G7Fyf9P-H7rOZdeJ2HHdr4w971EKReZTbsz7cZi-1Wa_49wbj-pGcJw'


h = {
    'authority': 'api.bukalapak.com',
    'accept': 'application/json',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://www.bukalapak.com',
    'referer': 'https://www.bukalapak.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'x-device-ad-id': '7e230b6758350eb328dbfd1b30057444',
}

p = {
    'keywords': str(cari),
    'limit': '50',
    'offset': '0',
    'facet': 'true',
    'page': '1',
    'shouldUseSeoMultistrategy': 'false',
    'isLoggedIn': 'false',
    'show_search_contexts': 'true',
    'access_token': token,
}


def get_params():
    jlmpg = int(input("Input Jumlah Page yang akan di Scrap : "))
    params=[]
    for i in range(1, jlmpg+1):
        param = {
            'keywords': str(cari),
            'limit': '50',
            'offset': str((i-1)*50),
            'facet': 'true',
            'page': str(i),
            'shouldUseSeoMultistrategy': 'false',
            'isLoggedIn': 'false',
            'show_search_contexts': 'true',
            'access_token': token,
            } 
                    
        params.append(param)
        # print(param)
    return params
    
def scrape_data(param):
    headers = {
        'authority': 'api.bukalapak.com',
        'accept': 'application/json',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'origin': 'https://www.bukalapak.com',
        'referer': 'https://www.bukalapak.com/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-device-ad-id': '7e230b6758350eb328dbfd1b30057444',
        }

    params = param

    req = requests.get(url, params=params, headers=headers).json()
    rows = req['data']
    
    scrape_data = []
    for i in range(0, len(rows)):
        toko = rows[i]['store']['name']
        lokasi = rows[i]['store']['address']['city']
        nama_produk = rows[i]['name']
        harga = rows[i]['price']
        stok = rows[i]['stock']
        link = rows[i]['url']
        kondisi = rows[i]['condition']
        
        scrape_data.append(
            (toko, nama_produk, lokasi, harga, stok, kondisi, link)
        )
    return scrape_data
    
    
def save_to_xlsx(df):
    df.to_excel(f'{cari}_{jlmrow}_bukalapak.xlsx', index=False)
    print(f'Data sudah disimpan di file "{cari}_{jlmrow}_bukalapak.xlsx"')    
    
    
if __name__ == '__main__':  
    # reqc = requests.get(url, params=p, headers=h).json()
    # tot_pg = reqc['meta']['total_pages']
    # print("Total Page : ", tot_pg)
    params = get_params()
    all_data = []
    for i in range(0, len(params)):
        param = params[i]
        data = scrape_data(param)
        # print(i)
        all_data.extend(data)
            
    df = pd.DataFrame(all_data, columns=['Nama Toko', 'Nama', 'Lokasi', 'Harga', 'Stok', 'Kondisi', 'Link'])
    print(df)
    jlmrow = len(df.axes[0])
    quit = input("Apakah Hasil Akan disimpan? Y/N : ")
    if  quit == "Y" or quit =="y":
        save_to_xlsx(df)
    exit()