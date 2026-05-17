class Database:
    _instance = None

    def __init__(self):
        print("constructor")

    def __new__(cls):
        if cls._instance is None:
            print("creating instance")
            # Parent class here is Python’s built-in object class.
            cls._instance = super().__new__(cls)
        return cls._instance

db_instance = Database()
