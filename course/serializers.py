from .models import Student
from course import serializers
class StudentSerializers(serializers.HyperlinkedModelSerializers):
    class Meta:
        model:Student
        fields('names','course','description','registration_date','graduation_date')