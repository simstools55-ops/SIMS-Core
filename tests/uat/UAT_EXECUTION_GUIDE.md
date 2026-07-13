# 実記事UAT実行ガイド

## 目的

Claude ProjectへProduction Packageを登録し、SIMS-Blog-Managerの現行依頼文が正しく処理されるか確認します。

## 実行

1. `distribution/SIMS-Core-Claude-Upload/01_Project_Instructions`の内容をClaude Projectの「手順」へ貼り付ける。
2. `02_Project_Knowledge`の6ファイルを「コンテキスト」へ登録する。
3. `tests/fixtures/request_A000012.txt`を新しいチャットへ貼り付ける。
4. 実際の記事本文またはURL参照を追加し、改善を実行する。
5. 回答末尾のJSONを保存する。
6. `tests/uat/UAT_CHECKLIST.md`で合否を判定する。

## 合格条件

- 優先指定されたタイトル、導入文、見出し、FAQが具体的に改善されている。
- 既存記事の良い部分を残す方針が守られている。
- JSONが1つだけで回答末尾にある。
- JSONの変更フラグと本文出力が一致する。
- 指定外の列挙値がない。
