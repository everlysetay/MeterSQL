# MeterSQL

# To execute the existing script
python generate_sql.py

# To Test current script
python -m unittest generate_sql_test.py

# Assumptions
NEM12 file will be a .csv file type.
Data provided is raw data.
Based on meter_readings TABLE provided. INSERT statements should only be interested in 3 of the following fields:
1. nmi
2. timestamp
3. consumption

# Possible Improvements to existing script

## Improvement 1
Based on my understanding of the assignement. I believe we are only interested in data that have 2 consecutive rows, with columns starting with 200 and 300.
There can be a function that goes through the raw file to remove all other rows that do not start with 200 or 300. 
That will ensure that we are working with a smaller raw file, ensuring faster processing time.

To further optimise it, we can remove rows that are not consective 200 and 300.
This should reduce the raw file size even greater. Helping with processing time.

## Improvement 2
There can be a counter before and after the SQL insert statements to notify the people who are looking at the script of the total number of lines that it will be generating.

e.g.

```
--- BEFORE(0)
SELECT COUNT(*)
FROM meter_readings;

...

--- AFTER (2)
SELECT COUNT(*)
FROM meter_readings;
```

We can definitely add more detailed conditions for the checks, e.g. by timestamp etc.