# Rest imports
from urllib import request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Models imports 
from heroes.models import Hero

# Serializers imports 
from heroes.serializer import HeroSerializer

#Helpers
from heroes.helpers.heroeErrors  import error

# Create your views here.


class HeroApiView(APIView):
    
    def get(self,request):
        """Retorna lista heroes almacenados"""
        
        heroes=Hero.objects.all()
        heroes_serializer= HeroSerializer(heroes, many=True)
        
        return Response(
            data=heroes_serializer.data,
            status=status.HTTP_200_OK
            )
        
    
@api_view(['GET'])
def hero_api_view(request):
        heroes=Hero.objects.all()
        heroes_serializer= HeroSerializer(heroes, many=True)
        
        return Response(
            data=heroes_serializer.data,
            status=status.HTTP_200_OK
            )
    
        
        
def post(self, request):
        
        """Crea registro/heroe"""
        print("PRIMER POST")
        
        serializer=HeroSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            data={
                 'mens':'Heroe creado correctamente'
            }
            return Response(
               data=data,
            status=status.HTTP_201_CREATED
             )
            
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
            
            
        
class ModificarHeroeApiView(APIView):
    def put (self, request,id):
        pass
    
class DeleteHeroeApiView(APIView):
    
    def delete(self, request, id):
        pass

    
class CreateHeroApiView(APIView):
    
    def post(self, request):
        
        """Crea registro/heroe"""
        print("SEGUNDO POST")
        
        serializer=HeroSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            data={
                 'mens':'Heroe creado correctamente'
            }
            return Response(
               data=data,
            status=status.HTTP_201_CREATED
             )
            
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class HeroDetailApiView(APIView):
    
    
    
    def get(self,request,pk):
        """Devuelve info de un heroe particular"""
        
        try:
            
           heroe=Hero.objects.get(id=pk)

           heroe_serializer= HeroSerializer(heroe)
        
           return Response(
            data=heroe_serializer.data,
            status=status.HTTP_200_OK
            )
        except:
            data={
                'message':'Heroe no encontrado'
            }
            return Response(
                data=data,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    
    def put(self,request,pk):
        """Modifica registros"""
        
        heroe = error(pk)
        
        # heroe=Hero.objects.get(id=pk)
        if heroe[0]:
        
          heroe_serializer= HeroSerializer(heroe[1], data=request.data)
        
          if heroe_serializer.is_valid():
               
            heroe_serializer.save()
            data={
                 'mens':'Heroe modificado correctamente'
            }
        
            return Response(
            data=data,
            status=status.HTTP_200_OK
            )
        return Response(
            data=heroe_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        

    
    def delete(self,request,pk):
        """elimina registros"""
        
        heroe=Hero.objects.get(id=pk)
        heroe.delete()
        
        data={
                 'mens':'Heroe eliminado correctamente'
            }
        
        return Response(
            data=data,
            status=status.HTTP_200_OK
            )
        
        
@api_view(['GET','PUT','dELETE'])
def hero_detail_api_view(request,pk):
    
    # Detail
    if request.method == 'GET':
        try:
            
           heroe=Hero.objects.get(id=pk)

           heroe_serializer= HeroSerializer(heroe)
        
           return Response(
            data=heroe_serializer.data,
            status=status.HTTP_200_OK
            )
        except:
            data={
                'message':'Heroe no encontrado'
            }
            return Response(
                data=data,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    # Update
    elif request.method == 'PUT':
        heroe = error(pk)
        
        # heroe=Hero.objects.get(id=pk)
        if heroe[0]:
        
          heroe_serializer= HeroSerializer(heroe[1], data=request.data)
        
          if heroe_serializer.is_valid():
               
            heroe_serializer.save()
            data={
                 'mens':'Heroe modificado correctamente'
            }
        
            return Response(
            data=data,
            status=status.HTTP_200_OK
            )
        return Response(
            data=heroe_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
    # Delete
    elif request.method == 'Delete':
        heroe=Hero.objects.get(id=pk)
        heroe.delete()
        
        data={
                 'mens':'Heroe eliminado correctamente'
            }
        
        return Response(
            data=data,
            status=status.HTTP_200_OK
            )
        
    
    