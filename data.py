
class Data:
    DEFAULT_VALUE = 10

    def __init__(self, **kwargs):
        self.__data = kwargs
        self.__internal_dict = kwargs
        for k, v in kwargs.items():
            if isinstance(v, dict):
                v = self.from_dict(v)
            setattr(self, k, v)

    @classmethod
    def from_dict(cls, d):
        new_d = Data(**d)
        new_d.__internal_dict = d
        return new_d

    def __getattr__(self, name):
        setattr(self, name, self.DEFAULT_VALUE)
        self.__internal_dict[name] = self.DEFAULT_VALUE
        return self.DEFAULT_VALUE

    def to_dict(self):
        return self.__internal_dict

