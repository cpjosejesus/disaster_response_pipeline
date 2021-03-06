import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """
    @description - load data from two csv files to create one unified DataFrame

    @input:
             message_filepath: (string) with the path of the messages.csv file
             categories_filepath: (string) with the path of categories.csv file
    @output:
             merged_df (DataFrame): messages and categories data merged together to one dataframe
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    df = pd.merge(messages, categories, on="id")
    return df


def clean_data(df):
    """
    @description - Clean the merged dataframe by following these steps:
                    1) rename the columns of different categories
                    2) remove duplicates

    @input - df (Dataframe) - unstructured and uncleaned data
    @output - df(dataFrame) cleaned data from messages and categories merged dataframe
    """
    categories = df["categories"].str.split(";", expand=True)

    row = categories.iloc[0]
    category_col = row.apply(lambda x: x.split("-")[0])
    categories.columns = category_col

    for col in categories:
        categories[col] = categories[col].apply(lambda x: int(x.split("-")[1]))

    df.drop("categories", axis=1, inplace=True)

    df = df.join(categories)
    df = df[df.related != 2]

    return df.drop_duplicates()


def save_data(df, database_filename):
    """
    @description - Save processed data into a sqlite database

    @input - df (dataframe): preprocessed and cleaned data

    @output - None
    """
    engine = create_engine(f"sqlite:///{database_filename}")
    df.to_sql("disaster_msg", engine, index=False, if_exists="replace")


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print("Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}".format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print("Cleaning data...")
        df = clean_data(df)

        print("Saving data...\n    DATABASE: {}".format(database_filepath))
        save_data(df, database_filepath)

        print("Cleaned data saved to database!")

    else:
        print(
            "Please provide the filepaths of the messages and categories "
            "datasets as the first and second argument respectively, as "
            "well as the filepath of the database to save the cleaned data "
            "to as the third argument. \n\nExample: python process_data.py "
            "disaster_messages.csv disaster_categories.csv "
            "DisasterResponse.db"
        )


if __name__ == "__main__":
    main()
