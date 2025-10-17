import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

try:
    df_data = st.session_state['data']
except:
    df_data = pd.read_csv('CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= 2023]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state['data'] = df_data

clubes = df_data['Club'].unique()
club = st.sidebar.selectbox("Clube", clubes)

df_player = df_data[(df_data['Club'] == club)]

players = df_player['Name'].unique()
player = st.sidebar.selectbox("Jogador", players)

player_stats = df_data[df_data['Name'] == player].iloc[0]

st.image(player_stats['Photo'])
st.title(player_stats['Name'])

st.markdown(f'**Clube:** {player_stats["Club"]}')
st.markdown(f'**Posição:** {player_stats["Position"]}')

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f'**Idade:** {player_stats["Age"]}')
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f'Overall {player_stats["Overall"]}')
st.progress(int(player_stats["Overall"]))

col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")