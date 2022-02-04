from django.shortcuts import render
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status
from rest_framework import viewsets

class EmployeeViewSet(viewsets.ViewSet):
	def list(self,request):
		print("***** List *****")
		print("Basename:",self.basename)
		print("Action:",self.action)
		print("Detail:",self.detail)
		print("Suffix:",self.suffix)
		print("Name:",self.name)
		print("Description:",self.description)

		emp=Employee.objects.all()
		serializer=EmployeeSerializer(emp,many=True)
		return Response(serializer.data)

	def retrieve(self,request,pk=None):
		print("***** Retrieve *****")
		print("Basename:",self.basename)
		print("Action:",self.action)
		print("Detail:",self.detail)
		print("Suffix:",self.suffix)
		print("Name:",self.name)
		print("Description:",self.description)
		id=pk
		if id is not None:
			emp=Employee.objects.get(id=id)
			serializer=EmployeeSerializer(emp)
			return Response(serializer.data)

	def create(self,request):
		print("***** Create *****")
		print("Basename:",self.basename)
		print("Action:",self.action)
		print("Detail:",self.detail)
		print("Suffix:",self.suffix)
		print("Name:",self.name)
		print("Description:",self.description)
		serializer=EmployeeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Data is created'},status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def update(self,request,pk):
		print("***** Update *****")
		print("Basename:",self.basename)
		print("Action:",self.action)
		print("Detail:",self.detail)
		print("Suffix:",self.suffix)
		print("Name:",self.name)
		print("Description:",self.description)
		id=pk
		emp=Employee.objects.get(pk=id)
		serializer=EmployeeSerializer(emp,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Complete Data Updated'})
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def partial_update(self,request,pk):
		print("***** Partial Update *****")
		print("Basename:",self.basename)
		print("Action:",self.action)
		print("Detail:",self.detail)
		print("Suffix:",self.suffix)
		print("Name:",self.name)
		print("Description:",self.description)
		id=pk
		emp=Employee.objects.get(pk=id)
		serializer=EmployeeSerializer(emp,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':'Partial Data Updated'})
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

	def destroy(self,request,pk):
		print("***** Destroy *****")
		print("Basename:",self.basename)
		print("Action:",self.action)
		print("Detail:",self.detail)
		print("Suffix:",self.suffix)
		print("Name:",self.name)
		print("Description:",self.description)
		id=pk
		emp=Employee.objects.get(pk=id)
		emp.delete()



		return Response({'msg':'Data is Deleted'})

