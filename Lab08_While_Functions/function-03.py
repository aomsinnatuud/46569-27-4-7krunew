def show_table(n: int, limit: int):
    i = 1
    while i <= limit:
        print(f"{n} x {i} = {n * i}")
        i += 1

def main():
    n = int(input().strip())
    limit = int(input().strip())
    show_table(n, limit)

if __name__ == "__main__":
    main()
