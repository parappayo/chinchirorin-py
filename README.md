# chinchirorin-py

Chinchirorin (aka Cee-lo) is a simple dice game, popular among Suikoden RPG fans.

# Usage

Requires Python 3.6+

From the cli try `python3 chinchirorin.py`

Alternatively, `python3 dice.py 3 6`

# Rules

Two players roll off and the higer score wins. Ties are possible. Many players can play simultaneously against the bank, similar to a Blackjack table.

Roll 3 dice into a bowl and score as follows:

* A roll of 4-5-6 is the best roll, beats all rolls below.
* Three dice matching beats two dice matching.
* When two dice match, the score is the value of the other (singleton) die.
* If none of the other rules apply, the roll scores 0.
* A roll of 1-2-3 is the worst roll, loses to all rolls above.
* If any dice leave the bowl, it is an automatic loss. (Not implemented here.)

# References

* [Suikoden Fan Wiki](https://suikoden.fandom.com/wiki/Chinchirorin)
* [Wikipedia](https://en.wikipedia.org/wiki/Cee-lo)
