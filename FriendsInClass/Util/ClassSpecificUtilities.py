'''
Created on Feb 12, 2012

@author: Hunlan
'''
from Event.EnumWeek import EnumWeekday
# from Event.Times.models import Time

def checkInstanceEnumWeek(enumWeek):
    if(not isinstance(enumWeek, EnumWeekday.__EnumAdapter__)) :
        raise TypeError('"' + str(enumWeek) + '" is not a EnumWeekday')
    
'''def checkInstanceTime(time):
    if(not isinstance(time, Time)) :
        raise TypeError('"' + str(time) + '" is not a Time')
    
'''