import re


import operator
from decimal import Decimal

import pymysql

db = pymysql.connect(host='172.24.135.80', port=3306, user='root', password='123456', db='hashtag_demo')
cursor = db.cursor()

# lsit_tweet_id = []
# dict_tweet_with_score = {}
# popular_hashtag_tweet = {}
# top100_tweet={}
# score_for_tweets = [{'tweet_id':"1","score":5},{'tweet_id':"2","score":6},{'tweet_id':"3","score":7},{'tweet_id':"4","score":8},{'tweet_id':"5","score":9},{'tweet_id':"6","score":10},{'tweet_id':"7","score":11},{'tweet_id':"8","score":12},{'tweet_id':"9","score":13}]
# top1_hashtagkeyword = {"a":['1','2','3','4','5','6','7','9'],"b":['2','3','4','5','6','7','8'],"c":['1','2','4','5','6','7','8','9'],"d":['1','2','3','4','5','6','7','8','9']}
#
# ###方法二
# for items in score_for_tweets:
#     dict_tweet_with_score[items['tweet_id']] = items['score']
# lsit_tweet_id = [key for key, value in dict_tweet_with_score.items()]
# set1_tweetid = set(lsit_tweet_id)
#
# for key, value in top1_hashtagkeyword.items():
#     set_tweet_id__for_one_hashtag = set(value)
#     set_tweet_id = set1_tweetid & set_tweet_id__for_one_hashtag
#     popular_hashtag_tweet[key] = {key: value for key, value in dict_tweet_with_score.items() if key in set_tweet_id}
#     print(popular_hashtag_tweet)
#
# for key, value in popular_hashtag_tweet.items():
#     for dict in value:
#         tweet_id_list = []
#         swd = sorted(value.items(), key=operator.itemgetter(1), reverse=True)
#         top10_tweet = swd[0:9]
#         for tweet_id in top10_tweet:
#             tweet_id_list.append(tweet_id)
#         top100_tweet[key] = tweet_id_list
# print(top100_tweet)


###方法一：效率较低
# for key, value in top1_hashtagkeyword.items():
#     dict_tweet_for_one_hashtag = []
#     dict_tweet_for_one = {}
#     for items in score_for_tweets:
#         if items['tweet_id'] in value:
#             dict_tweet_for_one[items['tweet_id']] = items['score']
#             dict_tweet_for_one_hashtag.append(dict_tweet_for_one)
#     popular_hashtag_tweet[key] = dict_tweet_for_one_hashtag
# print(popular_hashtag_tweet)
#
# for key, value in popular_hashtag_tweet.items():
#
#     for abu in value:
#         lsit = []
#         swd = sorted(abu.items(), key=operator.itemgetter(1), reverse=True)
#         tuple = swd[0:5]
#         for item in tuple:
#             lsit.append(item[0])
#         top100_tweet[key] = lsit
#
# print(top100_tweet)
#         top10_tweet = swd[0:3]
# print(top10_tweet)
# b = ['1','2']
#
# data = {'1012847289696600064': {'world_like': 0, 'world_followers': 268, 'world_friends': 183, 'world_retweet': 4677}, '1012847291357515777': {'world_like': 0, 'world_followers': 385, 'world_friends': 158, 'world_retweet': 16806}, '1012847293324816385': {'world_like': 0, 'world_followers': 928, 'world_friends': 145, 'world_retweet': 1998}, '1012847293932830720': {'world_like': 0, 'world_followers': 112, 'world_friends': 212, 'world_retweet': 42}, '1012847295988142080': {'world_like': 0, 'world_followers': 0, 'world_friends': 33, 'world_retweet': 5304}, '1012847296860573697': {'world_like': 0, 'world_followers': 2662, 'world_friends': 3174, 'world_retweet': 2}, '1012847298773217280': {'world_like': 0, 'world_followers': 63, 'world_friends': 89, 'world_retweet': 51}, '1012847301931536384': {'world_like': 0, 'world_followers': 1179, 'world_friends': 624, 'world_retweet': 75}, '1012847303122538496': {'world_like': 0, 'world_followers': 240, 'world_friends': 253, 'world_retweet': 14235}, '1012847304058032129': {'world_like': 0, 'world_followers': 63, 'world_friends': 89, 'world_retweet': 47}, '1012847306041724928': {'world_like': 0, 'world_followers': 26, 'world_friends': 85, 'world_retweet': 4677}, '1012847308843749377': {'world_like': 0, 'world_followers': 104, 'world_friends': 482, 'world_retweet': 237}, '1012847312346009600': {'world_like': 0, 'world_followers': 1, 'world_friends': 3, 'world_retweet': 29}, '1012847315185385472': {'world_like': 0, 'world_followers': 4, 'world_friends': 12, 'world_retweet': 135}, '1012847315877613568': {'world_like': 0, 'world_followers': 1813, 'world_friends': 971, 'world_retweet': 4677}, '1012847317404221440': {'world_like': 0, 'world_followers': 4, 'world_friends': 2, 'world_retweet': 1}, '1012847320273162240': {'world_like': 0, 'world_followers': 141, 'world_friends': 309, 'world_retweet': 20}, '1012847322110275586': {'world_like': 0, 'world_followers': 1, 'world_friends': 3, 'world_retweet': 18}, '1012847322957426689': {'world_like': 0, 'world_followers': 75, 'world_friends': 166, 'world_retweet': 266}, '1012847324425605125': {'world_like': 0, 'world_followers': 163, 'world_friends': 1407, 'world_retweet': 7401}, '1012847330071105536': {'world_like': 0, 'world_followers': 138, 'world_friends': 364, 'world_retweet': 36}, '1012847330444247040': {'world_like': 0, 'world_followers': 348, 'world_friends': 190, 'world_retweet': 4677}, '1012847332277223425': {'world_like': 0, 'world_followers': 63, 'world_friends': 89, 'world_retweet': 42}, '1012847332826771456': {'world_like': 0, 'world_followers': 51, 'world_friends': 180, 'world_retweet': 7401}, '1012847333665488897': {'world_like': 0, 'world_followers': 298, 'world_friends': 291, 'world_retweet': 120}, '1012847334269448192': {'world_like': 0, 'world_followers': 50, 'world_friends': 103, 'world_retweet': 66}, '1012847335095914497': {'world_like': 0, 'world_followers': 1, 'world_friends': 3, 'world_retweet': 32}, '1012847336404312064': {'world_like': 0, 'world_followers': 4, 'world_friends': 12, 'world_retweet': 614}, '1012847341525594112': {'world_like': 0, 'world_followers': 493, 'world_friends': 265, 'world_retweet': 1344}, '1012847348626673664': {'world_like': 0, 'world_followers': 328, 'world_friends': 632, 'world_retweet': 1300}, '1012847350027571200': {'world_like': 0, 'world_followers': 256, 'world_friends': 639, 'world_retweet': 7401}, '1012847352518971392': {'world_like': 0, 'world_followers': 30, 'world_friends': 77, 'world_retweet': 0}, '1012847353370497024': {'world_like': 0, 'world_followers': 153, 'world_friends': 85, 'world_retweet': 7401}, '1012847354079252481': {'world_like': 0, 'world_followers': 1, 'world_friends': 3, 'world_retweet': 35}, '1012847355840876544': {'world_like': 0, 'world_followers': 328, 'world_friends': 632, 'world_retweet': 101}, '1012847356042043392': {'world_like': 0, 'world_followers': 135, 'world_friends': 1202, 'world_retweet': 1157}, '1012847359766814721': {'world_like': 0, 'world_followers': 32, 'world_friends': 256, 'world_retweet': 1300}, '1012847360383356929': {'world_like': 0, 'world_followers': 63, 'world_friends': 89, 'world_retweet': 49}, '1012847365240311808': {'world_like': 0, 'world_followers': 49, 'world_friends': 130, 'world_retweet': 7401}, '1012847368796925952': {'world_like': 0, 'world_followers': 135, 'world_friends': 1202, 'world_retweet': 715}, '1012847368876617728': {'world_like': 0, 'world_followers': 112, 'world_friends': 212, 'world_retweet': 49}, '1012847370390786048': {'world_like': 0, 'world_followers': 55, 'world_friends': 185, 'world_retweet': 979}, '1012847375084376065': {'world_like': 0, 'world_followers': 63, 'world_friends': 89, 'world_retweet': 35}, '1012847375096958976': {'world_like': 0, 'world_followers': 282, 'world_friends': 256, 'world_retweet': 824}, '1012847376845889537': {'world_like': 0, 'world_followers': 880, 'world_friends': 585, 'world_retweet': 4677}, '1012847380192825344': {'world_like': 0, 'world_followers': 127, 'world_friends': 477, 'world_retweet': 7401}, '1012847381828816898': {'world_like': 0, 'world_followers': 1, 'world_friends': 3, 'world_retweet': 13}, '1012847383841943552': {'world_like': 0, 'world_followers': 349, 'world_friends': 304, 'world_retweet': 6425}, '1012847384815120385': {'world_like': 0, 'world_followers': 406, 'world_friends': 720, 'world_retweet': 22451}, '1012847385637081089': {'world_like': 0, 'world_followers': 152, 'world_friends': 196, 'world_retweet': 0}, '1012847386035662848': {'world_like': 0, 'world_followers': 31, 'world_friends': 120, 'world_retweet': 141}, '1012847387461718017': {'world_like': 0, 'world_followers': 568, 'world_friends': 478, 'world_retweet': 12380}, '1012847388606717952': {'world_like': 0, 'world_followers': 112, 'world_friends': 212, 'world_retweet': 35}, '1012847389537964033': {'world_like': 0, 'world_followers': 1323, 'world_friends': 308, 'world_retweet': 13}, '1012847392071155712': {'world_like': 0, 'world_followers': 13, 'world_friends': 34, 'world_retweet': 10}, '1012847394017464321': {'world_like': 0, 'world_followers': 63, 'world_friends': 89, 'world_retweet': 42}, '1012847394298519555': {'world_like': 0, 'world_followers': 532, 'world_friends': 565, 'world_retweet': 1}, '1012847401395056641': {'world_like': 0, 'world_followers': 207, 'world_friends': 854, 'world_retweet': 6425}, '1012847401588031488': {'world_like': 0, 'world_followers': 654, 'world_friends': 904, 'world_retweet': 715}, '1012847404104577024': {'world_like': 0, 'world_followers': 942, 'world_friends': 186, 'world_retweet': 900}, '1012847404280897536': {'world_like': 0, 'world_followers': 63, 'world_friends': 89, 'world_retweet': 34}, '1012847406927491077': {'world_like': 0, 'world_followers': 298, 'world_friends': 287, 'world_retweet': 3}, '1012847408349368321': {'world_like': 0, 'world_followers': 908, 'world_friends': 389, 'world_retweet': 50}, '1012847412564627456': {'world_like': 0, 'world_followers': 118, 'world_friends': 239, 'world_retweet': 1586}, '1012847419904516100': {'world_like': 0, 'world_followers': 4353, 'world_friends': 3016, 'world_retweet': 6425}, '1012847422127521792': {'world_like': 0, 'world_followers': 585, 'world_friends': 217, 'world_retweet': 2760}, '1012847422698123264': {'world_like': 0, 'world_followers': 423, 'world_friends': 350, 'world_retweet': 120}, '1012847423251628032': {'world_like': 0, 'world_followers': 230, 'world_friends': 223, 'world_retweet': 0}, '1012847424975622144': {'world_like': 0, 'world_followers': 63, 'world_friends': 89, 'world_retweet': 1300}, '1012847426212958208': {'world_like': 0, 'world_followers': 271, 'world_friends': 314, 'world_retweet': 1259}, '1012847427643064320': {'world_like': 0, 'world_followers': 3, 'world_friends': 126, 'world_retweet': 1300}, '1012847430256218112': {'world_like': 0, 'world_followers': 37, 'world_friends': 228, 'world_retweet': 23}, '1012847430633697281': {'world_like': 0, 'world_followers': 104, 'world_friends': 482, 'world_retweet': 543}, '1012847432089161735': {'world_like': 0, 'world_followers': 224, 'world_friends': 1089, 'world_retweet': 7401}, '1012847433372618755': {'world_like': 0, 'world_followers': 63, 'world_friends': 89, 'world_retweet': 101}, '1012847433708199938': {'world_like': 0, 'world_followers': 6, 'world_friends': 375, 'world_retweet': 1300}, '1012847436690161664': {'world_like': 0, 'world_followers': 597, 'world_friends': 452, 'world_retweet': 614}, '1012847437491273728': {'world_like': 0, 'world_followers': 112, 'world_friends': 212, 'world_retweet': 42}, '1012847440070881280': {'world_like': 0, 'world_followers': 80, 'world_friends': 26, 'world_retweet': 0}, '1012847442818039808': {'world_like': 0, 'world_followers': 186, 'world_friends': 293, 'world_retweet': 32}, '1012847448593596416': {'world_like': 0, 'world_followers': 334, 'world_friends': 498, 'world_retweet': 56}, '1012847450640482304': {'world_like': 0, 'world_followers': 481, 'world_friends': 874, 'world_retweet': 4}, '1012847454952271873': {'world_like': 0, 'world_followers': 133, 'world_friends': 115, 'world_retweet': 7401}, '1012847455983943681': {'world_like': 0, 'world_followers': 4, 'world_friends': 12, 'world_retweet': 23}, '1012847456524984320': {'world_like': 0, 'world_followers': 413, 'world_friends': 357, 'world_retweet': 2673}, '1012847458714439681': {'world_like': 0, 'world_followers': 112, 'world_friends': 212, 'world_retweet': 34}, '1012847462149697536': {'world_like': 0, 'world_followers': 1063, 'world_friends': 646, 'world_retweet': 9}, '1012847462296571904': {'world_like': 0, 'world_followers': 357, 'world_friends': 289, 'world_retweet': 10}, '1012847463835635717': {'world_like': 0, 'world_followers': 4, 'world_friends': 12, 'world_retweet': 25}, '1012847469930209281': {'world_like': 0, 'world_followers': 815, 'world_friends': 756, 'world_retweet': 622}, '1012847474153742338': {'world_like': 0, 'world_followers': 744, 'world_friends': 612, 'world_retweet': 26}, '1012847478012456960': {'world_like': 1, 'world_followers': 2, 'world_friends': 36, 'world_retweet': 1}, '1012847478050312197': {'world_like': 0, 'world_followers': 199, 'world_friends': 135, 'world_retweet': 67}, '1012847478071353344': {'world_like': 0, 'world_followers': 63, 'world_friends': 555, 'world_retweet': 1298}, '1012847485608431616': {'world_like': 0, 'world_followers': 4, 'world_friends': 2, 'world_retweet': 3}, '1012847490104733697': {'world_like': 0, 'world_followers': 490, 'world_friends': 819, 'world_retweet': 6425}, '1012847490402578432': {'world_like': 0, 'world_followers': 30, 'world_friends': 39, 'world_retweet': 1300}, '1012847490859782144': {'world_like': 0, 'world_followers': 18002, 'world_friends': 6743, 'world_retweet': 5570}, '1012847496933117952': {'world_like': 0, 'world_followers': 540, 'world_friends': 324, 'world_retweet': 264}}

#
# def popular_score(dict):
#         tweet_score = dict['world_like'] * 0.3 + dict['world_followers'] * 0.2 + dict['world_friends'] * 0.1 + dict['world_retweet'] * 0.4
#         return tweet_score
#
# nor_data = {}
# for key,value in data.items():
#     nor_data[key] = popular_score(value)
# print(nor_data)

# def hump2underline(hunp_str):
#     ''' 驼峰形式字符串转成下划线形式 :param hunp_str: 驼峰形式字符串 :return: 字母全小写的下划线形式字符串 '''
#     # 匹配正则，匹配小写字母和大写字母的分界位置
#     p = re.compile(r'([a-z]|\d)([A-Z])')
#     # 这里第二个参数使用了正则分组的后向引用
#     sub = re.sub(p, r'\1_\2', hunp_str).lower()
#     return sub
# print(hump2underline('WorldCup'))
#
# a.extend(b)
# print(a)

#####top 10 hashtag tweetid####
# dict1 = {'790074083929120768': ['fra'], '803258170298744839': ['fra'], '777079966190174208': ['emails', 'hillaryclinton', 'emails', 'worldcupfinal', 'emails', 'worldcup'], '848433356790300675': ['worldcup'],'777574017037393920': ['fbi'], '801764788791431168': ['iamthankfulfor'], '800650742616981505': ['tvlifelessonsilearned'], '868034968504729600': ['freitagmorgen'], '826055377624166400': ['insteadofwatchingthebiggame'], '672452712047362048': ['prayers4california'], '772825990854696960': ['toavoidworki']}
# top10_hashtag_list = ['worldcup', 'fra', 'cro', 'nationaldogday','worldcupfinal']
# dict = {}
#
# def get_tweet(top10_hashtag_list, dict1, dict2):
#     for hashtag_keyword in top10_hashtag_list:
#         list = []
#         for key, value in dict1.items():
#             if hashtag_keyword in value:
#                 list.append(key)
#                 dict2[hashtag_keyword] = list
#     return dict2
#
# print(get_tweet(top10_hashtag_list,dict1,dict))

###popular post###
# tweet = {'worldcup': [('1018552068083257344', Decimal('-0.15061653591458530')), ('1018554412002893827', Decimal('-0.15194400791319992')), ('1018553474051690496', Decimal('-0.16179617607441824')), ('1014271771288186880', Decimal('-0.16568496748827455')), ('1018554153235144704', Decimal('-0.16634932321014936')), ('1013525343527948289', Decimal('-0.16671408016082840')), ('1018551183298977792', Decimal('-0.16723606179494290')), ('1013527594493448193', Decimal('-0.16723912017249085')), ('1018557825964896256', Decimal('-0.16772377930424360')), ('1013525770424250368', Decimal('-0.16882714009376568'))],
#  'fra': [('1018553474051690496', Decimal('-0.16179617607441824')), ('1013101352367656960', Decimal('-0.17036866587876545')), ('1018383925046054913', Decimal('-0.17058722132598436')), ('1018551410743566344', Decimal('-0.17124240573202762')), ('1016786639283245062', Decimal('-0.17125714698289363')), ('1016755711731273729', Decimal('-0.17166590829392686')), ('1016739441350725634', Decimal('-0.17184908218018330')), ('1016711837038018560', Decimal('-0.17208044546045920')), ('1016806713817686016', Decimal('-0.17212430778567450')), ('1018556086822072328', Decimal('-0.17229584386661440'))]}
# dict = {}
# for key, value in tweet.items():
#     for item in value:
#         sql = "insert into `top100_tweet` (`tweet_id`,`score`,`hashtag`) values ('" + item[0]+ "', '" + str(item[1]) + "', '"+ key +"' )"
#         try:
#             cursor.execute(sql)
#         except Exception as e:
#             print("Error", str(e), sql)
#             pass
# db.commit()
# db.rollback()
# cursor.close()

####list test
list=[]
list1 = [1,2,3,4,5]
list2= [1,2,3,4,5]

list1.append(list2)
print(list1)