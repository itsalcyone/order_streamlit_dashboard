import streamlit as st

def show_results_block(dataset):
    """
    Блок дашборда с аналитическими выводами
    :param dataset: датасет
    """
    results_block = st.container(border=False)

    with results_block:
        st.subheader("Аналитические выводы")

        days = {
            0: "Пн",
            1: "Вт",
            2: "Ср",
            3: "Чт",
            4: "Пт",
            5: "Сб",
            6: "Вс"
        }

        st.markdown(f"Основная выручка приходится на категорию '{dataset.top_n_category_by_value('category','revenue', 'sum', 'revenue', False, 1).iloc[0,0]}'")
        st.markdown(f"Пик заказов наблюдается в {dataset.top_n_category_by_value('weekday','order_id', 'count', 'order_id', False, 1)['weekday'].map(lambda x: days[x]).iloc[0]}")
        st.markdown(f"Товар '{dataset.top_n_category_by_value('item_name','revenue', 'sum', 'revenue', False, 1).iloc[0,0]}' является лидером продаж")