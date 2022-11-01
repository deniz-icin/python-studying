import json
from unicodedata import name


class JSONReader:
    def __init__(self,id,filepath,first_name,last_name,email,password) -> None:
        self.filepath = filepath
        self.content = self.read_json_file()
        self.id= id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def read_json_file(self):
        with open(self.filepath, "r") as f:
            data = json.load(f)
        return data

    def write_json_file(self,content):
        with open(self.filepath, "w") as f:
            json.dump(content, f)
        self.content = self.read_json_file()
    
    def read_all_users(self):
        print(self.content)

    def read_user(self,id):
        if id in self.content[id]:
            return self.content
        return None

    def delete_user(self,id):
        if id in self.content:
            del id
        return None


    def create_user(self,first_name,last_name,email,password):
        pass


    def update_user(self,id,first_name,last_name,email,password):
        if(id in self.content):
            self.content["first_name"] = first_name
            self.content["last_name"] = last_name
            self.content["email"] = email
            self.content["password"] = password
        return None


    def get_by_id (self,id):
        pass

reader = JSONReader("userAPIv1/MOCK_DATA.json")

def test_creating_user():
    """
    JSON reader yarat
    user yarat
    userın id sini al
    read_user yapıp id yi ver
    yarattığın şey ?= verdiğin veri
    """
