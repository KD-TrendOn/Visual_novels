﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define i = Character('Изабель', color="#9b111e")
define audio.nrom = 'music/rom.mp3'
define audio.napryag = 'music/napryag.mp3'
define m = Character('Мама', color="#b8860b")
define p = Character('Патрик', color="#0000FF")
define l = Character('Лесник', color="#00ff00")
define LoveYou = False 
define raz = 0
define audio.teleport = 'audio/lazernyiy-teleport.mp3'
define bw = Character('Темная волшебница', color='#FF0000')
define ww = Character('Светлая волшебница', color='#420680')
define s = Character('Команда создателей игры', color='#FFFFFF')

init python:
    left1 = Position(xalign=0.1, yalign=1.6)

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# room- комната 
# mam- мама
# stret- улица
# stret2- улица с парнем
# pat- мальчик 

label start:

    scene black 

    m "Изабель, доброе утро! Пора вставать"
    scene room
    i "Ооо нет, опять это утро, и кто его только придумал?"
    show mam with fade
    m "Дрыхнешь целыми днями"
    m "Так, ты иди прогуляйся, а я пока разберу оставшиеся коробки."
    hide mam
    ##
    i ' Позвольте представиться, меня зовут Изабель. И совсем недавно мы с родителями переехали в новый город. На дворе Июль, до школы еще далеко, вот я и  кисну дома, одна без друзей. '
    i " Папе выдали квартиру на окраине города на работе. Тут и людей то мало,  а о сверстниках уж и нечего говорить."
    $ renpy.notify('Медальон получен ')
    i "Что ж, возможно, все не так уж и плохо, и я смогу найти здесь что-то интересное! Главное не потерять медальон, который  подарил мне папа, он с детства мне говорил, что он поможет мне в любой трудной ситуации"
    scene street
    i "Так, куда бы мне пойти?"
    menu:
        "Куда пойти?"
        "Налево":
            i " Прогуляюсь ка я налево, думаю, там есть что-нибудь интересное"
            jump forest
        "Направо":
            $YouLove = True
            i " Хм, кажется там справа вдали есть что-то интересное, пойду ка гляну"
            jump love
    return
label love:
    play music nrom
    scene street2
    i " Ой, что это за красивый мальчик там идет..."
    show pat  at right with moveinright
    p 'Привет, а ты откуда? Я знаю всех ребят в округе, но тебя я здесь ни разу не встречал. Как это ты забрела в наше " Захолустье"? '
    i "Ой, долгая это история, вообщем с недавних пор я здесь живу"
    p "Интересно было бы послушать твою истоию, я направляюсь в парк аттракционов, если тебе нечем заняться, пошли со мной. Как раз и расскажешь свою историю."
    menu:
        "Пойти ли с Патриком?"
        "Да":
            i "Хм, а почему бы и нет, я всегда любила парки атракционов"
            jump park
        "Нет":
            i "Нет, прости, у меня много дел, давай как нибудь в другой раз"
            hide pat
            i "Даже и не знаю что на меня нашло, я вроде хотела с ним пойти, но впоследний момент испугалась"        
            i "Ладно, обязателбно отыщу его позже, а пока прогуляюсь в другую сторону" 
            jump forest    
    return
label forest:
    scene lestrop
    i "Какой красивый лес, почему я не гуляла здесь раньше "
    show kust at left1 
    i "Ого сколько ягод, мама будет мной довольна если я их соберу"
    "Изабель долго гуляла по лесу и собрала много ягод, и совсем не заметила как забрела в глубь леса и потеряла дорогу домой"
    i "Уже тимнеет,  надо поскорее возращаться, иначе быть беде"
    "Изабель долго искала дорогу, ив набрела на старую  и на первый взгляд заброшенную избушку."
    scene izba
    
    i "Этот дом выглядит зловищи,но вдруг в нем есть карта или что-то что поможет мне выбраться и поскорее вернуться  домой."
    jump forest2
label forest2:     
    menu:
        i " Стоит ли мне туда заходить?"
        "Да, попробую отыскать там что нибудь полезное":
            jump izbain
        'Нет, меня это пугает, туда я точно не пойду! ' if raz > 0:
            jump hod2
            
        'Нет, мне не нравится эта затея, лучше поищу выход из леса или знакомую картинку' if raz==0:
           jump hod 
 
    return
label hod:
    $raz += 1
    scene les
    i "Идти туда, точно не лучшая идея. Кажется по той тропинке  я еще не ходила"

   
    i "а нет, кажется я ошиблась, пойду  ка я вон в ту сторону"
    scene izba 
    i " Что опять эта изба? как это возможно? я же шла в другую.  Это очень подозрительно." 
    jump forest2
label hod2:

    scene forestx
    i "Это все ооочень странно, я туда не пойду, пойду искать путь дальше."
    scene izba
   
    i "АААА, как это возможно"
    $ raz += 1
    if raz == 3 and LoveYou == False:
        jump lesnik
        
   
    jump forest2
label izbain:
    scene izbainf
    i "Мамочки, как же тут стращно, я очень боюсь"
    menu:
        "Что мне сейчас сделать?"
        "Там селва есть шкаф, интересно что в нем есть":
            jump boock
        "Кажется в правом углустоит стол, осмотрю его":
            jump tabel
        "Мне не нравится эта идея, уйду ка я отсюда!":
            jump hod2
label tabel:
    
    scene izbainf
    show tabel
    i "Интересный стол, ого  а что это за две книги черная и белая?"
    menu:
        "Какую книгу открыть?"
        "Белую":
            jump white
        "Черную":
            jump black
        "Нет, я уйду отсюда":
            jump hod2
        
define i = Character("Изабель", color="#c8ffc8")
label boock:
    scene bookcase
    i 'Я вижу, что тут две книги лежат, будто зазывая меня взять их.'
    menu:
        'Мне нужно выбрать, какую книгу я возьму'
        'Взять черную':
            jump black
        'Взять белую':
            jump white
        "Взять карту":
            $ renpy.notify('Карта получена')
            menu:
                "открыть карту"
                "ДА":
                    scene black
                    "Если вы не знаете кто такой патрик, то советую походить, побродить, и может наткнетесь на лесника"
                    jump hod2
                "Нет":
                    jump hod2
    return
label lesnik:
    scene les
    show lesnik
    l " Привет девочка, что ты тут делаешь, здесь сейчас происходят очень странные дела, я знаю короткий путь"
    i " Что? что происходит. Я совсем ничего не понимю!!!"
    l "Нет времени объяснять, бежиииим!"
    scene street2
    show lesnik
    l "Теперь мы в безопасности, и я могу тебе все рассказать"
    l "Тем лесом управляет злая волшебница. Она хотела заманить тебя в свой дом и обречь тебя на вечные страдания "
    i "Меня пугает все это"
    l " Ты не представляешь какие мистические и загадочные истории тут происходят, я зову тебя помочь" 
    jump end
label park:
    scene park
    "спустя 15 минут"
    i "И именно поэтому я переехала в новый дом"
    p "Да уж, вот так и история" 
    p "Как насчет пойти и повеселится?"
    i "Было бы неплохо!"
    p "Тогда давай пойдем прокатимся на Колесе Обозрения!"
    menu:
        "пойти с Патриком?"
        "Да":
            i "Да,давай пойдем"
            "спустя 30 минут хорошо проведенново времени"
            p "Это было так классно и страшно одновременно!!"
            i "Да,мне понравилось"
            p "А Ты не хочешь пойти в лес?"
            i "Хм"
            i "Давай, там и прогуляемся"
            scene les
            p "Ох, прости я совсем забыл что в 15 мне нужно быть дома, ПРОСТИ Я ПОБЕЖАЛ"
            hide pat with moveoutleft
            i"И чего это он так убежал, ну ладнос страннло"
            jump forest 
        "Нет":
            i "Нет,спасибо"
            i "Я пожалуй пойду"
            show street2  
            i "И зачем я только ему соврала, ну ладно, он мне начал надоедать"
            i "Хм,а не пойти ли мне всетаки направо"  
            jump forest 
label black:
    scene teleport
    play sound teleport
    pause
    scene dark
    i 'О нет, что произошло'
    show blackw with dissolve
    bw 'Приветствую Изабель, я ждала тебя.'
    i 'Как это ждала?! Я не понимаю ка здесь оказалась... Скачала была книга... Вроде черная'
    bw 'Это я привела тебя сюда, ты со своего приезда была под моим присмотром.'
    bw 'Устроить твоего папу на работу, твой переезд'
    if LoveYou:
        bw 'И встреча с тем милым мальчиком'
    i 'Не может этого быть!'
    i 'Где я вообще? И главное - Зачем я тебе так понадобилась???'
    bw 'Не торопись, девочка моя. Я призвала тебя сюда, чтобы получить твой медальон который сейчас лежит в твоем правом кармане.'
    i 'Медальон? Но зачем он тебе?'
    bw 'Не думай об этом, девочка моя. Осмотрись вокруг... Вся эта темная аура этого загадочного леса...'
    bw 'Знакомо ли тебе это? Помнишь ли ты все все свои темные желания?'
    bw 'Оставайся со мной, девочка моя и наслаждайся страданием...'
    i 'Её голос так заманивает меня...'
    menu:
        'Решительный выбор:'
        "Остаться вместе с королевой темной магии":
            $ renpy.notify('Медальон утерян...')
            'что же я наделала...'
        'Вспомнить себя и убежать':
            scene black
            show pat at left with dissolve
            show mam at right with dissolve
            'Мои друзья и семья...'
            scene black
            scene room
            'Мой дом...'
            scene black
            'Я должна убежать любой ценой'
            scene dark
            show blackw
            bw 'Ну что?'
            i 'Медальон, помоги мне убежать, прошу'
            $ renpy.notify('Медальон использован и утерян')
            scene teleport
            play sound teleport
            scene room
            i 'Я кажется дома...'
            'Хорошая концовка'
    jump end


label white:
    scene teleport
    play sound teleport
    pause
    scene white
    i 'О нет, что произошло'
    show whitew with dissolve
    ww 'Здравствуй Изабель.'
    i 'Здравствуйте. Простите, но вы не знаете, как я сюда попала?'
    ww 'Это я привела тебя сюда'
    i 'Но как? И зачем?'
    ww 'Изабель, я подстроила все чтобы ты попала ко мне, от твоего переезда до выбора белой книги'
    i 'Что ты хочешь от меня?'
    ww 'Моя маленькая Изабель, я благодарю тебя за правильный выбор!'
    i 'Но что я сделала?'
    ww 'Я поставила белую книгу рядом с черной чтобы ты выбрала. И ты выбрала светлую! Спасибо тебе, я отправлю тебя домой, не волнуйся.'
    i 'Хорошо, добрая волшебница'
    scene teleport
    play sound teleport
    scene street2
    i 'Это было прекрасное приключение...'
    jump end
    return
label end:
    scene black
    s "Спасибо за прохождение данной новеллы, мы надеемся что она вам очень понравилась"
    menu:
        s "Оцените подалуйста нашу новеллу"
        "1":   
            "Эх жалко, будем старасться"
        "2":
            "Эх жалко, будем старасться"
        "3":
            "Это не то что мы ожидали, будем старасться"
        "4":   
            "Неплохо, будем стараться чтобы получить максимум"
        "5":
            "Спасибо, будем работать и творить для вас!"
    scene pay
    "Тык тык тыквенный пирог"
    return
    