class Singleton(object):
    
    reunion = None
    carrera = None

    def instance():
        if '_instance' not in Singleton.__dict__:
            Singleton._instance = Singleton()
        
        return Singleton._instance