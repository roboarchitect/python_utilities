from flask import Flask
import os
from schemaValidation import schema_validator


app = Flask(__name__)

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['GET'])
def checkStatus():
    return 'Active Now!!'

@app.route('/validate', methods=['GET'])
def validate():
    base_dir = os.path.dirname(os.path.abspath(__file__)) +"\\resources"
    print(base_dir)
    schemaType = "json"
    schema_path = os.path.join(base_dir, "jsonSchema.json")
    payload_path = os.path.join(base_dir, "jsonPayload.json")

    result = []
    try:
        schema_validator(schema_path, payload_path, schemaType)
        result.append("Payload is valid against the schema.")
    except Exception as e:
        result.append(f"Payload validation failed: {str(e)}")

    return '\n'.join(result)

if __name__ == '__main__':
    app.run(port=8100)