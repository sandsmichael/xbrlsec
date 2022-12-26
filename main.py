from xbrl_instance import XbrlInstance
from us_gaap import UsGaap
import json

# XbrlInstance( url = "https://www.sec.gov/Archives/edgar/data/1018724/000101872422000023/amzn-20220930_htm.xml" )  #gaap
# XbrlInstance( url = "https://www.sec.gov/Archives/edgar/data/842180/000084218021000008/bbva-20201231.xml" )  # ifrs
xbrl = XbrlInstance(fp = './amzn-20220930_htm.xml')
# xbrl = XbrlInstance(fp = './bbva-20201231.xml')
parsedGaap = UsGaap().parse_gaap(xbrli = xbrl)
print(json.dumps(parsedGaap, indent = 4))
