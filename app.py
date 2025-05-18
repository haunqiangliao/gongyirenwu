import streamlit as st
import random
from datetime import datetime

# 预设任务库
DEFAULT_DEEDS = [
    "给外卖小哥说谢谢",
    "捡起路边垃圾",
    "给流浪猫添水",
    "关掉闲置电源",
    "捐赠闲置物品",
    "帮陌生人按电梯",
    "给父母发条问候"
]

# 初始化数据
if 'deeds_log' not in st.session_state:
    st.session_state.deeds_log = []

# 页面设置
st.set_page_config(
    page_title="功德+1",
    page_icon="🪷",
    layout="centered"
)

# 主界面
st.title("🪷 每日功德+1")
st.caption("每天做件小事，让世界变好一点点")

# 生成任务
if st.button("生成今日功德任务"):
    deed = random.choice(DEFAULT_DEEDS)
    st.session_state.deeds_log.append({
        "task": deed,
        "time": datetime.now().strftime("%m-%d %H:%M"),
        "status": "进行中"
    })
    st.success(f"今日任务：{deed}")

# 显示当前任务
if st.session_state.deeds_log:
    latest = st.session_state.deeds_log[-1]
    if latest["status"] == "进行中":
        st.subheader("当前任务")
        st.write(f"**{latest['task']}**")
        st.caption(f"生成时间：{latest['time']}")
        
        if st.button("标记完成"):
            st.session_state.deeds_log[-1]["status"] = "已完成"
            st.balloons()
            st.success("功德+1！")

# 功德记录
st.divider()
st.subheader("功德记录")
if st.session_state.deeds_log:
    for deed in reversed(st.session_state.deeds_log):
        status = "✅" if deed["status"] == "已完成" else "⏳"
        st.write(f"{status} {deed['time']} - {deed['task']}")
    
    # 统计
    completed = sum(1 for d in st.session_state.deeds_log if d["status"] == "已完成")
    st.metric("累计功德", f"{completed} 件")
else:
    st.info("点击上方按钮生成第一个任务")

# 页脚
st.divider()
st.caption("💡 数据仅保存在当前会话中")
