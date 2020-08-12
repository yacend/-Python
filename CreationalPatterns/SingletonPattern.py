class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

if __name__ == "__main__":
    s = Singleton()
    s1 = Singleton()
    print(id(s), id(s1))
    print(s is s1)