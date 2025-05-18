import streamlit as st
import random
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

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
    page_title="功德+1 Pro",
    page_icon="🪷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 主界面
st.title("🪷 每日功德+1 Pro")
st.caption("让善意成为习惯")

# 侧边栏 - 新增任务
with st.sidebar:
    st.subheader("添加自定义任务")
    new_deed = st.text_input("输入你的善意小任务")
    if st.button("添加任务"):
        if new_deed:
            st.session_state.custom_deeds.append(new_deed)
            st.success("添加成功！")
        else:
            st.warning("请输入任务内容")

# 功能区
tab1, tab2, tab3 = st.tabs(["今日任务", "功德记录", "成就统计"])

with tab1:
    # 任务生成区
    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader("生成今日任务")
        if st.button("随机推荐任务"):
            if st.session_state.custom_deeds:
                deed = random.choice(st.session_state.custom_deeds)
                st.session_state.deeds_log.append({
                    "task": deed,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "status": "进行中"
                })
                st.balloons()
                st.success(f"今日任务：**{deed}**")
            else:
                st.warning("请先添加任务")
    
    with col2:
        st.subheader("任务状态")
        if st.session_state.deeds_log and st.session_state.deeds_log[-1]["status"] == "进行中":
            if st.button("标记完成"):
                st.session_state.deeds_log[-1]["status"] = "已完成"
                st.success("功德+1！")

with tab2:
    # 记录展示
    st.subheader("功德簿")
    if st.session_state.deeds_log:
        df = pd.DataFrame(st.session_state.deeds_log)
        st.dataframe(df, hide_index=True, use_container_width=True)
        
        # 简单统计
        completed = df[df["status"]=="已完成"].shape[0]
        st.metric("累计功德", f"{completed} 件")
    else:
        st.info("还没有功德记录哦")

with tab3:
    # 可视化统计
    st.subheader("功德趋势")
    if st.session_state.deeds_log:
        df = pd.DataFrame(st.session_state.deeds_log)
        df['date'] = pd.to_datetime(df['time']).dt.date
        daily_count = df.groupby('date').size()
        
        fig, ax = plt.subplots()
        daily_count.plot(kind='bar', ax=ax, color='green')
        plt.xticks(rotation=45)
        plt.title("每日功德积累")
        st.pyplot(fig)
    else:
        st.info("暂无统计数据")

# 页脚
st.divider()
st.caption("💡 小善举积累大改变 | 数据仅保存在浏览器内存中")
