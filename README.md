# [ダツの旅](https://github.com/Kosuke-Nagamatsu/datsu-trip)：バックエンド

## 使用技術
- フレームワーク： [FastAPI](https://fastapi.tiangolo.com/ja/)

- データベース： PostgreSQL

- ORM： SQLAlchemy

- インフラ： Docker Desktop: 4.17.0
  - Engine: 20.10.23
  - Compose: v2.15.1

## 使い方
### 1. Dockerコンテナを起動
以下のコマンドで、Webアプリケーションとデータベースを実行する2つのコンテナを作成・起動します。
```
docker-compose up -d
```

Webサーバーが起動し、http://127.0.0.1:8000 にアクセスすると ["Hello！"] と表示されます。

### 2. seedデータを作成
`/app/seed.py` のリストをもとに、以下のコマンドでSeedデータを作成します。
```
curl -X POST http://127.0.0.1:8000/seed
```

データが作成されると、ターミナルに `{"message":"Seed data created."}` と表示されます。

これでゲームの準備は完了です。

### 3. APIドキュメントの確認
ドキュメントを確認する場合は http://127.0.0.1:8000/docs にアクセスします。

### 補足：環境を初期化
ゲーム終了後に、コンテナなどを削除しDocker環境をクリーンにする方法を記載します。

1. コンテナを停止（ダッシュボード画面の例）
<img width="1412" alt="スクリーンショット 2023-04-19 0 14 33" src="https://user-images.githubusercontent.com/83779040/232823394-d045ee47-bb97-465a-98de-7bfd7766b11e.png">

2. イメージ、コンテナ、ボリュームなどの使用状況を確認（以降はコマンドの例）
```
docker system df
```

実行すると以下が表示されます。
```
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          2         2         462.7MB   80.54MB (17%)
Containers      2         0         0B        0B
Local Volumes   1         1         48.09MB   0B (0%)
Build Cache     12        0         12.66kB   12.66kB
```

3. 停止したコンテナとすべての未使用のイメージを削除
```
docker system prune -a
```

4. 不要なボリュームを削除
```
docker volume prune
```

5. 削除できたか確認
```
docker system df
```
```
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          0         0         0B        0B
Containers      0         0         0B        0B
Local Volumes   0         0         0B        0B
Build Cache     0         0         0B        0B
```

これで環境の初期化は完了です。

## 参考
[FastAPI公式ドキュメント](https://fastapi.tiangolo.com/ja/)