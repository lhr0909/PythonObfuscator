import os, sys, cyclone.web
import pyobf
from twisted.python import log
from twisted.internet import reactor

class IndexHandler(cyclone.web.RequestHandler):
    def get(self):
        self.render("index.html", original="", obfuscated="", originalLen=0, obfLen=0)

    def post(self):
        string = self.get_argument("original", None)
        obf = pyobf.Obfuscator(string)
        obfuscated = obf.build_simple()
        self.render("index.html", original=string, obfuscated=obfuscated, originalLen=len(string), obfLen=len(obfuscated))


class Application(cyclone.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
        ]

        settings = {
            "debug": True,
            "static_path": "./static",
            "template_path": "./template",
            }

        cyclone.web.Application.__init__(self,
            handlers, **settings)

if __name__ == "__main__":
    log.startLogging(sys.stdout)
    port = int(os.environ.get('PORT', 5000))
    reactor.listenTCP(port, Application())
    reactor.run()
