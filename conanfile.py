from conans import ConanFile
from conans.tools import download, unzip


class NLJsonConan(ConanFile):
    name = "nlJson"
    version = "2.0.8"
    url = "https://github.com/arnemertz/conan-nlJson.git"
    license = "MIT"
    author = "Arne Mertz (arne-mertz.de/contact-me)"
    settings = None  # header only
    options = {"path": "ANY"}
    default_options = "path="

    def source(self):
        download("https://github.com/nlohmann/json/releases/download/v%s/json.hpp" % self.version, "json.hpp")

    def build(self):
        del self  # header only

    def package(self):
        header_dir = "include"
        if self.options.path != "":
            header_dir += "/" + str(self.options.path)
        self.copy("*.hpp", dst=header_dir)

