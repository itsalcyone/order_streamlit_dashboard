import streamlit as st

def show_metrics_block(dataset):
    """
    Блок дашборда с основными метриками
    :param dataset: датасет
    """
    metrics_block = st.container(border=False)

    with metrics_block:
        st.subheader("Ключевые показатели")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric('Общее количество заказов', dataset.get_column_aggregation('order_id', 'count'))

        with col2:
            st.metric('Общая выручка', round(dataset.get_column_aggregation('revenue', 'sum'), 2))

        with col3:
            st.metric('Количество уникальных пользователей', dataset.get_column_aggregation('user_id', 'nunique'))

        with col4:
            st.metric('Средний чек', round(dataset.get_column_aggregation('revenue', 'sum') * 1.
                                           / dataset.get_column_aggregation('order_id', 'count'), 2))