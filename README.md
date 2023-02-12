# Django-REST-API_tuts
I learned Django rest API through Django and REST API docs.

# Deserialization
Deserialization is the process of converting the data back into complex python object after validating it.<br>

## BytesIO
A stream implementation using an in-memory bytes buffer. It inherits BufferedIOBase. The buffer is discared when close() is called.

`
import io
stream = io.BytesIO(json_data)
`

## JSONParser()

`
from rest_framework.parsers import JSONParser
parsed_data = JSONParser().parse(stream)
`

### Deserialization

StepI: Create a Serializer Object <br>
`
serializer = Serializer_model_name(data = parsed_data)
`<br>
Step II: Validated data 
<br>
`
serializer.is_valid()
#get valid data from
serializer.validated_data()
#gives the errors
serializer.errors
`
