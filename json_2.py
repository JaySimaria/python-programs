# Json 2 program
import json
json_input='[person{"name":"yamini","city":"banglore"),{"name":"parita","city":"pune"}]}'
try:
    decorded=json.loads(json_input)
    for x in decorded['person']:
        print (x['city'])    
except(KeyError,ValueError,TypeError):
    print("JSON format error")
    # json data display
    import json
    json_data='{"name":"yamini","city":"ahmedabad"}'
    python_obj=json.loads(json_data)
    print (json.dumps(python_obj,sort_keys=true,indent=4))
    # display in real json syntax indent will give spacce to string
