"""
6) Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
dictionary = {}
with open("text.txt", 'r', encoding='utf-8') as f_obj:
    for line in f_obj.readlines():
        lst = []
        for item in line.split():
            HOURS = "".join(c for c in item if c.isdecimal())
            lst.append(HOURS)
        lst[:] = [x for x in lst if x]
        dictionary.update({line.split()[0]: sum(int(number) for number in lst)})
print(dictionary)
