import hashlib
data = {
    "api_key": "23e7f28019e8407b98b84cd05b5aef2c",
    "app_name": "shop_android",
    "app_version": "7.45.6",
    "channel_flag": "0_1",
    "client": "android",
    "client_type": "android",
    "context": "",
    "darkmode": "0",
    "deeplink_cps": "",
    "did": "0.0.8b7c1485b5c14a39511af05c7ab3fe77.1c7d15",
    "extParams": "{\"showSellPoint\":\"1\",\"mclabel\":\"1\",\"cmpStyle\":\"1\",\"ic2label\":\"1\",\"reco\":\"1\",\"vreimg\":\"1\",\"floatwin\":\"1\",\"preheatTipsVer\":\"4\",\"exclusivePrice\":\"1\",\"stdSizeVids\":\"\",\"rank\":\"2\",\"couponVer\":\"v2\",\"live\":\"1\"}",
    "fdc_area_id": "103102102106",
    "mars_cid": "ca80df7a-08a6-3f45-9ed5-212f6205aed2",
    "mobile_channel": "kowd7uq2:::",
    "mobile_platform": "3",
    "other_cps": "",
    "page_id": "page_te_commodity_search_1698026503833",
    "phone_model": "Pixel 4",
    "productIds": "6920468238887599571,6920201626111489235,6920494379145106643,6920505600051864787,6920513277897073875,6920401603189915987,6920260684243911507,6920474112576265683,6920472644902059475,6919453468868617043,6920513277897061587,6920403066637577683,6920442067411766547,6920504144689169619,6920513176371332307,6920482408805473747,6920401603206828371,6920504144689288403,6920516119363553747,6920201626128426195",
    "province_id": "103102",
    "referer": "com.achievo.vipshop.search.activity.VerticalTabSearchProductListActivity",
    "rom": "Dalvik/2.1.0 (Linux; U; Android 10; Pixel 4 Build/QQ2A.200405.005)",
    "scene": "search",
    "sd_tuijian": "0",
    "session_id": "ca80df7a-08a6-3f45-9ed5-212f6205aed2_shop_android_1698026465696",
    "skey": "2d30297ff20ec9b7442dc4f3c335abdc",
    "source_app": "android",
    "standby_id": "kowd7uq2:::",
    "sys_version": "29",
    "timestamp": "1698026513",
    "warehouse": "VIP_SH"
}
string = ""
for key, value in data.items():
    string += f"{key}={value}&"
# 去除末尾的"&"符号
string = string[:-1]
str = 'a84c5883206309ad076deea939e850dc'+string
sign1 = hashlib.sha1(str.encode('utf-8')).hexdigest()
api_sign = hashlib.sha1(('a84c5883206309ad076deea939e850dc'+sign1).encode('utf-8')).hexdigest()
print(api_sign)