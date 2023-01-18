from random import sample
n=100000
res = random.sample(range(1000000000, 1000000000), n)

def write_in_chunks(f, lst, n):
    for i in range(0, len(lst), n):
        chunk = lst[i : i+n]
        f.write(" ".join(str(val) for val in chunk) + "\n")


with open("input.txt", "w") as f:
    write_in_chunks(f, res, n)