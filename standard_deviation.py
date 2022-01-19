import pandas as pd
import statistics as s
import csv

df = pd.read_csv("SOCR-HeightWeight.csv") 
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()
height_mean = s.mean(height_list)
height_mode = s.mode(height_list)
height_median = s.median(height_list)
weight_mean = s.mean(weight_list)
weight_mode = s.mode(weight_list)
weight_median = s.median(weight_list)
print("mean,median,mode of height is {}, {} and {} repectively".format(height_mean,height_median,height_mode))
print("mean,median,mode of weight is {}, {} and {} repectively".format(weight_mean,weight_median,weight_mode))

height_std_dev = s.stdev(height_list)
weight_std_dev = s.stdev(weight_list)

height_first_std_dev_start,height_first_std_dev_end = height_mean - height_std_dev, height_mean + height_std_dev
height_second_std_dev_start,height_second_std_dev_end = height_mean - (2 * height_std_dev), height_mean +( 2 * height_std_dev)
height_third_std_dev_start,height_third_std_dev_end = height_mean - (3 * height_std_dev), height_mean + (3 * height_std_dev)
weight_first_std_dev_start,weight_first_std_dev_end = weight_mean - weight_std_dev, weight_mean + weight_std_dev
weight_second_std_dev_start,weight_second_std_dev_end = weight_mean - (2 * weight_std_dev), weight_mean + ( 2 * weight_std_dev)
weight_third_std_dev_start,weight_third_std_dev_end = weight_mean - (3 * weight_std_dev), weight_mean + (3 * weight_std_dev)

height_list_of_data_within_first_std_dev = [result for result in height_list if result>height_first_std_dev_start and result<height_first_std_dev_end]
height_list_of_data_within_second_std_dev = [result for result in height_list if result>height_second_std_dev_start and result<height_second_std_dev_end]
height_list_of_data_within_third_std_dev = [result for result in height_list if result>height_third_std_dev_start and result<height_third_std_dev_end]
weight_list_of_data_within_first_std_dev = [result for result in weight_list if result>weight_first_std_dev_start and result<weight_first_std_dev_end]
weight_list_of_data_within_second_std_dev = [result for result in weight_list if result>weight_second_std_dev_start and result<weight_second_std_dev_end]
weight_list_of_data_within_third_std_dev = [result for result in weight_list if result>weight_third_std_dev_start and result<weight_third_std_dev_end]

print("{}% of data for height lies within first standard deviation".format(len(height_list_of_data_within_first_std_dev) * 100.0/len(height_list)))
print("{}% of data for height lies within second standard deviation".format(len(height_list_of_data_within_second_std_dev) * 100.0/len(height_list)))
print("{}% of data for height lies within third standard deviation".format(len(height_list_of_data_within_third_std_dev) * 100.0/len(height_list)))
print("{}% of data for weight lies within first standard deviation".format(len(weight_list_of_data_within_first_std_dev) * 100.0/len(height_list)))
print("{}% of data for weight lies within second standard deviation".format(len(weight_list_of_data_within_second_std_dev) * 100.0/len(height_list)))
print("{}% of data for weight lies within third standard deviation".format(len(weight_list_of_data_within_third_std_dev) * 100.0/len(height_list)))




