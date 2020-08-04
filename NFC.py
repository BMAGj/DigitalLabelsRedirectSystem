# This will only work if rules of the CSV creation are adhered to. CSV must be called labelLinks.csv. The Python copies JS Templates which will have Analytics inserted (one custom metric for each type of label).
# The JS templates are selfaware of there names and use that to find the JSON of the same name created by this Python Script. One Python per type of label so 3 in total (NFC, QR, ShortURL)

import csv 
import json 
import os 
import shutil

# Python finds its current directory and then accesses the relevant JS file to copy and rename

directory = os.getcwd() + "/"
jsLocation = os.getcwd() + "/JS/NFCtemplate.js"

#Opens csv
csv_file = open(directory +  'labelLinks.csv', 'r')
csv_reader = csv.DictReader(csv_file)
lcount = 1 


# This """""" lcount could be replaced with a line by line read of the id field from the csv, notes at the end. 

# for loop that reads csv and outputs each row as a JSON file, creates a HTML with the script tag to a JS of the same Name, both our copied/created and moved to a Folder with the same name. The JS when called will find the JSON in the root directory of the system and redirect the user. 
 
for row in csv_reader:
    out = json.dumps(row)
    jsonoutput = open(directory + 'NFCTAG' + str(lcount)  +'.json' , 'w')
    jsonoutput.write(out)
    tagID = 'NFCTAG' + str(lcount)
    tagID2 = tagID + ".js"
    os.makedirs(tagID)
    jsPath = directory + "/" + tagID + "/" + tagID2
    htmlPath = directory + "/" + tagID + "/" + tagID + ".html"
    shutil.copy(jsLocation, directory + "/" + tagID + "/" + tagID2 )
    html = """<!doctype html>
<html>
<head>
<meta charset="utf-8">





<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-174478321-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
gtag('config', 'UA-174478321-1', {
  'custom_map': {'metric1': 'UA-174478321-1'}
});

  
</script>






<title>index</title>
</head>

<body>

""" + "<script src= """ + tagID2 + """></script>
</body>
</html>
"""
    file = open(htmlPath, "w")
    file.write(html)
    file.close()
    
    lcount+=1 
    

jsonoutput.close()
csv_file.close() 

# Might be good to add a part which finds the id in the JSON and names the file by that instead, that would help prevent user error, though the linking system will need strict rules to not lose track of which physical label holds which link, so not necessary.


