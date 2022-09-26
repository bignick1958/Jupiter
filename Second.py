def fibonacci(sequence_length):
    sequence = [0, 1]
    if sequence_length < 1:
        print("Последовательность Фибоначчи не может иметь длину, менбшую 1! ")
        return
    if 0 < sequence_length < 3:
        return sequence[0:sequence_length]
    for i in range(2, sequence_length):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


fibonacci(12)

