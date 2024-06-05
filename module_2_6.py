values_list = [1985, "Vadim", True]
values_dict = {"a": 25, "b": True, "c": "Fly"}
values_list_2 = ["Vadim", 2502]


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params()
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)


def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
        list_my.append(item)
        print(list_my)


append_to_list(45554)

