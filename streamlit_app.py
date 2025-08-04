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
def display_attendance_dashboard1(monthy_df):
    st.header("📊 Porcentagem de entrega de Dados - Piezômetro")

    if not monthy_df.empty and 'Node_ID' in monthy_df.columns:
        # Filtra apenas os Node_ID que começam com "100"
        filtered_df = monthy_df[monthy_df["Node_ID"].astype(str).str.startswith("100")]

        if not filtered_df.empty:
            node_id = st.selectbox(
                "Selecione um Piezômetro (Presença):",
                sorted(filtered_df["Node_ID"].unique())
            )
            df_filtrado = filtered_df[filtered_df["Node_ID"] == node_id].sort_values(by='Month')

            # Mostrar nome do mês (em inglês)
            df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%B')

            fig = px.bar(
                df_filtrado,
                x="Month_Str",
                y="Monthly_Attendance_Percentage",
                labels={"Month_Str": "Month", "Monthly_Attendance_Percentage": "Attendance (%)"},
                color="Monthly_Attendance_Percentage",
                color_continuous_scale=px.colors.sequential.Viridis
            )
            fig.update_layout(yaxis_range=[0, 100], xaxis_title="Month")
            st.subheader(f"Piezômetro Selecionado: {node_id}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Não há Piezômetros que começam com '100'.")
    else:
        st.warning("Nenhum dado disponível para exibir.")
def display_attendance_dashboard2(monthy_df):
    st.header("📊 Porcentagem de entrega de Dados - Medidor de nivel d'água")

    if not monthy_df.empty and 'Node_ID' in monthy_df.columns:
        # Filtra apenas os Node_ID que começam com "100"
        filtered_df = monthy_df[monthy_df["Node_ID"].astype(str).str.startswith("200")]

        if not filtered_df.empty:
            node_id = st.selectbox(
                "Selecione um NA (Presença):",
                sorted(filtered_df["Node_ID"].unique())
            )
            df_filtrado = filtered_df[filtered_df["Node_ID"] == node_id].sort_values(by='Month')

            # Mostrar nome do mês (em inglês)
            df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%B')

            fig = px.bar(
                df_filtrado,
                x="Month_Str",
                y="Monthly_Attendance_Percentage",
                labels={"Month_Str": "Month", "Monthly_Attendance_Percentage": "Attendance (%)"},
                color="Monthly_Attendance_Percentage",
                color_continuous_scale=px.colors.sequential.Viridis
            )
            fig.update_layout(yaxis_range=[0, 100], xaxis_title="Month")
            st.subheader(f"NA Selecionado: {node_id}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Não há Piezômetros que começam com '100'.")
    else:
        st.warning("Nenhum dado disponível para exibir.")
def display_attendance_dashboard3(monthy_df):
    st.header("📊 Porcentagem de entrega de Dados - MT")

    if not monthy_df.empty and 'Node_ID' in monthy_df.columns:
        # Filtra apenas os Node_ID que começam com "500"
        filtered_df = monthy_df[monthy_df["Node_ID"].astype(str).str.startswith("500")]

        if not filtered_df.empty:
            node_id = st.selectbox(
                "Selecione um MT (Presença):",
                sorted(filtered_df["Node_ID"].unique())
            )
            df_filtrado = filtered_df[filtered_df["Node_ID"] == node_id].sort_values(by='Month')

            # Mostrar nome do mês (em inglês)
            df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%B')

            fig = px.bar(
                df_filtrado,
                x="Month_Str",
                y="Monthly_Attendance_Percentage",
                labels={"Month_Str": "Month", "Monthly_Attendance_Percentage": "Attendance (%)"},
                color="Monthly_Attendance_Percentage",
                color_continuous_scale=px.colors.sequential.Viridis
            )
            fig.update_layout(yaxis_range=[0, 100], xaxis_title="Month")
            st.subheader(f"MT Selecionado: {node_id}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Não há Piezômetros que começam com '300'.")
    else:
        st.warning("Nenhum dado disponível para exibir.")

def display_attendance_dashboard4(monthy_df):
    st.header("📊 Porcentagem de entrega de Dados - Tiltímetro ")

    if not monthy_df.empty and 'Node_ID' in monthy_df.columns:
        # Filtra apenas os Node_ID que começam com "600"
        filtered_df = monthy_df[monthy_df["Node_ID"].astype(str).str.startswith("600")]

        if not filtered_df.empty:
            node_id = st.selectbox(
                "Selecione um Tiltimetro (Presença):",
                sorted(filtered_df["Node_ID"].unique())
            )
            df_filtrado = filtered_df[filtered_df["Node_ID"] == node_id].sort_values(by='Month')

            # Mostrar nome do mês (em inglês)
            df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%B')

            fig = px.bar(
                df_filtrado,
                x="Month_Str",
                y="Monthly_Attendance_Percentage",
                labels={"Month_Str": "Month", "Monthly_Attendance_Percentage": "Attendance (%)"},
                color="Monthly_Attendance_Percentage",
                color_continuous_scale=px.colors.sequential.Viridis
            )
            fig.update_layout(yaxis_range=[0, 100], xaxis_title="Month")
            st.subheader(f"Tiltimetro Selecionado: {node_id}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Não há Piezômetros que começam com '600'.")
    else:
        st.warning("Nenhum dado disponível para exibir.")

def display_attendance_dashboard5(monthy_df):
    st.header("📊 Porcentagem de entrega de Dados - LT ")

    if not monthy_df.empty and 'Node_ID' in monthy_df.columns:
        # Filtra apenas os Node_ID que começam com "900"
        filtered_df = monthy_df[monthy_df["Node_ID"].astype(str).str.startswith("900")]

        if not filtered_df.empty:
            node_id = st.selectbox(
                "Selecione um LT (Presença):",
                sorted(filtered_df["Node_ID"].unique())
            )
            df_filtrado = filtered_df[filtered_df["Node_ID"] == node_id].sort_values(by='Month')

            # Mostrar nome do mês (em inglês)
            df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%B')

            fig = px.bar(
                df_filtrado,
                x="Month_Str",
                y="Monthly_Attendance_Percentage",
                labels={"Month_Str": "Month", "Monthly_Attendance_Percentage": "Attendance (%)"},
                color="Monthly_Attendance_Percentage",
                color_continuous_scale=px.colors.sequential.Viridis
            )
            fig.update_layout(yaxis_range=[0, 100], xaxis_title="Month")
            st.subheader(f"Tiltimetro Selecionado: {node_id}")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Não há Piezômetros que começam com '600'.")
    else:
        st.warning("Nenhum dado disponível para exibir.")

def display_correlation_dashboard1(df_corr):
    st.header("📈 Funcionamento do sensor - Piezômetro")

    if not df_corr.empty and 'Node_ID' in df_corr.columns:
        # Filtra apenas os Node_ID que começam com "100"
        filtered_df = df_corr[df_corr["Node_ID"].astype(str).str.startswith("100")]

        if not filtered_df.empty:
            node_id = st.selectbox(
                "Selecione um Piezômetro (Correlação):",
                sorted(filtered_df["Node_ID"].unique())
            )
            df_filtrado = filtered_df[filtered_df["Node_ID"] == node_id].copy()
            df_filtrado = df_filtrado.sort_values(by='Month')

            # Mostrar nome do mês (em inglês)
            df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%B')

            # Verificar correlações acima de -0.75 e exibir mensagem única
            meses_falha = df_filtrado[df_filtrado['Correlation'] > -0.75]['Month_Str'].tolist()
            if meses_falha:
                meses_formatados = ', '.join(meses_falha)
                st.warning(f"⚠️ Possível falha no sensor ou na conversão dos dados nos meses de: {meses_formatados}.")

            fig = px.bar(
                df_filtrado,
                x="Month_Str",
                y="Correlation",
                labels={"Month_Str": "Month", "Correlation": "Correlation"},
                color_discrete_sequence=["indianred"]
            )
            fig.add_shape(
                type="line",
                x0=-0.5,
                x1=len(df_filtrado['Month_Str'].unique()) - 0.5,
                y0=-0.75,
                y1=-0.75,
                line=dict(color="Red", width=2, dash="dash")
            )
            fig.update_layout(yaxis_range=[-1, 1], xaxis_title="Month")
            st.subheader(f"Piezômetro Selecionado: {node_id}")
            st.plotly_chart(fig, use_container_width=True)
                    
    else:
        st.warning("Dados de correlação não disponíveis.")

def display_correlation_dashboard2(df_corr):
    st.header("📈 Funcionamento do sensor - Medidor de Nível d'água")

    if not df_corr.empty and 'Node_ID' in df_corr.columns:
        # Filtra apenas os Node_ID que começam com "200"
        filtered_df = df_corr[df_corr["Node_ID"].astype(str).str.startswith("200")]

        if not filtered_df.empty:
            node_id = st.selectbox(
                "Selecione um NA (Correlação):",
                sorted(filtered_df["Node_ID"].unique())
            )
            df_filtrado = filtered_df[filtered_df["Node_ID"] == node_id].copy()
            df_filtrado = df_filtrado.sort_values(by='Month')

            # Mostrar nome do mês (em inglês)
            df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%B')

            # Verificar correlações acima de -0.75 e exibir mensagem única
            meses_falha = df_filtrado[df_filtrado['Correlation'] > -0.75]['Month_Str'].tolist()
            if meses_falha:
                meses_formatados = ', '.join(meses_falha)
                st.warning(f"⚠️ Possível falha no sensor ou na conversão dos dados nos meses de: {meses_formatados}.")

            fig = px.bar(
                df_filtrado,
                x="Month_Str",
                y="Correlation",
                labels={"Month_Str": "Month", "Correlation": "Correlation"},
                color_discrete_sequence=["indianred"]
            )
            fig.add_shape(
                type="line",
                x0=-0.5,
                x1=len(df_filtrado['Month_Str'].unique()) - 0.5,
                y0=-0.75,
                y1=-0.75,
                line=dict(color="Red", width=2, dash="dash")
            )
            fig.update_layout(yaxis_range=[-1, 1], xaxis_title="Month")
            st.subheader(f"NA Selecionado: {node_id}")
            st.plotly_chart(fig, use_container_width=True)
                    
    else:
        st.warning("Dados de correlação não disponíveis.")

def display_correlation_dashboard3(df_corr):
    st.header("📈 Funcionamento do sensor - MT ")

    if not df_corr.empty and 'Node_ID' in df_corr.columns:
        # Filtra apenas os Node_ID que começam com "500"
        filtered_df = df_corr[df_corr["Node_ID"].astype(str).str.startswith("500")]

        if not filtered_df.empty:
            node_id = st.selectbox(
                "Selecione um MT (Correlação):",
                sorted(filtered_df["Node_ID"].unique())
            )
            df_filtrado = filtered_df[filtered_df["Node_ID"] == node_id].copy()
            df_filtrado = df_filtrado.sort_values(by='Month')

            # Mostrar nome do mês (em inglês)
            df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%B')

            # Verificar correlações acima de -0.75 e exibir mensagem única
            meses_falha = df_filtrado[df_filtrado['Correlation'] > -0.75]['Month_Str'].tolist()
            if meses_falha:
                meses_formatados = ', '.join(meses_falha)
                st.warning(f"⚠️ Possível falha no sensor ou na conversão dos dados nos meses de: {meses_formatados}.")

            fig = px.bar(
                df_filtrado,
                x="Month_Str",
                y="Correlation",
                labels={"Month_Str": "Month", "Correlation": "Correlation"},
                color_discrete_sequence=["indianred"]
            )
            fig.add_shape(
                type="line",
                x0=-0.5,
                x1=len(df_filtrado['Month_Str'].unique()) - 0.5,
                y0=-0.75,
                y1=-0.75,
                line=dict(color="Red", width=2, dash="dash")
            )
            fig.update_layout(yaxis_range=[-1, 1], xaxis_title="Month")
            st.subheader(f"NA Selecionado: {node_id}")
            st.plotly_chart(fig, use_container_width=True)
                    
    else:
        st.warning("Dados de correlação não disponíveis.")

def display_correlation_dashboard4(df_corr):
    st.header("📈 Funcionamento do sensor - Tiltímetro ")

    if not df_corr.empty and 'Node_ID' in df_corr.columns:
        # Filtra apenas os Node_ID que começam com "600"
        filtered_df = df_corr[df_corr["Node_ID"].astype(str).str.startswith("600")]

        if not filtered_df.empty:
            node_id = st.selectbox(
                "Selecione um Tiltímetro (Correlação):",
                sorted(filtered_df["Node_ID"].unique())
            )
            df_filtrado = filtered_df[filtered_df["Node_ID"] == node_id].copy()
            df_filtrado = df_filtrado.sort_values(by='Month')

            # Mostrar nome do mês (em inglês)
            df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%B')

            # Verificar correlações acima de -0.75 e exibir mensagem única
            meses_falha = df_filtrado[df_filtrado['Correlation'] > -0.75]['Month_Str'].tolist()
            if meses_falha:
                meses_formatados = ', '.join(meses_falha)
                st.warning(f"⚠️ Possível falha no sensor ou na conversão dos dados nos meses de: {meses_formatados}.")

            fig = px.bar(
                df_filtrado,
                x="Month_Str",
                y="Correlation",
                labels={"Month_Str": "Month", "Correlation": "Correlation"},
                color_discrete_sequence=["indianred"]
            )
            fig.add_shape(
                type="line",
                x0=-0.5,
                x1=len(df_filtrado['Month_Str'].unique()) - 0.5,
                y0=-0.75,
                y1=-0.75,
                line=dict(color="Red", width=2, dash="dash")
            )
            fig.update_layout(yaxis_range=[-1, 1], xaxis_title="Month")
            st.subheader(f"NA Selecionado: {node_id}")
            st.plotly_chart(fig, use_container_width=True)
                    
    else:
        st.warning("Dados de correlação não disponíveis.")

def display_correlation_dashboard5(df_corr):
    st.header("📈 Funcionamento do sensor - LT ")

    if not df_corr.empty and 'Node_ID' in df_corr.columns:
        # Filtra apenas os Node_ID que começam com "900"
        filtered_df = df_corr[df_corr["Node_ID"].astype(str).str.startswith("900")]

        if not filtered_df.empty:
            node_id = st.selectbox(
                "Selecione um LT (Correlação):",
                sorted(filtered_df["Node_ID"].unique())
            )
            df_filtrado = filtered_df[filtered_df["Node_ID"] == node_id].copy()
            df_filtrado = df_filtrado.sort_values(by='Month')

            # Mostrar nome do mês (em inglês)
            df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%B')

            # Verificar correlações acima de -0.75 e exibir mensagem única
            meses_falha = df_filtrado[df_filtrado['Correlation'] > -0.75]['Month_Str'].tolist()
            if meses_falha:
                meses_formatados = ', '.join(meses_falha)
                st.warning(f"⚠️ Possível falha no sensor ou na conversão dos dados nos meses de: {meses_formatados}.")

            fig = px.bar(
                df_filtrado,
                x="Month_Str",
                y="Correlation",
                labels={"Month_Str": "Month", "Correlation": "Correlation"},
                color_discrete_sequence=["indianred"]
            )
            fig.add_shape(
                type="line",
                x0=-0.5,
                x1=len(df_filtrado['Month_Str'].unique()) - 0.5,
                y0=-0.75,
                y1=-0.75,
                line=dict(color="Red", width=2, dash="dash")
            )
            fig.update_layout(yaxis_range=[-1, 1], xaxis_title="Month")
            st.subheader(f"NA Selecionado: {node_id}")
            st.plotly_chart(fig, use_container_width=True)
                    
    else:
        st.warning("Dados de correlação não disponíveis.")

def display_p_value_chart(df_selected):
    st.header("📊 Valores de p por Nó ao longo do Tempo")

    if not df_selected.empty and {'Node_ID', 'Month', 'P_Value'}.issubset(monthy_df.columns):
        # Filtra nós que começam com "100"
        filtered_df = df_selected[df_selected["Node_ID"].astype(str).str.startswith("100")]

        if not filtered_df.empty:
            node_options = sorted(filtered_df["Node_ID"].unique())
            selected_node = st.selectbox("Selecione um Piezômetro (Valor p):", node_options)

            df_filtrado = filtered_df[filtered_df["Node_ID"] == selected_node].copy()
            df_filtrado['Month_Str'] = pd.to_datetime(df_filtrado['Month']).dt.strftime('%Y-%m')

            fig = px.line(
                df_filtrado,
                x="Month_Str",
                y="P_Value",
                labels={"Month_Str": "Data", "P_Value": "Valor p"},
                title=f"Valor p ao longo do tempo - Nó {selected_node}",
                markers=True
            )
            fig.update_layout(xaxis_title="Data", yaxis_title="Valor p", yaxis_range=[0, 1])
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("⚠️ Não há dados de nós que comecem com '100'.")
    else:
        st.warning("⚠️ As colunas necessárias ('Node_ID', 'Month', 'P_Value') não estão disponíveis.")


def main():
    st.title("🔎 Dados de Instrumentação - Barragem Paiva Castro")
    monthy_df, corr_df, df_selected = update_and_load_data()
    display_attendance_dashboard1(monthy_df)
    display_attendance_dashboard2(monthy_df)
    display_attendance_dashboard3(monthy_df)
    display_attendance_dashboard4(monthy_df)
    display_attendance_dashboard5(monthy_df)
    display_correlation_dashboard1(corr_df)
    display_correlation_dashboard2(corr_df)
    display_correlation_dashboard3(corr_df)
    display_correlation_dashboard4(corr_df)
    display_correlation_dashboard5(corr_df)
    display_p_value_chart(df_selected)

if __name__ == "__main__":
    main()
