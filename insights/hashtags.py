import pandas
import constant
import matplotlib.pyplot as plt


def readcsv():
    return pandas.read_csv(constant.INSIGHTS_CSV)


def remove_element_list(input_list, to_be_removed):
    return [elem for elem in input_list if elem != to_be_removed]


def get_best_tags():
    df = readcsv()
    _get_best_tag_based_on(constant.IMPRESSIONS_COL, df, show_graphs=False)
    _get_best_tag_based_on(constant.ENGAGEMENT_COL, df, show_graphs=False)
    _get_best_tag_based_on(constant.REACH_COL, df)


def _get_best_tag_based_on(column_name, initial_df, show_graphs=False):
    tag_avg_impressions = dict()
    df = initial_df.copy(deep=True)
    columns_without_impressions = remove_element_list(constant.DEFAULT_COLUMNS, column_name)
    df = df.drop(columns_without_impressions, axis=1)
    tags_columns = remove_element_list(df.columns.values, column_name)
    for tag in tags_columns:
        tag_avg_impressions.update({tag: (df[tag]*df[column_name]).sum()/(df[tag].sum())})
    sorted_avg = dict(sorted(tag_avg_impressions.items(), key=lambda item: item[1]))
    print('Best  tag based on', column_name, ':', list(sorted_avg.keys())[-1])
    print('Worst tag based on', column_name, ':', list(sorted_avg.keys())[0])
    if show_graphs:
        plt.bar(*zip(*sorted_avg.items()))
        plt.show()
    return list(sorted_avg.keys())[-1],list(sorted_avg.keys())[0]
