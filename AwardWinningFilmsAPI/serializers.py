from rest_framework_mongoengine import serializers
from AwardWinningFilmsAPI.models import Awardwinningfilms

class AwardwinningfilmsSerializer(serializers.DocumentSerializer):
    
    class Meta:
        model = Awardwinningfilms
        fields = '__all__'

