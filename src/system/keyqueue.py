'''This module contains class KeyQueue.
'''


class KeyQueue(object):
    '''Keyqueue class provides method to only allow non-duplicated values.
    This class is mainly used to prevent user press multiple keys at the
    same time.
    '''
    _keys = list()
    _size = 5

    @classmethod
    def _is_key_allowed(cls, key):
        '''Check whether the key is allow to enter the queue.
        '''
        if key in cls._keys:
            return False

        return True

    @classmethod
    def pursh_key(cls, key):
        '''Add the key to the queue. Only non-duplicated key can be addedd.
        '''
        if len(cls._keys) <= cls._size:
            if cls._is_key_allowed(key):
                cls._keys.append(key)

    @classmethod
    def clean_keys(cls):
        '''Remove all keys in the queue.
        '''
        cls._keys[:] = []

    @classmethod
    def remove_key(cls, key):
        '''Remove one specific key in the queue.
        '''
        del cls._keys[cls._keys.index(key)]

    @classmethod
    def get_keys(cls):
        '''Get all keys.
        '''
        return tuple(cls._keys)
