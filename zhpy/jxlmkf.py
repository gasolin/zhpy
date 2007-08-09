# -*- coding: UTF-8 -*-

from pyparsing import *
#word dict
keywords = {"assert":"宣告","break":"跳出","continue":"繼續","del":"刪除",
            "elif":"不然","else":"否則","except":"異常","exec":"執行",            "finally":"最後","for":"取","global":"全域","if":"如果",
            "lambda":"函式","pass":"略過","print":"印出","raise":"舉出",
            "return":"返回","try":"嘗試","while":"當","yield":'圈',
            "as":"取名","with":"伴隨", "def":"定義", "import":"導入", 
            "from":"自", "in":"在"}

#En -> Zh
#kwd = MatchFirst(map(Keyword,#             "if then else def print while for".split()))
#Keyword = keywords.keys()
kwd = MatchFirst(map(Keyword, 
        keywords.keys()))
kwd.setParseAction(lambda t:"^%s^" % t[0].encode("utf8"))
#kwd.setParseAction(lambda t:"^%s^" % keywords[t[0].encode("utf8")].decode("utf8"))
#pythonStyleComment.setParseAction(lambda t:"_%s_" % t[0])    #quotedString.setParseAction(lambda t:">%s<" % t[0])    converter = kwd #| pythonStyleComment | quotedString#alphas = u''.join(unichr(x) for x in xrange(0x2E80, 0x2FA1D))


#keyword_if = Word("for")#Word(u"迴圈")
#keyword_in = Word("in")#Word(u"在")
#if_stmt = keyword_if + Word(alphas)+keyword_in+Word(alphas)+":"

#Zh -> En
chineseChars = srange(r"[\0x0080-\0xfe00]")chineseWord = Word(chineseChars)

if __name__ == '__main__':
    trad_code = """for a in range(10):"""
    #u"""迴圈 a 在 range(10):"""
    #print if_stmt.parseString(trad_code)
    #print keywords
    sampleCode = """# this is a sample Python program def fn(name,n):   for i in range(n):       print "Hello, %s!" % name fn("World", 100)"""     print converter.transformString(sampleCode)
    