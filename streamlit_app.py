import streamlit as st
import pandas as pd
import plotly.express as px
import sys

# Importa funções do arquivo de backend
sys.path.append('.')
from update_data import coletar_links, baixar_arquivos, processar_arquivos, analisar_e_salvar
@st.cache_data
def update_and_load_data():
    try:
        with st.spinner("🔄 Atualizando dados..."):
            file_links = coletar_links()
            downloaded_files = baixar_arquivos(file_links)
            all_dataframes = processar_arquivos(downloaded_files)
            monthy_df, corr_df, df_selected = analisar_e_salvar(all_dataframes)
        st.success("✅ Dados atualizados com sucesso!")
        return monthy_df, corr_df, df_selected
    except Exception as e:
        st.error(f"Erro durante atualização: {e}")
        return pd.DataFrame(), pd.DataFrame()
def display_attendance_dashboard(df, prefix, label):
    filtered_df = df[df["Node_ID"].astype(str).str.startswith(prefix)]
    if not filtered_df.empty:
        node_id = st.selectbox(f"Selecione um {label} (Presença):", sorted(filtered_df["Node_ID"].unique()))
        df_filtrado = filtered_df[filtered_df["Node_ID"] == node_id].sort_values(by='Month')
        df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%B')
        fig = px.bar(
            df_filtrado,
            x="Month_Str",
            y="Monthly_Attendance_Percentage",
            labels={"Month_Str": "Mês", "Monthly_Attendance_Percentage": "Presença (%)"},
            color="Monthly_Attendance_Percentage",
            color_continuous_scale=px.colors.sequential.Viridis
        )
        fig.update_layout(yaxis_range=[0, 100])
        st.subheader(f"{label} Selecionado: {node_id}")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning(f"Não há dados de presença para {label} com prefixo '{prefix}'.")

def display_correlation_dashboard(df, prefix, label):
    filtered_df = df[df["Node_ID"].astype(str).str.startswith(prefix)]
    if not filtered_df.empty:
        node_id = st.selectbox(f"Selecione um {label} (Correlação):", sorted(filtered_df["Node_ID"].unique()))
        df_filtrado = filtered_df[filtered_df["Node_ID"] == node_id].sort_values(by='Month')
        df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%B')
        meses_falha = df_filtrado[df_filtrado['Correlation'] > -0.75]['Month_Str'].tolist()
        if meses_falha:
            st.warning(f"⚠️ Possível falha nos meses: {', '.join(meses_falha)}.")
        fig = px.bar(
            df_filtrado,
            x="Month_Str",
            y="Correlation",
            labels={"Month_Str": "Mês", "Correlation": "Correlação"},
            color_discrete_sequence=["indianred"]
        )
        fig.add_shape(
            type="line", x0=-0.5, x1=len(df_filtrado['Month_Str'].unique()) - 0.5,
            y0=-0.75, y1=-0.75,
            line=dict(color="Red", width=2, dash="dash")
        )
        fig.update_layout(yaxis_range=[-1, 1])
        st.subheader(f"{label} Selecionado: {node_id}")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning(f"Não há dados de correlação para {label} com prefixo '{prefix}'.")

def display_p_value_chart(df_selected):
    st.subheader("📊 Valores de p por Nó")
    if not df_selected.empty and {'Node_ID', 'Month', 'P_Value'}.issubset(df_selected.columns):
        filtered_df = df_selected[df_selected["Node_ID"].astype(str).str.startswith("100")]
        if not filtered_df.empty:
            selected_node = st.selectbox("Selecione um Piezômetro (Valor p):", sorted(filtered_df["Node_ID"].unique()))
            df_filtrado = filtered_df[filtered_df["Node_ID"] == selected_node].copy()
            df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%Y-%m')
            fig = px.line(
                df_filtrado,
                x="Month_Str",
                y="P_Value",
                labels={"Month_Str": "Mês", "P_Value": "Valor p"},
                markers=True
            )
            fig.update_layout(yaxis_range=[0, 1])
            st.subheader(f"Nó Selecionado: {selected_node}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("⚠️ Sem dados disponíveis para nós com prefixo '100'.")
    else:
        st.warning("⚠️ As colunas necessárias não estão disponíveis.")

def main():
    st.title("🔎 Dados - Barragem Paiva Castro")
    monthy_df, corr_df, df_selected = update_and_load_data()

    tab1, tab2, tab3 = st.tabs(["📊 Presença", "📈 Correlação", "🧪 Valor p"])

    with tab1:
        display_attendance_dashboard(monthy_df, "100", "Piezômetro")
        display_attendance_dashboard(monthy_df, "200", "NA")
        display_attendance_dashboard(monthy_df, "500", "MT")
        display_attendance_dashboard(monthy_df, "600", "Tiltímetro")
        display_attendance_dashboard(monthy_df, "900", "LT")

    with tab2:
        display_correlation_dashboard(corr_df, "100", "Piezômetro")
        display_correlation_dashboard(corr_df, "200", "NA")
        display_correlation_dashboard(corr_df, "500", "MT")
        display_correlation_dashboard(corr_df, "600", "Tiltímetro")
        display_correlation_dashboard(corr_df, "900", "LT")

    with tab3:
        display_p_value_chart(df_selected)

if __name__ == "__main__":
    main()

