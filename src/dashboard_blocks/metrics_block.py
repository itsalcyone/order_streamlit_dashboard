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
            orders_number = dataset.get_column_aggregation('order_id', 'count')
            st.metric('Общее количество заказов',orders_number )

        with col2:
            total_revenue = round(dataset.get_column_aggregation('revenue', 'sum'), 2)
            st.metric('Общая выручка', total_revenue)

        with col3:
            st.metric('Количество уникальных пользователей', dataset.get_column_aggregation('user_id', 'nunique'))

        with col4:
            st.metric('Средний чек', round(total_revenue * 1./ orders_number, 2) if orders_number > 0 else '-')