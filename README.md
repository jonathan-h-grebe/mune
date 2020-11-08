# 開発環境
## 導入
### python/Django
local_settings.pyは別途用意
```sh
pip3 install -r requirement.txt
python3 manage.py migrate --settings=mune.local_settings
```

### ユーザ作成
```sh
python3 manage.py createsuperuser --settings=mune.local_settings
```

### node
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
defaultで8080で動く？
```sh
cd front
npm run serve
```

---

# Branch
## 各自のブランチ
ご自由にどうぞ

## develop
各自のブランチからdevelopへPullRequestをお願いします。
Unittestが動くので、念の為チェックする 
 
## master
developからmasterへPullRequestを作成する
マージされると、herokuへ反映されます
（2020/11/08時点では、Vueは未対応）

---
