import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        data = toml.loads(content)
        
        authors = []

        for author in data["project"]["authors"]:
            authors.append(author["name"])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            data["project"]["name"],
            data["project"]["description"],
            data["project"]["license"],
            authors,
            data["project"]["dependencies"],
            data["dependency-groups"]["dev"]
    )
   
