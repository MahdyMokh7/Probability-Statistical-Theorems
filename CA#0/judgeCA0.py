from CA0faze2 import *
from timeit import default_timer as timer
from math import ceil


def get_real_answer():
    df_test = pd.read_csv('books_test.csv')
    dict_correct_answers = dict()
    for i in range(len(df_test.index)):
        dict_correct_answers[i] = df_test.loc[i, 'categories']
    return dict_correct_answers


def print_answers(mine, real):
    correct_num_of_answers = 0
    dict_pob = dict()
    dict_tot = dict()

    for i in range(len(mine)):
        dict_tot[real[i]] = dict_tot.get(real[i], 0) + 1
        if mine[i] == real[i]:
            dict_pob[real[i]] = dict_pob.get(real[i], 0) + 1
            correct_num_of_answers += 1
        # print(i, '  mine: ', mine[i], '  real: ', real[i])
    save_report_file('Accuracy of each category:\n')
    for category in all_category_names:
        print(category, ':  %', ceil(100 * (dict_pob[category] / dict_tot[category])))
        save_report_file(f"{category}:  %{ceil(100 * (dict_pob[category] / dict_tot[category]))}\n")
    return int(100 * (correct_num_of_answers / len(mine)))


def save_report_file(line: str):
    with open('C:\\Users\\NoteBook\\Desktop\\programing\\python\\python EPS\\CA#0\\report.txt', 'a', encoding="utf-8") as f_hand:
        f_hand.write(line)



if __name__ == '__main__':
    timer1 = timer()
    my_answer = main_judge()
    real_answer = get_real_answer()
    save_report_file('-------------------\n')
    save_report_file(f"perm_lemm: {perm_lemm},  perm_stem: {perm_stem},  "
                     f"perm_clear_garbage_words: {perm_clear_garbage_words},  alpha: {ALPHA}\n")
    tot_accuracy = print_answers(mine=my_answer, real=real_answer)
    timer2 = timer()
    print(f'runTime:  {(timer2 - timer1) // 60}min {(timer2 - timer1) % 60}sec')
    save_report_file(f'runTime:  {(timer2 - timer1) // 60}min {(timer2 - timer1) % 60}sec\n')
    print('accuracy:  %', tot_accuracy)
    save_report_file(f'accuracy:  %{tot_accuracy}\n')

