#!/usr/bin/env python3
import re, requests, json

results = {}
root_url = 'http://www.sec.gov'
#Using requests Library, connect to http://www.sec.gov/divisions/enforce/friactions/friactions2002.shtml
url1 = requests.get('http://www.sec.gov/divisions/enforce/friactions/friactions2002.shtml')
text = url1.text

#use a regular expression to gather the first 5 enforcement urls (sec.gov/ligigations?)
#store the urls in a list
urls = re.findall('/litigation/.*htm', text)[:5]

#using a for loop, connect to each url in the list
for url in urls:
    url = root_url + url
    response = requests.get(url)
    text = response.text

    #again using regex, pull the following from each enforcement page
    # 1.	The release number (pull from the text, not from the url).
    # 2.	The case name of the enforcement (the text that starts with Securities and Exchange Commission v…).
    # 3.	All dollar amounts specified in the page.  A dollar amount starts with the dollar sign ($), contains numbers and commas, and may end with the text “thousand, million, billion”.
    release_num = re.search("Release No.  (.*) /", text)
    case_name = re.search("(Securities and Exchange Commission v. ([\w\s\.]*))", text)
    if case_name is not None:
        case_name = case_name.group(1)
    if case_name is None:
        case_name = 'not found'
    amounts = re.findall("(\$[0-9\,\.]+\s*(billion|million|thousand)*)", text)

    #create a dictonary for the items you gather from above
    # if items do not exist, simply record "not found" for its value
    # if multiple release numbers exist on the page, record only the first.
    # key the dict by the URL
    result = { url : {
                    'release number': int(release_num.group(1)),
                    'case name': case_name,
                    'amounts': amounts,
                    }
    }
    results.update(result)

#print the dict to the console using json-dumps()
print(json.dumps(results))

#print it again using for loops to print it manually
#found this loop at http://stackoverflow.com/questions/15785719/how-to-print-a-dictionary-line-by-line-in-python
for keys in results:
    print(keys)
    for values in results[keys]:
        print(values,':',results[keys][values])
    print("\n")