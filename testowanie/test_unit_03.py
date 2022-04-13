import time

def funcA():
    print("Uruchamiamy funkcję A")
    time.sleep(0.05)
    print("Konczymy funkcję A")

def funcB():
    print("Uruchamiamy funkcję B")
    time.sleep(0.01)
    print("Konczymy funkcję B")

def test_func_a(benchmark):
    benchmark(funcA)

def test_func_b(benchmark):
    benchmark.pedantic(funcB, iterations=100, rounds=10)