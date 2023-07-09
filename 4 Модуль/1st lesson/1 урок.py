# def strcounter(s):
#     for sym in set(s):
#         counter = 0
#         for sub_sym in s:
#             if sym == sub_sym:
#                 counter += 1
#         print(sym, counter)
#
#
# s = 'aaabc'
# strcounter(s)

def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    print(syms_counter)