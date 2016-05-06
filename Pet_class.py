class Pet:
    def __init__(self):
        self.__name = "name"
        self.__type = "type"
        self.__age = "age"


    def get_name(self):
        return self.__name
    def get_type(self):
        return self.__type
    def get_age(self):
        return self.__age

    def set_name(self, new_name):
        self.__name = new_name
    def set_type(self, new_type):
        self.__type = new_type
    def set_age(self, new_age):
        self.__age = new_age


def main():

    my_Pet = Pet()
    my_Pet.set_name(input('Name of animal:'))
    print(my_Pet.get_name())
    my_Pet.set_type(input('What type of animal is it:'))
    print(my_Pet.get_type())
    my_Pet.set_age(input('How old is your animal:'))
    print(my_Pet.get_age())

main()
