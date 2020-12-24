import constant
import pandas


def readcsv():
    return pandas.read_csv(constant.INSIGHTS_CSV)


def remove_element_list(input_list, to_be_removed):
    return [elem for elem in input_list if elem != to_be_removed]