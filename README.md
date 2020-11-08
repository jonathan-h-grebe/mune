# 開発環境
## 導入
### python/Django
local_settings.pyは別途用意
```sh
pip3 install -r requirement.txt
python3 manage.py migrate --settings=mune.local_settings
```

### node
まだ準備中（2020/11/08）
```sh
cd front
npm install
```

## 開発サーバの起動
### python/Django
```sh
python3 manage.py runserver 8081 --settings=mune.local_settings
``` 


### node.js
まだ準備中（2020/11/08）
defaultで8080で動く？
```sh
cd front
npm run serve
```

