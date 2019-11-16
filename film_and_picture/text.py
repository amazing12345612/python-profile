# import random
# c = string.ascii_letters
# infos = []
# for i in range(50):
#     infos.append(random.choice(c))
# # a = [j for i, j in enumerate(infos) if i % 2 == 0]
# b = [ i for i,j in enumerate(infos) if i % 2 == 0]
# print(infos)
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "hello world"
app.run()