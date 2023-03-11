from configparser import ConfigParser

class Config:
    def __init__(self) -> None:
        self.parser = ConfigParser()

    def config(self,filename='/path/database.ini',section = 'mysql'):
        db = {}
        self.parser.read(filename)

        if self.parser.has_section(section):
            self.params = self.parser.items(section)
            for param in self.params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section,filename))
        
        return db