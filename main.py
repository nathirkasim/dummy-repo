import math

def calculate_stats(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    variance = sum((x - mean) ** 2 for x in numbers) / count
    std_dev = math.sqrt(variance)
    return {
        "count": count,
        "sum": total,
        "mean": round(mean, 2),
        "std_dev": round(std_dev, 2),
    }

if __name__ == "__main__":
    results = calculate_stats([12, 45, 67, 89, 23, 56])
    print(f"Results: {results}")
