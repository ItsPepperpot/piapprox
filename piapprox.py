import random
import time
import sys


def main(number_of_dart_throws):
    start_time = time.time()
    dart_throws = []

    # Throw darts.
    print("Throwing darts...")
    for i in range(0, number_of_dart_throws):
        try:
            dart_throws.append([random.random(), random.random()])
        except MemoryError:
            print(f"Ran out of memory! Continuing with {i} dart throws.")
            number_of_dart_throws = i
            break

    # Calculate pi.
    num_of_darts_in_circle = 0
    print("Calculating pi...")
    for dart in dart_throws:
        # If distance to centre of square is larger than radius (0.5),
        # then the dart is outside the circle.
        if (dart[0] - 0.5)**2 + (dart[1] - 0.5)**2 <= 0.25:
            num_of_darts_in_circle += 1

    pi = (num_of_darts_in_circle / len(dart_throws)) * 4
    end_time = time.time()
    time_elapsed = end_time - start_time
    try:
        darts_per_second = number_of_dart_throws / time_elapsed
    except ZeroDivisionError:
        darts_per_second = number_of_dart_throws

    print(f"Pi is approximately equal to {pi}.")
    print(f"Took {time_elapsed} seconds (≈{darts_per_second} darts / second).")


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except (ValueError, IndexError):
        sys.exit("""Please run the script with the number of dart throws as \
an argument.""")
    if n < 1:
        sys.exit("Must throw at least 1 dart.")
    main(n)
