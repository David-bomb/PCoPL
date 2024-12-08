

class Group:

    def __init__(self, id : int, code : str, students : int, cathedra_id : int):
        self.id = id
        self.code = code
        self.students = students
        self.cathedra_id = cathedra_id


class Cathedra:

    def __init__(self, id : int, name : str):
        self.id = id
        self.name = name


class GroupCathedra:
    # Многое ко многим

    def __init__(self, cathedra_id : int, group_id : int):
        self.cathedra_id = cathedra_id
        self.group_id = group_id


'''Список кафедр'''
cathedras = [
    Cathedra(1, 'Системы обработки информации и управления'),
    Cathedra(2, 'Техническая физика'),
    Cathedra(3, 'Компьютерные системы и сети')
]

# Преподаватели
groups = [
    Group(1, 'ИУ5-34Б', 27, 1),
    Group(2, 'ИУ5-33Б', 28, 1),
    Group(3, 'ИУ5-31Б', 25, 1),
    Group(4, 'ФН4-32Б', 18, 2),
    Group(5, 'ИУ6-31Б', 16, 3),
]

group_cathedras = [
    GroupCathedra(1, 1),
    GroupCathedra(1, 2),
    GroupCathedra(1, 3),
    GroupCathedra(2, 4),
    GroupCathedra(3, 5)
]

# Создание кортежей 1:М
one_to_many = [(group.code, group.students, cathedra.name)
               for cathedra in cathedras
               for group in groups
               if group.cathedra_id == cathedra.id]

# Создание кортежей М:М
many_to_many_temp = [(cathedra.name, elem.cathedra_id, elem.group_id)
                     for cathedra in cathedras
                     for elem in group_cathedras
                     if cathedra.id == elem.cathedra_id]

many_to_many = [(group.code, group.students, cathedra_name)
                for cathedra_name, cathedra_id, group_id in many_to_many_temp
                for group in groups if group.id == group_id]


def task_1(mass):
    res1_temp = list(filter(lambda x: x[0].startswith('И'),
                            mass))  # "А" заменено на "И", т.к. в списке нет групп, начинающихся на "А"
    res1 = [(code, cathedra) for code, _, cathedra in res1_temp]
    return res1




def task_2(mass):
    res2_unsorted = []
    for cathedra in cathedras:
        res_2_temp = list(filter(lambda x: x[2] == cathedra.name, mass))
        if len(res_2_temp) > 0:
            cathedra_studs = [studs for _, studs, _ in res_2_temp]
            cath_studs_min = min(cathedra_studs)
            res2_unsorted.append((cathedra.name, cath_studs_min))
    res2 = sorted(res2_unsorted, key=lambda x: x[1])
    return [': '.join(list(map(str, ans))) for ans in res2]



def task_3(mass):
    res_3_temp = sorted(mass, key=lambda x: x[0])
    res_3 = [(code, cath) for code, _, cath in res_3_temp]
    return [': '.join(ans) for ans in res_3]




def main():
    pass
    # print(one_to_many)
    # print('№1') # Группы начинающиеся в "И"
    # print(task_1(one_to_many))
    #
    # print('\n№2')  # минимальное кол-во студентов
    # print(task_2(one_to_many), sep='\n')
    #
    # print('\n№3')  # сортируем по названию группы
    # print(task_3(many_to_many), sep='\n')
    mass = [("ИУ5", 125, "Мы"), ("ФН12", 60, "Слишком умные"), ("ИБМ3", 46, "Слишком богатые"),
            ("РК1", 74, "Слишком умные")]
    print(task_3(mass))


if __name__ == '__main__':
    main()