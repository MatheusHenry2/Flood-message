import time
from pynput.keyboard import Key, Controller
import random

messages = ["eai silas malafaio", "tem algum boca aberta aqui?", "eai caraguatatubo", "que isso delicio", "fica bravo não cnpjoto"
            , "eai sandalio", "eai ludmilo", "que isso claudio arraio", "aqui é peri", "eai margarido", "salve gasolino", "eai tigreso"
            , "eai calabreso", "salve prexeco", "eai trembolono", "fala creatino", "fala lombrigo", "eai princeso", "eai aeromoço",
            "que iso prostituto", "me arrebente delicio", "que isso lesmo", "eai macaxeiro", "eai borboleto", "eai tadalafilo", 
            "eai xoxoto", "fica bravo não sonho de valso", "que isso carniço", "se der 5 minutos em mim", "eai lesbico", "valeu ai glutamino", "eai asthetico"
            "aqui é gueto", "o dilatafilo", "pé de breque", "eai lacraio", "mo cara de boca aberta mano", "aqui é quebrada irmao, aqui é peri", 
            "aqui é pitango", "eai jiboio"]

keyboard = Controller()

time.sleep(5)

for num in range(200):
  var = random.randint(0, len(messages) -1)
  for letter in messages[var]:
    keyboard.press(letter)
    keyboard.release(letter)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  time.sleep(0.1)
