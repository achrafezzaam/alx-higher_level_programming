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
    for key, value in sorted(stats_dict.items()):
        print("{}: {}".format(key, value))


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
    stat_dict = {'200': 0,
                 '301': 0,
                 '400': 0,
                 '401': 0,
                 '403': 0,
                 '404': 0,
                 '405': 0,
                 '500': 0}
    while True:
        if count != 10:
            try:
                data = input()
                size, status = get_info(data)
                if status in stat_dict:
                    full_size += int(size)
                    stat_dict[status] += 1
                    count += 1
            except KeyboardInterrupt:
                stats(full_size, stat_dict)
                raise
        else:
            stats(full_size, stat_dict)
            count = 0
