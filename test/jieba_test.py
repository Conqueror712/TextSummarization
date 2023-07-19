from __future__ import print_function
from importlib import reload
import sys

try:
    reload(sys)
    # sys.setdefaultencoding('utf-8')
except:
    pass

import jieba.posseg as pseg

words = pseg.cut("我爱北京天安门.。；‘你的#")
for w in words:
    print('{0} {1}'.format(w.word, w.flag))
    print(type(w.word))
