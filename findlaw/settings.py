# -*- coding: utf-8 -*-

# Scrapy settings for findlaw project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'findlaw'

SPIDER_MODULES = ['findlaw.spiders']
NEWSPIDER_MODULE = 'findlaw.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'findlaw (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False
COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'findlaw.middlewares.FindlawSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'findlaw.middlewares.MyCustomDownloaderMiddleware': 543,
#}
DOWNLOADER_MIDDLEWARES = {
    'findlaw.middlewares.ProxyMiddleware': 543,
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'findlaw.middlewares.MyUserAgentMiddleware': 400,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'findlaw.pipelines.FindlawPipeline': 300,
#}
ITEM_PIPELINES = {
    'findlaw.pipelines.JsonWriterPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False
#CONCURRENT_REQUESTS_PER_IP = 4
CONCURRENT_REQUESTS = 16
DOWNLOAD_TIMEOUT = 60
# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
MY_USER_AGENT = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]








PROXIES = ['http://176.106.39.20:53281', 'http://190.11.26.58:52136', 'http://45.221.221.147:65205', 'http://201.16.227.225:8080', 'http://45.126.120.68:8888', 'http://110.50.85.159:8080', 'http://185.117.74.75:1080', 'http://152.231.81.122:53281', 'http://160.16.241.139:8080', 'http://45.77.174.116:1080', 'http://223.30.74.214:80', 'http://185.117.74.66:1080', 'http://117.158.57.2:3128', 'http://118.193.107.97:80', 'http://142.147.114.227:8080', 'http://181.30.101.242:3128', 'http://118.193.107.184:80', 'http://118.193.107.104:80', 'http://118.114.77.47:8080', 'http://118.193.107.209:80', 'http://104.236.103.124:3128', 'http://103.251.167.10:1080', 'http://5.2.69.166:1080', 'http://128.199.121.141:3128', 'http://5.2.69.101:1080', 'http://216.100.88.228:8080', 'http://118.193.107.142:80', 'http://66.102.228.123:8080', 'http://167.205.6.6:80', 'http://189.90.96.5:53281', 'http://139.59.2.223:8888', 'http://36.66.187.177:3128', 'http://179.126.141.72:8080', 'http://5.133.31.252:8080', 'http://5.154.37.28:53281', 'http://187.53.62.68:80', 'http://54.87.190.148:80', 'http://177.5.219.112:8080', 'http://41.76.44.76:3128', 'http://172.104.186.253:80', 'http://41.87.82.75:8080', 'http://191.240.149.251:54132', 'http://85.214.243.92:80', 'http://202.152.40.28:8080', 'http://93.64.234.126:8080', 'http://103.53.83.168:54132', 'http://54.174.39.32:8989', 'http://196.205.203.102:8080', 'http://200.149.1.106:8080', 'http://197.248.17.18:8080', 'http://36.67.50.242:8080', 'http://41.160.118.226:8080', 'http://200.151.202.186:8080', 'http://82.130.246.64:53281', 'http://189.39.241.3:53281', 'http://87.226.68.130:2020', 'http://40.87.66.157:80', 'http://182.253.125.7:3128', 'http://179.198.244.181:8080', 'http://43.250.80.226:80', 'http://180.183.198.109:8080', 'http://92.38.47.226:80', 'http://77.222.139.57:8080', 'http://222.189.238.41:3128', 'http://222.189.238.47:3128', 'http://84.241.16.50:8080', 'http://200.165.71.202:8080', 'http://54.144.57.153:80', 'http://183.89.178.119:8080', 'http://59.34.204.60:808', 'http://182.16.187.170:8080', 'http://181.168.138.192:8080', 'http://187.12.121.34:8080', 'http://202.93.230.41:1234', 'http://200.141.202.162:8080', 'http://93.150.40.94:8080', 'http://203.95.220.110:53281', 'http://213.37.198.221:80', 'http://46.35.188.7:8080', 'http://95.79.102.124:8080', 'http://37.99.214.45:3128', 'http://187.87.77.76:3128', 'http://83.18.150.52:3128', 'http://94.228.196.23:8081', 'http://77.94.122.213:8080', 'http://202.179.186.138:53281', 'http://52.38.145.107:80', 'http://203.142.66.194:8080', 'http://91.225.190.159:53281', 'http://201.49.69.251:8080', 'http://186.103.130.91:8080', 'http://187.125.23.26:8080', 'http://200.184.27.4:8080', 'http://192.158.236.57:3128', 'http://193.165.79.30:8080', 'http://187.12.116.170:8080', 'http://190.14.213.26:65103', 'http://85.202.233.46:53281', 'http://88.119.49.66:63909', 'http://196.12.154.94:8080', 'http://202.162.215.170:8080', 'http://45.116.186.13:8080', 'http://182.253.188.180:8080', 'http://187.85.255.47:53281', 'http://58.252.6.165:9000', 'http://187.76.190.74:8080', 'http://74.116.59.8:53281', 'http://221.121.12.228:8080', 'http://189.126.241.202:53281', 'http://50.93.200.253:1080', 'http://222.189.228.56:3128', 'http://177.182.217.29:8080', 'http://47.94.81.119:8888', 'http://200.199.108.34:8080', 'http://202.79.37.14:53281', 'http://187.38.178.32:3128', 'http://61.234.123.16:82', 'http://70.169.70.90:80', 'http://222.189.228.41:3128', 'http://200.216.227.141:53281', 'http://49.4.2.76:80', 'http://200.223.245.178:8080', 'http://200.141.202.178:8080', 'http://36.89.29.27:8080', 'http://217.182.92.162:3128', 'http://203.76.220.209:8080', 'http://50.93.201.250:1080', 'http://46.44.49.225:8081', 'http://200.165.177.66:8080', 'http://121.196.218.35:3128', 'http://193.34.9.140:8080', 'http://197.210.153.234:54132', 'http://191.222.149.154:8080', 'http://54.37.98.158:3128', 'http://212.117.19.215:55555', 'http://82.200.205.49:3128', 'http://94.130.245.70:3128', 'http://191.209.31.200:3128', 'http://96.9.77.135:8080', 'http://46.191.237.63:65309', 'http://189.194.115.97:8080', 'http://84.11.164.74:8080', 'http://200.217.185.179:8080', 'http://202.73.51.102:80', 'http://31.25.141.46:53281', 'http://190.12.102.205:8080', 'http://37.204.255.79:8081', 'http://186.237.53.212:8080', 'http://96.9.90.15:8080', 'http://202.74.243.112:8080', 'http://96.9.69.210:53281', 'http://96.9.79.216:62225', 'http://36.67.97.223:8080', 'http://82.147.103.97:8080', 'http://50.93.200.30:1080', 'http://50.93.202.65:1080', 'http://197.93.164.4:8080', 'http://47.104.83.184:1080', 'http://197.215.144.213:3128', 'http://191.0.70.90:8080', 'http://5.160.130.56:53281', 'http://190.79.50.124:3128', 'http://37.230.161.115:8080', 'http://177.222.248.42:8080', 'http://202.131.233.202:53281', 'http://210.186.121.103:8080', 'http://77.87.75.10:80', 'http://223.243.206.69:54132', 'http://210.56.8.143:8080', 'http://213.111.160.200:8080', 'http://177.126.89.105:8080', 'http://182.88.196.48:9797', 'http://52.230.2.226:8080', 'http://98.109.52.53:80', 'http://185.106.138.143:53281', 'http://200.96.211.228:8080', 'http://190.117.115.150:65103', 'http://201.208.98.152:8080', 'http://45.112.126.130:80', 'http://50.93.201.236:1080', 'http://182.74.200.207:80', 'http://84.241.30.132:8080', 'http://89.175.162.186:8080', 'http://64.77.242.74:3128', 'http://182.253.40.199:3128', 'http://185.81.93.232:8080', 'http://59.44.244.14:9797', 'http://176.235.99.159:8080', 'http://77.85.206.165:53281', 'http://177.69.166.124:8080', 'http://177.107.164.21:3128', 'http://43.240.102.34:8080', 'http://217.194.255.217:3128', 'http://200.128.10.63:80', 'http://186.227.213.242:8085', 'http://47.89.17.54:80', 'http://177.6.147.202:8080', 'http://208.110.116.153:65301', 'http://180.253.51.159:8080', 'http://189.80.124.122:8080', 'http://182.253.209.203:3128', 'http://177.190.197.123:3128', 'http://186.188.210.114:53281', 'http://201.165.103.3:8080', 'http://71.191.75.67:3128', 'http://78.140.6.68:53281', 'http://46.44.51.5:8081', 'http://191.184.223.96:3128', 'http://46.101.252.129:3128', 'http://194.110.77.189:8080', 'http://87.190.11.94:3128', 'http://219.244.186.30:3128', 'http://200.25.233.166:8080', 'http://89.175.58.20:3128', 'http://182.253.130.185:8080', 'http://190.77.78.148:3128', 'http://202.40.177.90:53281', 'http://196.6.232.1:8080', 'http://213.157.62.137:3128', 'http://200.114.104.4:53281', 'http://180.210.205.53:3129', 'http://177.131.49.77:3128', 'http://96.9.69.164:53281', 'http://212.110.20.141:88', 'http://5.13.171.232:8080', 'http://201.183.227.197:8080', 'http://200.232.14.226:3128', 'http://212.8.40.78:3128', 'http://93.183.245.248:53281', 'http://223.150.48.126:8888', 'http://177.154.50.77:53281', 'http://96.9.87.2:8080', 'http://49.231.146.82:3129', 'http://190.116.51.26:8080', 'http://187.60.161.68:8080', 'http://194.60.237.201:53281', 'http://180.211.134.238:65205', 'http://87.250.119.165:53281', 'http://182.52.137.215:8080', 'http://45.76.187.145:80', 'http://179.178.20.129:8080', 'http://196.201.206.121:8080', 'http://93.190.142.214:80', 'http://190.60.234.131:3128', 'http://223.206.146.75:8080', 'http://212.52.198.81:8080', 'http://187.153.95.197:8080', 'http://180.183.40.142:8080', 'http://177.19.23.214:8080', 'http://36.73.107.92:8080', 'http://50.93.197.230:1080', 'http://190.57.138.118:8000', 'http://204.11.243.70:3128', 'http://95.87.220.19:15600', 'http://180.210.205.104:3128', 'http://186.101.33.146:8080', 'http://200.30.194.77:8080', 'http://37.17.56.44:80', 'http://191.178.16.11:8080', 'http://180.250.8.74:8080', 'http://180.250.149.73:8080', 'http://194.169.206.141:8080', 'http://185.97.122.226:53281', 'http://177.159.6.25:8080', 'http://187.32.183.66:3128', 'http://96.9.79.20:55555', 'http://95.104.16.21:8080', 'http://47.89.18.250:80', 'http://203.142.73.234:8080', 'http://209.150.233.83:80', 'http://187.76.206.50:8080', 'http://187.189.26.23:53281', 'http://118.175.36.79:53281', ]



