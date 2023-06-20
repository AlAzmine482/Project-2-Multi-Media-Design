#proj2.py
#python3 proj2.py Baselight_JJacobs_20230323.txt Flame_DFlowers_20230323.txt Flame_MFelix_20230323.txt -xytech Xytech_20230323.txt --output db
#python3 proj2.py Baselight_TDanza_20230324.txt -xytech Xytech_20230324.txt --output db
#python3 proj2.py Baselight_GLopez_20230325.txt -xytech Xytech_20230325.txt --output db
#python3 proj2.py Baselight_THolland_20230326.txt Flame_DFlowers_20230326.txt -xytech Xytech_20230326.txt --output db
#python3 proj2.py Baselight_THolland_20230327.txt Flame_DFlowers_20230327.txt -xytech Xytech_20230327.txt --output db
import argparse
import collections
import csv
import datetime
from email.mime import base
import getpass
import numbers
import os
from re import T, sub
from tokenize import Number 
import pymongo
import re
#import datetime
from datetime import date

def extract_numbers(path):
    """
    A helper function to extract the numbers from a given path.
    """
    numbers = []
    for word in path.split():
        if "[" in word and "]" in word:
            numbers.extend(map(int, word.strip("[]").split("-")))
        elif word.isdigit():
            numbers.append(int(word))
    return numbers

"""
def find_ranges(nums):
    start = end = nums[0]
    ranges = []

    for num in nums[1:]:
        if not num.strip().isnumeric():
            continue
        if int(num) == int(end) + 1:
            end = num
        else:
            ranges.append((start, end))
            start = end = num

    # add last range to list of ranges
    ranges.append((start, end))

    # convert ranges to string representation
    ranges_str = ' '.join(f'[{start}-{end}]' for start, end in ranges)
    ranges_str = ' '.join(f'[{start}-{end}]' for start, end in ranges)
    return ranges_str
    #return ranges
"""
def find_ranges(nums):
    start = end = nums[0]
    ranges = []

    for num in nums[1:]:
        if not num.strip().isnumeric():
            continue
        if int(num) == int(end) + 1:
            end = num
        else:
            ranges.append((start, end))
            start = end = num

    # add last range to list of ranges
    ranges.append((start, end))

    return ranges



scriptrun = []



listb4set = []
"""
parser = argparse.ArgumentParser(description='Import a text file and optionally print its lines.')
parser.add_argument('filename', type=str, help='the path to the text file to import')
parser.add_argument('-v', '--verbose', action='store_true', help='print each line of the imported file')
#, dest = "workfiles"
args = parser.parse_args()
"""

username = getpass.getuser()
#print(username)
scriptrun.append(username)

"""

parser = argparse.ArgumentParser()
parser.add_argument('files',  nargs='+', help='Baselight/Flame text files')
parser.add_argument('--xytech',  nargs='+', help='Xytech file input')
parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose output")
parser.add_argument("--output", choices=["csv", "db"])


args = parser.parse_args()

if args.workFiles is None: 
    print("\nNo baselight or Flame File selected")
else: 
    print("\nBaselight File or Flame File", args.workFiles)
    print("\n Xytech File", args.xytech)
if args.output == 'csv':
    print("\nCSV: ")
else:
    print("\n DataBase: ")
    filename = os.path.basename(args.files)
print(f'{filename}')
#filenames.append(filename)
name, ext = os.path.splitext(filename)
basefile_parts = name.split('_')
machine.append(basefile_parts[0])
person.append(basefile_parts[1])
date.append(basefile_parts[2])

print(machine)
print(person)
print(date)
print(f'User running script: {scriptrun}')
    """

filenames = []
filenum = []
storage = []
machine = []
person = []
datev2 = []
test = []
numpath = []
testnum = []
remrand = []
filedict = {}
submittedate = []

"""    filename = os.path.basename(args.files)
print(f'{filename}')
#filenames.append(filename)
name, ext = os.path.splitext(filename)
basefile_parts = name.split('_')
machine.append(basefile_parts[0])
person.append(basefile_parts[1])
date.append(basefile_parts[2])

print(machine)
print(person)
print(date)
print(f'User running script: {scriptrun}')"""

xytechlocfiles = []
numberList = []

parser = argparse.ArgumentParser()
parser.add_argument('files', nargs='+', help='Baselight/Flame text files')
parser.add_argument('-xytech',  help='Xytech file input')
parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose output")
parser.add_argument("--output", choices=["csv", "db"])
args = parser.parse_args()

for file_path in args.files:
    filename = os.path.basename(file_path)
    print(f'Processing file: {filename}')

    name, ext = os.path.splitext(filename)
    now = date.today()
    basefile_parts = name.split('_')
    machine.append(basefile_parts[0])
    person.append(basefile_parts[1])
    datev2.append(basefile_parts[2])
    submittedate.append(now)

    print(f'Machine: {machine}')
    print(f'Person: {person}')
    print(f'Date: {datev2}')
    print(f'Submitted: {submittedate}')


    with open(file_path) as f:
        lines = f.readlines()
        for each in lines: 
            #x = each.strip("/net/flame-archive")
            #y =  each.strip("/images1/")
            y = each.replace("/images1/", "").replace("/net/flame-archive", "").strip()
            z = each.replace('<null>', "").replace('<err>', "").strip()
            #xsplit = x.split()
            ysplit = y.split()[0]
            pathnum = y.strip().split(" ")[1:]
            #pathnumv2 = [int(x) if x.isdigit() else None for x in z.strip().split(" ")[1:] if x != ""]
            pathnumv2 = [int(x) if x.isdigit() else None for x in z.strip().split(" ")[1:] if x != ""]

            print(y)# Avatar/pickups/shot_3ab/1920x1080
            #print("this is files loc")
            #print(ysplit) works i only get location path
            #print("this is after loc")
            listb4set.append(y)
            #list.append(x)
            print("this is pathnum")
            print(pathnum)
            
            print(" below is a copy of pathnum")
            print(pathnumv2)
            #pathnum = [s.replace('<err>', '').replace('<null>', '') for s in pathnum]


            #for err in pathnum:
             #  x = err.replace("<err>", "").replace("<null>", "")
            
             #  remrand.append(x)

            #ranges = find_ranges(remrand)
            #first_range_str = f'[{ranges[0][0]}-{ranges[0][1]}]'
            #print(first_range_str)  # output: '[32-34]'
            #ranges_str = find_ranges(remrand)
            #testnum.append(ranges_str[0])
            #numranges = list(set(testnum))
            #print("below is testnum")
            #print(numranges)

            
            #testnum.extend(ranges_str)
            
            #print(testnum)
            #print(f'Frame ranges: {ranges_str}')
            #testnum.append(f'Frame ranges: {ranges_str}')
            

            filenum.append(pathnum)
            #filenum.append(x)
            #help =  each.split()
            filenames.append(ysplit)
            #if "1920x1080" in each:
             #   path = y.strip()
                #path works
             #   locfile ,splitframes = path.split('1920x1080')
             #   print(f'Location of files: {locfile}')
             #   print("This is frames", splitframes)
                #filenames.append(locfile)
              #  filenum.append(splitframes)
                #filenames.append((path, splitframes))
            new_filenum = []
            for sublist in filenum:
                new_list = []
                sublist = [int(i) for i in sublist if i not in ('<err>', '<null>')]
                sublist.sort()
                start = sublist[0]
                end = sublist[0]
                for i in range(1, len(sublist)):
                     if sublist[i] == end+1:
                            end = sublist[i]
                     else:
                        if start == end:
                            new_list.append(str(start))
                        else:
                            new_list.append(f"[{start}-{end}]")
                        start = sublist[i]
                        end = sublist[i]
                if start == end:
                    new_list.append(str(start))
                else:
                     new_list.append(f"[{start}-{end}]")
                new_filenum.append(new_list)


            """
            ranges =[]
            first = ""
            last = ""
            pointer = ""

            new_filenum = []
            for sublist in filenum:
                new_list = []
                sublist = [int(i) for i in sublist]
                sublist.sort()
                start = sublist[0]
                end = sublist[0]
                for i in range(1, len(sublist)):
                    if sublist[i] == end+1:
                       end = sublist[i]
                    else:
                       if start == end:
                            new_list.append(str(start))
                       else:
                            new_list.append(f"{start}-{end}")
                            start = sublist[i]
                            end = sublist[i]
                if start == end:
                    new_list.append(str(start))
                else:
                    new_list.append(f"{start}-{end}")
                new_filenum.append(new_list)
                    """

# print(filenum)
# print("-------------")
# print(new_filenum)
# print("-------------")

        
    

                
    print("end of baselight")
    print(filenames)
    print("filenames")

    #print(filenum)
    #print(listb4set)

    print("filenum:")
    print(filenum)
    
    print("remrand")
    #print(remrand)
    print(new_filenum)

    producer = ""
    operator = ""
    job = ""
    xytechcontent = ""
    notes = ""
    DictionaryFiles = {}
    with open(args.xytech) as f2: 
        xytechline = f2.readlines()
        for xyeach in  xytechline: 
            print(xyeach)
            if xyeach.__contains__("/"):
                xyeachhold = xyeach
                xytechlocfiles.append(xyeach)
                
            if xyeach.startswith("Producer:"):
                w = xyeach.replace("Producer: ", "")
                stripn = w.strip('\n')
                producer = (stripn)
            if xyeach.startswith("Operator:"):
                operators = xyeach.replace("Operator: ", "")
                stripopn = operators.strip('\n')
                operator = (stripopn)
            if xyeach.startswith('Job:'):
                jobrep = xyeach.replace("Job: ", "") 
                jobsp = jobrep.strip('\n')
                job = (jobsp)
            if xyeach.startswith('Please '):
                notes = (xyeach)

            helpxytech = xyeach.strip('\n')
            #for each in filenames:
            #   for eachnum in filenum:
             #     if helpxytech in each:
              #         test.append(eachnum) list num is correct
            #for name, nums in zip(filenames, filenum):
            for name, nums in zip(filenames, new_filenum):
                if helpxytech.endswith(name):
                  test.append(f"{helpxytech} {' '.join(nums)}")
                  if helpxytech not in DictionaryFiles:
                        finalkey = helpxytech
                        #finalvalue = DictionaryFiles[nums]
                        DictionaryFiles[finalkey] = nums

            
              #   x = helpxytech.strip()
                 #xytechcontent.append(x)
                #for eachfile in list:
                 #   if helpxytech.endswith(each):
                  #      y = helpxytech.join(filenum)
                        #test.append(y)
                 #xytechcontent.append(helpxytech)

#print(xytechcontent)

                        
                 #print("todo")
    #for eachnum in filenum:
     #   print(
     # eachnum)
   
  
    #print(f'{filedict}')

    mylist = list(set(test))
  
    #print(f"{test}\n")
    mylist.sort()
    print(args.files)
    print("Below is a set")
   
    print(mylist)
    mydict = {}
    for item in mylist:
        file_path, nums = item.split(' ', 1)
        nums = nums.split()
        if file_path in mydict:
            mydict[file_path].extend(nums)
        else:
            mydict[file_path] = nums

    
    #print("fuck")
    #print(mydict)

    
    
    finaldict = {}

    for line in mylist:
         parts = line.split()
         filepath = parts[0]
         filenums = parts[1:]
         if filepath in finaldict:
           finaldict[filepath] = list(set(finaldict[filepath] + filenums))
         else:
           finaldict[filepath] = filenums

   # print(finaldict)
    #print(xytechlocfiles)
    #print(producer)
    #print(operator)
    #print(job)
    #print(notes)
    print("User thats running the Script: ", scriptrun)
    # print(xytechcontent)
    #print(DictionaryFiles)
   
    new_list = []
    
    #sorted_list = []

    sorted_list = sorted(mylist, key=extract_numbers)
    for item in sorted_list:
        items = item.split(" ")
        for i in range(1, len(items)):
             new_list.append(f"{items[0]} {items[i]}")

    #new_list.sort()
   # print(new_list)
    
    print(new_list)

if args.output == "csv":
    print("CSV File output\n")
    with open("proj2.csv", "w", newline="") as csvfile:
        fieldnames = ["Producer", "Operator", "Job", "Notes"]
        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        thewriter.writeheader()
        thewriter.writerow({"Producer": producer,
                            "Operator": operator,
                            "Job": job,
                            "Notes": notes})
        Write = csv.writer(csvfile)
        splitDR = ["directory", "frames"]
        lastWrite = csv.DictWriter(csvfile, fieldnames = splitDR)
        
        for item in sorted_list:
            directory, pathnums = item.split(' ', 1)
            nums = pathnums.split()
            for num in nums:
                lastWrite.writerow({"directory": directory, "frames": num})
                
                 
           
        #for filename, nums in mydict.items():
            #lastWrite.writerow({"directory": filename, "frames": ""})
         #   for number in nums:
          #      lastWrite.writerow({"directory": filename, "frames": number})
        
        #works code below
        """
        for item in mylist:
             split_item = item.split()
             directory = split_item[0]
             frames = split_item[1:]
             for frame in frames:
                lastWrite.writerow({"directory": directory, "frames": frame})
                """
        """
        for combined in mylist:
            x = combined.split()
            data = {}
            data["directory"] = combined.split()[0]
            data["frames"] = ",".join(combined.split()[1:])
            lastWrite.writerow(data)
       
        for filename, nums in mydict.items():
            lastWrite.writerow({"directory": filename, "frames": ""})
            for number in nums:
                lastWrite.writerow({"directory": filename, "frames": number})
                """     

       
            #lastWrite.writerow({"directory": })

        #works
        """
        for file_str in mylist:
            dir_str, frames_str = file_str.split(' ', 1)
            frames_list = frames_str.split(' ')
            lastWrite.writerow({'directory': dir_str, 'frames': ' '.join(frames_list)})
          
        for filename, nums in mydict.items():
            #lastWrite.writerow({'directory': filename, 'frames': ' '.join(nums)})
            Write.writerow(["directory", filename])
        for number in nums:
            Write.writerow(["frames", number])

        """
        

else: 
    print("db")
     #for eachlist in list:
#dmongo db test code not trying to get it working rn
    client = pymongo.MongoClient("mongodb+srv://alazmine:Muda@cluster0.fdnlwld.mongodb.net/?retryWrites=true&w=majority")

    mydb = client["mydatabase"]
    print(client.list_database_names())

    dblist = client.list_database_names()
    if "mydatabase" in dblist:
        print("The database exists.")
    filesub = mydb["files"]
   # machine = "MyMachine"
    mycollection = mydb["mycollection"]
    collection2 = mydb["collection2"]
   # person = "John Doe"
    #date = datetime.now()
    #datesubmitted = datetime(2023, 4, 2)
    #for y in range(len(machine)):
    
    mydict = {"machine": machine, "person": person, "date": datev2,  "datesubmited": datetime.datetime.now()}
   
    # Iterate over each element in the machine list and add it to the dictionary
  
    x  = mycollection.insert_one(mydict)
    for x in mycollection.find():
        #print(x)
        mydict = {"date": datev2, "datesubmited": datetime.datetime.now()}

    i = 0
    
    dbdict = {"User":person[i], "datesubmited": datev2[i] ,"Files to Fix": new_list }
    i +=1
    y = collection2.insert_one(dbdict)
    print("\nQ1:Work By TDanza ")
    question1 = {"User": "TDanza"}
    q1_result = collection2.find(question1)
    file_set = set() 
    resultofq1 = q1_result


    for res in resultofq1:
        #print(f"\n{res}")
        for file in res["Files to Fix"]:
            file_set.add(file)
    
    for file in file_set:
         print(file)
    index_flame = machine.count("Flame") 

    print("\nQ2: Work done Before 3-25-2023 on Flame")
    # Define the query to find documents in collection1
    query2 = {"machine": {"$elemMatch": {"$eq": "Flame"}}, "date": {"$lt": "20230325"}}

    # Find documents in collection1 matching the query
    resultofusers = mycollection.find(query2)

    # Iterate over the matching documents in collection1
    flameuser = []
    
    for doc in resultofusers:
      # Extract the person and machine arrays from the document
     person_valu = doc["person"]  # Only extract the first two values
     machine_valu = doc["machine"]
     date_valu = doc["date"]

        # Find the index of "Flame" in the machine array
    flame_index = [i for i, machine in enumerate(machine_valu) if machine == "Flame"]

    # Iterate over the flame index and person values in parallel using zip
    for index, person in zip(flame_index, person_valu):
        x = person_valu[index]
        flameuser.append((x, date_valu[index]))

    # Create a list of file paths
    file_paths = []
    print(flameuser)
    directory = os.path.dirname(os.path.abspath(__file__))

    # Loop through the list of tuples
    for person, date in flameuser:
     filename = f"Flame_{person}_{date}.txt"
     filepath = os.path.join(directory, filename)
     file_paths.append(filepath)
    
    # Open and read each file in the list of file paths
    for filepath in file_paths:
        with open(filepath, "r") as f:
          content = f.read()
          #print(content)
          #netreplacer = content.replace("/net/flame-archine "," ")
          # Do something with the file content, e.g. print it
          #print(f"\n{content}")
          #lines = [line.strip() for line in content.split('\n') if 'Hydraulx' in line or 'AnimalLogic' in line or 'Framestore' in line]
          lines = [line.strip().replace("/net/flame-archive", "") for line in content.split('\n') if 'Hydraulx' in line or 'AnimalLogic' in line or 'Framestore' in line]
          # Get the file name from the file path
          filename = os.path.basename(filepath)
          print(lines)
          # Match the lines with the file array in collection 2
          query3 = {"Files to Fix": {"$in": lines}}
          #print(query3)
          resultofmatches = collection2.find(query3)
          #print(query3)
          for line in lines:
            query = {"Files to Fix": {"$regex": line}}
            resultofmatche = collection2.find(query)
            
            # Extract the desired information from the matching documents
        matches = [x for x in new_list if "Avatar/reel1/VFX/Hydraulx" in x or "Avatar/reel1/VFX/AnimalLogic" in x or "Avatar/reel1/VFX/Framestore" in x]
        #print(matches)
    
          # Extract the desired information from the matching documents
         
            #print(f"{doc['Files to Fix']}")
            #for each in doc["Files to Fix"]:
       

          
    """
    print("Q2: Work done Before 3-25-2023")
    # Define the query to find documents in collection1
    query2 = {"machine": {"$elemMatch": {"$eq": "Flame"}}, "date": {"$lt": "20230325"}}

    # Find documents in collection1 matching the query
    resultofusers = mycollection.find(query2)

    # Iterate over the matching documents in collection1
    flameuser = []

    for doc in resultofusers:
        # Extract the person and machine arrays from the document
        person_valu = doc["person"]  # Only extract the first two values
        machine_valu = doc["machine"]
        date_valu = doc["date"]

    # Find the index of "Flame" in the machine array
    flame_index = [i for i, machine in enumerate(machine_valu) if machine == "Flame"]

    # Iterate over the flame index and person values in parallel using zip
    for index, person in zip(flame_index, person_valu):
        x = person_valu[index]
        flameuser.append((x, date_valu[index]))

    print(flameuser)
    directory = os.path.dirname(os.path.abspath(__file__))

    # Loop through the list of tuples
    for person, date in flameuser:
        filename = f"Flame_{person}_{date}.txt"
        filepath = os.path.join(directory, filename)
    with open(filepath, "r") as f:
        content = f.read()
        # Do something with the file content, e.g. print it
        print(content)
  
    """
    """
    
    question2 = { "date": { "$lt":"20230325"}, "machine": "Flame" 
    }
    
    q2_Result = mycollection.find(question2)
    result = mycollection.aggregate([{
        "$lookup": {
        "$lt": "date",
        "localField": "datesubmited"

        }
    }])
    
    resultofq2 = q2_Result
    index = []
    for i, machine in enumerate(mycollection.find_one()["machine"]):
        if machine == "Flame":
            index.append(i)

    for inte in index: 
        userne = mycollection.find_one()["person"][index]
        date2 =  mycollection.find_one()["date"] [index]
    db_call = collection2.find_one({
        "person": userne, 
        "date": date2
    })
    if db_call: 
        """

    

    print("\nQ3: work for hpsans13 on date 3-26-2023")
    question3 = {
        "frame_ranges": {"$regex": "hpsans13"},
         "date": "20230326"
    }
    
    q3_result = collection2.find(question3)
    results_list = list(q3_result)
    count = len(results_list)


    if count == 0:
        print("No results Found")
    else:

        print(f"Number of results:{count}")
        for result in results_list:
            print(result)

    print("\nQ4: Name all Autodesk Flame Users ")
    query4 = { "machine": {"$regex": "Flame"} }
    testq4 = mycollection.find(query4) 
    fileflameusersset = set() 
        
    query = {"machine": {"$elemMatch": {"$eq": "Flame"}}}

    # Find documents in collection1 matching the query
    result1 = mycollection.find(query)

# Find index of "Flame" machine in machines array
    flame_index = machine.count("Flame")
   
# Get the first document from result1 cursor and extract its person values
    doc = next(result1)
    person_values = doc["person"]  # Only extract the first two values

# Find the index of "Flame" in the machine array
    machine_values = doc["machine"]
    flame_index = [i for i, machine in enumerate(machine_values) if machine == "Flame"]

# Iterate over the flame index and person values in parallel using zip
    flameusers = [person_values[index] for index in flame_index]

    print(flameusers)
#for resflame in testq4: 
   # if "Flame" in resflame["machine"]: 
        #for person in resflame["person"]:
            #x = person[resflame["machine"]]
            #print(x)
            #fileflameusersset.add(person)

#flameusers = list(fileflameusersset)
#print(flameusers)
"""
# Query to find matching documents in collection1
query = {"machine": {"$elemMatch": {"$eq": "Flame"}}}


# Find documents in collection1 matching the query
result1 = mycollection.find(query)

# Find index of "Flame" machine in machines array
flame_index = machine.count("Flame")


# Iterate over the matching documents in collection1
fileflameusersset = set()
flameusers = []

for doc in result1:
    # Extract the person and machine arrays from the document
    person_values = doc["person"]  # Only extract the first two values
    machine_values = doc["machine"]

    # Find the index of "Flame" in the machine array
    flame_index = [i for i, machine in enumerate(machine_values) if machine == "Flame"]

    # Iterate over the flame index and person values in parallel using zip
    for index, person in zip(flame_index, person_values):
        x = person_values[index]
        #fileflameusersset.add(x)
        #flameusers.extend(x)
        flameusers.append(x)
      
    flameusers = list(set(flameusers))
        
    #print(x, index)
    
   
    print(flameusers[:2])
   # print(fileflameusersset)

"""
    
   # query = {"machine": {"$elemMatch": {"$eq": "Flame"}}}

    # Find documents in collection1 matching the query
   # result1 = mycollection.find(query)

# Find index of "Flame" machine in machines array
   # flame_index = machine.count("Flame")

# Get the first document from result1 cursor and extract its person values
  #  doc = next(result1)
   # person_values = doc["person"]  # Only extract the first two values

# Find the index of "Flame" in the machine array
   # machine_values = doc["machine"]
   # flame_index = [i for i, machine in enumerate(machine_values) if machine == "Flame"]

# Iterate over the flame index and person values in parallel using zip
  #  flameusers = [person_values[index] for index in flame_index]

  #  print(flameusers)


    #mycol = mydb[scriptrun , machine, person, date]

    #print(mydb.list_collection_names())
    #collist = mydb.list_collection_names()
    #if "customers" in collist:
     #   print("The collection exists.")

#x = mycol.insert_one(mylist)
#print(x.inserted_id)
#print(xytechcontent)

#
#fields = ['Producer', 'Operator', 'Job', 'Notes', 'Files', 'Day'] 

"""
with open(args.files) as f:
    lines = f.readlines()
    #print(lines) works
    for each in lines:
        x = each.strip("/net/flame-archive")
        y =  each.strip("/images1/")
        xsplit = x.split()
        ysplit = y.split()
        pathnum = y.strip().split(" ")[1:]
   
        
        print(y)# Avatar/pickups/shot_3ab/1920x1080
        list.append(y)
        list.append(x)
        
         #if args.workfiles is None:
         #   print("please put in files")
         #   x =test.join(lines)
          #  t = lines.replace("/images1/","")
          """

