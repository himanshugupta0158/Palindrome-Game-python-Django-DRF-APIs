from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import User, Game
from .serializers import UserSerializer, GameSerializer, LoginSerializer
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
import uuid
import random

class UserCreateView(APIView):
    serializer_class = UserSerializer
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        try:
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        try:
            user = User.objects.get(id=request.user.id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)


class UserLogin(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data 
        print(data)
        user = authenticate(username=data["username"], password=data["password"])
        print(user)

        if user is not None:
            login(request, user)
            return Response({"message" : "{} have successfully Logged into Game".format(data["username"])})
        else:
            return Response({'error': 'Invalid username or password'})


class UserLogout(APIView):
    def get(self, request):
        logout(request)
        return Response({"message" : "Logout Successfully from Game."})


class getBoardView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        # Check if an existing game with an empty board and is_completed=False exists for the user
        existing_game = Game.objects.filter(
            user=request.user,
            is_completed=False
        ).first()

        if existing_game:
            # Use the existing game
            existing_game.is_palindrome = False  # Reset the is_palindrome field if needed
        else:
            # Create a new game
            existing_game = Game(
                user=request.user,
                game_id=str(uuid.uuid4()),
                board="",
                is_completed=False,
                is_palindrome=False
            )
            existing_game.save()

        serializer = GameSerializer(existing_game)
        return Response({"Game ID" : serializer.data["game_id"]}, status=status.HTTP_201_CREATED)

def get_random_character():
    characters = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(characters)
    return random.choice(characters)

class UpdateBoardView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if Game.objects.filter(user=request.user,is_completed=False).exists():
            game = Game.objects.filter(
                user=request.user,
                is_completed=False
            ).first()
        else:
            return Response({"Message" : "Please, Create New Game by using getBoard."})

        if len(game.board) == 6 :
            board = game.board
            if board == board[::-1] :
                game.is_completed = True
                game.is_palindrome = True
                game.save()
                return Response({"Congratulations" : "Your Board string is Palindrome, You WON !!!"})
            else:
                game.is_completed = True
                game.is_palindrome = False
                game.save()
                return Response({"Game OVER" : "Your Board string is not Palindrome, You LOSE !!!"})
        else:
            game.board += get_random_character()
            game.save()
            return Response({"Game ID" : game.game_id, "Board String" : game.board})
        
class CombinedUpdateBoardView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if Game.objects.filter(user=request.user,is_completed=False).exists():
            game = Game.objects.filter(
                user=request.user,
                is_completed=False
            ).first()
        else:
            return Response({"Message" : "Please, Create New Game by using getBoard."})
        
        board_length = len(game.board)
        for _ in range(board_length,6-board_length):
            game.board += get_random_character()
            if len(game.board) == 6 :
                board = game.board
                if board == board[::-1] :
                    game.is_completed = True
                    game.is_palindrome = True
                    game.save()
                    return Response({"Congratulations" : "Your Board string is Palindrome, You WON !!!","Game ID" : game.game_id, "Board String" : game.board})
                else:
                    game.is_completed = True
                    game.is_palindrome = False
                    game.save()
                    return Response({"Game OVER" : "Your Board string is not Palindrome, You LOSE !!!", "Game ID" : game.game_id, "Board String" : game.board})
        
class ListGamesView(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        games = {"Game-Info" : []}

        for game in Game.objects.all():
            games["Game-Info"].append({
                # "User" : game.user.id,
                "Game ID" : game.game_id
            })

        return Response(games)
