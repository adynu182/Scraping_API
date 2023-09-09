import requests
import pandas as pd
import math
import time
import random

cari = input("Masukan Kata Kunci : ")

base_url = 'https://www.lazada.co.id/tag/dslr/?_keyori=ss&ajax=true&catalog_redirect_tag=true&from=input&isFirstRequest=true&page=1&q={cari}&spm=a2o4j.home.search.go.579953e0qcLIT0'

headers = {
'authority': 'www.lazada.co.id',
'method': 'GET',
'scheme': 'https',
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'bx-v': '2.5.1',
'cookie': '__wpkreporterwid_=e1e48345-52de-4bf7-9190-9b3d9b53388c; lzd_cid=5179446e-9ced-41bc-ea5b-dc6a3a8b9f2b; t_uid=5179446e-9ced-41bc-ea5b-dc6a3a8b9f2b; hng=ID|id|IDR|360; userLanguageML=id; xlly_s=1; t_fv=1693202983545; cna=KShzHcqPoBECAXIE1DsjxJuc; _bl_uid=q7lmql5sudph81cOC8Cmw3kdm1jm; _gcl_au=1.1.1603069516.1693393288; _uetsid=9f1a48b0472411ee83be279481ebc12c; _uetvid=9f1a91f0472411eeaf9fe3b6bce012f1; _fbp=fb.2.1693393311211.1958124869; cto_bundle=8TMfNV9QSjQ4SFIlMkJkaGlvT2JKazAyMWczTWpqQk9XcmpqWEVncDBSWjVDQTlkODFtQyUyQjVLcDNvNlNLR3RNb0RTU290dDZDNkVqTmxZS2doQUhBVnZBTk1NMmJoVExYNkQlMkJlZHl2RFF5Q25QeUU0VDZHY3BKUDRpb01zU0xhbVMlMkZKdTVQVnk0c1lCeXNVc2UzNXM5V3FMcWYzUSUzRCUzRA; AMCV_126E248D54200F960A4C98C6%40AdobeOrg=-1124106680%7CMCIDTS%7C19600%7CMCMID%7C16495244756288265824603856252365736687%7CMCAAMLH-1693998118%7C3%7CMCAAMB-1693998118%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1693400518s%7CNONE%7CvVersion%7C5.2.0; lwrid=AQGKRhvhOh7zQDK8CTPxX39uI26G; bm_mi=5C36998EECF2835F333C8BDC6589C1D1~YAAQT6gEchiyY0iKAQAAWcp/SRT6c8yPq8UszZ+OPpZMcjWucH+3RAgA4mMyQbM3qpEGPbEh/5gbFP6glh1N/T0zVD8lDB/3L5uUtRJLfB+sZN12a4DQsJLmn7mk9MwFkVSthp6sNAWBeuOUcK5dUAdopphXBmDtHWwg1u75wvDzGuNM5QjReiD6hbSkS3nRNa1Izt4IJd1+RodIaMy3m6ZigoalQgFlyaXEKtg0Ae6bdJqbpKfrKpLFwwVXHlTqZ4gtXESOroOJTia/59pj7PrvO7TPrvZIcnZDq0vdIcxVISaKL7c4l3dhTJcz4+sy~1; _m_h5_tk=e107e7e681be922d36017160565f2442_1693457427190; _m_h5_tk_enc=20c500dc203ed5be39bcfb0647cf2b0a; lzd_sid=166ab5406f6df68604d98f1c4c5c5577; _tb_token_=e835e75e333ae; t_sid=3b1WANWDyShDk3vsT0YCdXLNHoUqnnaM; utm_channel=NA; ak_bmsc=2C14309052EA0A6ADF2FF4FC6CECEDC7~000000000000000000000000000000~YAAQT6gEcp21Y0iKAQAAYg2ASRTDAhYa7XsjnVopAtNO2jQ5qg+vuDdYMLfPACRHh/PFMXYdAUHuKyf7vXt854T4AkzDnLHCtY9DH+Xaj61jGe24qXgKsv/TZI3xGj4Kuep64luBcC0WXSvb5GusdEnll6KZ3RmA85xtKsrLg8WtRtHqbP+Dwnc0/hGWMTdCz759IvRiXFcNGyaY+9Ox/T4Kf3MxAEdPBSlj344LpgerkCKBiYgoUgR8nmo5ThiuC64bmSf/m9PVnUTdsongxMVySN/xD26sUuav4HUy+FwCNvgeZoLNcIgr83Zhh7v4drNHINxcLct1kRGBXCMqd3Dxb0HTRmUHWAi0rz7rAxo81usBL3NkpUkEnM5IU4G3eYtsdBB90+wC+gcr0ELul2+GMaxgeI7rX795c6atuPGiurkGUWxOpngDRRTzkGAT8ggZJ5KEUtSZR2+GSCzCaypQiqVy0rJQUtFVCXug/uYOgF7kNx/5AND7VZQ=; bm_sv=837F7504B6D50C7A8F2AE2D55DC0ACDF~YAAQr6gEcl/ei0KKAQAAs6iBSRTcE6ZNgLbRjWbYNiig4vM21RKJtnt3GhqCThzGt+Z/z99n8nbu4dtiD3jHzLQMpxXL4osByUC/KSkL7Db1c2V23jEEjX9acOglRnhi/096+95KTzJCWboRUym6cbNAAF6/8BrhpdUMALN5/aK3btBZC6syalpqKL8eGCi/F99YyUeqdYA01XF5a8Z2aOx2B+GdWMv4Au/iaOYk3W7VE02sW4S9aZ8OttwwBHpL5HQ=~1; epssw=1*gKN911gcn5UOGADMIA7GEtF1_Aj4QODwJuhXA4J13zz4uzFP1PA6Q4FwIA5eUv1CecxM6TT_blPlZMCtF1QukbO6F_sgHKZsP9GurDye1KFO_J-MjhXE_46K3Ks1d61OF9pvdtRJH9TaYM-G1AM0kdmLH66UbKRsvenDaAlroWXiav96uFuEeq4mdLenwp6-xDmnxDm3dGXIevp8zE8WPLB4NlTCij336PtUPH87BJRoeDo3YHKfxX6CYTBBeDmE; tfstk=dhLeXjjyr23UFwjkqi7ygB37UhbdSZHjTU65ZQAlO9X3RywkbdpzNXH-vhWyIOOBPwDdz_vWI99C-U-TzIdJRXQS9wddyaDjhqMX9BQ-JJyMYZsdc5NJDxgjlBnYSraxhYQX9Ujir_2EuPs_NQ6MRaUN3tFYE9auremdYtuhK1CM7usChBYEpO77e1jIfUKUEuSh61Wj_fonnOcl.; l=fBMGyqpqN7rUaY5jBO5alurza779WQRf1sPzaNbMiIEGa6OOgtzpRNC6kELvzdtjQT55Hetz_ANlDdF9yYz38xtSVX3iysUDfXpMReiduzKl.; isg=BEpKM7qdGnXwUpbFPtvohUpzmzDsO86V9-x2ttSBDB0Vh-lBvM-ppOCxl-tbd0Yt',
'referer': 'https://www.lazada.co.id/',
'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
'x-csrf-token': 'e835e75e333ae',
'x-requested-with': 'XMLHttpRequest',
'x-ua': '140#1mFrGBQXzzZgLzo2Kin+wpSrrpk16Qsn17u7RAEn6vqwj4PfUlOb0EsOkdFn8SU/+qp+isnVL5iYVu2+LQsslp1zzq6pWC73Ezzx0oqxatluzzrb22U3lp1xxUcsvb/xZZV/4IAu03vXxzFi2Duvlp1xzLbDCzEPxrvZrI7Zbh1aLGGSYMVlGNeGQ2aAACpeVIIF8HqliZpuuqu304kU8yYYUJWREQeyORJAYfA5YVq20oraWhfcDNmmimgiMUNDbizAiMC2pQ/+rN9iHMVTNRlFqOJZf6+7rcfIN10AWuETqdqygzCszjeft1B5YEnLjIU38ACGh1qPiZixfF39Jc1860ZN58qJbmHR+a5cc24Z+yY7+umYwkwx69NgEiegW6SS47QsTC86TlY9Xar0PHIauGGiFdoNJv9yLiXxguHFKurbfMNM4KgCduqNIsdXliRW6JzAwOs3QJ8og6PwzHwIUiTbsYXeZ1gIFAaC6FZp9RpnelgjU2yTy1XJBN7q80kmrhdY62kpz2YVTkmdUuO3ZmKLO5sM1tMYHP0XwybjQKboqbJCZxkDZmjJAJtYL64dVniXZ6lgEm95eRTIr4ubFCMkcn+zf29AJfxzHlarDSB/hmNSvI5ISpN+XgvdK2/elHsK4atkmWEvVpYkn0HS366WyxU+K1JC2sjraZeC4hR0JRkxPGH6aaATHRXZKnyDOqyyUgB6nVBL4eqeQxd1/0ULLiQaQw+3l+8zZIzbMpAu0cVEMeBKNeaS3VuxVT/kDn/KBEHLzkg5VbGEzB0hx44rEWRzjJ3sZyMmhZWQrZ86rsCDKXC4FjavM2SJnplkiE1v+dB+2JphoZrloUdXQKa1DspVm1NUqn1LQActeCEtkp9KjUwmacktNHWsRj++pWZRjKPGhYH4y8H2f6eJPcEd++qSflHZ7Chu9BFu9oDKbK1VqosRYzZNd1GdttffDW78ggQdGC7dB9Qsz6eSFgoxWXqGtFFA34Hr1SEIMuKSORtNW9d6WucVH4buhC+e836x3AJ8FnLu56fUwJ/7dFMrZIpwy4l3dvsst9Ot1lp4p0GV6jV9pl1YhhEKmK2QMkm/tDQUh3FMicKGDyzS1Z/q64rkVyXZgIPRfEtLWhr5caF63cY7OfDyIaoqWXc8m9UdoxAmBfPD66AQ/MGDprcXPaUtpvnbtcq/cat0aYc89JXTo7V7LPnimELs91oRtQopVBbKI+pre4U2a2B5mTHSYe6TcBc3FeA4XYwfkeCxsDJUcEaPtG8TpF2ALEr2lsBx20eNR0ARJk+YnP8L6kIv4fFjIkH3yhc4VkxSGuqyhfr64UBTZBTLv28Ode5Oy0eUiyZFCW6Zk8syZWkAq0TdelkKo0Bk8fvuIVfaTGlvvNXb8fY3Ab4rMC7MlA5DIvS7xehFmZF/5Bpe7aUBF1mr5JbfhoqGZuCjrfFmny1dGxKmpWk/T4ed9dAcT6sgBz0Kl16QLKaw+yIOvSRCMQdT+gyuAWfFIr+SRyv+e15gNbNU1o8C7o+Hnt1DGABue2QPzLy8spmIFF3Scw1smvOCJy0NxWDQTjn4j2Hi/iANc1UcemOuqnOiJ7UHX3G9cJMGVh9nPxv3P+bMIZb=',
'x-umidtoken': 'T2gAyvp-eRBTy5BWuxKRA_lj_7BIF2GlE77j7kbnKBjZTv_SD-xaWzWZQMc2QxAwiTw=',
}



def get_urls():
    req = requests.get(base_url).json()
    tot_produk = int(req['mainInfo']['totalResults'])
    pg_size = int(req['mainInfo']['pageSize'])
    ttl_pg = math.ceil(tot_produk/pg_size)
    print("Total Page : ", ttl_pg)
    ttl_pg = int(input("Input Jumlah Page yang akan di Scrap : "))
    
    urls = []
    for i in range(1, ttl_pg+1):
    #for i in range(1, 6):
        url = 'https://www.lazada.co.id/tag/dslr/?_keyori=ss&ajax=true&catalog_redirect_tag=true&from=input&isFirstRequest=true&page={}&q={}&spm=a2o4j.home.search.go.579953e0qcLIT0'.format(
            i, cari)
        urls.append(url)
    return urls


def scrape(url):
    req = requests.get(url, headers=headers).json()
    rows = req['mods']['listItems']
    
    produk_all = []
    for i in range(0, len(rows)):
        toko = rows[i]['sellerName']
        lokasi = rows[i]['location']
        nama_produk = rows[i]['name']
        harga = float(rows[i]['price'])
             
        if "originalPrice" in rows[i]:
            harga_real = float(rows[i]['originalPrice'])
        else:
            harga_real = harga
            
        if "itemSoldCntShow" in rows[i]:
            item_sold = rows[i]['itemSoldCntShow']
        else:
            item_sold = 0
        
        rating = float(rows[i]['ratingScore'])
        
        if rows[i]['review'] == "":
            review = 0
        else:
            review = int(rows[i]['review'])
            
        produk_all.append(
            (toko, lokasi, nama_produk, harga, harga_real, item_sold, rating, review)
        )
    return produk_all


def data_frame(data):
    df = pd.DataFrame(data, columns=['nama toko', 'lokasi', 'Nama Barang', 'Harga', 'Harga Real', 'Terjual', 'Rating', 'Review'])
    return df


def save_to_xlsx(df):
    df.to_excel(f'{cari}_{jlmrow}_Lazada.xlsx', index=False)
    print(f'Data sudah disimpan di file "{cari}_{jlmrow}_Lazada.xlsx"')

if __name__ == '__main__':
    urls = get_urls()

    semua_produk = []
    for i in range(0, len(urls)):
        produk = scrape(urls[i])
        time.sleep(random.randint(2, 6))
        print(i)
        semua_produk.extend(produk)

    df = data_frame(semua_produk)
    print(df)
    jlmrow = len(df.axes[0])
    quit = input("Apakah Hasil Akan disimpan? Y/N : ")
    if  quit == "Y" or quit =="y":
        save_to_xlsx(df)
    exit()
