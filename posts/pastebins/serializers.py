from .models import pastebins
from rest_framework import serializers

class PasteSerializer(serializers.ModelSerializer):
 class Meta:
     model = pastebins
     fields=('id','content','username','created','shared','private','public')