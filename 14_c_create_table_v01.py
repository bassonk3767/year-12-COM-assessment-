# Import pandas for creating
# the table for the statistics output
import pandas as pd


# Creates a table for
# the file output
def create_table(un_sorted):  # "un_sorted" variable is an array that
                              # has items in it that are the following:
                              # ["name",[mean,med,min_val,max_val,rng,low_q,up_q,in_rng,sd]]

     statistics_summary_dict = {
        "Mean (Average)": un_sorted[1][0],
        "Median": un_sorted[1][1],
        "": un_sorted[1][2],
    }
