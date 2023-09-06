import requests
import json
import pandas as pd
import time
import random

key = input("Masukan Kata Kunci : ")

headers = {
    'authority': 'affiliate.shopee.co.id',
    'method': 'GET',
    'path': '/api/v3/offer/product/list?list_type=0&keyword=earphone&sort_type=1&page_offset=0&page_limit=20&client_type=1',
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'affiliate-program-type': '1',
    'cookie': '_gcl_au=1.1.493501351.1691111613; _fbp=fb.2.1691111614484.620002206; REC_T_ID=22db79ff-3264-11ee-a78a-f4ee082619f5; SPC_F=5QcIgUE18FhYCIv89toRTIQ9hDyc282x; SPC_CLIENTID=NVFjSWdVRTE4RmhZwacmjapqayykuhzk; SC_DFP=yWvtXTHkKPMeKnjqgNTUNouMEhNNGkWb; _med=refer; SPC_SI=cYPkZAAAAABKU2FHMmJnRorSggAAAAAAc3N5ZG9TbUs=; SPC_U=90470252; SPC_R_T_ID=HmueTIdumwixCPmuFlbuKvWFLUIUCWytZAZP7Lf99MtWZBKvH/pnpuyk5ZawfCJagqyKbUOiVjKsZtgs9Vzs66WiobAducWw9FXph9+c8ntQ6zyF6VEWRqNRcokh6SS/RX+H3ollNshKkhmWQjbP83CChaXGq0WrzjVT0ZGPM7c=; SPC_R_T_IV=NmdjVnZTMGJmaVdrN3V1bQ==; SPC_T_ID=HmueTIdumwixCPmuFlbuKvWFLUIUCWytZAZP7Lf99MtWZBKvH/pnpuyk5ZawfCJagqyKbUOiVjKsZtgs9Vzs66WiobAducWw9FXph9+c8ntQ6zyF6VEWRqNRcokh6SS/RX+H3ollNshKkhmWQjbP83CChaXGq0WrzjVT0ZGPM7c=; SPC_T_IV=NmdjVnZTMGJmaVdrN3V1bQ==; _ga_8TJ45E514C=GS1.1.1693191352.1.1.1693191864.58.0.0; _gid=GA1.3.1775482023.1693293010; SPC_ST=.cEFmVEtuZWlQWnZ2NEZMSuTduHlagepr6elfqmJckFIEPevFFcsjZOiJ+Iu6u0s2M7tK3bXagi0+UGDf4UiU128TBz4Uwb1qx+BgBTWkbRUtl1XTM9QUbl6ldrv4oZXorubI6QoAyN37xQ4TrIPS2KGA9n3ihKKXr3pgrQPx76xc2VYBw5q7N00yXe0K8nMz+OIX9ftLTqaQs4gquFFYug==; _ga=GA1.3.271571051.1693293010; SPC_EC=ZWRMYlZOcDhMVk91YW84Obl3A+tWvTFjpOib2aKT2kf1tgnnInLRTI00eAsClWCOch0GjTv7dhB6jNU2gGuDYJKxhaWxY9MTV6CQTqHlr/t9Zv4QVgBMdgHgZVtIzAxheD00HZiRhoVQMP954Mx3fp13r8caBfklfeKDi183kbk=; _ga_SW6D8G0HXK=GS1.1.1693312661.4.1.1693312748.60.0.0; _dc_gtm_UA-61904553-8=1; language=id',
    'csrf-token': 'RSBkeiJ9-Lh9hT6MCystEr5Z4wITWsmFEvok',
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
    
    urlcc = f"https://affiliate.shopee.co.id/api/v3/offer/product/list?list_type=0&keyword=earphone&sort_type=1&page_offset=0&page_limit=20&client_type=1"
    resc = requests.get(urlcc, headers=headers).json()
    tot = int(resc['data']['total_count'])
    pg = int(tot//20)
    print("Total Page : ", pg)
    pg = int(input("Input Jumlah Page yang akan di Scrap : "))
    
    for page in range (0, pg):
    #for page in range(0, 10):
        url = f"https://affiliate.shopee.co.id/api/v3/offer/product/list?list_type=0&keyword={key}&sort_type=1&page_offset={offset}&page_limit=20&client_type=1"
        res = requests.get(url, headers=headers).json()
        rows = res['data']['list']
        time.sleep(random.randint(2, 5))
        offset += 20
        print(page)
        
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
    df.to_excel(f'{key}_{jlmrow}_shoopeaffiliate.xlsx', index=False)
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