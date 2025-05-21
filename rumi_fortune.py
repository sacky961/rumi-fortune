import streamlit as st
from datetime import datetime, timedelta
from random import choice, choices

st.title("🌟先生専用！Rumiの癒し占い🌟")

# 日本時間に変換（UTC +9）
now = datetime.utcnow() + timedelta(hours=9)
is_birthday = now.month == 5 and now.day == 17

# にゃんこランダム
cats = ["Ginくん", "Limeちゃん", "Sunちゃん"]
cat = choice(cats)

# 運勢とその出現確率
運勢と確率 = [
    ("大吉✨", 25),
    ("中吉😊", 20),
    ("小吉🙂", 20),
    ("末吉🤔", 20),
    ("凶😢", 10),
    ("大凶💀", 5)
]
運勢リスト = [u[0] for u in 運勢と確率]
確率リスト = [u[1] for u in 運勢と確率]
今日の運勢 = choices(運勢リスト, weights=確率リスト, k=1)[0]

# メッセージ
メッセージ = {
    "大吉✨": [
        f"今日は最高にツイてる1日！ノリにノッちゃお！🌟",
        f"今日は特別映える日！🫃✨いつもかっこいんだけどね💕",
        f"今日は{cat}の癒し効果倍増日🐾特別かまってあげてね🐈",
    ],
    "中吉😊": ["爽やかさが幸運のカギ🌟", "深呼吸してリズムを整えてね✨"],
    "小吉🙂": ["肩の力抜いてゆるっと行こう🍀", "笑顔がラッキーアイテム😊"],
    "末吉🤔": ["注意モード。無理せず休憩を💤", f"{cat}の様子を見てあげて🐈"],
    "凶😢": [f"深呼吸して、{cat}に癒されよう🐈", f"{cat}と一緒にのんびりしよう🐾"],
    "大凶💀": ["お酒かトマトジュースでまったり🍶🥫詰んじゃうよ♪"]
}

st.subheader(f"🔮 今日の運勢：{今日の運勢}")
if is_birthday:
    st.success("🎂今日は先生のお誕生日！『祝福モード』発動です🎉")
else:
    msg = choice(メッセージ[今日の運勢])
    st.write(msg)
