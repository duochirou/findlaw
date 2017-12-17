from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(("scrapy crawl findlaw -L WARNING").split())
#scrapy crawl quotes -o quotes.json
# scrapy crawl quotes -o quotes.jl
