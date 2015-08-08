# RoadMap #


## 3.0a1 (2011/06/25) ##

code name: Tusk

  * python 3 compatible
  * Remap the architecture to easily support Multiple Language (such as jp, kr, or old-chinese)

## zhpy3 TODO ##

  * Interpreter
  * Import zhpy3 modules
  * Export to python3
  * Convert from python3
  * Doc with sphinx

---


## 0.2 (08/9/2007) ##

code name: zhou (周蟒)

  * Add Traditional Chinese keywords
  * easy\_install-abled
  * executable command line
  * **export python source from zhpy**

## 0.3 (08/12/2007) ##

code name: JoJo

  * allow to **dynamic add keywords by append ini** files in same folder
  * catalog keywords
  * basic documents

## 0.4 (08/15/2007) ##

code name: Dio

  * translate most of build-in types
  * **enhanced command line with optparse**
  * "compile to python and run" option (-p)

## 0.5 (08/19/2007) ##

code name: Star Platinum

  * implement 'zh\_exec' to **embed zhpy in python**
  * ship with test suite
  * fix examples

cheesecake rate: 60%

## 0.6 (08/21/2007) ##

code name: Crazy Diomand

  * "input raw zhpy source and run" option (-r) for **shell scripting**
  * better simplified chinese support
  * **functions test** with doctest
  * **unit test cover traditional/simplified chinese**.
  * increased [cheesecake rating](http://www.pycheesecake.org)
  * **example test suite**

cheesecake rate: 81% (445/545)

## 0.7 (8/24/2007) ##

code name: Gold Experience

  * **universe reference identifier (URI)** for variable/constant/class/methods
  * corresponding to python command, **use option (-c) instead of (-r)** for scripting
  * use **.twpy, .cnpy** as zhpy subname to distinguish the coding
  * test the command line options
  * able to run zhpy in main
  * maintain tw, cn keyword in seperate dict

cheesecake rate: 83% (453/545)

## 0.8 (8/30/2007) ##

code name: Stone Free

  * **zhpy -> python library** in pyzh.py
  * bi-directional variable 

&lt;-&gt;

 number function
  * basic zhpy **interpreter**
  * **auto detect encodings** (mostly for windows user)
  * host all dictionaries in zhdc.py

cheesecake rate: 83% (453/545)

## 0.8.1 (9/2/2007) ##

code name: Hermit Purple

  * fix interpreter muiti-line issue
  * update example test cases

## 0.9 (9/05/2007) ##

code name: The World

  * **module keyword library plug-in system**
  * annotation support in interpreter
  * use encoding utf8 as default encoding while auto detection in low confidence(<0.8)
  * **bundle a plugin sample** (zhpy\_ext/)
  * **able to run zhpy script as system script**
  * increase cheesecake rate

cheesecake rate: 92% (502/545)

## 0.9.1 (9/07/2007) ##

code name: Magician Red

  * **enhanced "zhpy --info" command**
  * twdict, cndict now shown in plugin
  * **worddict formed dynamically without exceptions**
  * add chinese keywords for zhpy

## 0.9.2 (9/9/2007) ##

code name: Hierophant Green

  * **move twdict, cndict keyword into separate plugins**
  * keywords update

## 0.9.3 (9/15/2007) ##

code name: Tower of Gray

  * **API document for Download**
  * **update exception keywords**
  * make chinese punctuation be a plugin
  * Downloadable API Doc

## 0.9.4 (9/27/2007) ##

code name: Silver Chariot

  * rewrite command parser to **allow zhpy script with commandline arguments**
  * fix comment shouldn't be translated
  * remove chinese punctuations support

## 1.0 (10/2/2007) ##

code name: Killer Queen

  * Stable API
  * Stable keywords
  * improved install pack and guide
  * document ready: **Byte of zhpy on python**
  * catch up most syntax in http://www.chinesepython.org/doc/ref.html
  * improved APIDOC
  * improved docs
  * advocation

## 1.1 (10/8/2007) ##

code name: Echoes

  * update zhpy to python library
  * **"compile py to twpy source" option (--tw)**
  * **"compile py to cnpy source" option (--cn)**

## 1.1.1 (10/12/2007) ##

code name: Dark Blue Moon

  * Able to **import modules in current directory**
  * fix **multilines comments** translated incorrectly
  * bug fixes

## 1.2 (10/19/2007) ##

code name: Requiem

  * **experimental chinese file name support**
  * support chinese filename to uri filename while convert with '-p' option
  * refactor number\_to\_variable to zh\_chr
  * refactor variable\_to\_number to zh\_ord
  * zh\_ord and zh\_chr are bi-direction convertable
  * **buildin sys module plugin**

## 1.3 (11/5/2007) ##

code name: White Snake

  * **you can try zhpy without install**
  * **custom name space in zh\_exec**
  * Separate traditional and simplified chinese keywords from zhdc to plug[lang](lang.md).py
  * moveout plugins' setuptools dependency
  * profiling zhpy in standalone interpreter mode
  * ship with pyparsing

## 1.4 beta 1 (12/3/2007) ##

code name: Yellow Temperance

  * keyword revision
  * limited chinese traceback
  * testable with nosetests

## 1.4 (1/18/2008) ##

code name: Hanged Man

  * fix windows interpreter encoding issue
  * better chinese traceback

cheesecake rate: 83% (453/545)

## 1.5 (2/29/2008) ##

code name: Emperor

  * rewrite import\_hook (zhimport)
  * refactor

## 1.5.1 (3/21/2008) ##

code name: Empress

  * fix pyzh pattern missing since 1.5 refactor

## 1.5.2 (4/3/2008) ##

code name: Wheel of Fortune

  * no need calling annotator before calling convertor,
> > annotator will be called automatically
  * PEP8 cleanup
  * refactor
  * pick up [ http://weijr-note.blogspot.com/2008/02/python-magiccodec-01.html

> MagicCodec]

cheesecake rate: 82% (452/545)

## 1.6 (4/12/2008) ##

code name: Justice

  * online zhpy shell
  * bug and options fix

## 1.7 (5/21/2008) ##

code name: Lovers

  * intentable interpreter autocomplete in **nix
  * chinese keyword autocomplete in**nix
  * 'zhpy -V' command

## 1.7.1 (9/11/2008) ##

code name: Sun

  * Maintainance release
  * [crunchy support](http://zhpy.blogspot.com/2008/08/58.html)

## 1.7.2 (8/11/2009) ##

code name: Death Thirteen

  * python 2.6 compatibility

## 1.7.3 (12/08/2009) ##

code name: Justice

  * Move repository to mercurial
  * Partial Android(ASE) support
＊Update docs layout

## 1.7.4 (6//2010) ##

code name: High Priestess

**fix the windows/mac EOF exception**

## zhpy TODO ##

  * **plugin with namespace**
  * windows installer
  * Android, IronPython, jython support
  * pygments syntax highlighter with 'zhpy'
  * add keyword convertor between traditional chinese and simplified chinese
  * compatible editor
  * Pickle the keyword dict to increase the bootstrap speed
  * eval the itertools-based rev\_dict
  * Simplified Chinese version of **Byte of zhpy on python** Book
  * ship with Byte of zhpy example
  * support unicode string (u'')


---


# Preserved code name #

Code names are digested from JoJo's Advanture
http://zh.wikipedia.org/wiki/%E6%9B%BF%E8%BA%AB_(JoJo%E7%9A%84%E5%A5%87%E5%A6%99%E5%86%92%E9%9A%AA)

[Cheesecake](http://www.pycheesecake.org/) is a 'mechanism' that guides and encourages relevant 'good practices'.



