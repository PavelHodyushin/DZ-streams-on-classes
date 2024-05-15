from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, skill, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.skill = skill


    def run(self):
        enemy = 100
        day = 0
        print(f"{self.name}, на нас напали!")
        for i in range(11):
            sleep(1)
            enemy -= self.skill
            day += 1
            if enemy == 0:
                break
            print(f"{self.name} сражается {day} день(дня)..., осталось {enemy} воинов")
        if enemy == 0:
            print(f"{self.name} одержал победу спустя {day} дней!")





knight1 = Knight("Sir Lancelot",10)   # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)    # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print("Все битвы закончились!")