import os

current_path = os.path.abspath(__file__)
parent_path = os.path.join(current_path, '..')
parent_parent_path = os.path.join(parent_path, '..')

def get_all_files(path):
    for name in os.listdir(path):
        new_path = os.path.join(path, name)
        if os.path.isdir(new_path):
            print("Папка", name)
            get_all_files(new_path)
        else:
            print("-", name)


get_all_files(parent_parent_path)





# def recurs(count):
#     print(count)
#     if count == 5:
#         return
#     recurs(count + 1)
#
#
# recurs(0)