# Compatibility Policy

## 現行契約

- Input: SIMS_REQUEST_TEXT_V1
- Output: SIMS_FEEDBACK_V1 version 1.1

## 方針

1. Production 1.xでは自然文入力を第一級インターフェースとして維持する。
2. 将来JSON入力を追加しても、自然文入力を直ちに廃止しない。
3. 入力形式と出力形式は独立してバージョン管理する。
4. Claude固有機能を製品契約へ持ち込まない。
5. 破壊的変更はメジャーバージョンでのみ行う。
6. SIMS-Blog-Managerが読み取るフィールド名・型・列挙値を無断変更しない。
