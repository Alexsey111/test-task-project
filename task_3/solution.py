# Когда пользователь заходит на страницу урока, мы сохраняем время его захода.
# Когда пользователь выходит с урока (или закрывает вкладку, браузер – в общем как-то
# разрывает соединение с сервером), мы фиксируем время выхода с урока. Время присутствия каждого
# пользователя на уроке хранится у нас в виде интервалов. В функцию передается словарь, содержащий
# три списка с таймстемпами (время в секундах):
# lesson – начало и конец урока
# pupil – интервалы присутствия ученика
# tutor – интервалы присутствия учителя
# Интервалы устроены следующим образом – это всегда список из четного количества элементов.
# Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
# Нужно написать функцию appearance, которая получает на вход словарь с интервалами и возвращает
# время общего присутствия ученика и учителя на уроке (в секундах).
#
# def appearance(intervals: dict[str, list[int]]) -> int:
#     pass
#
# tests = [
#     {'intervals': {'lesson': [1594663200, 1594666800],
#              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
#              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
#      'answer': 3117
#     },
#     {'intervals': {'lesson': [1594702800, 1594706400],
#              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
#              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
#     'answer': 3577
#     },
#     {'intervals': {'lesson': [1594692000, 1594695600],
#              'pupil': [1594692033, 1594696347],
#              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
#     'answer': 3565
#     },
# ]
#
# if __name__ == '__main__':
#    for i, test in enumerate(tests):
#        test_answer = appearance(test['intervals'])
#        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'


def merge_intervals(times: list[int]) -> list[tuple[int, int]]:
    """Преобразует список в список пар (интервалов), и объединяет пересекающиеся интервалы."""
    intervals = [(times[i], times[i+1]) for i in range(0, len(times), 2)]
    intervals.sort()

    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged


def intersect_intervals(a: list[tuple[int, int]], b: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Находит пересечения между двумя списками интервалов."""
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        start = max(a[i][0], b[j][0])
        end = min(a[i][1], b[j][1])
        if start < end:
            result.append((start, end))
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    lesson_interval = [(lesson_start, lesson_end)]

    pupil_intervals = merge_intervals(intervals['pupil'])
    tutor_intervals = merge_intervals(intervals['tutor'])

    pupil_during_lesson = intersect_intervals(pupil_intervals, lesson_interval)
    tutor_during_lesson = intersect_intervals(tutor_intervals, lesson_interval)

    overlap = intersect_intervals(pupil_during_lesson, tutor_during_lesson)

    return sum(end - start for start, end in overlap)


