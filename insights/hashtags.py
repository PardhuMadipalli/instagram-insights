import constant
from commons import readcsv
from commons import remove_element_list

import matplotlib.pyplot as plt


def get_best_tags(show_graphs=False):
    df = readcsv()
    for metric in constant.METRICS_COLUMNS:
        _get_best_tag_based_on(metric, df, show_graphs=show_graphs)


def _get_best_tag_based_on(column_name, initial_df, show_graphs=False):
    tag_avg_impressions = dict()
    df = initial_df.copy(deep=True)
    columns_without_impressions = remove_element_list(constant.DEFAULT_COLUMNS, column_name)
    df = df.drop(columns_without_impressions, axis=1)
    tags_columns = remove_element_list(df.columns.values, column_name)
    for tag in tags_columns:
        tag_avg_impressions.update({tag: (df[tag]*df[column_name]).sum()/(df[tag].sum())})
    sorted_avg = dict(sorted(tag_avg_impressions.items(), key=lambda item: item[1]))

    print(f'Best  tags based on {column_name}           : {list(sorted_avg.keys())[-4:][::-1]}')
    print(f'Their corresponding {column_name} values are: {list(sorted_avg.values())[-4:][::-1]}')
    print()

    print(f'Worst tags based on {column_name}           : {list(sorted_avg.keys())[:4]}')
    print(f'Their corresponding {column_name} values are: {list(sorted_avg.values())[:4]}')
    print()

    if show_graphs:
        plt.bar(*zip(*sorted_avg.items()))
        plt.show()
    return list(sorted_avg.keys())[-1], list(sorted_avg.keys())[0]
