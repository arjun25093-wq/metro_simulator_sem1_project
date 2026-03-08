#f.read()
#f.readline()
#f.readlines()
#f.tell()
#f.seek()

metro_data = open("metro_data.txt",'r')
#metro_data = open("/2025093-metro-simulator/metro_data.txt",'r')
#this address does not work

metro_stations={}
is_interchange_station={}
interchange_stations={}

metro_data.readline()
for i in range(83):
    a,b=metro_data.readline().strip().split(',')
    if a not in metro_stations:
        metro_stations[a]=b
    else:
        is_interchange_station[a]=True
        interchange_stations[a]=b
#print(metro_data.tell())
#print(is_interchange_station) #=v
#print(interchange_stations) #=>{'JANAKPURI WEST': 'b14', 'BOTANICAL GARDEN': 'b42'}
#print(metro_stations['dabri mor - janakpuri south'][0])

#########################################################################################################################
#Q1

def valid_time_rush_hour(time):
    hr,min=time.strip().split(':')
    hr=int(hr)
    min=int(min)
    sys_time=hr*60 + min

    if not 0<=min<60:
        return print("please enter a valid time")
    if not 0<=hr<24:
        return print("please enter a valid time")
    if not 360<=sys_time<1380:
        return print("no metro is available before 6am or after 11pm") #code needs improvement
    
    if 6<=hr<8 or 10<=hr<17 or 19<=hr<23:
        is_rush=False
    if 8<=hr<10 or 17<=hr<19:
        is_rush=True
    return sys_time,is_rush

def time_converter(time):
    hr=time//60
    min=time%60
    if min>9:
        return f"{hr}:{min}"
    else:
        return f"{hr}:0{min}"

def metro_time(time,is_rush):
    if not is_rush:
        i=2
    else:
        i=1
    next_metro=((time//4)+1*i)*4
    next_metro1=((time//4)+2*i)*4
    next_metro2=((time//4)+3*i)*4
    next_metro3=((time//4)+4*i)*4
    next_metro4=((time//4)+5*i)*4

    return time_converter(next_metro), time_converter(next_metro1), time_converter(next_metro2), time_converter(next_metro3), time_converter(next_metro4)



def Q1():
    line=input("Line = ").strip().lower()
    if line=='magenta' or line=='blue':
        pass
    else:
        print("enter a valid metro line.")
        return 
    station=input("Station = ").lower().strip()
    if station not in metro_stations and metro_stations[station][0]!=line[0]:
        print("please enter a metro staiton on the blue or magenta line.")
        return 
    time=input("time(Hr:Min) = ")
    print()
    sys_time,is_rush=valid_time_rush_hour(time)
    print(f"next metro at {metro_time(sys_time,is_rush)[0]}")
    print(f"subsequent metros at {metro_time(sys_time,is_rush)[1]} {metro_time(sys_time,is_rush)[2]} {metro_time(sys_time,is_rush)[3]} {metro_time(sys_time,is_rush)[4]} ....")
#Q1()

#########################################################################################################################
#Q2

station_time_difference={}
metro_data.readline()
metro_data.readline()
for i in metro_data:
    a,b=i.strip().split(",")
    b=int(b)
    station_time_difference[a]=b
#print(station_time_difference)

def is_same_line(scource,destination):
    if (scource in is_interchange_station) or (destination in is_interchange_station):
        return True 
    scr_st=metro_stations[scource][0]
    des_st=metro_stations[destination][0]
    if scr_st==des_st:
        return True
    else:
        return False
#print(is_same_line(scource="UTTAM NAGAR WEST",destination="PANCHSHEEL PARK"))

def lower_station(a,b):
    if a[0]==b[0]:
        if a[1:] > b[1:]:
            return b,a
        elif b[1:]>a[1:]:
            return a,b
        else:
            return print("both stations are same")
#print(lower_station('b05','m03'))

def station_encoder(a):
    b=a[0]
    c=a[1:]
    if int(c)+1<10:
        d=f"0{str(int(c)+1)}"
    else:
        d=str(int(c)+1)
    return f"{b}{c}{b}{d}"
#print(station_encoder('b94'))

def station_time_adder(a,i):
    b=a[0]
    c=a[4:]
    if int(c)+1<10:
        d=f"0{str(int(c)+1)}"
    else:
        d=str(int(c)+1)
    e=f"{b}{c}{b}{d}"
    
    return station_time_difference[a] + station_time_adder(e,i) if not a==i else 0
#print(station_time_adder("m02m03","m04m05"))

def Q2_1(scource,destination):
    try:
        low_st_code,high_st_code=lower_station(metro_stations[scource],metro_stations[destination])
    except:
        low_st_code,high_st_code=lower_station(metro_stations[scource],interchange_stations[destination])
    low_st_encode=station_encoder(low_st_code)
    high_st_encode=station_encoder(high_st_code)
    time_taken=station_time_adder(low_st_encode,high_st_encode)
    return time_taken

def interchange_janakpuri(scource,destination):
    if scource[0]=="m" and destination[0]=="b":
        magenta_liner=scource
        blue_liner=destination
    else:
        magenta_liner=destination
        blue_liner=scource
    
    time_taken_m=Q2_1(magenta_liner,"janakpuri west")
    time_taken_b=Q2_1(blue_liner,"janakpuri west")
    total_time=time_taken_b+time_taken_m+10
    return time_taken_m,time_taken_b,"janakpuri west",total_time

def interchange_botanical(scource,destination):
    if scource[0]=="m" and destination[0]=="b":
        magenta_liner=scource
        blue_liner=destination
    else:
        magenta_liner=destination
        blue_liner=scource
    
    time_taken_m=Q2_1(magenta_liner,"botanical garden")
    time_taken_b=Q2_1(blue_liner,"botanical garden")
    total_time=time_taken_b+time_taken_m+10
    return time_taken_m,time_taken_b,"botanical garden",total_time

def multi_line_handler(scource,destination):
    if interchange_botanical(scource,destination)[3]<interchange_janakpuri(scource,destination)[3]:
        return interchange_botanical(scource,destination)[0],interchange_botanical(scource,destination)[1],interchange_botanical(scource,destination)[2]
    
    elif interchange_botanical(scource,destination)[3]>interchange_janakpuri(scource,destination)[3]:
        return interchange_janakpuri(scource,destination)[0],interchange_janakpuri(scource,destination)[1],interchange_janakpuri(scource,destination)[2]


def Q2():
    scource=input("scource: ").strip().lower()
    destination=input("destination: ").strip().lower()
    time=input("time of travel: ")
    if scource not in metro_stations:
        print("please enter a valid metro station.")
    if destination not in metro_stations:
        print("please enter a valid metro station.")
    if is_same_line(scource,destination):
        time_taken=Q2_1(scource,destination)
        next_metro_scource=metro_time(valid_time_rush_hour(time)[0],valid_time_rush_hour(time)[1])[0]
        arrival_interchange=metro_time(valid_time_rush_hour(time)[0]+time_taken,valid_time_rush_hour(time)[1])[0]
    else:
        magenta_time_taken=multi_line_handler(scource,destination)[0]
        blue_time_taken=multi_line_handler(scource,destination)[1]
        interchange_time_taken=10
        interchanging_station=multi_line_handler(scource,destination)[2]
        if metro_stations[scource][0]=="m":
            first_travel=magenta_time_taken
            second_travel=blue_time_taken
        elif metro_stations[scource][0]=="b":
            first_travel=blue_time_taken
            second_travel=magenta_time_taken
        
        next_metro_scource=metro_time(valid_time_rush_hour(time)[0],valid_time_rush_hour(time)[1])[0]
        arrival_interchange=time_converter(valid_time_rush_hour(next_metro_scource)[0]+first_travel)
        next_metro_interchange=metro_time(valid_time_rush_hour(arrival_interchange)[0]+10,valid_time_rush_hour(arrival_interchange)[1]+10)[0]
        arrival_destination=time_converter(valid_time_rush_hour(next_metro_interchange)[0]+second_travel)
        time_taken=(int(valid_time_rush_hour(arrival_destination)[0])-int(valid_time_rush_hour(next_metro_scource)[0]))
        #print(arrival_interchange)
        #print(next_metro_interchange)
        #print(arrival_destination)

    print("Journey Plan:")
    if scource[0]=="b":
        print(f"start at {scource} (blue line)")
    elif scource[0]=="m":
        print(f"start at {scource} (magenta line)")
    print(f"Next metro at {next_metro_scource}")
    try:
        print(f"Arrive at {interchanging_station} at {arrival_interchange}")
    except:
        print(f"Arrive at {destination} at {arrival_interchange}")
    if not is_same_line(scource,destination):
        if scource[0]=="b":
            print(f"transfer to magenta line")
        elif scource[0]=="m":
            print(f"transfer to blue line")
        print(f"Next metro departs at {next_metro_interchange}")
        print(f"Arrive at {destination} at {arrival_destination}")
    print(f"Total travel time: {time_taken} minutes")
#print(type(interchange_botanical("uttam nagar east","dabri mor - janakpuri south")))

#Q2()

def question_selector():
    try:
        x=int(input('''What would you like to try:

Metro Timings Module:(press 0)

Ride journey planner:(press 1)
===>'''))
    
        if not x:
            return Q1()
        elif x==1:
            return Q2()
    except:
        print("invalid input")
        return question_selector



#########################################################################################################################

#CODE RUN
question_selector()