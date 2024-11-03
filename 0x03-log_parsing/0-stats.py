#!/usr/bin/python3
"""
log parsing
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
Warning: In this sample, you will have random value - it’s normal to not have the same output as this one.
"""

import sys
import re


def initialize_log():
    status_code = [200, 301, 400, 401, 403, 404, 405, 500]
    log = {"file_size": 0, "code_list": {str(code): 0 for code in status_code}}
    return log


def parse_line():
    match = regex.fullmatch(line)
    if match:
        status_code, file_size * match.group(1,2)
        log["file_size"] += int(file_size)
        if stat_code.isdecimal():
            log["code_list"][stat_code] += 1
    return log



def print_codes():
    print("file size: {}".format(log["file_size"]))
    sorted_code_list = sorted(log["code_list"])
    for code in sorted_code_list:
        if log["code_list"][code]:
            print(f"{code}: {log["code_list"][code]}")




def main():
    regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8

    log = initialize_log()

    line_count = 0

    for line in sys.stdin:
        line = line.strip()
        line_count = line_count + 1
        parsed_log = parse_line(line, regex, log)
        if line_count % 10 == 0:
            print_codes(parsed_log)



if __name__ == "__main__":
    main()
