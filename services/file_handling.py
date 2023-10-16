import os
import sys

BOOK_PATH = 'book/Bredberi_Marsianskie-hroniki.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(
        text: str,
        start: int,
        size: int
) -> tuple[str, int]:

    if len(text) <= size:
        return text, len(text)

    punctuation_marks = (
        ',', '.', '!', ':', ';', '?'
    )
    page_text = text[start: start + size]

    i = -1
    while i > -len(page_text):
        if page_text[i] in punctuation_marks:

            if (i == -1 and
                    page_text[-2] in punctuation_marks and
                    page_text[-3] in punctuation_marks):
                return page_text, len(page_text)

            elif i == -1 and page_text[-2] in punctuation_marks:
                i -= 1

            elif i == -1 and page_text[-2] not in punctuation_marks:
                return page_text, len(page_text)

            else:
                page_text = page_text[:i + 1]
                return page_text, len(page_text)

            i -= 1

        else:
            i -= 1


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:

    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()

    start = 0
    end = start + PAGE_SIZE
    i = 1

    while end < len(text) - 1:
        end = start + PAGE_SIZE
        page_text, page_real_size = _get_part_text(
            text, start, PAGE_SIZE
        )
        start += page_real_size + 1
        book[i] = page_text
        i += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))