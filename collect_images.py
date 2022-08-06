# from icrawler.builtin import GoogleImageCrawler

# google_crawler = GoogleImageCrawler(storage={'root_dir': 'data/nanami'})
# google_crawler.crawl(keyword='橋本奈々未', max_num=500)

#=========================================================================
# 上記にて、Googleからスクレイピングするのは禁止されているため、Bingからスクレイピング
# see: https://senablog.com/python-icrawler-image-scraping/
#=========================================================================

"""
Bingから画像をスクレイピング
"""

from icrawler.builtin import BingImageCrawler

actresses = {'aragaki': '新垣結衣', 'hirose': '広瀬すず', 'ishihara': '石原さとみ', 'takei': '武井咲'}

for key, value in actresses.items():
    crawler = BingImageCrawler(storage={'root_dir': f'Original/{key}'}) # ダウンロード先のディレクトリを指定
    crawler.crawl(keyword=value, max_num=600) # クロール実行

# 新垣結衣
# 広瀬すず
# 石原さとみ
# 武井咲