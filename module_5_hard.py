import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = ""
        self.password = ""
        self.age = 0

    def __hash__(self):
        return self.password

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def add(self, *args):                   # принимает неограниченное кол-во объектов класса Video
        video = []
        check_video = False
        for i in args:
            video = [i.title, i.duration, i.time_now, i.adult_mode]
            if self.videos == []:
                self.videos.append(video)
            else:
                for j in self.videos:
                    if i.title != j[0]:
                        check_video = True
                    else:
                        check_video = False
                        break
                if check_video == True:
                    self.videos.append(video)
                else:
                    print(f'\033[31m фильм {i.title} уже существует !!! \033[0m')
                    time.sleep(1)
            video = []

    def get_videos(self, search_video): #принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое слово
        self.search_video = search_video.lower()
        self.my_search_list = []
        for i in self.videos:
            my_str = i[0]
            self.my_str = my_str.lower()
            if self.my_str.find(self.search_video) != -1:
                self.my_search_list.append(i[0])
        return self.my_search_list

    def watch_video(self, get_video): # принимает название фильма
        self.get_video = get_video
        if self.current_user != None:
            for i in self.videos:
                if i[0] == self.get_video and i[3] == True:
                    self.current_duration = i[1]
                    self.current_time_now = i[2]
                    if self.age > 18:
                        print(f'\033[34m Воспроизводится: {self.get_video}\033[0m')
                        for j in range(self.current_duration):
                            self.current_time_now = j
                            print("\033[35m * \033[0m", end="")
                            print(self.current_time_now, sep="", end="")
                            time.sleep(1)
                        print("\033[31m  Конец видео\033[0m")
                        time.sleep(2)
                    else:
                        print("\033[31m Вам нет 18 лет, пожалуйста, покиньте страницу\033[0m")
                    self.log_out()
        else:
            print("\033[31m Войдите в аккаунт, чтобы смотреть видео\033[0m")

    def register(self, nickname, password, age): # добавляет пользователя в список, если пользователя не существует
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.user = [self.nickname, self.password, self.age]
        self.veryfy_user = 0
        for i in self.users:
            if i[0] == self.nickname:   # проверяет имя пользователя
                self.log_in(self.nickname, self.password)     # авторизирует

        if self.veryfy_user == 0:     # если пользователь не найден, добавляет и автоматически авторизирует
            self.users.append(self.user)
            self.log_in(self.nickname, self.password)
        elif self.veryfy_user == 1:    # авторизация успешна
            print(f'\033[32m Пользователь {self.nickname} авторизирован\033[0m')
        elif self.veryfy_user == 2:
            print(f'\033[32m Пользователь {self.login} уже существует \033[0m')

    def log_in(self, login, password): # пытается найти пользователя в users с такими же логином и паролем
        self.login = login
        self.password = password
        for i in self.users:
            if i[0] == self.login and i[1] == self.password:
                self.current_user = self.login
                self.veryfy_user = 1
            elif i[0] == self.login and i[1] != self.password:
                self.veryfy_user = 2
        return self.veryfy_user

    def log_out(self): # сброс текущего пользователя на None
        self.current_user = None
        self.nickname = ""
        self.password = hash("")
        self.age = 0
        return

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')