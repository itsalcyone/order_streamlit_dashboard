import streamlit as st

def show_dataset_block(dataset):
    """
    Блок дашборда с датасетом и фильтрами
    :param dataset: датасет
    """
    dataset_block = st.container(border=False)

    with dataset_block:
        st.subheader("Сырые данные")
        col1, col2 = st.columns(2)

        with col1:
            order_date = st.date_input("Период", value=(dataset.get_column_aggregation('order_date', 'min'),
                                                        dataset.get_column_aggregation('order_date', 'max')))


        with col2:
            category = st.multiselect( "Категория", list(dataset.get_unique_column_values('category')))

        dataset.dataset = dataset.apply_filters(category, order_date)
        st.dataframe(dataset.dataset)