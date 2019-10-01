class CallDetail:
    def __init__(self,caller,called,duration,call_type):
        self.called_from = caller
        self.called_to = called
        self.call_duration = duration
        self.call_type = call_type

    def report(self):
        print(self.called_from.ljust(15),self.called_to.ljust(15),self.call_duration.ljust(15),self.call_type.ljust(15))
  
class Util:
    def __init__(self):
        self.list_of_call_objects=None 
 
    def parse_customer(self,list_of_call_string):
        self.list_of_call_string = list_of_call_string
        for x in list_of_call_string:
            call=x.split(",")
            callD = CallDetail(call[0],call[1],call[2],call[3])
            callD.report()
        
 
call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD' 
 
list_of_call_string=[call,call2,call3]
print("called_from".ljust(15),"called_to".ljust(15),"call_duration".ljust(15),"call_type".ljust(15))
Util5=Util()
Util().parse_customer(list_of_call_string)

