import tj, pickle, time,os, sys,requests

DAY=60*60*24
FREQUENCY=2
FILE="C:\\Users\\Public\\Documents\\Rates.data"
Base_Currency='INR'
url=fr'https://v3.exchangerate-api.com/bulk/6e4ac702b06d5f6094492c37/{Base_Currency}'

today=time.time()
cmd=False
args=sys.argv
run=True


if len(args)>1:    # It means that the programs is running through CMD args
    cmd=True


Currency={'AED': 'United Arab Emirates Dirham', 'ALL': 'Albanian Lek', 'AMD': 'Armenian Dram', 'ANG': 'Netherlands Antillean Guilder',
          'AOA': 'Angolan Kwanza', 'ARS': 'Argentine Peso', 'AUD': 'Australian Dollar', 'AZN': 'Azerbaijani Manat',
          'BBD': 'Barbadian Dollar', 'BDT': 'Bangladeshi Taka', 'BGN': 'Bulgarian Lev', 'BHD': 'Bahraini Dinar',
          'BRL': 'Brazilian Real', 'BSD': 'Bahamian Dollar', 'BWP': 'Botswanan Pula', 'BYN': 'Belarusian Ruble',
          'CAD': 'Canadian Dollar', 'CHF': 'Swiss Franc', 'CLP': 'Chilean Peso', 'CNY': 'Chinese Yuan', 'COP': 'Colombian Peso',
          'CZK': 'Czech Koruna', 'DKK': 'Danish Krone', 'DOP': 'Dominican Peso', 'DZD': 'Algerian Dinar', 'EGP': 'Egyptian Pound',
          'ETB': 'Ethiopian Birr', 'EUR': 'Euro', 'FJD': 'Fijian Dollar', 'GBP': 'Pound Sterling', 'GEL': 'Georgian Lari',
          'GHS': 'Ghanaian Cedi', 'GNF': 'Guinean Franc', 'GTQ': 'Guatemalan Quetzal ', 'HKD': 'Hong Kong Dollar',
          'HNL': 'Honduran Lempira', 'HRK': 'Croatian Kuna', 'HUF': 'Hungarian Forint', 'IDR': 'Indonesian Rupiah',
          'ILS': 'Israeli New Shekel', 'INR': 'Indian Rupee', 'IQD': 'Iraqi Dinar', 'IRR': 'Iranian Rial', 'ISK': 'Icelandic Krona',
          'JMD': 'Jamaican Dollar', 'JOD': 'Jordanian Dinar', 'JPY': 'Japanese Yen', 'KES': 'Kenyan Shilling',
          'KHR': 'Cambodian Riel', 'KRW': 'South Korean Won', 'KWD': 'Kuwaiti Dinar', 'KZT': 'Kazakhstani Tenge',
          'LAK': 'Laotian Kip', 'LBP': 'Lebanese Pound', 'LKR': 'Sri Lankan Rupee', 'MAD': 'Moroccan Dirham',
          'MDL': 'Moldovan Leu', 'MKD': 'Macedonian Denar', 'MMK': 'Myanmar Kyat', 'MUR': 'Mauritian Rupee',
          'MXN': 'Mexican Peso', 'MYR': 'Malaysian Ringgit', 'NAD': 'Namibian Dollar', 'NGN': 'Nigerian Naira',
          'NOK': 'Norwegian Krone', 'NZD': 'New Zealand Dollar', 'OMR': 'Omani Rial', 'PAB': 'Panamanian Balboa',
          'PEN': 'Peruvian Sol', 'PGK': 'Papua New Guinean Kina', 'PHP': 'Philippine Piso', 'PKR': 'Pakistani Rupee',
          'PLN': 'Poland Zloty', 'PYG': 'Paraguayan Guarani', 'QAR': 'Qatari Rial', 'RON': 'Romanian Leu', 'RSD': 'Serbian Dinar',
          'RUB': 'Russian Ruble', 'SAR': 'Saudi Riyal', 'SCR': 'Seychellois Rupee', 'SEK': 'Swedish Krona',
          'SGD': 'Singapore Dollar', 'THB': 'Thai Baht', 'TJS': 'Tajikistani Somoni', 'TND': 'Tunisian Dinar',
          'TRY': 'Turkish Lira', 'TTD': 'Trinidad & Tobago Dollar', 'TWD': 'New Taiwan Dollar', 'TZS': 'Tanzanian Shilling',
          'UAH': 'Ukrainian Hryvnia', 'USD': 'United States Dollar', 'UYU': 'Uruguayan Peso', 'UZS': 'Uzbekistani Som',
          'VEF': 'Venezuelan Bolivar (Fuerte)', 'VND': 'Vietnamese Dong', 'XAF': 'Central African CFA Franc',
          'XCD': 'East Caribbean Dollar', 'XOF': 'West African CFA Franc', 'XPF': 'CFP Franc', 'ZAR': 'South African Rand',
          'ZMW': 'Zambian Kwacha'}

Currency_Keys=list(Currency.keys())



try:
    f=open(FILE,"rb")
    L=pickle.load(f)
    f.close()
    last_date=L[0]
    D=L[1]
    make_file=False

except:
    make_file=True
    last_date=today

def refresh_rates(last_date, make_file, url):
    global run
    refresh=False
    if (last_date+(DAY*FREQUENCY)<today):
        refresh=True
        
    if refresh or make_file:
        # Fetch exchange from internet
        if refresh:print('Updating currency exchange rates...\n\n')
        else:print('Fetching exchange rates from internet...\n\n')
        #c = CurrencyRates()
        #D=c.get_rates(Base_Currency)
        try:response = requests.get(url)
        except:
            if make_file:
                input('Internet is needed for first time use!\nPlease make sure you have internet...')
                run=False
        data = response.json()
        D=data['rates']
        
        L=[today, D]

        f=open(FILE, 'ab')
        pickle.dump(L, f)
        f.close()

try:refresh_rates(last_date, make_file, url)
except:print('')


def convert(c1,c2):
    # Convert TYPE1 to 
    # Convert INR to TYPE2
    type1=c1[-3:].upper()
    type2=c2.upper()


    #if type1==Base_Currency:rateA=1
    #else:
    rateA=D[type1]  # 1 INR = rateA*TYPE1 which is why we need to inverse rateA
    
    #if type2==Base_Currency: rateB=1
    #else:
    rateB=D[type2]  # TYPE2 = rateB*INR

    c1=tj.convert_currency(c1, Base_Currency, 1.0/rateA,False)
    c1=c1.upper()
    c2=tj.convert_currency(c1, c2, rateB,flag=False)
    
    return c2


def play_CMD(args, doc, logo):
    print(logo)
    if args[1].upper() in ['D', '-D', 'DOCS', '-DOCS','DOCUMENTATION', '--D', '-H', '-HELP']:
        print(doc)

    elif args[1].upper() in ['-R', 'R', 'U', '-U', 'REFRESH', 'UPDATE', 'UPGRADE']:
        print('Updating currency exchange rates...')
        refresh_rates(last_date, True)
        print('Done updateing!')

    elif args[1].upper() in ['C', '-C', 'ALL CURRENCIES', 'CURRENCIES', 'CURRENCY', 'A', '-A']:
        for key in Currency_Keys:print(f"{key} : {Currency[key]}")

    else:
        amt1=args[1].upper()
        type1=args[2].upper()
        type2=args[3].upper()
        c1=amt1+" "+type1
        c2=type2

        try:
            c2=convert(c1,c2)
            amt2=c2.split(" ")[0] 
            print(f"\n  {amt1}  {Currency[type1].upper()}   =   {amt2}  {Currency[type2].upper()}")
        except:
            print ('\n\n    LOOKS LIKE YOU MESSED-UP. YOU CAN READ THIS DOCUMENTATION FOR HELP\n\n')
            print(doc)
            
    sys.exit()
           

doc=f"""
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
    """


logo='''
WELCOME TO 
  ___ _   _ _ __ _ __ ___ _ __   ___ _   _ 
 / __| | | | '__| '__/ _ \ '_ \ / __| | | |
| (__| |_| | |  | | |  __/ | | | (__| |_| |
 \___|\__,_|_|  |_|  \___|_| |_|\___|\__, |
                               _      __/ |
                              | |    |___/                    
  ___ ___  _ ____   _____ _ __| |_ ___ _ __ 
 / __/ _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| (_| (_) | | | \ V /  __/ |  | ||  __/ |   
 \___\___/|_| |_|\_/ \___|_|   \__\___|_|   
'''
menu=f'''
{logo}

MENU:

1) Convert Currency

2) See All Currency Acronyms

3) Update Currency Exchange Rates

4) Documentation

5) Quit       
'''
msg='Enter your choice from 1-5: '

if (cmd and run):play_CMD(args, doc, logo)

while run:
    os.system('cls')
    print(menu)
    
    choice=input(msg)
    
    if choice not in [str(i) for i in range(1,6)]:
        msg='Enter your choice only from 1-5: '
        continue

    if choice=='1':
        print('Enter currency only in the form written below->')
        print('''eg.->
    Enter amount and currency to be converted: 40.5 USD
    Enter currency in which you want to convert into: INR\n\n''')
        c1=input('Enter amount and currency to be converted: ').upper()  # c1='AMT TYPE'
        c2=input('Enter currency in which you want to convert into: ').upper()  # c2='TYPE'
        try:c2=convert(c1,c2)
        except:
            print ('\n\n    LOOKS LIKE YOU MESSED-UP. YOU CAN READ THIS DOCUMENTATION FOR HELP\n\n')
            print(doc)
            input('\nEnter to ocntinue...')
            continue

        type1=c1.split(" ")[1]
        amt1=c1.split(" ")[0]
        type2=c2.split(" ")[1]
        amt2=c2.split(" ")[0]
        print(f"\n  {amt1}  {Currency[type1].upper()}   =   {amt2}  {Currency[type2].upper()}")
        input('\n\nEnter to continue...')

    if choice=='2':
        print('These are all the currency acronyms:\n')
        for i in range(0,len(Currency_Keys),2):
            key1=Currency_Keys[i]
            s1=f"{key1} : {Currency[key1]}"
            try:
                key2=Currency_Keys[i+1]
                s2=f"{key2} : {Currency[key2]}"
                print(f"%-35s |\t %s" % (s1,s2))
            except:
                key2=None
                print(f"{s1}")

        
        input('\n\nEnter to continue...')

    if choice=='3':
        print('Updating currency exchange rates...')
        refresh_rates(last_date, True, url)
        print('Done updating!')
        input('\n\nEnter to continue...')

    if choice=='4':
        print(doc)
        input('\n\nEnter to continue...')
            
    if choice=='5':break

