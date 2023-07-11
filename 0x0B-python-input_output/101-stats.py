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
        print("{}: {}".format(key, stats_dict[value]))


def get_info(string):
    '''Gets the file size and the status code of the current input

    Args:
        string (str): The string to get the info from
    '''
    str_list = string.split()
    return str_list[-1], str_list[-2]


if __name__ == '__main__':
    count = 0
    full_size = 0
    stat_list = ['200', '301', '400', '401', '403', '404', '405', '500']
    stat_dict = {}
    while True:
        if count != 10:
            try:
                data = input()
                size, status = get_info(data)
                if status in stat_list:
                    full_size += int(size)
                    if status in stat_dict.keys():
                        stat_dict[status] += 1
                    else:
                        stat_dict[status] = 1
                    count += 1
            except KeyboardInterrupt:
                stats(full_size, stat_dict)
                raise
        else:
            stats(full_size, stat_dict)
            count = 0
