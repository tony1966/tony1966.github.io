import requests
import hashlib
import os

def if_ubike_updated():
    old_hash=''
    hash_file='ubike_hash.txt'
    if os.path.exists(hash_file):
        with open(hash_file, 'r') as f:
            old_hash=f.read()    
    url='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/' +\
        'v2/youbike_immediate.json'
    response=requests.get(url)
    m=hashlib.md5()
    m.update(response.text.encode('utf-8'))
    new_hash=m.hexdigest()
    with open(hash_file, 'w') as f:
        f.write(new_hash)
    if new_hash == old_hash:
        return False
    else:
        return True
    
if __name__ == '__main__':
    if if_ubike_updated():
        print('Youbike 即時資訊已更新')
    else:
        print('Youbike 即時資訊未更新')
    