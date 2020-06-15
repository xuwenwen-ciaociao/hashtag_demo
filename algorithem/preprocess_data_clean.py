import re
def hashtags_clean(hashtags):
    hahstags_removesymbol = re.sub(r'[\[\]]', '', hashtags)
    hahstags_removesymbol2 = re.sub(r'[#]', '', hahstags_removesymbol)
    hahstags_removesymbol4 = re.sub(r'[\"]', '', hahstags_removesymbol2)

    return hahstags_removesymbol4