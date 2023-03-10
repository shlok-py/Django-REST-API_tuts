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
# ModelSerilizer
ModelSerializer class is a shortcut method that lets to create a Serializer class with fields that corresponds to django model automatically.

Create a serializers.py file
`
from rest_framework import serializers
class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = name_of_the_model_you_Want_to_serialize
    fields = [name of the fields required]
    # you can also write fields = '__all__' to select all the fields required
    #also use exclude = [name of the fields] to exclude the field you dont want
`
