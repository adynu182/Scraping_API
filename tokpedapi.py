import requests
import json
import pandas as pd
import sys, os
import re

url = 'https://gql.tokopedia.com/graphql/SearchProductQueryV4'
 
headers = {
      'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
      'Tkpd-UserId': '232707250',
      'X-Version': 'b078a1e',
      'sec-ch-ua-mobile': '?0',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
      'content-type': 'application/json',
      'accept': '*/*',
      'Referer': 'https://www.tokopedia.com/search?st=&q=spidol&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource=',
      'X-Source': 'tokopedia-lite',
      'x-device': 'desktop-0.0',
      'X-Tkpd-Lite-Service': 'zeus',
      'sec-ch-ua-platform': '"Windows"',
    }

def get_tes_param(i):

    
    param = "device=desktop&navsource=&ob=23&page={}&q={}&related=true&rows=60&safe_search=false&scheme=https&shipping=&source=search&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product&start={}&topads_bucket=true&unique_id=f4f82d8fb302f3cb843b59e665c3e3d3&user_addressId=&user_cityId=176&user_districtId=2274&user_id=232707250&user_lat=&user_long=&user_postCode=&user_warehouseId=12210375&variants=&warehouses=12210375%232h%2C0%2315m".format(i, cari, (i-1)*60)

    payload = [
          {
            "operationName": "SearchProductQueryV4",
            "variables": {
              "params": param
              },
            "query": "query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      componentId\n      __typename\n    }\n    data {\n      banner {\n        position\n        text\n        imageUrl\n        url\n        componentId\n        trackingOption\n        __typename\n      }\n      backendFilters\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        componentId\n        trackingOption\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        position\n        trackingOption\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            wishlist\n            shop {\n              city\n              isOfficial\n              isPowerBadge\n              __typename\n            }\n            ads {\n              adsId: id\n              productClickUrl\n              productWishlistUrl\n              shopClickUrl\n              productViewUrl\n              __typename\n            }\n            badges {\n              title\n              imageUrl\n              show\n              __typename\n            }\n            ratingAverage\n            labelGroups {\n              position\n              type\n              title\n              url\n              __typename\n            }\n            componentId\n            __typename\n          }\n          componentId\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        componentId\n        trackingOption\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          adsId: id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        customVideoURL\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          url\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        ratingAverage\n        shop {\n          shopId: id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      violation {\n        headerText\n        descriptionText\n        imageURL\n        ctaURL\n        ctaApplink\n        buttonText\n        buttonType\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
          }
        ]
    
    return payload
    
def cari_page():
    
    i = 256
    a = i
    sv = 0
    while a >= 1:  
        payload = get_tes_param(i)
        req = requests.post(url, headers=headers, json=payload).json()
        rows = req[0]['data']['ace_search_product_v4']['data']['products']
        qq = len(rows)
        
        if qq > 0 :
            sv = i
            a = a//2
            i = i + a
        else:
            a = a//2
            i = i - a
    # else: 
        # print('Total Page ', sv)
    return sv

def get_params():
    sv = cari_page()
    print('Total Page ', sv)
    jlmpg = int(input("Input Jumlah Page yang akan di Scrap : "))
    params=[]
    for i in range(1, jlmpg+1):
        param = "device=desktop&navsource=&ob=23&page={}&q={}&related=true&rows=60&safe_search=false&scheme=https&shipping=&source=search&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&st=product&start={}&topads_bucket=true&unique_id=f4f82d8fb302f3cb843b59e665c3e3d3&user_addressId=&user_cityId=176&user_districtId=2274&user_id=232707250&user_lat=&user_long=&user_postCode=&user_warehouseId=12210375&variants=&warehouses=12210375%232h%2C0%2315m".format(i, cari, (i-1)*60)
        params.append(param)
    return params

def scrape_data(param):
    payload = [
      {
        "operationName": "SearchProductQueryV4",
        "variables": {
          "params": param
        },
        "query": "query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      componentId\n      __typename\n    }\n    data {\n      banner {\n        position\n        text\n        imageUrl\n        url\n        componentId\n        trackingOption\n        __typename\n      }\n      backendFilters\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        componentId\n        trackingOption\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        position\n        trackingOption\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            wishlist\n            shop {\n              city\n              isOfficial\n              isPowerBadge\n              __typename\n            }\n            ads {\n              adsId: id\n              productClickUrl\n              productWishlistUrl\n              shopClickUrl\n              productViewUrl\n              __typename\n            }\n            badges {\n              title\n              imageUrl\n              show\n              __typename\n            }\n            ratingAverage\n            labelGroups {\n              position\n              type\n              title\n              url\n              __typename\n            }\n            componentId\n            __typename\n          }\n          componentId\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        componentId\n        trackingOption\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          adsId: id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        customVideoURL\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          url\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        ratingAverage\n        shop {\n          shopId: id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      violation {\n        headerText\n        descriptionText\n        imageURL\n        ctaURL\n        ctaApplink\n        buttonText\n        buttonType\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
      }
    ]

    try:
        req = requests.post(url, headers=headers, json=payload).json()
        rows = req[0]['data']['ace_search_product_v4']['data']['products']
    except KeyError:
        return scrape_data

    scrape_data = []
    for i in range(0, len(rows)):
        nama = rows[i]['name']
        
        hrg = rows[i]['price']
        hr = ""
        for y in hrg:
            if y.isdigit():
              hr += y
        harga = int(hr)
        
        if rows[i]['ratingAverage'] == "":
            rating = 0
        else:
            rating = float(rows[i]['ratingAverage'])
            
        toko = rows[i]['shop']['name']
        lokasi = rows[i]['shop']['city']
        link = rows[i]['url']
        jlm_review = rows[i]['countReview']
        
        try:
            ts = rows[i]['labelGroups'][0]
        except Exception as e:
            # print(e)
            terjual = 0
        else:
            ltrj = rows[i]['labelGroups']
            for j in range(0, len(ltrj)):
                pss = ltrj[j]['position']
                if pss == "integrity":
                    terjual = ltrj[j]['title']
                    angka = re.findall('[0-9]+', terjual)
                    if terjual.find('rb+')  > 0:
                        terjual = (int(*angka))*1000
                    else:
                        terjual = int(*angka)
                    break
                else:
                    terjual = 0
        
        scrape_data.append(
            (nama, harga, rating, terjual, toko, lokasi, jlm_review, link)
        )
    return scrape_data
    
def save_to_xlsx(df):
    subdir = sys.path[0]
    try:
        subdir = subdir.replace('\\','/') 
        os.mkdir(f'{subdir}/DataExcel/') 
    except FileExistsError:  
        subdir = f'{subdir}/DataExcel/'
    df.to_excel(f'{subdir}{cari}_{jlmrow}_tokopedia.xlsx', index=False)
    print(f'Data sudah disimpan di file "{cari}_{jlmrow}_Tokopedia.xlsx"')

if __name__ == '__main__':
    cari = input("Masukan Kata Kunci : ")
    prm = get_params()
    all_data = []
    for i in range(0, len(prm)):
        param = prm[i]
        data = scrape_data(param)
        print(i)
        all_data.extend(data)
            
    df = pd.DataFrame(all_data, columns=['Nama Produk', 'Harga', 'Rating', 'Terjual', 'Nama Toko', 'lokasi', 'Jumlah Review', 'Link Produk'])
    print(df)
    jlmrow = len(df.axes[0])
    quit = input("Apakah Hasil Akan disimpan? Y/N : ")
    if  quit == "Y" or quit =="y":
        save_to_xlsx(df)
    exit()