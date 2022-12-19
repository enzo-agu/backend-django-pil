# Models imports 
from heroes.models import Hero

def error(pk):
    
    try:
        heroe=Hero.objects.get(id=pk)    
        
        return [True, heroe]
    
    except:
        return [False]
    