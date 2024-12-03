def process_input(filename):
    reports = []
    with open(filename, 'r') as puzzle_input:
        for line in puzzle_input:
            reports.append([int(x) for x in line.split()])
    return reports


def is_safe(report):
    increasing = report[1] > report[0]
    for x in range(1, len(report)):
        diff = report[x] - report[x-1]
        if not 1 <= abs(diff) <= 3:
            return False
        if (increasing and diff < 0) or (not increasing and diff > 0):
            return False
    return True


def get_safe_reports(reports):
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
    return count


def get_safe_reports_with_dampener(reports):
    count = 0
    for report in reports:
        if is_safe(report):
            count += 1
            continue
        for x in range(len(report)):
            amended_report = report.copy()
            del amended_report[x]
            if is_safe(amended_report):
                count += 1
                break
    return count


reports = process_input('input.txt')
print(f'Part 1: {get_safe_reports(reports)}')
print(f'Part 2: {get_safe_reports_with_dampener(reports)}')
