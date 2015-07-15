from entities.enum import *

class KeyQueue(object):
    _keys = list()
    _size = 5
    
    @classmethod
    def _is_key_allowed(cls, key):
        if key in cls._keys:
            return False
            
        return True
            
    @classmethod
    def pursh_key(cls, key):
        if len(cls._keys) <= cls._size:
            if cls._is_key_allowed(key):
                cls._keys.append(key)
    
    @classmethod
    def clean_keys(cls):
        cls._keys[:] = []
    
    @classmethod
    def remove_key(cls, key):
        print cls._keys
        del cls._keys[cls._keys.index(key)]
        
    @classmethod
    def get_keys(cls):
        if len(cls._keys) == 0:
            return ()
        
        if len(cls._keys) == 1:
            return (cls._keys[0])
        
        if len(cls._keys) == 2:
            return (cls._keys[0], cls._keys[1])