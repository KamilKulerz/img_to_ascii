# Image to ascii converter

Simple converter that takes grayscale png image and converts it to visual text representation.

To make translation:

- initialize AsciiGrayscaleImageTranslator with desired translation_table
- initialize AsciiGrayscaleImageHandler with AsciiGrayscaleImageTranslator
- handler translates on initialization
- save file to .txt with selected vertical spacing

---

## Examples of result:

### Input:

![alt text](./img_to_ascii/input/lena1.png "Title")

---

### Translation table:

```
" :=*%"
```

### Output:

```
=====::   : :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::=====================*%%%%=:::::::::::::
=====::   :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::=======================%%%%%:::::::::::
=====::   :: :::  :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::========================*%%%%*:::::::
=====::   :::::: ::::::::::::::::::::::::::::::::::===:::::::::::::::::::::::::::::=========================*%%%%=::::
=====::    :: :::::::::::::::::::::::::::=:==========*==*****=::::::::::::::::::::::==================:::===:*%%%%*:
=====::         ::::::::::::::::::====:::::::=========*=*********::::::::::::::::::====:============:==========%%%*
=====::         ::::::::::::::::::::::::::::::::=====***************:::::::::::::::======:=::===================*:
=====::        ::::::::::::::::=:::::::::::::::::=====******%*%****%%%%% :::::: :::======:::::========::=======
=====::        :::::::::::::::::::::::::::::::=::::===******==%%%%%%%%%%%   ::  :::======::  ::=======:=:====:
=====::       ::::::::::::::::::::::::::::::==========**==%*%%%%%%%%%%%%%%*     :::=======:    :=======:====
=====::          ::::::::::::::::::::::::::::=:::::===****%%**%%%%%%%%%%%%%%%:   ::=======:     ::===:====:
=====::          :::::::::::::::::::::::==:==::::::=**%******%*%%*%%%%%%*%%%%%%:  :======::       ::=::==:                :
=====::          ::::::::*: :::::::::::::::::::::=*****==******%%%***%%*%%%%%%%%  :=======:       %%**%%*                :=
=====::           ::::: %=::::::::::::::::::::=**==*=**=*****%*****%%*%*%%%%%%%%%=::======:    %==%%%%%%%*              ==:
=====::        :::::::::*::::: ::::::::::::=*===*=====***=************%*=%%%**%%%%%:=====::*%**%%%%%%%%%%=            :====
=====::    : ::::::::::%=::::::::::::::::=====:===*====*==*****=*********************==*%***%%**%*%%%%%%%            :=====
=====::        :: :::: %*::::: :::::::::=:=:========*==*=***===*************=****==*****%%******%%%**%%%:          :=======
======:       :  : :: :*==:::::::::::====:====:==========*=*==*=**=******=***=*==%***%%***********==*=*%          :========
======:      : :  :::  *====::::: =:::=::====::=======*=====*======*=========*==*%%***********%%===:==*          :=========
======:        ::  :: *%*===:=: :::::::::::::=:====:::====:=============:**=***********%*%%%%%%==:  :%=         :==========
======:      ::: :::: =%***:==::::::::::::::::====::    :==:::         %=*************%*%*%**:    :*%          :===========
======:          :  :  %***=::::::::::::::::::::::::     ::::   :   *:******************=     :=**%           :============
======:    :   :: : :  %%*==::*:::::::::::::::::       ::         *:=****************: :::======*            :=============
======:         : ::::: %%*=*::::::::::::=::               :    ==*******==******=   : =::===*=             :::============
======:        : : ::::::****:=::::::::  :                 : := =****=*==*=********:    ::::                :::============
======:          :::::::: %%*::::::::::                      =:****===**=****%*****=:    :=:              :::==============
======::    ::::  ::::::::%%::::::::::              =    =:*==:=**======******%*%%%*=     =:              :::==============
======:         : :::::::::=:::::::                  : =:==***:=*======******%%%%%%**:    =:             :::===============
======:     : ::: :::::::::  :::::                     *====**=======**********%*%%**=     =            :::===============:
======:      :  :: :::::=:   =*      :              ::=**==**:===::  :=***********=:       =:          :::=================
======:        :: : ::====*==:   :                 :==*****         :=::===****=::         =:          =:==================
=======:       :   =*:===::   :    :             =:==****        *=   :::==*%*     :       ==         ::===================
===*==::    :::::   :*%=           :            ===****::::: :: *%%==::::==%%:::  *:       =*        :::===================
==**==::   :::: ==::=    : :    ::::           :===*: ::========:=====::::=%%*==::::       :*        ::=================:::
==**===:   :::::::      :      : :  =         :**** :::====*=*=========:::=*%**===::::      =:      :::==============:=::=*
==*====:   :::::         :           :      =:***   ::::====*******=====::=*%%====::::      ==      ::==============:=::=**
======::   :::::: : :   :            : :   ::***    ::::=====****=====:=::==*%=====::       =::    ::================::=***
======::  ==::: :::   :::        :  :*:   ::**:     ::::=============::::::=*%%===:::       :::   :::=============:::=*****
=======:  : ::   :     :::       :       ==:==      :::::============::===:==%*==:::         =:   ================:::=****%
=======:   :::   :  :  : : =      :     :===      : :::::=============::::::**==:::          =:  :================::=****%%
=======:    :=    :    :: =:        ::*  *        :::::::================*=**===:::          == :=================::****%%%
=======:   : :  :         ::::    :==*: *         : ::::::===:==========*%*%**::::           :=:================:=::**%%%%%
===**==:  : ::        :      : *:***  =           :  ::::::====:  ::::   ::: ::=              ===================::=*%%%%%%
===*===::  =   :      :  :   ::=:=::==               ::::::::====:::::=====:==:               :==================::=%%%%%%%
=======:  = :        *:     := =:=:=                   :::::::===::::=::===:=          :      :=================:::=%%%%%%%
===*===:  :          =:==::  : : *                       :::::==============:          :      :=:============::::::=%%%%%%%
=======:      :      =:   ::::=                             ::::===========:           :       =:::=:=======:::::::*%%%%%%%
=======: * :         ::   ::: =: =:                      :::=:==:=========***          :      :=::  ::::::::::::::=%%%%%%%*
========               ::::=  ::::= *                    ::::::==========*********:           ==:::::::: :     :: =*%*%%%**
=======:           :    :::= :: :: =                     :::::::=========*******%%%**         =:===:::::::::: ::: *%%%%**=
========:                    : ::== =                    ::::=:===========*******%%%%%%       :===:==:::::::::::::%%%%%*=
========:          :           : ::=  **             ::  ::::=::============*****%%%%%%%%    ==:======:::::::::==*%%%%*=:
====*==:           :     :   :   ===   %            :::   :::=:==============*****%%%%%%%%   ========:=::::::=*%*%%%%*=:  :
===**==:          :           :  ===  ===           :::  :::=================******%%%%%%%*  :======:::::::::*%%%%%%*=::: :
=======:          :            ::::::===:          ::::  ::=:====::===========*****%%%%%%%%  ======:=:::::::=*%%*%%%=:::  :
=======:                      : :::::              :::  :::========:===========****%%%%%%%%% =========:::::::==**%**:::::
=======::                        :   :*          ::::: ::=======================****%%%%%%%%*:   :::::::=====::*%%*=::
=======::                     ::    *           :::::  ::::======================****%%%%%%%%             ::*==%%*::      :
=======::                      :=:::           ::::  ::=:=========================*****%%%%%%%  :         :**=***:
```

---

### Translation table:

```
""" .\'`^~+_-?][}{1)(rxnuvczQ0OZmwqo*#M%B@$"""
```

### Output:

`````
unxx(1?~++?_-----?-][}}{{1{1{{{{{{{{1{{11}1{{{{{}}}}}}{}{{{1{{{{}1}{}}}}{}}[[????]1rxnnnxxxxxxxrxxxxrrr(OoMMou??-][[[}[[{}}
xxxr({?~~+_---__---?[[[[{}}}{}}{}}{{}}{}}}}{}}}[[[[}}[][}}}}{{}}}{}}}}[[}}}]]]?-?]1(rxxxrrxxxrrxrrxxrr(r(xq#MMq?-?]]][][[[^
rrrr({?+~~__+--_++?-?]]]][[[}}[}}}{{}}}{}[[[}}}[][[}[[[[[}}[}[}}}}}}}}[}}[[[]]]??]{1)(rrrrrrrrrrrr(rr(()()rO#%%oz---?]}?~
xrrr({-~~+______+--??][[[[[[}}[{}}}}}}}}}[}}}[[][[1()r[]?]][[[}}[}}[[[}[}[[]]]??-?}))1((rrrrr((rxrrr)))11))(m*MM*x-_?-^.  .
xxxr({?~^++__+-----?]][[[}}[[[}}{}}}}}{}}11()1)xxnxuucuvcccQ0u]][][[[[]][}[[[???-?}1)))))(((((((((()))11{)))1zwMMMQ]`......
xuxr({?+^+++___+-_??]]][][[}[}}}[}))r)}[[{{}}((r(xnnuuQuQz0000O0c?]]?[[[][]]]---?]}))))1))((r(11))))1)111)))1))q#%Z+....'..
xnxx({?``~+++_++_-???]?]][}[[[[}[-]]?]}]]{]][{}1)(rxvccQQ0QO00OZOZOm_?--???----_??})((())11{1((1))())1)111())))(z-...... ..
nxrx({?^`^+++____---?]??]][][[[)]]-?]][]}}1[1{}1[)((xvQzZQ0Ow0w0OzZ#*M%M+-?---_+-?{)rr(()1]--})())))))111)))1)(~.. ..'.....
nnxr(}?^^^++_++___---]??]]][[[}?--][?]]][[}}}})}{11(nvz0QZzOvvq##q*qoo*M%+++__+__?{)r(r()1]^`_])()))11111))(({~'.... .. ...
nnxr(}-^`^~~++_____??]]][[[?}-_--[}?[[-[[[}{1))1))))nuczuxwmwq#ooowww*##%*m~~~~+-?}(rr(((1[^.'~[)(()1))111)(+... .'.. ...'.
xxxx)}-~^^~++~+__-_--??][]]{?]???]]][]]}[}11})11{11(n)OOmmwqmOwowwoqo*qoo***%-^^+?})rr(((1]^'..^]}))){1))r{^ .  .....'. ..'
rxxx)}-^`^~~+_~++___???]-[}_---_?]-??[]}11]))1}{[}}v0zq00mzz0wZqwQ*qoqqoZwo#*%%_^+[)((r))1[~'...'^-})}{1)]. ...... .....'.?
xxxr(}?^``~~~+_~__-_---?-0-+---???[][{}[{}{}1[}?}n0mQcOvvmZZmmOwwqmZZqwm**woq#%M`~[1(((())]~'..'''%*Qw**O'....... .'.'...](
nnxr({?^`^^~+_++++_-_?-_qu--_?_?-]?[{[?_[{[{?[nzcuxcuO0uzZ00cwwc0mwwqmwmwqoo*oq*%x-1(rrr()[^`''%uuMMo*qq%c...... ..''''~1)1
nxnx({_^``~~+++___-????1Z{-_-_~?[}][]]}{}[?rcunx0xvvuvzZcvm0cOQ0mmmZm0qOvwwqmmqww*M{)rrr){-ZM0c**qqwwwo*ou''''..'... .{r)1x
xuun(1?~`^~_+-_____??__*x[]_--__[]?{}?]][)n1(n{urvznuxvQnuQzOczv00mOmcZZO00Z000OZ00mcr(OoZZO*owmwmwwwqo*#''.'.'.'.'`^1)1)xx
uunnx1?~^^~++++__+---_+qc1]_??+?[]?][-}1(1r[)()nrrnvcxr0vcvQvuucQczQ0z0ZOZzQuQQczun0ZzmZqommmmmmwqqzZwwq_'.....''''_())(rrx
uunur1?~^^++++__+____+_mu)1][--?-]?_])1)1]))(r{)(rurrvvvrzvznrznvcxQzzcOQvczQncnvoz0ZwwmZZZmZmmmmmnrcnQq'.'`....''?())rrxrr
uuxnr)]~`^~~~_+_++---++Ou())1-__-+){{{)_}1)(r{}rn))u(uznnxnxc)nnuuvcuvuuuvr(nZuvOwqZOOZOZZZmmmwoxru}rrQ`...'....`[())rrr(r(
nnnnr)]+^^~++~__-_+-_+zqZrrx1)]~{{}}{[{1{{}[1x{1rxr}[}x1(r-nxn(nxnuruvux{m0uQmOO0OOZZZmwmqwwwqqr(}~+{qn......'.'?()(rrrx(r(
uuunx)[~`^~+~________~(wczz{))}-?[?]}1{{}}}}[1))1)}?+^^'{v)[}-`~'`^'.'.o)cZZZ0OZ0OOZmmwmqmwmQ[+~~+]cw'.........{)1(xxxrrr(r
uuuux)]+^`~~+_++___+-~~wQZz)-?]{?-[1{[_}{}}}1{-}}-[?^.`'~___-~''1.`.01QZz0O0OQQO0OOOZOOmn+~~++?(czw .....'.'..]11rxxxrrrrrr
unnnx([^`^+_+_+_-+_+-++BqQvr[}v-[{{}]?[}}-1{[{{?~'^^'''-?^.''~'.+.z}um0QczQQQzQQQ0OZO?^-]1xnuxuvm^.....'..''.]))1xxxxxrrxrr
unnnn(}~`^~++_~+____--_+%wQnQ?-{}1?[[]?][1}]+'`^^`.+. ``''+_.` .()0mO0zzzvucczQzcv+~`]')}_)xuOu'.'....'.''.'?{}(xxnxrxxrxrr
uuunn(}~'`^+~+___-+_?-?-_cO0O-)[]]]}]-?~`?'```~'.'`.'^.'~~+_.-1+nQc0zucvvcvczZ00Om0}+ '^1}1]^.. .'.'.'. ..'~[]}nnnnnnxxxxrr
unnnn)}~`^~~++++_-__-???-~#oz-[?]??[[}[^+``...'^^'`+^... .'_^u{ccQzuxuccrcQmOwmZmmZx?^.``-(_. .....'.. ..'?{])x(xnxnnxxrnnr
unnun([_``~+____+___--??]-%q--_?-}]}?-~'.^.....'`'^').. .v?cxn[rzcuvnv(ncQ0mZmwmqqoQ(~..''1['.'.'''`'..'''1{1r(((1(((xxxrrx
uuuunr{_`^~++++__+_-?-][]??v]?_}[[-+`.'.....'. `'`'^~].x]uuzzz}xmnnxxnvcc0Zmwwwwqoowc-^..')[^..'''''....^11}xxxxxr(((r()))1
uuuuux}_^`~+_+___+---][[][}_+}}[--'~....'.~' '..'. ..`+cxuxvQQvurxuvvczQzQQmmZmwmqowZ1+....n~.'.'''....'}{}(rxxxrrxxxrr(()1
uuuuur{+'~~++_++___--?][1-'. uZ~~'~..- ..''...+`^ '.?_ncZxxQO1)rr]_``_xvzcc0OQOOOQ(_^^`.'.'u}'.`''...'.?{}rxxxrr((rrxxx(r((
uvuvn({+^^^~+_+____+?})x((cv1-^.'_`^^ `.` ._... .. -uv0Zzcm+~_``'..`]1{[(xn0OO0u?_'...'`..^u1`.''...'.'1})rrrr(r(r(r(rr(r((
vvvvur1_``^++++_+++xZ[1()[]' .?.~`^_' `^'...+^'..r?uvcZQQ`^'.'`.`Zv'.`[[1(xQqm+....}'.... `()+'.......?1)xrrrrr(((r(((r)(()
vvvvur{_^^+__-_-]~'.?z%) . .`'^`^`~] .. .'` '.. x(xcOOc?]}{-`][~Zwq(r[[[})n*M[_1^^c{~.'' .`)c`^''..'']{{rrxr(r(r(((((r(())1
vvvcvx1-^++?---.)([]n.`' ].]''~~___]~`   ......-(vvZ{~}1()r)()11{)rr(({1{1nwBzx)[}[_++'.'.'{z~`...`.^1{(r(((r((r((((r()){{}
uvvcvn1-^~+_-?-[_? ~''.`-+.'...-.[``x  . ... `-cz0m`-[}1(xnvvcuuvuvux)(11{(ZMmcv(1{[]-`''.'`x['. ..'}}1xrr(r)((r(1))(111{)z
uvcvvx1?`~+[[?]{^ `'''~~~]' ..'.~.. `{+.... r?0zQ`'^?[[1(rxuzcQzzccux(r){{1Q#ovnx(1}[-''`'..xx'''''+11rxrr(()(()(()(1)1}r0Z
uvuvnn1-^^+_-??1}`_`-.'.?^..'.  .^^ ^_~?   -]z0m..'+][}1)rrxuvczvvuxr)11{{1um#xnr)1}[~'..' .n{{ .'.{1rrxxrr((()))))))1{vOO0
uvnuvx1?``u1{?['}[_''^?}-'.... .'?'^]Q[`^.{]QZ[ '`^~?]{{1)xxxnnnnnux){}{}}{nc%wr()1}?^..'''.]][...?11xxxr((x((())){{{1vZZOO
uuvvvn)?``}+?-+^^]`^'+.?{-' .'. `}.^^....xn?v(...'+^?[}{1)((rrxxxxx(1?11)1[)vqZ))1[]_....` ..n1^ `))rxrr(r(r((1())111vZZOOw
nvuvvn)?^`~_-_``^?` -~^?~[.n..'. ._^ .. }rnr`...''-~[[}}11(r((rxxxxr()[}{}}{zzx({{['...'^''..v}_'{)1xr(rr(((()()111}nOZZmqo
nuuvvn1[^`^~_)`'``]^.`~_-`({''.``..^-{z+^O ....''`?_?][}11))()rxrxxxxr()xZnmOvr1{}-.. ''~.'..r)'[))rx(()())))))))11{cOZmqoo
nuuvuu([^`^1+[''?`''. ^`` _]-]_ `+-)vc_~Q .''.`'.._+?]}{{11((1)((()()(rnz#m*0z{{{].. .''```..-n_)))r(r((((())))(11{{zZwo**o
uvvvvu(]``[~_?`'~`.`''[~^`~^+}^Q{0m0+~x ..`...'`. -++?[{1{{1)))[`^-?--~^~]]_+[}1^... '`'^`.^.'rrr))rr((r((()())))1})0q**o*o
uvvcvnr}[^~)++`?'  ^^.1._-`~.-{){v_-xr...  '..``'.^^^_?[[[}{{1((1}[}{{rrr((11)}......'.~`~.~..[(x(r((((r(((())1))1{rwM#***#
uvvvvn)]`'n+-.'~..+'^Q1+++`'}x.r]x]x ...'... ..'...`'^~_-?[}{{)11{1{{11})(({1+^....'..._^+'`'.]))(r(r((((()()1))1}])*%M##M#
uvuvvu(]^^]_^.`...^.'x}1x__'^-~?_Z ..' .....'..'`'.'''^~_--[{{)1)((xxnuvnx(){.....'....-`^'~`'?(1(rr(()(((()){1{{}]r%%M**o*
nuvvvnr]``+^. -.' '. )}'`~][-?1+~.     .'.`.'....''''.'`.'~_]}}{)((rxuvnnr)[+'...''''''-^~`^`'~r{}}11)))))))111{}[[O%M**o*o
nuunun)?'O^[ ''..`...}]_^'}]]`)? n].  .`` '. . ...''.'.`~--])1(1{1)rxrxxxuzOm' ...'. .'-`^`~`'1x_-+_-??-]]}{{{}[]]vq*wwqqqZ
nuuuuxxx'^   .^.`.^^`.`-}11(^']-]?)~O .'`.`. ......'..''+]][}{}11))))))(nc0ZZmmZOm?.'.`^`^```.n)}1{}}?]]_-+++~~_?~umwmqwwOc
nuuuvn)[^`. ...` ..[^ ..]?-)'__^1}`r.  ''.^... ......`.'^_]]}{}{)1)))(rxvQ0OOZOmwwqww '^'````.n{()){1}}}}[]?-+-}]~cqqqqmOr'
xuvuun(u_~..' '. ^`'`^' +.`^'-~?{() ).  . `' ...'..^.+~.^?[}?1{11)))(rxuuvczcQ0Zmwoooo*.`'``^`{1)){)1{1{{[}}][]}}1wooowzx^`
nvvvvn(([' . .` ...-'..~ +~.``+_+?1(~ zZ .^'.. ... `+]-'`_]{1)11))))(rrxxuuvvQ0QZwwooo**B'...u)1))1))1{1}}{}][]rxz**owZ(_^+
xvvvvur{~+ .... ..'} . ..-``+-~~^1)) ^`*+ `. . .`..'?--~`+]1{1111(((((rrrnnvvcQ0OZqoo#*M#*'`.1(()(1)111}}{][])Qwmq#*qZx_++_
nvvccnr{~. .  ....-+ . . .' '.{''1)x` uru.'.'......+]}]`~-[{1))1111))((rrxunuczQOZmoooo***Z' })(1)))111{}{}[[Z*#qo*oO(?--__
nvuuun(1+'... .'`._`..`   `.+.._{][-[(vr_. `''...'`-[}['+]}111)1){{))))rrxnnvvcQ0Zmqqo***o#'.1(())111{11}[}}1w*wm**wx[]-++-
nuvuuu({+'...'.....' . `  '.` {+_-?-1 .. '.'.`..'^_[[[+'-{{)11)))111)))((rnnnuvcQ0mwwo*##**w~)))(11))11}{11{1)ucO#mO}--_-+~
xuuuvur}?'. .' ....'..' ' '`._' .?+.'?Q ' ......^-?[[['_}11)))(()))))(()rxrrnuvvczOZwoo#****m_~++-?][}{{)1(r)1{cq#0(?-~^+~`
xnuuuvr1_`..'  .'.' ''. .  ~ +[{.~`'c.'....  .'~_]??-.+{11{)))()))))1)))((rxrxnuvcQOZwooo***#`^^~^``.''`^+[1zx(woZ{-`'^^`^_
rnvnvvn}}`.  .'.'.' .......`'. ]([?]`...  ...'+-]]]''?{1111))1)(()())1)1)))(rxnnuvzQ0wwqooo***~+_++^^''. .[OOrQmO}'.'`'^++`

`````

---

### Translation table:

```
" ░▒▓"
```

### Output:

```
▒▒▒░░░    ░      ░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░▒░░░░░░░░░▒▓▓▓▓▒ ░ ░░░░░░░░░░
▒▒░░░░░            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░░░░▒░░░▒▒▒░░▒░░░░░░░░░▒▓▓▓▓▓░ ░░░░░░░░░
░░░░░░░             ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▒    ░░░
▒░░░░░              ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓░  ░
▒▒▒░░░░            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▒░
▒▒▒░░░░           ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓
▒▒░▒░░░           ░░░░░░░░░░░░░░░ ░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▒▓ ░  ░░░     ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒
▒▒░░░░░             ░░░░░░░░░░░░░░ ░░░░░░░░░░░░░░░░░░▒▒▒▓▒▒▒▓▒▓▒▒▒▓▓▓▓▓▓  ░      ░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░
▒▒▒░░░░              ░░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓        ░░░░░░░░░░   ░░░░░░░░░░░░░░░░
▒▒▒░░░             ░░░░░░░░░░    ░░░░░ ░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ░░░░░░░░░░    ░░░░░░░░░░░░░
▒▒▒░░░               ░░░░░░░░░░ ░░░░░░░░░░░░░░░░░░░░▒░▒▒▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ░░░░░░░░░     ░░░░░░░░░░░
░░▒▒░░              ░░░░ ░░     ░░ ░░░░░░░░░░░░░░░░▒▒▒▓▒▒▓▒▒▒▓▒▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓   ░░░░░░░░░        ░░░░░░░                ░
▒░░░░░                 ░ ▒     ░░░░░░░░░░░░░░░░░░▒▒▓▒▒▒▒▒▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░░░░░░░░░       ▓▓▒▓▓▓▒                ░░
▒▒░░░░               ░  ▓▒   ░ ░ ░ ░░░░ ░░░░░░▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒ ░░░░░░░░    ▓▒▒▓▓▓▓▓▓▓▒              ░░░
▒▒▒▒░░             ░░░░░▓░      ░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▓▓▓▓▓▒▓▒▒▓▓▓▓▓▓▓▓▓▓░░░░░░░ ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒            ░░░░░
▒▒▒▒░░░            ░░  ▓▒░░     ░░░░░░░░░░▒░░▒░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓▒░░▒▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓            ░░░░░▒
▒▒▒▒▒░░                ▓▒░░ ░  ░░░ ░░ ░░░░░░░░░▒░░▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▓▒▓▒▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓            ░░░░░░░
▒▒▒▒░░░                ▓▒░░░░    ░░ ░░░░░░░░░░░░░░▒░░▒▒▒░▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▓▓▓▒▒▒▓▓▓▓▓▓▓▒░▒▒▒▓           ░░░░░░░░
▒▒▒▒░░░                ▒▒░░░░     ░░░░░ ░░░░░░░░▒░░▒░▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▓▒▒▒▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▒░▒░░░▒          ░░░░░░░░░░
▒▒▒▒░░░               ▒▓▓░░▒░░░ ░░░░░░░░░░░░░▒░░░▒░░░░▒░░░ ▒░▒░▒▒▒▒░▒▒▒▒░▓▒▒▒▓▒▒▒▒▒▓▒▒▓▓▓▓▓▓▓▓▓░░░  ░▓▒         ░░░░░░░▒░░░
▒▒▒▒░░░               ░▓▒▒▒░░░░ ░░░░░░░░░░░░░░░░░░░░    ░▒░░░          ▓░▒▓▒▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▒░    ░▒▓          ░░░░▒░▒░░░░░
▒▒▒▒▒░░                ▓▒▒▒░ ░░░░ ░░░░ ░░░░░░░ ░░ ░░            ░   ▒░▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒     ░░▒▒▓           ░░░░▒▒▒░░░░░░
▒▒▒▒▒░░                ▓▓▒▒░░░▒ ░░░░░░░░░ ░░░░░░                  ▒░▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒░  ░░▒▒▒▒▒▒▓            ░░░░▒▒▒▒▒░░░░░
▒▒▒▒▒░░                 ▓▓▒▒▒░ ░░░░░░░░░░░░░                    ░░▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ░ ░░ ░▒▒▒▒              ░░░▒▒▒▒░░▒░▒░░
▒▒▒▒▒░░             ░ ░  ▒▒▒▒ ░░░░░░░    ░                    ░ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒░    ░░░░                ░░░▒▒▒▒▒▒▒░▒▒░░
▒▒▒▒▒░░              ░ ░  ▓▓▒ ░░░░░░░░░                      ▒░▒▒▒▒▒▒▒▒▒░▒▒▓▒▓▓▓▓▓▒░░     ░               ░░░░░░▒▒▒▒▒▒▒░▒▒░
▒▒▒▒▒░░               ░ ░ ▓▓   ░ ░░░                ░    ▒░▒▒▒░░▒▒▒▒▒▒░▒▒▒▒▓▒▓▓▓▓▓▓▒░     ░░              ░░░░░░░░░░░▒▒▒░░▒
▒▒▒▒▒░░             ░ ░░░░░▒░░ ░░░                   ░ ▒░▒▒▒▒▒░▒▓▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒     ░░             ░░░▒▒▒▒▒░░░░░░░░░░
▒▒▒▒▒▒░              ░░░░░░  ░░░                       ▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓░     ▒            ░░░░░▒▒▒░░▒▒▒░░░░░░
▒▒▒▒▒░░              ░░░░    ▒▓                     ░ ▒▒▓▒▒▒▒░░░░░    ▒▒▒▒▒▒▒▒▒▒▒▒░        ▒░          ░░░░▒▒░░░░░░░░░░░░░░
▒▒▒▒▒░░             ░░░░░░▒▒░                       ▒▒▒▓▒▒▓         ░░░░░▒▒▒▒▒▒▒░          ▒░          ░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒░░            ░▓░░░░░░   ░                  ░░▒▒▒▓▒▒        ▓▒   ░░░░▒▒▓▓     ░       ░░         ░░░▒░░░░░░░░░░░░░░░░░
▒▒▒▒▒░░         ░    ▒▓░           ░            ▒░▒▒▒▒▒ ░░░  ░░ ▓▓▓░░░░░░░▒▓▓░ ░  ▒░       ░▒        ░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒░    ░    ░░░░▒    ░ ░       ░            ░▒▒▓░ ░░░░░░░░░░░░░░░░░░░░▒▓▓▒░░░░░        ░▒        ░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒░      ░ ░                 ░  ▒          ▒▒▒▓  ░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▓▓▓▒▒░░░░░       ▒░      ░░░▒░░░░░░░░░░░░░░░░░░▒
▒▒▒▒▒▒░░   ░░░░░         ░           ░      ░ ▒▒▒   ░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░▒▓▓▒▒░░░░░       ▒░      ░░░░░░░░░░░░░░░░░░░░░▒▒
▒▒▒▒▒▒░       ░░░       ░              ░    ░▒▒▓    ░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░▒▓▓▒▒░░░░░       ▒░░    ░░░░░░░░░░░░░░░░░░░░▒▒▒▒
▒▒▒▒▒▒░░  ▒░░░░ ░░    ░░         ░  ░▒░   ░░▒▒░     ░░░░░░▒░░▒▒▒▒▒▒▒░░░░░░░▒▒▓▓░░░░░░       ░░░    ░░▒░░░░░░░░░░░░░░░░▒▒▒▒▒
▒▒▒▒▒▒░░  ░      ░     ░░        ░       ▒▒░▒░      ░░░░░░░░░░░░▒▒░░░░░░░░░░▒▓▒░░░░░         ▒░   ░░░░░░░░░░░░░░░░░░░▒▒▓▒▒▓
▒▒▒▒▒▒░░         ░     ░ ░ ▒            ░░▒░        ░░░░░░░░░░░▒░░░░░░░░░░░░▒▒░░░░░          ▒░  ░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓
▒▒▒▒▒▒░░     ░    ░       ░░         ░▒  ▒          ░░░░░░░░░░░▒░░▒▒░░░░▒▓▒▓▒▒░░░░           ░░ ░░░░░░░░░░░░░░░░░░░░▒▒▒▓▓▓▓
▒▒▒▒▒▒░░   ░ ░  ░          ░ ░     ░▒▒  ▒           ░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▒▒░░░░            ▒ ░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓
▒▒▒▒▒▒░░  ░  ░        ░      ░ ▒░▒▓▒  ░              ░░░░░░░░░░░   ░     ░░  ░░░              ░░░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓
▒▒▒▒▒▒░░░  ░   ░      ░       ░░░▒  ▒░                ░░░░░░░░░░░░░░░░░░░░░░░░░               ░░▒░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓
▒▒▒▒▒▒░░  ▒          ▒░     ░▒ ░░▒░░                     ░░░░░░░░░░░░░░░░░░░░                 ░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓
▒▒▒▒▒▒░░  ░          ░░░░        ▓                         ░░░░░░░░▒░▒▒▒▒▒░░░                 ░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓
▒▒▒▒▒▒░░             ░░   ░░ ░░                             ░░░░░░░░▒▒▒▒▒░░░                   ░░░░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▓
▒▒▒▒▒▒░░ ▒ ░         ░░   ░░░ ░  ▒░                        ░░░░░░░░░▒░▒▒▒▒▒▒▓                 ░▒     ░░ ░░░░░░░░░░▒▓▓▓▓▓▓▓▓
▒▒▒▒▒▒▒▒                ░░░░  ░ ░░░ ▒                    ░░░░░░░░░░░░░░░▒▒▒▓▒▓▓▓▒▓░           ▒░░░░░░░░░          ▒▓▓▓▓▓▓▒▒
▒▒▒▒▒▒░░           ░    ░░ ░    ░░ ░                      ░░░░░░░░░░░░░░▒▒▒▒▒▓▒▓▓▓▓▓▓         ▒░░░░░░░░░░░░░   ░░ ▒▓▓▓▓▓▒░
▒▒▒▒▒▒░▒                       ░░░░ ░                    ░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓       ░░░░░░░░░░░░░░░░░░░░▓▓▓▓▓▒▒
▒▒▒▒▒▒░░░                        ░░░  ▒▒             ░    ░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓    ▒░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓░
▒▒▒▒▒▒░░           ░             ░░░   ▓            ░     ░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓   ░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▒▒
▒▒▒▒▒▒░░                      ░  ░░▒  ▒░▒           ░░░   ░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓  ░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▒░░
▒▒▒▒▒▒░░                        ░░░ ░░▒░            ░░░  ░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓  ░░░░░░░░░░░░░░░░▓▓▓▓▓▓▓▒░░
▒▒▒▒▒▒░░                      ░     ░              ░░░   ░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓ ░░░░░░░░░░░░░░░░░▒▒▒▓▓▒░
▒▒▒▒▒▒░░                         ░   ░▒           ░░░░  ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓     ░░░░░░░░░░░░░▒▓▓▒░░
░▒▒▒▒▒░░                      ░░    ▒            ░░░   ░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓             ░░▒▒░▓▓▓░
░▒▒▒▒▒▒░░                      ░░░░░            ░░░  ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓            ░▒▒░▒▓▒░

```
