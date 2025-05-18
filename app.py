import streamlit as st
from datetime import datetime

# 公益任务库（可自由修改）
GOOD_DEEDS = [
    "给外卖小哥说谢谢",
    "捡起路边垃圾",
    "给流浪猫添水",
    "捐赠闲置衣物",
    "关掉闲置电源"
]

# 页面设置
st.set_page_config(
    page_title="功德+1",
    page_icon="🪷",
    layout="centered"
)

# 初始化数据
if "deeds_log" not in st.session_state:
    st.session_state.deeds_log = []

# 主界面
st.title("🪷 每日功德+1")
st.write("每天做件小事，让世界变好一点点")

# 1. 随机推荐任务
st.subheader("今日功德任务")
if st.button("随机生成"):
    deed = random.choice(GOOD_DEEDS)
    st.session_state.deeds_log.append({
        "task": deed,
        "time": datetime.now().strftime("%m-%d %H:%M")
    })
    st.success(f"✅ 今日任务：{deed}")

# 2. 功德记录
st.subheader("功德簿")
if st.session_state.deeds_log:
    for log in st.session_state.deeds_log:
        st.write(f"{log['time']} - {log['task']}")
else:
    st.info("还没开始积累功德哦")

# 页脚彩蛋
st.divider()
st.caption("💡 真正的公益是养成习惯")
