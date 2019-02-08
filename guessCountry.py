import random

def find_letter(haystack,needle,start=0,end=-1):
    for index,letter in enumerate(haystack[start:]):
        if letter==needle:
            return index+start
    return -1

def put_letter(letter_list,word,letter):
    start=0
    while(1):
        pos=find_letter(word,letter,start)

        if pos!=-1:
            letter_list[pos]=letter
            start=pos+1

        else:
            break

print('{0:^60}'.format('GUESS THE COUNTRY'))
print('{0:^60}'.format('-----------------'))
rule_layout='{0:<15}{1}'
print(rule_layout.format('Rules to play:','1.Guess the letters to reveal the country'))
print(rule_layout.format('','2.Difficulty modes are set on given lives'))
print(rule_layout.format('','3.One life will be taken per wrong guessing\n'))
print(rule_layout.format('','Tip: Start with vowels!\n'))

key=input("Enter 'y' to start or 'n' to quit the game: ")

if key=='y' or key=='Y':
    layout = '{0:<7}{1:<2}{2}'
    print('\n')
    print(layout.format('EASY',':','10 Lives'))
    print(layout.format('MEDIUM',':','7 Lives'))
    print(layout.format('HARD',':','4 Lives'))

    mode=input('To choose mode enter e,m or h: ' )
    if mode=='h':
        life=4
    elif mode=='m':
        life=7
    elif mode=='e':
        life=10
    else:
        life=10
        print('You entered wrong keyword. Play now by default in easy mode.\n')

    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # COUNTRIES

    country_list='''Afghanistan
Albania
Algeria
America
Andorra
Angola
Antigua
Argentina
Armenia
Australia
Austria
Azerbaijan
Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bhutan
Bolivia
Bosnia Herzegovina
Botswana
Brazil
Brunei
Bulgaria
Burkina
Burundi
Cambodia
Cameroon
Canada
CapeVerde
Chad
Chile
China
Colombia
Comoros
Congo
CostaRica
Croatia
Cuba
Cyprus
Czech
Denmark
Djibouti
Dominica
Ecuador
Egypt
Eritrea
Estonia
Ethiopia
Fiji
Finland
France
Gabon
Gambia
Georgia
Germany
Ghana
Greece
Grenada
Guatemala
Guinea
Guyana
Haiti
Honduras
Hungary
Iceland
India
Indonesia
Iran
Iraq
Ireland
Israel
Italy
IvoryCoast
Jamaica
Japan
Jordan
Kazakhstan
Kenya
Kiribati
Korea
Kosovo
Kuwait
Kyrgyzstan
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Macedonia
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Mauritania
Mauritius
Mexico
Micronesia
Moldova
Monaco
Mongolia
Montenegro
Morocco
Mozambique
Myanmar
Namibia
Nauru
Nepal
Netherlands
NewZealand
Nicaragua
Niger
Nigeria
Norway
Oman
Pakistan
Palau
Panama
Paraguay
Peru
Philippines
Poland
Portugal
Qatar
Romania
Russia
Rwanda
Samoa
SaudiArabia
Senegal
Serbia
Seychelles
Singapore
Slovakia
Slovenia
Somalia
SouthAfrica
SouthSudan
Spain
SriLanka
Sudan
Suriname
Swaziland
Sweden
Switzerland
Syria
Taiwan
Tajikistan
Tanzania
Thailand
Togo
Tonga
Tunisia
Turkey
Turkmenistan
Tuvalu
Uganda
Ukraine
Uruguay
Uzbekistan
Vanuatu
Venezuela
Vietnam
Yemen
Zambia
Zimbabwe'''
    country_list=country_list.upper()
    country_list=country_list.split()
    tot_country=len(country_list)

    while key == 'y' or key == 'Y':
        rndm=random.randrange(1,tot_country)
        country=country_list[rndm]
        l=len(country)
        blank_space=[]

        for _ in range(l):
            blank_space.append('_ ')
        print(' '.join(blank_space))

        count=0
        _try=0

        #MAIN GAME ITERATION
        while(count!=life):
            letter=input('Guess the letter to reveal the country!! :  ')
            letter=letter.upper()

            if letter not in alphabet or letter=='':
                print('Wrong Keyword. Use only alphabet.')
                print(' '.join(blank_space))
                continue

            elif letter in blank_space:
                print('You already used it once')
                print(' '.join(blank_space))
                continue

            elif letter in country:
                _try += 1
                put_letter(blank_space,country, letter)
                print(' '.join(blank_space))
                if '_ ' not in blank_space:
                    print('\nCongrtas!! Your guess is right & it took',_try,'attempt.')
                    count=life

            #if letter not in country
            else:
                _try += 1
                count+=1
                if count<life-1:
                    print('{0:^45}'.format("Wrong Guess!!!"))
                    print(' '.join(blank_space))
                elif count==life-1:
                    print("\nWrong Guess!!! You have one life left. Play carefully!!!\n")
                    print(' '.join(blank_space))
                else:
                    print('\nSorry! You have failed. It was',country,)
                    print('You took',_try,'attempt.')
                    break


        print('\n\n\n\n')
        key=input("Do you want to try again? If yes enter 'y' nor any other key: ")


print('{0:^50}'.format('_________________'))
print('{0:<16}{1}'.format('','You quit the game'))
print('{0:^50}'.format('_________________'))