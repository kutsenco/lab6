"""
This file will sort the lists by different keys (song_length, title_length, last_word)
"""
from typing import List, Tuple, Callable, Union

def song_length(result_last_word: Tuple[str]) -> float :
    """
    sorting by song length ('1.12', '2.76', '3.78', '3.87')
    """
    return result_last_word[1]

def title_length(result_last_word: Tuple[str]) -> int :
    """
    sorting by song title length ('Мало мені', 'Відпусти', 'Поясни', 'Фіалки')
    """
    return len(result_last_word[0])

def last_word(result_last_word: Tuple[str]) -> str :
    """
    sorting song titles by the first letter of the last word
    >>> last_word(('Африка'))
    'а'
    >>> last_word(('Кавачай'))
    'к'
    >>> last_word(('Коли тебе нема'))
    'н'
    >>> last_word(('Той день'))
    'д'
    """
    result_last_word = str(result_last_word)
    return result_last_word.split()[-1][0].lower()
print(last_word(('Коли тебе нема')))

def sort_songs(
    song_titles: List[str],
    length_songs: List[str],
    anyone: Callable[[tuple], Union[int, str, float]]) -> List[tuple]:
    """
    Sorts songs by the specified parameter
    >>> sort_songs(['Янанебібув', 'Той день'], ['3.19', '3.58'] , song_length)
    [('Янанебібув', '3.19'), ('Той день', '3.58')]
    >>> sort_songs(['Сосни', 'Мало мені'], ['4.31', '5.06'], song_length)
    [('Сосни', '4.31'), ('Мало мені', '5.06')]
    >>> sort_songs(['Відпусти', 'Кавачай'], ['3.52', '4.39'], song_length)
    [('Відпусти', '3.52'), ('Кавачай', '4.39')]
    >>> sort_songs(['Фіалки', 'Етюд'], ['3.43', '2.21'], song_length)
    [('Етюд', '2.21'), ('Фіалки', '3.43')]
    """
    if len(song_titles) != len(length_songs) :
        return None
    for i in range(len(song_titles)) :
        if not isinstance(song_titles[i], str) :
            return None
    for j in range(len(length_songs)) :
        try :
            float(length_songs[j])
        except TypeError :
            return None
    sorts_on = list(zip(song_titles, length_songs))

    return sorted(sorts_on, key=anyone)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
