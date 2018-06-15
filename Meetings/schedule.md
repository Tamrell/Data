
# Schedule
Here will be kept a weekly schedule for the project in order to keep track of:
- goals
- task management

## Current challenges and remarks

-----

- Wind speed (m/s) is measured every 3 hours, while the chemicals are measured every hour. We will have to use interpolar regression in order to fill in the Wind speeds at every hour.
- The elevation (m) only has 1 value, apparantly this is the same at all points so it is irrelevent for comparison.
- Column 'Date Time' is actually 'Date Time ' (with a space at the end)
- Each year in the date appears to be the same, can we scrap the year from the format?
- Might be a fun idea to plot the wind currents on top of the map! (if the wind speed varies per area?)
- It looks like we might deduce the missing wind currents from the changes in measured concentrations of chemicals?
- We want to make a simplified grid that only contains the factories and the sensors.
- Redundant Data, we can add columns for each chemical sensor pair?, leaving out the reading, in the following form:
------

- Pandas is acting weird (double timestamp but 7 columns? pls halp)
- Making plots with a slider is not going so well (sadde libie, need halp)

------
Reservations in June:

Date | Time | Location
---- | ---- | ----
8 | 14-17 | B1.19
12 | 9-12 | B1.19
19 | 12-15 | B1.19
21 | 12-15 | B1.19

## Week 1

#### Monday
> After the first seminar, we had a meeting in order to discuss which dataset/project we are going to use.
> The current options are:
>  - Power Consumption Amsterdam
>  - Vast 2017 mini challenge 2

#### Tuesday
> ##### First meeting with Nick:
> During this meeting, we have unanimously chosen for the Vast 2017 mini challenge 2
> The meeting on thursday the 14th has been moved to friday the 15th

#### Wednesday
> On wednesday we will meet at 11:00.
> - jupyter notebook/python3
> - Which data are we going to compare? -> data format

  | chemical | sensor | reading | wind direction | wind speed | time
--- | --- | --- | --- | --- | --- |
 Data Type | nominal | nominal | ratio | ratio/ordinal? | ratio | Interval


 Elevation?

#### Thursday
#### Friday
> Hidde: 460 was een lege regel, alles hier onder 1 omhoog geschoven.
