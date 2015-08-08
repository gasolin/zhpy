# Input/Output Example #

## Origin Python Code ##

```
# -*- coding: utf-8 -*-
data = raw_input("Type your name: ")
print "Hello, ", data
```

## Python In Chinese ##

Let's take an example. Save following code in file "inout.py":

```
# -*- coding: utf-8 -*-
姓名 = 輸入("輸入名稱: ")
印出 ">歡迎, ", 姓名
```

[Source](http://zhpy.googlecode.com/svn/trunk/examples/inout/inout.twpy)

and run inout.py with zhpy in command line, the result is:

```
    $zhpy inout,py
    輸入名稱: fred
    >歡迎, fred
```

## Converted Python Source ##

```
# -*- coding: utf-8 -*-
p0 = raw_input("輸入名稱: ")
print "歡迎, ", p0
```

[Source](http://zhpy.googlecode.com/svn/trunk/examples/inout/n_inout.py)