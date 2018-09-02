def print_all_binary_numbers(N, output):
    if N == 0:
        print(output)
    else:
        print_all_binary_numbers(N-1, output+"0")
        print_all_binary_numbers(N-1, output+"1")

if __name__ == "__main__":

    print_all_binary_numbers(4, "")
