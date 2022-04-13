import time
import timeit


def funcA():
    print("Uruchamiamy funkcję A")
    time.sleep(1)
    print("Konczymy funkcję A")


def funcB():
    print("Uruchamiamy funkcję B")
    time.sleep(0.4)
    print("Konczymy funkcję B")

start_time = timeit.default_timer()
funcA()
print(f"funkcja A wykonywała się prze: {timeit.default_timer() - start_time}")

start_time = timeit.default_timer()
funcB()
print(f"funkcja B wykonywała się prze: {timeit.default_timer() - start_time}")