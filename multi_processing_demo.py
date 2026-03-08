"""Multiprocessing demo."""
import asyncio
import os
import time
from concurrent.futures import ProcessPoolExecutor  # pylint: disable=E0611

def slow_square(n):
    """Calculate square with slow computation."""
    total = 0
    for i in range(10_000_000):
        total += i * n
    return total

#
async def main():
    """Run sequential and parallel processing demo."""
    numbers = list(range(14))

    # Sequential Run
    start = time.perf_counter()
    single = [slow_square(n) for n in numbers]
    print(f"Seq: {time.perf_counter() - start:.4f} seconds, Slow_Square: {single}")

    print(f"Cores: {os.cpu_count()}")

    # Parallel run using asyncio + ProcessPoolExecutor
    loop = asyncio.get_event_loop()
    with ProcessPoolExecutor() as executor:
        start = time.perf_counter()
        tasks = [loop.run_in_executor(executor, slow_square, n) for n in numbers]
        multi = await asyncio.gather(*tasks)
    print(f"Per: {time.perf_counter() - start:.4f} seconds, Multi_Square: {multi}")

if __name__ == "__main__":
    asyncio.run(main())

#     numbers = list(range(36))

#     start = time.perf_counter()
#     single = [slow_square(n) for n in numbers]
#     print(f"Seq: {time.perf_counter() - start:.4f} seconds")

#     print(f"Cores: {cpu_count()}")

#     start = time.perf_counter()
#     with Pool() as pool:
#         multi = pool.map(slow_square, numbers)
#     print(f"Per: {time.perf_counter() - start:.4f} seconds")
