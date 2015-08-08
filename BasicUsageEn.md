You could use zhpy interpreter to test zhpy::

```
    $ zhpy
    >>> 印出 'hello'
    hello
```

You could use python interpretor to test zhpy with [zh\_exec](http://code.google.com/p/zhpy/wiki/EmbededInPython) method::

```
    $ python
    >>> from zhpy import zh_exec
    >>> zh_exec("印出 hello") 
    hello
```

You could use 'zhpy' command instead of "python" in command line to
execute source code mixed in Chinese and English.::

```
    $ zhpy hello.py
    hello, world!
```

You could assign a file name to export the zhpy source to the normal
python source (english)::

```
    $ zhpy hello.py n_hello.py
```

Then run the exported file as normal python source::

```
    $ python n_hello.py
    hello, world!
```

Or you could combine these two steps in one command (with '-p' option)::

```
    $ python -p hello.py
    hello, world!
    $ ls
    hello.py n_hello.py
```
