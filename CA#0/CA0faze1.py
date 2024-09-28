import hazm as hz
import pandas as pd


FILE_ADDRESS_IN_PC = "C:\\Users\\NoteBook\\Desktop\\BoW.csv"


PUNCTUATION_MARKS = ()
PERSIAN_NUMBERS = ()
JUNK_WORDS = ()
all_of_words = set()
all_of_words_train = set()
all_of_words_test = set()
all_words_in_categories = dict()
all_words_in_categories_train = dict()
all_words_in_categories_test = dict()
all_category_names = set()
num_of_books_in_each_category = dict()
all_tests = dict()

normalizer = hz.Normalizer()
stemmer = hz.Stemmer()
lemmatizer = hz.Lemmatizer()

perm_lemm = True
perm_stem = True
perm_clear_garbage_words = True
ALPHA = 1e-100


def get_permissions():
    global perm_stem
    global perm_lemm
    global perm_clear_garbage_words
    global ALPHA
    try:
        perm_stem = bool(int(input("permission for stemming:(write '1' for yes or '0 for no)  ")))
        perm_lemm = bool(int(input("permission for lemmatizing:(write '1' for yes or '0 for no)  ")))
        perm_clear_garbage_words = bool(int(input("permission for clear garbage words:(write '1' for yes or '0 for no)  ")))
        ALPHA = float(input("initialize alpha:(write a number or '0' for the default value of program)  "))
        if ALPHA == 0:
            ALPHA = 0.7
    except Exception:
        print('Error permit: the program will run with default all true permits')



def init_const():
    global PUNCTUATION_MARKS
    global JUNK_WORDS
    global PERSIAN_NUMBERS
    PUNCTUATION_MARKS = ('.', '،', '؛', ':', '...', '؟', '!', '-')
    PERSIAN_NUMBERS = ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    JUNK_WORDS = hz.stopwords_list()


def cleanup(mode):
    global all_of_words
    global all_of_words_test
    global all_of_words_train
    global all_words_in_categories
    global all_words_in_categories_test
    global all_words_in_categories_train
    if mode == 'DataBase':
        all_words_in_categories_train = all_words_in_categories
        all_of_words_train = all_of_words
        all_of_words = set()
        all_words_in_categories = dict()
    elif mode == 'Test':
        all_words_in_categories_train = all_words_in_categories
        all_of_words_train = all_of_words
        all_of_words = set()
        all_words_in_categories = dict()


def filtering_words_advance(word: str) -> str:
    word = normalizer.normalize(word)
    if perm_clear_garbage_words:
        if word in JUNK_WORDS or word in PUNCTUATION_MARKS or word in PERSIAN_NUMBERS:
            return ''
    if perm_stem:
        word = stemmer.stem(word)
    if perm_lemm:
        word = lemmatizer.lemmatize(word)
    return word


def find_all_categories(categories):
    for category in categories:
        all_category_names.add(category)
        num_of_books_in_each_category[category] = num_of_books_in_each_category.get(category, 0) + 1


def update_all_words_in_categories(word: str, category: str):
    all_words_in_categories[category] = all_words_in_categories.get(category, []) + [word]


def update_all_words(word: str):
    all_of_words.add(word)


def convert_dict_to_df(mode):  # can do batter in time
    full_df = pd.DataFrame
    if mode == 'DataBase':
        from collections import Counter
        nul_df = pd.DataFrame(0, columns=list(all_of_words), index=list(all_category_names))
        for cat, list_cat in all_words_in_categories.items():
            all_words_in_categories[cat] = Counter(list_cat)

        for category in nul_df.index:
            for word in nul_df.columns:
                nul_df.loc[category, word] = all_words_in_categories[category].get(word, 0)
        full_df = nul_df
    elif mode == 'Test':
        full_df = all_tests
    return full_df


def update_row_of_test(word, row_i):
    all_tests[row_i] = all_tests.get(row_i, []) + [word]


def process_all_words(df, mode):
    for row_i in range(df.shape[0]):
        new_list_of_words_for_row = hz.word_tokenize(df.loc[row_i, 'title'])\
                                    + hz.word_tokenize((df.loc[row_i, 'description']))
        category = df.loc[row_i, 'categories']
        for word in new_list_of_words_for_row:
            filtered_word = filtering_words_advance(word)
            if filtered_word:
                update_all_words(filtered_word)
                if mode == 'DataBase':
                    update_all_words_in_categories(filtered_word, category)
                elif mode == 'Test':
                    update_row_of_test(filtered_word, row_i)
    return convert_dict_to_df(mode)


def pre_process(csv_file_name, mode):
    raw_df = pd.read_csv(csv_file_name)
    if mode == 'DataBase':
        find_all_categories(raw_df['categories'])
    my_df = process_all_words(raw_df, mode)
    cleanup(mode)
    return my_df


def temp_save(df_train):
    df_train.to_csv(FILE_ADDRESS_IN_PC)


if __name__ == '__main__':
    init_const()
    df_train = pre_process('books_train.csv', 'DataBase')  # just for train
    temp_save(df_train)
