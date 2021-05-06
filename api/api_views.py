from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ApplicationsSerializer
from bboard.models import Applications

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class ApplicationsListApiView(ListAPIView):
    
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ApplicationsSerializer
    queryset = Applications.objects.all()


class ApplicationDetailApiView(RetrieveAPIView):

    serializer_class = ApplicationsSerializer
    queryset = Applications.objects.all()
