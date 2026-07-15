from rest_framework import viewsets
from .models import Case
from .serializers import CaseSerializer


class CaseViewset(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    http_method_names = ["get", "post", "patch", "head", "options"]

