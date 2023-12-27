""""two methods 
    1]open(filename,mode,encoding) :only opens the file need to close using close function
    2]with open() : with statement calls 2 built-in methods behind the scene – __enter()__ and __exit()__ , which auto close the file
    conclusion : it is always good to go with open() """

# data=open(""./dummy_car_details.csv"",'r')
# print(data.read())

#==========================read=================================
import csv
# with open("./dummy_car_details.csv","r") as data:
#     #print(data.read())
#     csv_read=csv.reader(data)

#     for i in csv_read:
#         print(i[0])

#==========================append=================================

with open("./dummy_car_details.csv","a") as data:
    #print(data.read())
    fieldname=["sr no","Brand"]
    write=csv.DictWriter(data,fieldnames=fieldname)
    #write.writeheader()
    write.writerow({'sr no':'11','Brand':'Maserati'})

#==================================write=================================
    
fields = ['Name', 'Branch', 'Year', 'CGPA']  

rows = [ ['Nikhil', 'COE', '2', '9.0'],  
         ['Sanchit', 'COE', '2', '9.1'],  
         ['Aditya', 'IT', '2', '9.3'],  
         ['Sagar', 'SE', '1', '9.5'],  
         ['Prateek', 'MCE', '3', '7.8'],  
         ['Sahil', 'EP', '2', '9.1']]  
  
filename = "university_records.csv"

with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows) 