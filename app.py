# Prototype

# rfc2822: Mon, 3 Jul 2006 17:18:43 +0200
# iso8601: 2006-07-03 17:18:43 +0200

from subprocess import run, PIPE
from os import system

dates = [
    #     'aug 25',
    #     '19',
    #     '7',
    #     '15',
    #     '13',
    #     '23',
    #     '31',
    #     'jul 28',
    #     '29',
    #     '30',
    #     '31',
    #     'aug 1',
    #     '2',
    #     '3',
    #     'jul 14',
    #     '7',
    #     'jun 30',
    #     '23',
    #     '16 17 18 19 20 21 22 29'
    #     'jul 20 13 6 19 18 17 10 3'

    '2017-08-25 18:00:00 +0530',
    '2017-08-19 18:00:00 +0530',
    '2017-08-07 18:00:00 +0530',
    '2017-08-15 18:00:00 +0530',
    '2017-08-13 18:00:00 +0530',
    '2017-08-23 18:00:00 +0530',
    '2017-08-31 18:00:00 +0530',
    '2017-07-28 18:00:00 +0530',
    '2017-07-29 18:00:00 +0530',
    '2017-07-30 18:00:00 +0530',
    '2017-07-31 18:00:00 +0530',
    '2017-08-01 18:00:00 +0530',
    '2017-08-02 18:00:00 +0530',
    '2017-08-03 18:00:00 +0530',
    '2017-07-14 18:00:00 +0530',
    '2017-07-07 18:00:00 +0530',
    '2017-06-30 18:00:00 +0530',
    '2017-06-23 18:00:00 +0530',
    '2017-06-16 18:00:00 +0530',
    '2017-06-17 18:00:00 +0530',
    '2017-06-18 18:00:00 +0530',
    '2017-06-19 18:00:00 +0530',
    '2017-06-20 18:00:00 +0530',
    '2017-06-21 18:00:00 +0530',
    '2017-06-22 18:00:00 +0530',
    '2017-06-29 18:00:00 +0530',
    '2017-07-20 18:00:00 +0530',
    '2017-07-13 18:00:00 +0530',
    '2017-07-06 18:00:00 +0530',
    '2017-07-19 18:00:00 +0530',
    '2017-07-18 18:00:00 +0530',
    '2017-07-17 18:00:00 +0530',
    '2017-07-10 18:00:00 +0530',
    '2017-07-03 18:00:00 +0530',
]


def get_commit_hash(op1):
    return op1.split(' ')[1]


def draw(dates):
    for date in dates:
        print(date)
        data="2017-08-25 18:00:00 +0530"
        command = 'echo "commit' + data + '">> test.txt'
        system(command)  # number of times
        command = 'git add -A'
        system(command)
        command = 'git commit -m "commit"'
        system(command)
        #     command = r'git log -1'
        #     op = check_output(command)
        #     commit_hash = get_commit_hash(op)
        command = 'git commit --amend --no-edit --date ' + '\"' + date + '\"'
        # format: "Mon 10 Jan 2019 20:19:19 IST"
        system(command)


git commit --amend --no-edit --date  $date