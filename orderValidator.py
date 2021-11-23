import json
import jsonschema
import os
from jsonschema import validate

def validateJson(jsonData, schema):
	try:
		validate(instance=jsonData, schema=schema)
	except jsonschema.exceptions.ValidationError as err:
		print(file + " " + "KO " + err.message)
		global invalidDocument
		invalidDocument += 1


	else :
		print(file + " " + "OK ")
		global validDocument
		validDocument += 1



pathSchema=r"OrderSchema.json"
path = 'C:\\Users\\MATTIA CAPANO\\PycharmProjects\\jsonValidator\\order\\'
docPath= os.listdir('C:\\Users\\MATTIA CAPANO\\PycharmProjects\\jsonValidator\\order\\')
docNumber = len(docPath)

validDocument = 0
invalidDocument = 0



fileSchema=os.path.join(pathSchema)
with open(fileSchema) as f:
 dataSchema = json.load(f)

print("Validating "+str(docNumber)+ " document")
print("\n")
for i in range(docNumber):
		finalPath = path+docPath[i]
		i += 1
		file = os.path.join(finalPath)
		with open(file, encoding="utf8") as f:
			data = json.load(f)
			validateJson(data, dataSchema)


print("\n")
print("Valid document: "+ str(validDocument))
print("Invalid document: "+ str(invalidDocument))
