WELCOME, this program helps to easily convert currencies, from one to another in just a jiffy.

All you need to do is, open the program and enter which currency you want to convert, how much amount
and to which currency. This program, unlike many other programs and softwares, this program does not
require you to put the currency exchange rates by yourself. The program aquires the latest currency
rates all by itself, and keeps those currency rates up-to-date.

This programs works offline, but if you are opening the program for the first time, you need an internet
connection, so that the program can fetch the exchange rates form the internet. One that is done, you will
never need to worry, as firstly, the program is capable of working offline and secondly, the program keeps
its currency exchange rate data, up-to-date when you have internet connection.

HOW TO USE THIS PROGRAM-
    Its easy to use once you are fimiliar with the commands that you need to give.

    Just open the program and use it. To use the currency exchange function, just enter 1 in the main menu.
    Then you need to enter the amount and the currency information in this way-
    
    1) The currency you need to ocnvert- lets call it c1. You need to enter the amount of c1 as well as its
        type/unit. For eg. you should enter '45 USD' (without quotes) or '95 INR' or '50 eur' or '100.3 nzd' etc.

    2) The currency you need to convert to- lets call it c2. You need to enter only the type/unit of this
        currency. For eg. 'USD' or 'AUD' or 'inr' or 'CnY' or 'jPy' etc. Also as you can see, it is not
        case-sensitive.

    In summary you need to enter like this-
        Enter amount and currency to be converted: 100 CNY
        Enter currency in which you want to convert into: USD


    *BUT IT DOES NOT END HERE. THERE IS AN EVEN FASTER WAY OF DOING THE CURRENCY CONVERSION, WITHOUT EVEN
    OPENING THIS PROGRAM. YES, WITHOUT EVEN OPENING THIS PROGRAM, FROM ANYWHERE IN YOUR COMPUTER, YOU CAN
    DO CURRENCY CONVERSION AND MORE, USING THIS TECHNIQUE-

    For that, you have to use CMD or Command Prompt, a powerful Windows Console to get things done.

    1) Open CMD by typing cmd in the run box (Windows Key + R to open run box)
    2) Type 'cc <arguments>' in the command prompt (wihtout quotes). The arguments can be -
        a) -A or -C for opening all Currency Acronyms. eg. 'cc -a' or 'cc -c' (without quotes ofcourse)
        b) -D or -docs or -h or -help to open this help documentation. eg. 'cc -d' or 'cc -help'
        c) -R or -U or -UPDATE or -REFRESH to forcefully update to the latest currency exchange rates
            eg. 'cc -r' or 'cc -update'
        d) Lastly, to do actual currecy exchange, just type c1 and c2 in the place of arguments.
            For eg. 'cc 1 usd inr' this will convert 1 USD into INR. 'cc 50.2 EUR AUD' this will convert
            50.2 EUR into AUD.

    *If you are getting an error like 'cc' is not recognized as an internal or external command. Then you need
    to add Currency Converter to your computer's environment variables. Don't be intimidated by this, its a very
    small process. The program tries to do this automatically, but sometimes it can fail, and you have to do this
    manually. Just copy this path-> '{os.getcwd()}' without quotes, and paste it in your PATH environment variable.
    Just google 'how to paste a PATH in PATH Environment Variable' and follow the procedures. You will really like it.

    *If the above procedure does not work, then copy paste this program in C:\\Windows folder.
    It will ask for admin rights, give it.