from rest_framework.generics import (
	CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
)
from .serializers import (
	UserCreateSerializer, CreateUpdateProfileSerializer,
	RecipeDetailsSerializer, RecipesListSerializer, IngredientSerializer
	 )
from .models import Recipe, Profile, Ingredient
from rest_framework.permissions import IsAuthenticated


class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer


class ProfileView(RetrieveUpdateAPIView):
	serializer_class = CreateUpdateProfileSerializer
	permission_classes = [IsAuthenticated]

	def get_object(self):
		return Profile.objects.get(user=self.request.user)


class RecipeListView(ListAPIView):
	queryset = Recipe.objects.all()
	serializer_class = RecipesListSerializer
 

class RecipeDetailsView(RetrieveAPIView):
	queryset = Recipe.objects.all()
	serializer_class = RecipeDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'recipe_id'


class IngredientsListView(ListAPIView):
	queryset = Ingredient.objects.all()
	serializer_class = IngredientSerializer


class RecipesByMealListView(ListAPIView):
	serializer_class = RecipesListSerializer

	def get_queryset(self):
		return Recipe.objects.filter(meal__name=self.kwargs['meal_type'])	

 