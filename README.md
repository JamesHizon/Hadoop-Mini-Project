# Hadoop Mini-Project

### Description:
In this mini-project, I had to write a Hadoop MapReduce program to process an automobile report data set.
Given that there were missing values (make and year) for a given record when the "incident_type" is an accident, I needed to find a way to populate values from records with "incident_type" == "I". I basically had to create a Python dictionary which kept track of make and year for a given vin_number, and use this information to in combination with incident_type as "A" to obtain a final count of occurences based on make and year.

### Files
1. ```Final_mapper.py``` - Maps the vin_number, make, year and incident type from every record of ```report_data.csv```.
2. ```final_reducer.py``` - Creates master Python dictionary used to keep track of records with incident_type "I" to populate make and year. We filter through incident_type "A" in order to update and automatically increment the "accident_count" by 1 based on occurrence.
3. ```final_mapper2.py``` - Map out the make and year as key, and accident_count as a value.
4. ```final_reducer2.py``` - Aggregate (reduce) and collect final count for every make and year combination.
5. ```Hadoop_MP_CLI.txt``` - All of the messages from using terminal to execute bash script and read the output text file.

### How to test Python script using Python 3

```
cat report_data.csv | python3 Final_mapper.py | sort | final_reducer.py | final_mapper2.py | sort | final_reducer2.py
```

### How to run bash script

```
chmod u+x auto_report.sh
bash auto_report.sh
```
