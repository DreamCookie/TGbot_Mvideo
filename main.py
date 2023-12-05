import requests
import json

def get_data():
    cookies = {
        '__lhash_': '190aa3f058e778d01386c0bf2a6ae031',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_GUEST_ID': '23287740139',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'JSESSIONID': 'h53gltyRz4yhsr1WQV6sr9VjyqWWh9Y6vRRL8yWH5CnQk2GgNhyQ!30444480',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_REGION_ID': '1',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_YANDEX_WIDGET': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'searchType2': '3',
        'COMPARISON_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '1812257802.20480.0000',
        'bIPs': '434929338',
        'BIGipServeratg-ps-prod_tcp80_clone': '1812257802.20480.0000',
        'CACHE_INDICATOR': 'true',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        'MVID_GEOLOCATION_NEEDED': 'false',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        '__cpatrack': 'google_organic',
        '__sourceid': 'google',
        '__allsource': 'google',
        'SMSError': '',
        'authError': '',
        'advcake_track_id': '2f5303f8-a720-1163-a138-7d14e43d9cb7',
        'advcake_session_id': '9bd66cc3-f176-e6ec-e934-54edfb9449d8',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2Fe-tender-integraciya%3Futm_source%3Dgoogle%26utm_medium%3Dorganic%26utm_campaign%3Dgoogle%26utm_referrer%3Dgoogle',
        'advcake_utm_partner': 'google',
        'advcake_utm_webmaster': '',
        'advcake_click_id': '',
        '_gid': 'GA1.2.485823768.1701704467',
        '_ga': 'GA1.1.690055108.1701704467',
        'tmr_lvid': 'b2f99655803c98c796dbf8d7f57ddeba',
        'tmr_lvidTS': '1691668239553',
        'flocktory-uuid': '915c80f5-852c-4b5b-91de-73988a1a94aa-1',
        '_ym_uid': '1691668236967034356',
        '_ym_d': '1701704467',
        '_ym_isad': '1',
        'st_uid': '8f5908bacbd80cac0e661b64629d48db',
        '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"100025D5"}',
        'afUserId': '2bf55432-3f69-4296-91f0-7e5c89215cae-p',
        'AF_SYNC': '1701704467252',
        'MVID_AB_PERSONAL_RECOMMENDS': 'true',
        'MVID_AB_UPSALE': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_CASCADE_CMN': 'true',
        'MVID_CHAT_VERSION': '4.16.4',
        'MVID_CREDIT_DIGITAL': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_CROSS_POLLINATION': 'true',
        'MVID_DISPLAY_ACCRUED_BR': 'true',
        'MVID_EMPLOYEE_DISCOUNT': 'true',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PODELI_PDP': 'true',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SERVICE_AVLB': 'true',
        'MVID_SINGLE_CHECKOUT': 'true',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_ENVCLOUD': 'prod2',
        'mindboxDeviceUUID': '1ac638a4-1e0f-40ed-80cc-90995853317b',
        'directCrm-session': '%7B%22deviceGuid%22%3A%221ac638a4-1e0f-40ed-80cc-90995853317b%22%7D',
        '_ga_CFMZTSS5FM': 'GS1.1.1701767641.2.1.1701769312.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1701767641.2.1.1701769312.48.0.0',
        '_sp_id.d61c': '11aaa497-015a-4955-a15d-93484c7baead.1701704467.2.1701769313.1701704467.08614fbb-6880-4cfd-b090-d2713f9d71ed.0db30c41-8976-4065-8911-a41528f0a794.99194035-53da-44da-b5b3-28b04e7078b1.1701767641830.40',
        'tmr_detect': '1%7C1701769315767',
        '_gp100025D5': '{"utm":"-2e849f2c","hits":6,"vc":1,"ac":1,"a6":1}',
        'gsscgib-w-mvideo': 'lf+sZDMRPO+x69jbnHJD7fe192T5Arw+E0VbGKW+2y2Xc3bHfQnTA8m9lMr4oBjI4TIrrTEbRJZpYCl+ANDydjwbMc/AzAP4GKagNM1/kGCr91dTDl4YFKDLy7RxOVSZkAtbJHKGLiex3iIet6xeAL7Ynt4MWPabzF7amQzUIl11NAWM1u6FjeSaWi8eZnXzp16DUtBJXKdZqmSc7/PGtUny71aXZlXLPzTu+rp5yGt4y0ciSGiRLu1o/w2Ws1cXyC3RyBg2QNVFJqxnlOz0cg==',
        'gsscgib-w-mvideo': 'lf+sZDMRPO+x69jbnHJD7fe192T5Arw+E0VbGKW+2y2Xc3bHfQnTA8m9lMr4oBjI4TIrrTEbRJZpYCl+ANDydjwbMc/AzAP4GKagNM1/kGCr91dTDl4YFKDLy7RxOVSZkAtbJHKGLiex3iIet6xeAL7Ynt4MWPabzF7amQzUIl11NAWM1u6FjeSaWi8eZnXzp16DUtBJXKdZqmSc7/PGtUny71aXZlXLPzTu+rp5yGt4y0ciSGiRLu1o/w2Ws1cXyC3RyBg2QNVFJqxnlOz0cg==',
        'fgsscgib-w-mvideo': 'rIlp59659b4cf33bfa3217ab7392163ccea64785',
        'fgsscgib-w-mvideo': 'rIlp59659b4cf33bfa3217ab7392163ccea64785',
        '__js_p_': '342,1800,0,1,0',
        '__jhash_': '313',
        '__jua_': 'Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F119.0.0.0%20Safari%2F537.36',
        '__hash_': 'cfad9dee6c713d399763c94890af3dc1',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'baggage': 'sentry-environment=production,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=80ccb932fe3343e6a75aecc10d1fbc02,sentry-sample_rate=0.5,sentry-transaction=%2F**%2F,sentry-sampled=false',
        # 'cookie': '__lhash_=190aa3f058e778d01386c0bf2a6ae031; MVID_CITY_ID=CityCZ_975; MVID_GUEST_ID=23287740139; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; JSESSIONID=h53gltyRz4yhsr1WQV6sr9VjyqWWh9Y6vRRL8yWH5CnQk2GgNhyQ!30444480; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_REGION_ID=1; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=3; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; flacktory=no; BIGipServeratg-ps-prod_tcp80=1812257802.20480.0000; bIPs=434929338; BIGipServeratg-ps-prod_tcp80_clone=1812257802.20480.0000; CACHE_INDICATOR=true; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; MVID_GEOLOCATION_NEEDED=false; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; __cpatrack=google_organic; __sourceid=google; __allsource=google; SMSError=; authError=; advcake_track_id=2f5303f8-a720-1163-a138-7d14e43d9cb7; advcake_session_id=9bd66cc3-f176-e6ec-e934-54edfb9449d8; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2Fe-tender-integraciya%3Futm_source%3Dgoogle%26utm_medium%3Dorganic%26utm_campaign%3Dgoogle%26utm_referrer%3Dgoogle; advcake_utm_partner=google; advcake_utm_webmaster=; advcake_click_id=; _gid=GA1.2.485823768.1701704467; _ga=GA1.1.690055108.1701704467; tmr_lvid=b2f99655803c98c796dbf8d7f57ddeba; tmr_lvidTS=1691668239553; flocktory-uuid=915c80f5-852c-4b5b-91de-73988a1a94aa-1; _ym_uid=1691668236967034356; _ym_d=1701704467; _ym_isad=1; st_uid=8f5908bacbd80cac0e661b64629d48db; _gpVisits={"isFirstVisitDomain":true,"idContainer":"100025D5"}; afUserId=2bf55432-3f69-4296-91f0-7e5c89215cae-p; AF_SYNC=1701704467252; MVID_AB_PERSONAL_RECOMMENDS=true; MVID_AB_UPSALE=true; MVID_ALFA_PODELI_NEW=true; MVID_CASCADE_CMN=true; MVID_CHAT_VERSION=4.16.4; MVID_CREDIT_DIGITAL=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_CROSS_POLLINATION=true; MVID_DISPLAY_ACCRUED_BR=true; MVID_EMPLOYEE_DISCOUNT=true; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_MINDBOX_DYNAMICALLY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PODELI_PDP=true; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICE_AVLB=true; MVID_SINGLE_CHECKOUT=true; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod2; mindboxDeviceUUID=1ac638a4-1e0f-40ed-80cc-90995853317b; directCrm-session=%7B%22deviceGuid%22%3A%221ac638a4-1e0f-40ed-80cc-90995853317b%22%7D; _ga_CFMZTSS5FM=GS1.1.1701767641.2.1.1701769312.0.0.0; _ga_BNX5WPP3YK=GS1.1.1701767641.2.1.1701769312.48.0.0; _sp_id.d61c=11aaa497-015a-4955-a15d-93484c7baead.1701704467.2.1701769313.1701704467.08614fbb-6880-4cfd-b090-d2713f9d71ed.0db30c41-8976-4065-8911-a41528f0a794.99194035-53da-44da-b5b3-28b04e7078b1.1701767641830.40; tmr_detect=1%7C1701769315767; _gp100025D5={"utm":"-2e849f2c","hits":6,"vc":1,"ac":1,"a6":1}; gsscgib-w-mvideo=lf+sZDMRPO+x69jbnHJD7fe192T5Arw+E0VbGKW+2y2Xc3bHfQnTA8m9lMr4oBjI4TIrrTEbRJZpYCl+ANDydjwbMc/AzAP4GKagNM1/kGCr91dTDl4YFKDLy7RxOVSZkAtbJHKGLiex3iIet6xeAL7Ynt4MWPabzF7amQzUIl11NAWM1u6FjeSaWi8eZnXzp16DUtBJXKdZqmSc7/PGtUny71aXZlXLPzTu+rp5yGt4y0ciSGiRLu1o/w2Ws1cXyC3RyBg2QNVFJqxnlOz0cg==; gsscgib-w-mvideo=lf+sZDMRPO+x69jbnHJD7fe192T5Arw+E0VbGKW+2y2Xc3bHfQnTA8m9lMr4oBjI4TIrrTEbRJZpYCl+ANDydjwbMc/AzAP4GKagNM1/kGCr91dTDl4YFKDLy7RxOVSZkAtbJHKGLiex3iIet6xeAL7Ynt4MWPabzF7amQzUIl11NAWM1u6FjeSaWi8eZnXzp16DUtBJXKdZqmSc7/PGtUny71aXZlXLPzTu+rp5yGt4y0ciSGiRLu1o/w2Ws1cXyC3RyBg2QNVFJqxnlOz0cg==; fgsscgib-w-mvideo=rIlp59659b4cf33bfa3217ab7392163ccea64785; fgsscgib-w-mvideo=rIlp59659b4cf33bfa3217ab7392163ccea64785; __js_p_=342,1800,0,1,0; __jhash_=313; __jua_=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F119.0.0.0%20Safari%2F537.36; __hash_=cfad9dee6c713d399763c94890af3dc1',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/tolko-v-nalichii=da/skidka=da',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '80ccb932fe3343e6a75aecc10d1fbc02-acaa6c239f336b86-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'x-set-application-id': 'c1b81847-63c8-45cd-8100-98090edf8c68',
    }

    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
            'WyJza2lka2EiLCIiLCJkYSJd',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    print(response)
    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    # print(products_ids)
    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()


    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get('body').get('products')))
    products_ids_str = ','.join(products_ids)
    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
        }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()
    print(response)
    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')
    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice' : item_base_price,
            'item_salePrice' : item_sale_price,
            'item_bonus' : item_bonus
        }
    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)
    
    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]
        
        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')
    
    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    #get_data()
    get_result()




if __name__ == '__main__':
    main()