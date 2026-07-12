import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

def show_charts_block(dataset):
    """
    Блок дашборда с графиками
    :param dataset: датасет
    """
    charts_block = st.container(border=False)

    with charts_block:
        st.subheader("Визуализация")
        col1, col2, col3 = st.columns(3)

        with col1:
            top_items_by_revenue = dataset.top_n_category_by_value('item_name','revenue', 'sum', 'revenue', False, 10)

            fig = px.bar(
                top_items_by_revenue,
                x="revenue",
                y="item_name",
                orientation="h",
                title="ТОП товаров по выручке"
            )

            fig.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig, width='stretch')

        with col2:
            categories_by_revenue = dataset.top_n_category_by_value('category', 'revenue', 'sum', 'revenue', False)

            fig = px.pie(
                categories_by_revenue,
                values="revenue",
                names="category",
                title="Выручка по категориям"
            )

            fig.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig, width='stretch')

        with col3:

            days = {
                0: "Пн",
                1: "Вт",
                2: "Ср",
                3: "Чт",
                4: "Пт",
                5: "Сб",
                6: "Вс"
            }

            weekdays_by_orders_number = dataset.top_n_category_by_value('weekday', 'order_id', 'count', 'weekday', True)
            weekdays_by_orders_number['weekday'] = weekdays_by_orders_number['weekday'].map(lambda x: days[x])

            fig = px.bar(
                weekdays_by_orders_number,
                x="weekday",
                y="order_id",
                title="Заказы по дням недели"
            )

            fig.update_layout(height=350, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig, width='stretch')