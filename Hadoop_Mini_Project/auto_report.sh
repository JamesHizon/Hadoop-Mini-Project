#!/bin/bash

hadoop jar /usr/local/opt/hadoop/libexec/share/hadoop/common/hadoop-streaming-3.3.0.jar \
-file /Users/jameshizon/PycharmProjects/MiniProjects/Hadoop_Mini_Project/Final_mapper.py -mapper "python3 Final_mapper.py" \
-file /Users/jameshizon/PycharmProjects/MiniProjects/Hadoop_Mini_Project/final_reducer.py -reducer "python3 final_reducer.py" \
-input /Users/jameshizon/PycharmProjects/MiniProjects/Hadoop_Mini_Project/input/data.csv -output /Users/jameshizon/PycharmProjects/MiniProjects/Hadoop_Mini_Project/output/all_accidents

hadoop jar /usr/local/opt/hadoop/libexec/share/hadoop/common/hadoop-streaming-3.3.0.jar \
-file /Users/jameshizon/PycharmProjects/MiniProjects/Hadoop_Mini_Project/final_mapper2.py -mapper "python3 final_mapper2.py" \
-file /Users/jameshizon/PycharmProjects/MiniProjects/Hadoop_Mini_Project/final_reducer2.py -reducer "python3 final_reducer2.py" \
-input /Users/jameshizon/PycharmProjects/MiniProjects/Hadoop_Mini_Project/output/all_accidents -output /Users/jameshizon/PycharmProjects/MiniProjects/Hadoop_Mini_Project/output/make_year_count