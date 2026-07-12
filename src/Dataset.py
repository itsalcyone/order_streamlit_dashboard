import pandas as pd
from pathlib import Path
import streamlit as st
from datetime import timedelta

@st.cache_data
def load_data(folder_path='data/'):
    """
    Загрузка датасетов с товарами (items.csv), заказами (orders.csv) и пользователями (users.csv) и объединение в
    один датасет
    """
    items_df = pd.read_csv(folder_path / "items.csv")
    orders_df = pd.read_csv(folder_path / "orders.csv")
    users_df = pd.read_csv(folder_path / "users.csv")

    return orders_df.merge(users_df, on="user_id", how="left").merge(items_df, on="item_id", how="left")

def clean_and_enrich_data(dataset):
    """
    Приведение типов и очистка данных
    :param dataset: датасет
    """
    dataset['order_date'] = pd.to_datetime(dataset['order_date'], errors="coerce")
    dataset['registration_date'] = pd.to_datetime(dataset['registration_date'], errors="coerce")
    dataset['revenue'] = dataset['quantity'] * dataset['price_per_unit']
    dataset['weekday'] = dataset['order_date'].dt.weekday

    return dataset

class Dataset:
    """
    Класс предназначен для формирования датасета и работы с ним
    """
    def __init__(self, folder_path):
        self.dataset = load_data(Path(folder_path))
        self.dataset = clean_and_enrich_data(self.dataset)

    def get_unique_column_values(self, column_name):
        """
        Возвращает список уникальных значений столбца
        :param column_name: наименование столбца
        """
        return sorted(self.dataset[column_name].unique())

    def get_column_aggregation(self, column_name, aggregation_function):
        """
        Возвращает агрегат по столбцу
        :param column_name: наименование столбца
        :param aggregation_function: функция агрегации
        """
        allowed = {
            "max",
            "min",
            "count",
            "nunique",
            "sum"
        }

        if aggregation_function not in allowed:
            raise ValueError(
                f"Unsupported aggregation: {aggregation_function}"
            )

        return getattr(self.dataset[column_name], aggregation_function)()

    def apply_filters(self, categories, period):
        """
        Фильтрует датасет
        :param categories: список категорий для фильтрации
        :param period: период для фильтрации
        """
        copy_dataset = self.dataset.copy()


        if len(categories) > 0:
            copy_dataset = copy_dataset[copy_dataset["category"].isin(categories)]

        if len(period) == 2:
            start, end = pd.to_datetime(period)
            copy_dataset = copy_dataset[(copy_dataset["order_date"] >= start) & (copy_dataset["order_date"] < end + timedelta(days=1))]

        return copy_dataset

    def top_n_category_by_value(self, category_column, value_column, aggregation_function, sort_column, ascending=False, n=None):
        """
        Получает топ n товаров по выручке
        :param category_column: наименование категориального столбца топа
        :param value_column: наименование числового столбца топа
        :param aggregation_function: функция агрегации
        :param sort_column: наименование столбца сортировки
        :param ascending: направление сортировки
        :param n: количество позиций в топе
        """
        allowed = {
            "max",
            "min",
            "count",
            "nunique",
            "sum"
        }

        if aggregation_function not in allowed:
            raise ValueError(
                f"Unsupported aggregation: {aggregation_function}"
            )

        df = self.dataset.groupby(category_column).agg({value_column: aggregation_function}).reset_index().sort_values(by=sort_column,
                                                                                                                       ascending=ascending)

        if n is not None:
            return df.head(n)

        return df


