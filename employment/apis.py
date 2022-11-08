from rest_framework.views import APIView
from rest_framework import serializers

'''
    Naming convention:
    <Entity><Action>Api
    Examples: UserCreateApi, UserSendResetPasswordApi, UserDeactivateApi
    
    Class-based or Function-based Apis?
    1. Pick class-based APIs/vies by default
'''
class EmployeeCreateApi(APIView):
    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField()
        middle_name = serializers.CharField()
        last_name = serializers.CharField()
        
    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        #TODO: finish up post