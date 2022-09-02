class settings:
    def __init__(self) -> None:
        self.settings_dict = dict()
        self.settings_dict["eg"] = "nothing"
        self.settings_dict["dump"] = False
        self.settings_dict["file"] = "../data/auto93.csv"
        self.settings_dict["help"] = False
        self.settings_dict["nums"] = 512
        self.settings_dict["seed"] = 10019
        self.settings_dict["seperator"] = ","
        
    def settings_dict_get(self):
        return self.settings_dict

    def settings_dict_set(self,key, value):
        self.settings_dict[key] = value
        print(self.settings_dict[key])