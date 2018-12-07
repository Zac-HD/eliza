# eliza

A Python project to explore Joseph Weizenbaum's 1966 ELIZA program.
ELIZA was the first ever program that could attempt the Turing test,
and was a landmark in artificial intelligence.

The [Wikipedia page on ELIZA](https://en.wikipedia.org/wiki/ELIZA)
gives a good overview of the history and some context of ELIZA.
The [original ACM paper can be found here](https://dl.acm.org/citation.cfm?id=365168),
and describes how ELIZA works, some of the design choices, and
early reactions to the program.
There is [a website dedicated to the genealogy of ELIZA](http://elizagen.org/),
including links to several ports and an archive of the
[original source code recovered from paper tape]
(https://github.com/jeffshrager/elizagen/tree/master/doctor_bbn_lisp_1966).

----------------

`simpleliza.py` is a much simpler, "inspired by", chatbot with only
one layer of matching and substitution but no context or memory.

`ELIZA.py` is an unfinished implementation based on the 1966 paper;
the only really useful part is `parser.py`... but investigating the
archive above shows that the published script (see `DOCTOR.txt`) used
a different dialect, presumably compatible with the long-vanished
[MAD](https://en.wikipedia.org/wiki/MAD_(programming_language\))
-[SLIP](https://en.wikipedia.org/wiki/SLIP_(programming_language\))
language.
