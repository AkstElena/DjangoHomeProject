"""
Домашнее задание
� Создайте пару представлений в вашем первом приложении: главная и о себе.
� Внутри каждого представления должна быть переменная html - многострочный текст с HTML вёрсткой и данными о
вашем первом Django сайте и о вас.
� *Сохраняйте в логи данные о посещении страниц
"""
from django.shortcuts import render
from django.http import HttpResponse
# import logging
#
# logger = logging.getLogger(__name__)


def main(request):
    html = """
    <!doctype html>
        <html lang="ru">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link rel="icon" href="data:;base64,=">
            <title>
                  Homework 1 - Main
            </title>
        </head>
        <body>
        <div class="container-fluid">
            <ul class="nav nav-pills justify-content-end align-items-end">
                <li class="nav-item"><a href="" class="nav-link">Главная</a></li>
                <li class="nav-item"><a href="/hw/about/" class="nav-link">Обо мне</a></li>
            </ul>
        

                <h1 class="heading">Главная страница</h1>
                <h2 class="heading">Первый проект на Django</h2>
                <h3 class="heading">Что такое Django</h3>
                
                <p>
                 Django — это высокоуровневый Python веб-фреймворк, который позволяет быстро создавать безопасные и 
                 поддерживаемые веб-сайты. Созданный опытными разработчиками, Django берёт на себя большую часть хлопот
                веб-разработки, поэтому вы можете сосредоточиться на написании своего веб-приложения без необходимости
                изобретать велосипед. Он бесплатный и с открытым исходным кодом, имеет растущее и активное сообщество, 
                отличную документацию и множество вариантов как бесплатной, так и платной поддержки.</p>
                <p>Django помогает писать программное обеспечение, которое будет:</p>
                <div class="li">

                    <li>Полным</li>
                    <p>
                    Django следует философии «Всё включено» и предоставляет почти всё, что разработчики могут захотеть 
                    сделать «из коробки». Поскольку всё, что вам нужно, является частью единого «продукта», всё это 
                    безупречно работает вместе, соответствует последовательным принципам проектирования и имеет обширную 
                    и актуальную документацию.
                    </p>
                    
                    <li>Разносторонним</li>
                    <p>
                    Django может быть (и был) использован для создания практически любого типа веб-сайтов — от систем 
                    управления контентом и wiki до социальных сетей и новостных сайтов. Он может работать с любой 
                    клиентской средой и может доставлять контент практически в любом формате 
                    (включая HTML, RSS-каналы, JSON, XML и т. д.). Сайт, который вы сейчас читаете,
                     создан с помощью Django!
                     </p>
                    <p> Хотя Django предоставляет решения практически для любой функциональности, которая вам может 
                     понадобиться (например, для нескольких популярных баз данных, шаблонизаторов и т. д.), 
                     внутренне он также может быть расширен сторонними компонентами, если это необходимо.
                    </p>
                    <li>Безопасным</li>
                    <p>
                    Django помогает разработчикам избежать многих распространённых ошибок безопасности, предоставляя 
                    фреймворк, разработанный чтобы «делать правильные вещи» для автоматической защиты сайта. Например, 
                    Django предоставляет безопасный способ управления учётными записями пользователей и паролями, 
                    избегая распространённых ошибок, таких как размещение информации о сеансе в файлы cookie, 
                    где она уязвима (вместо этого файлы cookie содержат только ключ, а фактические данные хранятся в 
                    базе данных) или непосредственное хранение паролей вместо хэша пароля.</p>
                    <p>Хэш пароля — это значение фиксированной длины, созданное путём обработки пароля через 
                    криптографическую хэш-функцию Django может проверить правильность введённого пароля, 
                    пропустив его через хэш-функцию и сравнив вывод с сохранённым значением хэша. 
                    Благодаря «одностороннему» характеру функции, даже если сохранённое хэш-значение скомпрометировано, 
                    злоумышленнику будет сложно определить исходный пароль.    </p>
                    <p>Django, по умолчанию, обеспечивает защиту от многих уязвимостей, включая SQL-инъекцию, 
                    межсайтовый скриптинг, подделку межсайтовых запросов и кликджекинг (см. Website security для 
                    получения дополнительной информации об этих атаках).
                    </p>
                    <li>Масштабируемым</li>
                    <p>Django использует компонентную "shared-nothing" архитектуру (каждая её часть независима от других
                     и, следовательно, может быть заменена или изменена, если это необходимо). 
                     Чёткое разделение частей означает, что Django может масштабироваться при увеличении трафика, 
                     путём добавления оборудования на любом уровне: серверы кеширования, серверы баз данных или серверы 
                     приложений. Одни из самых загруженных сайтов успешно масштабировали Django (например, 
                     Instagram и Disqus, если назвать только два из них).                    
                    </p>                    
                    <li>Удобным в сопровождении</li>
                    <p>Код Django написан с использованием принципов и шаблонов проектирования, которые поощряют 
                    создание поддерживаемого и повторно используемого кода. В частности, в нём используется принцип 
                    «Don't Repeat Yourself» (DRY, «не повторяйся»), поэтому нет ненужного дублирования, что сокращает 
                    объём кода. Django также способствует группированию связанных функциональных возможностей в 
                    повторно используемые «приложения» и, на более низком уровне, группирует связанный код в модули 
                    (в соответствии с шаблоном Model View Controller (MVC) (en-US)).                    
                    </p>                    
                    <li>Переносным</li>
                    <p>
                    Django написан на Python, который работает на многих платформах. Это означает, что вы не привязаны 
                    к какой-либо конкретной серверной платформе и можете запускать приложения на многих версиях Linux, 
                    Windows и Mac OS X. Кроме того, Django хорошо поддерживается многими веб-хостингами, которые часто 
                    предоставляют определённую инфраструктуру и документацию для размещения сайтов Django.
                    </p>                    
              </div> 
            <div class="row fixed-bottom modal-footer">
                <hr>
                <p>Все права защищены &copy;</p>
            </div>
        </div>
        </body>
        </html>
    """
    return HttpResponse(html)


def about(request):
    html = """
    <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <link rel="icon" href="data:;base64,=">
            <title>Document</title>
          </head>
          <body>
            <title>
                  Homework 1 - About
            </title>
            <div class="container-fluid">
            <ul class="nav nav-pills justify-content-end align-items-end">
                <li class="nav-item"><a href="/hw/main" class="nav-link">Главная</a></li>
                <li class="nav-item"><a href="" class="nav-link">Обо мне</a></li>
            </ul>
            <div class="top">
              <h1 class="title">Акст Елена</h1>
              <img src="https://s.pfst.net/2015.11/9077976675676864009d9230eac50283d74b78de5a31_b.jpg" alt="top photo" 
              height="400" />
            </div>
            <div class="about">
              <h2 class="heading">Обо мне</h2>
              <div class="about__content">
                <p class="about__text">
                  Бывший преподаватель экономических дисциплин в вузе, ныне главный специалист экономического отдела в
                   отпуске по уходу за ребенком)
                  Хочу сменить сферу деятельности на it, как более перспективную, интересную и высокооплачиваемую
                </p>
              </div>
            </div>
            <div class="skills">
              <h2 class="heading">Навыки</h2>
              <div class="li">
                <li>Python</li>
                <li>Flask</li>
                <li>FastAPI</li>
                <li>Коммуникативность</li>
                <li>Быстрая обучаемость</li>          

              </div>
            </div>
            <div class="contacts">
              <h2 class="heading">Контакты</h2>
              <p class="text">akstelena@mail.ru</p>
              <p class="text">+7 903 319 73 54</p>
            </div>
            <div class="row fixed-bottom modal-footer">
                <hr>
                <p>Все права защищены &copy;</p>
            </div>
          </body>
        </html>
    """
    # logger.info('Data provided')
    return HttpResponse(html)
