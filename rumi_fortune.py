import streamlit as st
from datetime import datetime, timedelta
from random import choice, choices

st.markdown("<p style='text-align: center; color: #e91e63; font-size: 30px;'>🌟 おしゃべりBot 🌟</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 22px;'>先生！今日もめちゃめちゃイケてますね✨<br>今日の運勢占ってみましょ？🔮</p>", unsafe_allow_html=True)

# 日本時間に変換（UTC +9）
now = datetime.utcnow() + timedelta(hours=9)
is_birthday = now.month == 5 and now.day == 17

# にゃんこランダム
cats = ["Ginくん", "Limeちゃん", "Sunちゃん"]
cat = choice(cats)

# 占うボタン
st.markdown("""
<style>
div.stButton > button {
    background-color: #E98FB8;
    color: #eb6877;
    font-weight: bold;
    border-radius: 10px;
    padding: 15px 30px;
    font-size: 18px;
    text-shadow: -1px -1px 1px rgba(255,255,255,0.44), 1px 1px 1px #4A0825;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    margin: auto;
    display: block;
}
</style>
""", unsafe_allow_html=True)

if st.button("🔮 占ってみる！ ＞"):
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
            "今日は最高にツイてる1日！ノリにノッちゃお！🌟",
            "今日は特別映える日！🫃✨いつもかっこいんだけどね💕",
            f"今日は{cat}の癒し効果倍増日🐾特別かまってあげてね🐈",
        ],
        "中吉😊": [
            "まずまずいい感じ！爽やかさが幸運のカギ🌟", 
            "いい日になりそう！深呼吸してリズムを整えてね✨", 
        ],
        "小吉🙂": [
            "リラックスして過ごすといい日！肩の力抜いてゆるっと行こう🍀", 
            "ラッキーアイテムは笑顔😊和やかムードでゆるっと行こう (´・ω・)旦", 
        ],
        "末吉🤔": [
            "ちょっと注意モード。無理せず休憩を忘れずに💤",
            f"なんとなく注意モード。{cat}の様子を見てあげて🐈", 
        ],
        "凶😢": [
            f"ちょっと休憩して深呼吸。{cat}と一緒にのんびりしよう🐾", 
            f"忙しいからって、無理は禁物❌{cat}に癒されよう🐈", 
        ],
        "大凶💀": ["もうお酒でまったりしよ🍶まだお仕事あるならトマトジュースでガマン🥫詰んじゃうよ♪"]
    }

    # 出力
    st.subheader(f"🔮 今日の運勢：{今日の運勢}")
    if is_birthday:
        st.success("🎂今日は先生のお誕生日！すべての運勢を超える『祝福モード』発動です㊗️")
        st.success("🎉Happy B-day🎉今日の運勢に関係なく１年のうち最高の祝福がもたらされます💖")
    else:
        msg = choice(メッセージ[今日の運勢])
        st.write(msg)