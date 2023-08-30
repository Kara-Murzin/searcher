import os
import time
spisok = []
for address, dirs, files in os.walk("/Users/zhanserik/Desktop/examp"):
    for file in files:
        full = os.path.join(address, file)
        if time.time() - os.path.getctime(full) < 86400:
            spisok.append(full)
print(spisok)