import logging
from lol import *
class My_Test(unittest.TestCase):
def test_args(self):
 self.assertEqual(adder(2, 2), 4)
 logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log", filemode="a",
                    format="We have next logging message: "
                    "%(asctime)s:%(levelname)s-%(message)s")

logging.basicConfig(level=logging.DEBUG)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
try:
   print(10/0)
except Exception:
   logging.exception("Exception")

assert 2+2 == 5, "wrong assert uslovie nepravilno"

def adder(*args, **kwargs):
result = 0
for _ in args:
  if type(_) == int or type(_) == bool or type(_) == float:
  result += _
  else:
  try:
  result += float(_)
  continue
  except (ValueError, TypeError):
  pass
  try:
class My_Test(unittest.TestCase):
    def test_args(self):

            self.assertEqual(adder(2, 2), 4)


    def test_kwargs(self):
        self.assertEqual(adder(a=10, b=11), 21)


    def test_mixed(self):
        self.assertEqual(adder(1, a=2), 3)


    def test_diff(self):
        x = 10