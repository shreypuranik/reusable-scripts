import csv
import json

class CsvToJson:
    def process(self):
        csvFilePath = './csv_filename.csv'
        jsonFilePath = './final_json_filename.json'

        dataDictionary = {}

        with open(csvFilePath, encoding = 'utf-8') as csvFileHandler:
            csvReader = csv.DictReader(csvFileHandler)

            for rows in csvReader:
                key = rows['MediaId'] #Change MediaId to your index of choice
                dataDictionary[key] = rows
        
        with open(jsonFilePath, 'w', encoding = 'utf-8') as jsonFileHandler:
            jsonFileHandler.write(json.dumps(dataDictionary, indent = 4))


process = CsvToJson()
process.process()
