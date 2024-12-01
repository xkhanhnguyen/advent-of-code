def get_data(filename: str) -> list[str]: 
    with open(filename) as f:
        data = [x for x in f.read()]
        return data

def answer(data: list[str]) -> int:
    marker = 4
    # marker = 14
    for i in range(marker, len(data)):
        l = data[i-marker:i]
        if len(set(l)) == marker:
            return i

if __name__ == "__main__":
    data = get_data('input.txt')
    print(answer(data))