import pandas as pd
import os
from CA0faze1 import *
from math import log


num_of_all_words_in_each_category = dict()


def re_init(df_train):
    for category in all_category_names:
        num_of_all_words_in_each_category[category] = sum(df_train.loc[category])


def calc_log_prob_pC(category) -> float:
    return log(num_of_books_in_each_category[category] / sum(num_of_books_in_each_category.values()))


def calc_log_prob_sum_pXC(category, df_train, list_of_words_in_test) -> float:
    # Additive smoothing (n_word + alpha) / (n_total + alpha*n_unique_all_words_dataBase)
    sum_of_logs = 0
    for word in list_of_words_in_test:
        if word in all_of_words:
            face_of_fraction = df_train.loc[category, word] + ALPHA
            dominator_of_fraction = num_of_all_words_in_each_category[category] + (ALPHA * len(df_train.columns))
            sum_of_logs += log(face_of_fraction / dominator_of_fraction)
        else:
            face_of_fraction = 0 + ALPHA
            dominator_of_fraction = num_of_all_words_in_each_category[category] + (ALPHA * len(df_train.columns))
            sum_of_logs += log(face_of_fraction / dominator_of_fraction)
    return sum_of_logs


def calc_probability(df_train, list_of_words_in_test) -> dict:
        # p(C|X) ~ log(p(C)) + sum(log(p(x[1] | C) ... log(p(x[n])))
    all_category_prob = dict()
    for category in all_category_names:
        all_category_prob[category] = calc_log_prob_pC(category)\
                                      + calc_log_prob_sum_pXC(category, df_train, list_of_words_in_test)
    return all_category_prob


def solve_problem(dict_test, df_train):
    all_categories_of_each_row = dict()
    for index, list_of_words_in_book in dict_test.items():
        all_category_prob_for_one_book = calc_probability(df_train, list_of_words_in_book)
        category_max_prob = max(all_category_prob_for_one_book, key=all_category_prob_for_one_book.get)
        all_categories_of_each_row[index] = category_max_prob
    return all_categories_of_each_row


def get_BoW_from_file():
    return pd.read_csv(FILE_ADDRESS_IN_PC)


def main_judge():
    get_permissions()
    init_const()
    df_train = pre_process('books_train.csv', mode='DataBase')  # BoW
    dict_test = pre_process('books_test.csv', mode='Test')
    re_init(df_train)
    answer = solve_problem(dict_test, df_train)
    return answer


if '__main__' == __name__:
    init_const()

    df_train = pre_process('books_train.csv', mode='DataBase')  # BoW

    df_test = pre_process('books_test.csv', mode='Test')

    re_init(df_train)

    answer = solve_problem(df_test, df_train)
