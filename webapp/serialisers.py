from rest_framework import serializers
from .models import employees

class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        #fields =('firstname','lastname')
        fields = '__all__'


# serialize a class that is used to convert your model to your JSON data
# serializer coverts python dictionary data into json formate data.
# when we dont want data from server in Html formate we want in json fromate we have to use serializer
