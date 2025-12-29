import json
import xmlschema # type: ignore
from jsonschema import validate, ValidationError # type: ignore

def schema_validator(schema_path, payload_path, schemaType):
    if schemaType == "json":
        with open(schema_path, 'r') as schema_file:
            schema = json.load(schema_file)
        with open(payload_path, 'r') as payload_file:
            payload = json.load(payload_file)
    else:
        print("Unsupported schema type.")
        
    try:
        validate(instance=payload, schema=schema)
        print("Payload is valid against the schema.")
    except ValidationError as e:
        print(f"Payload validation failed: {e.message}")
