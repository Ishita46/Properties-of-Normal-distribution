import random
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

count = []
dice_result = []
for i in range(0,1000):
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  dice_result.append(dice1+dice2)

#Calculating the mean, median, mode and the standard deviation
mean = sum(dice_result)/len(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
std_deviation = statistics.stdev(dice_result)

#finding 1,2 and 3 standard deviation, start and end values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

#plotting the chart and lines for mean, 1 and 2 standard deviations
fig = ff.create_distplot([dice_result], ["RESULT"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0,0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0,0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0,0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0,0.17], mode = "lines", name = "STANDARD DEVIATION 2"))
fig.show()

#Printing the findings
list_of_data_withing_1_std_deviation = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_withing_2_std_deviation = [result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_withing_3_std_deviation = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard Deviation of this data is {}".format(std_deviation))
#{} means format string or something
print("{}% of data lies withing 1 standard deviation".format(len(list_of_data_withing_1_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies withing 2 standard deviation".format(len(list_of_data_withing_2_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies withing 3 standard deviation".format(len(list_of_data_withing_3_std_deviation)*100.0/len(dice_result)))
