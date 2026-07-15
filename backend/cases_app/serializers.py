from rest_framework import serializers
from .models import Case

class CaseSerializer(serializers.ModelSerializer):
    responsible_lawyer_name = serializers.CharField(
        source="responsible_lawyer.get_full_name", read_only = True
    )

    class Meta:
        model = Case
        fields = [
            "id",
            "reference",
            "client",
            "opponent",
            "area_of_law",
            "responsible_lawyer",
            "responsible_lawyer_name",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]