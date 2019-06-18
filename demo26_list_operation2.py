number_list = [3, 1, 4, 1, 5, 9, 26, 83, 47, 100, 3, 9, 7]
r1 = sorted(x for x in number_list if x < 30)
print r1
r2 = sorted((y for y in number_list if y > 10), reverse=True)
print r2