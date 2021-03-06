from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import random
from datetime import datetime

class MainHandler(webapp.RequestHandler):
  errors = [400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,500,501,502,503,504,505]
  def get(self):
    opts = self.request.path.split('/')

    odds = 1
    if(opts.count>1):
      if( (opts[1]=="hour") & (datetime.utcnow().hour % 2) ):
        odds = -1
      elif( (opts[1]=="day") & (datetime.utcnow().day % 2) ):
        odds = -1
      elif( (opts[1]=="month") & (datetime.utcnow().month % 2) ):
        odds = -1
      else:
        try:
          odds = int(opts[1])
        except:
           odds = 1

    try:
      err = 500;
      if(int(opts[2]) in self.errors):
        err = int(opts[2])
    except:
      err = random.choice(self.errors)

    if( (odds > 0) & (random.randint(1, max(odds,1)) == 1) ):
      self.response.set_status(err)
      self.response.out.write("<h1>Error: " + str(err) + "</h1><br>\n")
      self.response.out.write('I am indeed amazed when I consider how weak my mind is and how prone to error. ')
    else:  
      self.response.out.write('<h1>Welcome, have some content</h1>I think therefore I am')

    self.response.out.write('<hr><a href="/">Flakey Error-prone Server 0.0</a>')
      

def main():
  application = webapp.WSGIApplication([
    ('/.*', MainHandler)
  ],debug=True)
  util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
