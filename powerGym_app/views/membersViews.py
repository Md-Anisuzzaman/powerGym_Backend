from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..model.membersModel import Member
from ..serializer.membersSerializer import MemberSerializer,UserRegistrationSerializer
import json
from ..utils import global_response

class MemberListView(APIView):
    def get(self,request):
            try:
                members = Member.objects.all()
                if not members.exists():
                    return global_response(
                        msg ="No members found", status=status.HTTP_404_NOT_FOUND)
                serializer = MemberSerializer(members, many=True)
                return global_response(
                    data = serializer.data, msg="All members fetched successfully", status=status.HTTP_200_OK)
            except Exception as e:
                return global_response(
                    errors = "An error occurred while fetching members.", msg = str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)        
        
    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return global_response(data = serializer.data, msg="Data created successfully",
                            status=status.HTTP_201_CREATED)
        return global_response(errors = serializer.errors, status=status.HTTP_417_EXPECTATION_FAILED)   
    
class MemberDeatilsView(APIView):
    def get(self,request,pk):
            try:
                member = Member.objects.get(pk=pk)
                serializer = MemberSerializer(member)
                return global_response(data =serializer.data, msg = "Single member data provided",
                    status=status.HTTP_200_OK,
                )
            except Member.DoesNotExist:
                return global_response(msg ="Requested member not found", status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return global_response(
                    errors = "An unexpected error occurred.", msg =str(e),status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            # Fetch the Member object by primary key (id)
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return Response(
                {"error": "Requested member not found to update"},
                status=status.HTTP_404_NOT_FOUND,
            )
        # Deserialize and validate the data
        serializer = MemberSerializer(member, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # Save the updated object
            return Response(
                {"message": "Member updated successfully.", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Invalid data.", "details": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
    
    def delete(self, request, pk):
        try:
            member = Member.objects.get(pk=pk)
            member.delete()
            return global_response(msg="Member deleted successfully", status=status.HTTP_200_OK)
        except Member.DoesNotExist:
            return Response({"error": "Requested member not found to delete"}, status=status.HTTP_404_NOT_FOUND)


class MemberRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            member = serializer.save()  # Save the validated data (calls `create` method)
            return global_response( data={"member_id": member.member_id,
                "full_name": member.full_name},msg="User registered successfully", status=status.HTTP_201_CREATED)
        return global_response(errors=serializer.errors,msg="user not create", status=status.HTTP_400_BAD_REQUEST)