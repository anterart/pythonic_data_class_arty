import copy


class Data:
    DEFAULT_VALUE = 100

    def __init__(self, **kwargs):
        self.__internal_dict = kwargs
        self.__attr_map = dict()

        for k, v in kwargs.items():
            if isinstance(v, dict):
                v = self.from_dict(v)
                self.__attr_map.update(v.__attr_map)
            else:
                self.__attr_map[k] = v
            setattr(self, k, v)

    @classmethod
    def from_dict(cls, d):
        d = copy.deepcopy(d)
        new_d = Data(**d)
        new_d.__internal_dict = d
        return new_d

    def __getattr__(self, attr_name):
        if attr_name in self.__attr_map:
            return self.__attr_map[attr_name]

        setattr(self, attr_name, self.DEFAULT_VALUE)
        self.__internal_dict[attr_name] = self.DEFAULT_VALUE
        self.__attr_map[attr_name] = self.DEFAULT_VALUE

        print(attr_name)
        return self.DEFAULT_VALUE

    def to_dict(self):
        return self.__internal_dict

    def __repr__(self):
        return str(self.__internal_dict)

