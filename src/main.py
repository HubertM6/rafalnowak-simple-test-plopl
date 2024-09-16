def task_one():
    input_file = "./numbers.txt"
    numbers = []
    with open(input_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            numbers.append(int(line))

    amount = len(numbers)
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += number
    min = sorted(numbers)[0]
    max = sorted(numbers)[amount - 1]
    avg = sum_of_numbers / amount

    info = f"amount = {amount}, sum = {sum_of_numbers}, min = {min}, max = {max}, avg = {avg}"
    print(info)
    return(min, max, avg)

if __name__ == '__main__':
    task_one()