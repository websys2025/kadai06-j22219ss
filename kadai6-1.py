import requests

APP_ID = "95c1962e3de697ab2038e4cccc135739a8ece751"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId": "0003285752",  #家計調査
    "cdArea": "04100",            #宮城県仙台市のコード
    "cdCat01": "010110000",       #米を例として表示
    "metaGetFlg": "Y",
    "cntGetFlg": "N",
    "explanationGetFlg": "Y",
    "annotationGetFlg": "Y",
    "sectionHeaderFlg": "1",
    "replaceSpChars": "0",
    "lang": "J"                   #日本語
}

response = requests.get(API_URL, params=params)
data = response.json()

#結果表示
for item in data['GET_STATS_DATA']['STATISTICAL_DATA']['DATA_INF']['VALUE']:
    print(item)

