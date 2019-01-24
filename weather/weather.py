'''
Weather
'''
import json
import xmltodict

def menu():
    '''
    this is xml to json program
    
    how to use xml to json
    1.give your xml file to directory xml
    2.write your file name (do not write .xml)
    3.your json file is in json directory
    '''
    print("Hello, This is Convert program")
    print("Please drag your file to xml program's directory and write your file name")

    #Recieve file name
    while True:
        file_name = input("Your file name to convert to json (do not type .xml ex. weather.xml) : ")
        file_name += ".xml"
        try:
            file_string = open("xml/" + file_name).read()
            jsonString = json.dumps(xmltodict.parse(file_string), indent=4)
            break
        except:
            print("Something went wrong please try again...")
            continue
    while True:
        try:
            output_name = input("Please enter your output name (do not type .json ex. weather.json) : ")
            #Take output
            file = open("json/" + output_name + ".json", "w").write(jsonString)
            print("Success !! please check your program directory json")
            break
        except:
            print("Something went wrong please try again...")
            continue
menu()
