# SauterTaper

SauterTaper is the twin input method of JumpType for French.

Online [Demo](https://jumptype.netlify.app/)

## encoding rules

~~the encoding is based on CMU French pronunciation dictionary (there are several difference, e.g. for English `ch` is affricative as in `change` while fricative for French, and all phonetics are represented in two letters)~~

the encoding is based on [Lexique383](http://www.lexique.org/databases/Lexique383/) dataset, its github page [here](https://github.com/chrplr/openlexicon). The encoding rules are the same but they used a different phonology representations. I'm lazy to redraw the encoding table.

|      stop       |    fricative    |          nasal          |   approximant   |
| :-------------: | :-------------: | :---------------------: | :-------------: |
| pp(`p`)/bb(`b`) | ff(`f`)/vv(`v`) | mm(`m`)/nn(`n`)/gn(`n`) | ll(`l`)/rr(`r`) |
| tt(`t`)/dd(`d`) | ss(`s`)/zz(`z`) |                         |     ww(`w`)     |
| kk(`k`)/gg(`g`) | ch(`c`)/jj(`j`) |                         | yy(`y`)/uy(`u`) |

Besides, we use `a` as plural encoding and `i` for nasal vowels.
