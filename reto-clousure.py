def make_division(n: int) -> int:
    def numero(x: int) -> int:
        return x / n
    return numero

def run():
    division_by5 = make_division(5)
    print(division_by5(100))

if __name__ == "__main__":
    run()