def seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    remainder = total_seconds % 3600
    minutes = remainder // 60
    seconds = remainder % 60
    return f"{hours}:{minutes:02d}:{seconds:02d}"

def admission_price(age):
    if age < 5:
        return 0.0
    elif age <= 12:
        return 8.0
    elif age <= 64:
        return 15.0
    else:
        return 10.0

def sum_multiples(limit):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

def total_of_positives(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

def main():
    pass

if __name__ == "__main__":
    main()
