import webapp2
import random

def getRandomFortune():
    # list of possible fortunes
    fortunes = [
        "I see much code in your future",
        "Consider eating more fortune cookies",
        "You have tamed the mighty Python, now you must free it onto the Great Spider's Web!"
    ]
    # randomly select one of the fortunes
    index = random.randint(0,2)

    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortune_sentence = "Your fortune: " + fortune
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"

        lucky_num = "<strong>" + str(random.randint(1, 101)) + "</strong>"
        num_sentence = "Your lucky number: " + lucky_num
        num_paragraph = "<p>" + num_sentence + "</p>"

        cookie_again_button = "<a href='.'><button>Another Cookie Plz!</button></a>"

        content = header + fortune_paragraph + num_paragraph + cookie_again_button
        self.response.write(content)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks for trying to log in.")
routes = [
    ('/', MainHandler),
    ('/login', LoginHandler)
]

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
