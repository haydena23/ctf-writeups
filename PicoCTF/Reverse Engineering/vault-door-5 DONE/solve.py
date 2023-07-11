import base64
import urllib.parse

expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"\
         + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"\
         + "JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0"

decoded = base64.b64decode(expected)
flag = urllib.parse.unquote(decoded)
print(flag)