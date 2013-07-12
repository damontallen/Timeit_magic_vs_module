from timeit import Timer, timeit, repeat
from numpy import mean, floor, log10, ceil

def time_func(func_name, data, variables, loops):
    """This function just executes a repeat function on the passed in func_name."""
    return repeat(func_name+"("+data+")", setup="from __main__ import "+func_name+ variables, repeat=3, number=loops)

def Repeat_time(func_name, data_name):
    """This funtion behavious very simular to the %timeit magic except it returns a tuple containing the result text,
th average time, and the number of loops used."""
    data_passed = [x.strip() for x in data_name.split(',')] #if multiple pieces of data need to be passed we need to derermine what are the variables
    variables=""
    for x in data_passed:
        if x in globals().keys() and '=' not in x:
            variables+=', '+x #only import variables and not literals
    tent_time = mean(time_func(func_name, data_name, variables, 10)) #Preliminary time
    n =5/(tent_time/10) #Determine how many loops would take 5 seconds
    b = floor(log10(n)) #Make this a round number
    num = int(10**b)
    time = min(time_func(func_name, data_name, variables, num)) #Timeit
    ave_time = time/num #the avarage time
    base = int(round(log10(ave_time))) #get the base fo rscientific notation
    Ave = ave_time/(10**base)
    text = "The best of 3 time is {:.3f}x10^{} seconds for {} trials.".format(Ave, base, num)
    return (text, ave_time, num)
    
def testing(func_list, Data):
    global data #data needs tobe in the global namespace
    data = Data
    units={}
    units[0]="s"
    units[-3]="ms"
    units[-6]="us"
    units[-9]="ns"
    html_text="<table><tr><td>Function</td><td>Best time of 3</td><td>Loops</td></tr>\n" 
    for func_parts in func_list: #func_list was populated by the decorator function "decotate"
        txt, ave_time, trials =  Repeat_time(func_parts[0],"data")
        base = int(ceil(log10(ave_time)/3-1)*3) #This is to determine the units
        if base>0:
            base=0 #don't worry about kilo and mega seconds
        Time = "{:.3f} {}".format(ave_time/(10**base),units[base]) #Scaled time text
        html_text +="<tr><td>"+func_parts[0]+"</td><td>"+Time+"</td><td>"+str(trials)+"</td></tr>\n"
        #print(txt) #Print out a running log
    html_text +="</table>"
    return html_text
