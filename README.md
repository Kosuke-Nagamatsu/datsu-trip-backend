# [ダツの旅](https://github.com/Kosuke-Nagamatsu/datsu-trip)：バックエンド

## 使用技術
フレームワーク： FastAPI

データベース： PostgreSQL

ORM： SQLAlchemy

## 使い方
### 1. webサーバーを起動
```
docker-compose up -d
```

http://127.0.0.1:8000 へアクセスすると ["Hello！"] と表示されます。


### 2. seedデータを作成
```
curl -X POST http://127.0.0.1:8000/seed
```
作成するとターミナルに以下が表示されます。
```
{"message":"Seed data created."}
```
これでダーツゲームの準備は完了です。

### 3. APIドキュメントの確認
ドキュメントを確認する場合は http://127.0.0.1:8000/docs にアクセスします。
