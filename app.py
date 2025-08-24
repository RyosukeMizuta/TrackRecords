
import streamlit as st
import pandas as pd

st.title("HUTE陸上記録データベース")

CSV_URL = "https://raw.githubusercontent.com/RyosukeMizuta/TrackRecords/main/TrackRecords.csv"

@st.cache_data
def load_data():
    return pd.read_csv(CSV_URL, encoding="shift-jis")

try:
    df = load_data()
    st.success("CSVファイルの読み込みに成功しました！")
except Exception as e:
    st.error(f"CSVファイルの読み込みに失敗しました: {e}")

st.sidebar.header("検索条件")

name_options = [""] + sorted(df["氏名"].dropna().unique().tolist())
grade_options = [""] + sorted(df["学年"].dropna().unique().tolist())
gender_options = [""] + sorted(df["性別"].dropna().unique().tolist())
date_options = [""] + sorted(df["日時"].dropna().unique().tolist())
event_options = [""] + sorted(df["種目"].dropna().unique().tolist())
venue_options = [""] + sorted(df["会場"].dropna().unique().tolist())
meet_options = [""] + sorted(df["大会名"].dropna().unique().tolist())
wind_options = [""] + sorted(df["風速"].dropna().unique().tolist())

name = st.sidebar.selectbox("氏名", name_options)
grade = st.sidebar.selectbox("学年", grade_options)
gender = st.sidebar.selectbox("性別", gender_options)
date = st.sidebar.selectbox("日時", date_options)
event = st.sidebar.selectbox("種目", event_options)
venue = st.sidebar.selectbox("会場", venue_options)
meet = st.sidebar.selectbox("大会名", meet_options)
wind = st.sidebar.selectbox("風速", wind_options)

filtered_df = df.copy()
if name:
    filtered_df = filtered_df[filtered_df["氏名"] == name]
if grade:
    filtered_df = filtered_df[filtered_df["学年"] == grade]
if gender:
    filtered_df = filtered_df[filtered_df["性別"] == gender]
if date:
    filtered_df = filtered_df[filtered_df["日時"] == date]
if event:
    filtered_df = filtered_df[filtered_df["種目"] == event]
if venue:
    filtered_df = filtered_df[filtered_df["会場"] == venue]
if meet:
    filtered_df = filtered_df[filtered_df["大会名"] == meet]
if wind:
    filtered_df = filtered_df[filtered_df["風速"] == wind]

st.subheader("検索結果")
st.dataframe(filtered_df)

st.subheader("記録の統計")
if not filtered_df.empty:
    records = pd.to_numeric(filtered_df["記録"], errors="coerce").dropna()
    st.write(f"平均記録: {records.mean():.2f}")
    st.write(f"最高記録: {records.max():.2f}")

    st.write(f"最低記録: {records.min():.2f}")
