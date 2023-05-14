import play

play.set_backdrop("purple")

#коли програма прцює фнкція для початку гри
@play.when_program_starts
def start():
    text1 = play.new_text(words="г - гладити, з - зіграти, с - спати" , x=0 , y=250, font_size=40)
    text2 = play.new_text(words="к - кормити, п - прибрати, пробіл - піти", x=0 , y=210, font_size=40)
    img = play.new_image(image="hello!.jpg", x=0, y=0, size=100)

#повторювати завжди(ігровий цикл)
@play.repeat_forever
def do():
    pass

#запуск програми
play.start_program()
