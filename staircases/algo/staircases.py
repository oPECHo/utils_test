def staircase(n):
    result = ""
    for i in range(1, n + 1):
        result += f'{"#"*i:>{n}}\n'

    return result.rstrip()


#if __name__ == "__main__":
#    print(staircase(3))
