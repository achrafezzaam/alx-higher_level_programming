#!/usr/bin/python3
'''Define the stats and get_info method'''


def stats(file_size, stats_dict):
    '''Print the File size and the status codes

    Args:
        file_size (int): The summ of all the previous files sizes
        stats_dict (dict): Contain all the status codes
        and their occurencies
    '''
    print("File size: {}".format(file_size))
    for key in sorted(stats_dict):
        print("{}: {}".format(key, stats_dict[key]))


if __name__ == "__main__":
    import sys

    size = 0
    codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_dict = {}
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                stats(size, status_dict)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in codes:
                    if status_dict.get(line[-2], -1) == -1:
                        status_dict[line[-2]] = 1
                    else:
                        status_dict[line[-2]] += 1
            except IndexError:
                pass

        stats(size, status_dict)

    except KeyboardInterrupt:
        stats(size, status_dict)
        raise
