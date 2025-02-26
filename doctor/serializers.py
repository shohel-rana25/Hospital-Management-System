from rest_framework import serializers
from .models import DoctorModel
from .models import DesignationModel
from .models import SpecializationModel
from .models import ReviewModel
from .models import AvailableTimeModel


class DoctorSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(many=False)
    designation=serializers.StringRelatedField(many=True)
    specialization=serializers.StringRelatedField(many=True)
    available_time=serializers.StringRelatedField(many=True)

    class Meta:
        model=DoctorModel
        fields='__all__'

        
class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=DesignationModel
        fields='__all__'

        
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model=SpecializationModel
        fields='__all__'

class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=AvailableTimeModel
        fields='__all__'


class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReviewModel
        fields='__all__'

