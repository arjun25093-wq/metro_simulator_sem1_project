the metro simulator works by reading a txt file and creating a dictionary in which every station is given a code e.g: m01 for the first station in the magenta line

the time in hours and minutes is completely converted to minutes for calculation and reconverted to hr:min format for display

the txt file also contains time taken to travel from every station to next

the time is stored to special codes e.g: m01m02,5 =>means to travel from the first to the second station on magenta line 5 min are needed

the python program creates these special codes from the codes already obtained, it then recursively adds these codes until the sum reaches the last station from the first

the program also functions on the basis of assigning lower index value and higher index value to stations on the same line so that its easier to calculate for metros traveling to either directions

assumptions: there would be one metro at each station at a given time, given that at that time a metro is expected

data scources:
LIST AND ORDER OF METRO STATIONS: DMRC website
TIME DIFFERENCE BETWEEN CONSEQUTIVE STATIONS OF MAGENTA LINE: DMRC WEBSITE
TIME DIFFERENCE BETWEEN CONSEQUTIVE STATIONS OF BLUE LINE: ASKED COPILOT(seperatly finding times for 50 stations was very very time consuming)

Instructions:
the program asks input in every step.
start by selecting the question and then attempt the question as per instructed in the assignment PDF
It has been attempted to locate file with the short form address but it gives error message:
  
File "c:\Users\arjun\OneDrive\Desktop\2025093-metro-simulator\metro-simulator.py", line 8, in <module>
    metro_data = open("/2025093-metro-simulator/metro_data.txt",'r')
FileNotFoundError: [Errno 2] No such file or directory: '/2025093-metro-simulator/metro_data.txt'
PS C:\Users\arjun> 

hence the long path is used. I am unsure would work on other computers
please consider this prior notice as i could not make it work otherwise even after several attemps