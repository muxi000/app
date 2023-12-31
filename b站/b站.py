import hashlib
from urllib.parse import quote, unquote
params = {
    "ad_extra": "E86F4CFF1F8FA890A75155EEAA51E6AE4FA9DBE62FCE708186D0CE5EF37B86948620D8BA1D991685B1288E2EDE09C6D52F8C2D33D59872EAE1EB776D11F71523CE1AF2112D8A950B98F6A1A48F848BC6871A849C3ED14308F46431A85625726A929A8906FA0C16FEE2CEB33209AE6F1E0C6856961045F53A0FE3470E4E223F48DAE7923040EAC4541BE6F728DEA350329AC40887CB773083BB4D6D91DCCCDF8D16C5672A5E344293F5EFD2F3654B88602781A8869076E96FF8359FC76D3CD5851A733D0CF38E11DC869D660D1624928815C2A13497B215CCEA52053B302039B9B93DFABDD6A71A16AC8898285A37C7DEB5AB5ADD788C2456B5D9B2F8FDB1ACD334E8127D56B144B523155DE8AB49A1D1173CB590E379CCF33EFAE8C388100D5CEA7AD220E2AAA2256FF16D4BE28C8AA3D7BAE19B1FE6AA860276BB86B27ACCA34B8E081D67E8C699CF4ED4D7A45E8556B05584B35B1E11E80B9B41DC51C47B260C602E07B1936C73DDB8D7FFBBD148894822C5F7C9A688C5A25DB2CA92D77CA7C35E3AFD807D0AE95967943A42B30D0F0EF8EAD9D2E74A20BB4EA72014B5A3BFD53B2ECFB15B47455D97A4FBFDDFB4A3E30853E0B9CBF16AC70F25CB6B939540328256BF42AB6DF9D3DD4649E3F0B340376B162F859D5EE92D99A778FB313E28BCAD195FB59A30EC374436735A9732BF013A78FE3F606425B48A74137C267DAB91A00962C5FFECB7E798AC130FCF7F9428A05082C6D717D13F129F809818E05DB11EA3DE2EA80728D30DB7EECAE1231085C4E3B47B98506F261D89D15997AC09FB46DBA3444A438F43A59D232385F3C5548DFF3F51733A80A80880E7945035A18DCDDCDEB85A2DCCF755CD1AEBCA759CB2BE4AF6D5AB3A9FA8F7429DD37B740E33D80E1F11B8BD4DD312DEAECEEBAB7DC6FF57EFC5A81D3D7D02E798AA5CDCD387EAD885EE8D89368FA301463658FA52",
    "appkey": "1d8b6e7d45233436",
    "autoplay_card": "11",
    "autoplay_timestamp": "0",
    "build": "7500300",
    "c_locale": "zh-Hans_CN",
    "channel": "alifenfa",
    "column": "2",
    "column_timestamp": "0",
    "device_name": "Pixel 4",
    "device_type": "0",
    "disable_rcmd": "0",
    "flush": "8",
    "fnval": "464",
    "fnver": "0",
    "force_host": "0",
    "fourk": "1",
    "guidance": "0",
    "https_url_req": "0",
    "idx": "1698066410",
    "inline_danmu": "2",
    "inline_sound": "1",
    "interest_id": "0",
    "login_event": "0",
    "mobi_app": "android",
    "network": "wifi",
    "open_event": "",
    "platform": "android",
    "player_net": "1",
    "pull": "false",
    "qn": "32",
    "recsys_mode": "0",
    "s_locale": "zh-Hans_CN",
    "splash_id": "",
    "statistics": "{\"appId\":1,\"platform\":3,\"version\":\"7.50.0\",\"abtest\":\"\"}",
    "ts": "1698066416",
    "video_mode": "1",
    "voice_balance": "0",
    # "sign": "002c2395f37e8800095c41e08b652517"
}
sorted_params = sorted(params.items(), key=lambda x: x[0])
sorted_str = '&'.join([f'{k}={v}' for k, v in sorted_params])

print(sorted_str)
original_string = sorted_str
# 分割字符串，然后仅对值进行编码
parts = original_string.split("&")
encoded_parts = []
for part in parts:
    key, value = part.split("=")
    encoded_value = quote(value)
    encoded_parts.append(f"{key}={encoded_value}")
# 重新组合编码后的部分
encoded_string = "&".join(encoded_parts)

# 盐值 560c52ccd288fed045859ed18bffd973
str = encoded_string+'560c52ccd288fed045859ed18bffd973'
sign = hashlib.md5(str.encode('utf-8')).hexdigest()
print(sign)

