# 簡介 #

Python3與Python2不相容，
提供了

**Unicode變量名稱** 支援parsing Unicode的tokenize module

# 方法 #

1. 避開使用chardet module:

**用system模塊來取得默認編碼** 將zhpy命令用分開的cnpy/twpy命令來取代

2. 避開使用pyparsing module

**使用tokenize轉換keyword**

# 規格 #

**支援命令行執行**

1. twpy 正體中文

支援格式: .twpy

2. cnpy 簡體中文

支援格式: .cnpy

3. jppy (opt)

支援格式: .jppy

4. krpy (opt)

支援格式: .krpy

**支援 import modules (not yet)** 支援 trackback 翻譯
**支援 interpreter**


# 參考 #
**使用tokenize轉換keyword https://groups.google.com/forum/#!topic/python-cn/J4VAMQIo-hg** 使用ctypes轉換keyword http://weijr-note.blogspot.com/2011/06/python-32-keyword.html