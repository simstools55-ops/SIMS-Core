# 改善依頼サンプル

次の記事をSEO改善してください。
ArticleID: A000012
URL: https://example.com/article.html
記事タイトル: 現在の記事タイトル
SEOタイトル: 現在のSEOタイトル
メタディスクリプション: 現在の説明文
メインクエリ: メインクエリ
現在値: クリック 16、表示 2946、CTR 0.5%、順位 7.2位
改善目的: 改善候補。タイトル、導入文、見出し、FAQを優先し、既存記事の良い部分は残してください。

【SIMSへのフィードバック出力ルール】
回答の最後に、下記仕様のJSONをコードブロックで必ず1つ出力してください。JSONの前後に説明を書いても構いませんが、JSON内にはコメントを入れないでください。

```json
{
  "format": "SIMS_FEEDBACK_V1",
  "version": "1.1",
  "article_id": "A000012",
  "article_url": "https://example.com/article.html",
  "completed_at": "YYYY-MM-DD",
  "changes": {
    "article_title": false,
    "seo_title": false,
    "description": false,
    "introduction": false,
    "headings": false,
    "faq": false,
    "internal_links": false,
    "body": false,
    "images": false
  },
  "new_values": {
    "article_title": "",
    "seo_title": "",
    "description": "",
    "main_query": "メインクエリ"
  },
  "improvement_type": "normal",
  "confidence": "high",
  "expected_effect": {"ctr": "", "clicks": ""},
  "next_action": "monitor",
  "summary": "実施した改善の要約",
  "warnings": [],
  "estimated_minutes": 20,
  "recommended_review_days": 14
}
```

変更していない項目はfalse、変更後の値がない項目は空文字にしてください。recommended_review_daysは7・14・30のいずれかにしてください。improvement_typeはminor・normal・major、confidenceはhigh・medium・low、next_actionはmonitor・remeasure・rewrite・noneのいずれかにしてください。
