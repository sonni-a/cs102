import time
import tracemalloc
tracemalloc.start()
ts = time.perf_counter()


with open('input.txt') as input:
    n = int(input.readline())
    array = [int(x) for x in input.readline().split()]  # считываем n целых числа из файла input в массиве
end = open('output.txt', 'w+')


def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        q = array[randint(0, len(array) - 1)]
    l_arr = [n for n in array if n < q]
    e_arr = [q] * array.count(q)
    b_arr = [n for n in array if n > q]
    return quicksort(l_arr) + e_arr + quicksort(b_arr)


end.write(' '.join(map(str, quicksort(array))))

print('time:', (time.perf_counter() - ts))
print('memory:', tracemalloc.get_traced_memory())