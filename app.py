import streamlit as st
import random
from datetime import datetime
import pandas as pd

# 初始化数据
if 'deeds_log' not in st.session_state:
    st.session_state.deeds_log = []
if 'custom_deeds' not in st.session_state:
    st.session_state.custom_deeds = [
        "给外卖小哥说谢谢",
        "捡起路边垃圾",
        "给流浪猫添水"
    ]

# 页面设置
st.set_page_config(
    page_title="功德+1 Lite",
    page_icon="🪷",
    layout="centered"
)

# 主界面
st.title("🪷 每日功德+1 Lite")
st.caption("让善意成为习惯 - 极简版")

# 功能区
col1, col2 = st.columns([3, 2])

with col1:
    # 任务管理
    st.subheader("任务管理")
    
    # 添加新任务
    new_deed = st.text_input("添加自定义任务", placeholder="输入你的善意小行动")
    if st.button("添加任务"):
        if new_deed:
            st.session_state.custom_deeds.append(new_deed)
            st.success("添加成功！")
        else:
            st.warning("请输入任务内容")
    
    # 生成任务
    st.divider()
    if st.button("生成今日任务"):
        if st.session_state.custom_deeds:
            deed = random.choice(st.session_state.custom_deeds)
            st.session_state.deeds_log.append({
                "task": deed,
                "time": datetime.now().strftime("%m-%d %H:%M"),
                "status": "进行中"
            })
            st.success(f"今日任务：**{deed}**")
        else:
            st.warning("请先添加任务")

with col2:
    # 任务状态
    st.subheader("当前任务")
    if st.session_state.deeds_log and st.session_state.deeds_log[-1]["status"] == "进行中":
        latest = st.session_state.deeds_log[-1]
        st.write(f"**{latest['task']}**")
        st.caption(f"生成时间：{latest['time']}")
        
        if st.button("标记完成"):
            st.session_state.deeds_log[-1]["status"] = "已完成"
            st.balloons()
            st.success("功德+1！")
    else:
        st.info("暂无进行中任务")

# 功德记录
st.divider()
st.subheader("功德记录")
if st.session_state.deeds_log:
    # 使用原生Streamlit展示代替DataFrame
    for deed in reversed(st.session_state.deeds_log):
        status_emoji = "✅" if deed["status"] == "已完成" else "⏳"
        st.write(f"{status_emoji} {deed['time']} - {deed['task']}")
    
    # 简单计数
    completed = sum(1 for d in st.session_state.deeds_log if d["status"] == "已完成")
    st.metric("累计完成", f"{completed} 件功德")
else:
    st.info("还没有功德记录哦")

# 页脚
st.divider()
st.caption("💡 数据仅保存在浏览器内存中，刷新会重置")
