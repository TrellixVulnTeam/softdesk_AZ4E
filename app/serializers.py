from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError
from app import models 

class ProjectSerializer(ModelSerializer):

	class Meta:
		model = models.Project
		fields = ['id', 'title', 'description', 'projet_type']


class ProjectDetailSerializer(ModelSerializer):

	issues = SerializerMethodField()

	class Meta:
		model = models.Project
		fields = ['id', 'title', 'description', 'projet_type', 'issues']

	def get_issues(self, instance):
		queryset = models.Issue.objects.filter(project_id=instance.id)
		serializer = IssueSerializer(queryset, many=True)
		return serializer.data


class IssueSerializer(ModelSerializer):

	comments = SerializerMethodField()

	class Meta:
		model = models.Issue
		fields = ['title', 'description', 'tag', 'priority', 'status', 'assignee_user_id', 'created_time', 'comments']

	def get_comments(self, instance):
		queryset = models.Comment.objects.filter(issue_id=instance.id)
		serializer = CommentSerializer(queryset, many=True)
		return serializer.data


class CommentSerializer(ModelSerializer):

	class Meta:
		model = models.Comment
		fields = ['description', 'author_id', 'created_time']