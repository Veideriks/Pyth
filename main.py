# 34

stih = (input().lower().split())

character = ["а","у","е","ы","о","э","я","и","ю","ё"]
def chek (stih, character)->bool:
    return len(set(map(lambda itm: sum(map(lambda item: itm.count(item), character)), stih)))<2

if chek(stih, character):
    print("Парам пам-пам")
else:
    print("Пам парам")

# 36
num_rows = int(input())
num_columns = int(input())

def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(*list(map(operation, [i], [j])), end="\t")
        print()

print_operation_table(lambda x,y: x*y, num_rows, num_columns)

