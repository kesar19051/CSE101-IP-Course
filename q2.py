def DateMeRight(date):
	"""Returns the given date in DD-MMM-YYYY format, where MMM is the string of the first 3 Letters of the Month.
	Parameters:
	date: a String in DD.MM.YYYY format""" 
	s_index=date.find(".")
	e_index=date.rfind(".")
	month=date[s_index:e_index] 
	month_str=""
	
	if(month<=6):
		if(month<3):
			if(month==1):
				month_str="Jan"
			elif(month==2):
				month_str="Feb"
			else:
				month_str="Mar"		
		else:
			if(month==5):
				month_str="May"
			else:			
				month_str="Apr"		
	else:
		if(month>9):
			if(month==10):
				month_str="Oct"
			else:					
				month_str="Nov"
			if(month==12):
				month_str="Dec"
		elif(month<9):
			if(month==6):
				month_str="Jun"		
			elif(month==7):
				month_str="Jul"	
			else:
				month_str="Aug"		

	return date[0:s_index]+"-"+month_str+"-"+date[e_index+1:]


d="5.12.1533"
print(DateMeRight(d))