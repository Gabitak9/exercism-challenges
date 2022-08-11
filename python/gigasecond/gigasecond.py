from datetime import timedelta

GIGASECONDS = timedelta(seconds=10**9)


def add(moment):
    return moment + GIGASECONDS
