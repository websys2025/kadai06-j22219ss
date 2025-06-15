import pandas as pd

#東京の2023年5月の日別気象データCSV
url = "https://www.data.jma.go.jp/obd/stats/etrn/view/daily/s1.csv?prec_no=44&block_no=47662&year=2023&month=5&day=&view=p1"

#pandasで読み込む
df = pd.read_csv(url, encoding="shift_jis")

#データの一部表示
print(df.head())
