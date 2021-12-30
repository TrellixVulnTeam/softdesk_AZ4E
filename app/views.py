from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from app import models, serializers

class SignUp(APIView):

	def get(self, request):
		content = {
			"username":"xxxxxxx",
			"password":"xxxxxxx",
			"password2":"xxxxxxx",
			"email":"xxxxxxx",
			"first_name":"xxxxxxx",
			"last_name":"xxxxxxx",
		}
		return Response(content)

	def post(self, request):
		serializer = serializers.SignUpSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContributorProject(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, project_id):
		try:
			print("11111111111111111")
			project = models.Project.objects.filter(id=project_id)
			print("2222222222222222222222")
			if project.count() != 0:
				contributors = models.Contributor.objects.filter(project_id=project_id)
				if contributors.count() != 0:
					serializer = serializers.ContributorSerializer(contributors, many=True)
					return Response(serializer.data)
				content = {"detail":"Project has no contributors"}
				return Response(content, status=status.HTTP_404_NOT_FOUND)
			else:
				content = {"detail":"Not found project with this id"}
				return Response(content, status=status.HTTP_404_NOT_FOUND)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)


	def post(self, request, project_id):
		try:
			project = models.Project.objects.filter(id=project_id)
			if project.count() != 0:
				if request.user.username == 'admin':
					serializer = serializers.AddContributorSerializer(data=request.data)
					if serializer.is_valid():
						serializer.save()
						return Response(serializer.data, status.HTTP_201_CREATED)
					return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
				else:
					content = {"detail":"only admin acount can add new contributors"}
					return Response(content)
			else:
				content = {"detail":"Not found project with this id"}
				return Response(content, status=status.HTTP_404_NOT_FOUND)

		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, project_id):
		try:
			project = models.Project.objects.filter(id=project_id).count()
			if project.count() != 0:
				if request.user.username == 'admin':
					contributor_deleted = models.Contributor.objects.filter(project_id=project_id).filter(
					user_id=request.data['user_id'])
					if contributor_deleted.count() != 0:
						contributor_deleted.delete()
						content = {"detail": f"contributor user_id {request.data['user_id']} deleted"}
						return Response(content)
					else:
						content = {"detail":"No found contributor with this id"}
						return Response(content, status=status.HTTP_404_NOT_FOUND)
				else:
					content = {"detail":"only admin acount can delete contributors"}
					return Response(content)
			else:
				content = {"detail":"Not found project with this id"}
				return Response(content, status=status.HTTP_404_NOT_FOUND)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)


class Project_list(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, format=None):
		projects = models.Project.objects.all()
		serializer = serializers.ProjectSerializer(projects, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = serializers.ProjectSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(author_user_id=request.user)
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Project_detail(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request, pk):
		try:
			project = models.Project.objects.get(pk=pk)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = serializers.ProjectDetailSerializer(project)
		return Response(serializer.data)

	def put(self, request, pk):
		try:
			project = models.Project.objects.get(pk=pk)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = serializers.ProjectSerializer(project, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		try:
			project = models.Project.objects.get(pk=pk)
		except:
			return Response(status=status.HTTP_404_NOT_FOUND)
		content = {"detail":f"Projet {pk} deleted"}

		project.delete()
		return Response(content, status=status.HTTP_204_NO_CONTENT)


class Issue_list(APIView):

	permission_classes = [IsAuthenticated]

	def get(self, request):
		issues = models.Issue.objects.all()
		serializer = serializers.IssueSerializer(issues, many=True)
		return Response(serializer.data)


