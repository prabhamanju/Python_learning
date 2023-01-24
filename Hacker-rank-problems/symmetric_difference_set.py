# Sets are an unordered immutable collection of unique values.
#The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but
#not both.
#Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
# m = int(input())
# set_m = set(map(int, input().split()))
# n = int(input())
# set_n = set(map(int, input().split()))
# union_setm_setn = set_m.union(set_n)
# intersect_setm_setn = set_m.intersection(set_n)
# #diff_setm_setn = set_m.difference(set_n)
# diff = union_setm_setn.difference(intersect_setm_setn)
# # print(union_setm_setn)
# # print(intersect_setm_setn)
# x = sorted(diff)
# print(type(x))
# # print(x)
# for i in x:
#     print(i)


n_e = int(input())
r_e = input().split()

n_f = int(input())
r_f = input().split()

print(len((set(r_e)&set(r_f))^(set(r_e)|set(r_f))))