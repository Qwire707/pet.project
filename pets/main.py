import play

play.set_backdrop("purple")

#коли програма прцює фнкція для початку гри
@play.when_program_starts
def start():
    global player, speech
    text1 = play.new_text(words="г - гладити, р - розсмішити, в - відпочивати" , x=0 , y=250, font_size=40)
    text2 = play.new_text(words="к - кормити, п - причепурити, пробіл - піти", x=0 , y=210, font_size=40)
    player = play.new_image(image="hello!.jpg", x=0, y=0, size=100)
    speech = play.new_text(words="Hello my friend", x=0, y=-250, font_size=40)


#повторювати завжди(ігровий цикл)
@play.repeat_forever
async def do():
    if play.key_is_pressed("г") or play.key_is_pressed("Г"):
        player.image = "hello!.jpg"
        speech.words = "Hello my friend"
        await play.timer(2.0)
        player.image = "normX2.jpg"
        speech.words = "Good"
        await play.timer(1.0)
    if play.key_is_pressed("р") or play.key_is_pressed("Р"):
        await play.timer(2.0)
        player.image = "smile.jpg"
        speech.words = "Nice joke*)"
    if play.key_is_pressed("к") or play.key_is_pressed("К"):
        await play.timer(1.0)
        player.image = "boss.jpg"
        speech.words = "thanks for the food*)"
    if play.key_is_pressed("в") or play.key_is_pressed("В"):
        await play.timer(1.0)
        player.image = "lazy.jpg"
        speech.words = "how to rest well*)"
    if play.key_is_pressed("п"):
        await play.timer(1.0)
        player.image = "pon.jpg"
        speech.words = "don't touch me, I'm still resting"
    if play.key_is_pressed("П"):
        await play.timer(1.0)
        player.image = "Beautiful.jpg"
        speech.words = "i am beautiful now"


    



    
        

    




    

#запуск програми
play.start_program()
