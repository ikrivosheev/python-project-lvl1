from . import calc
from . import even
from . import gcd
from . import prime
from . import progression

EVEN_GAME = (even.HEADER, even.game_step)
CALC_GAME = (calc.HEADER, calc.game_step)
GCD_GAME = (gcd.HEADER, gcd.game_step)
PRIME_GAME = (prime.HEADER, prime.game_step)
PROGRESSION_GAME = (progression.HEADER, progression.game_step)
