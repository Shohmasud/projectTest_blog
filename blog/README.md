    Это приложение Блог, с реализацией дерево коментарий состоящий из вложеностей

    Какие технологии были использованны?
    ---Пользовательская часть:fron-end
       Html
       Css
       Js

     ----Backend:
       Django,DjangoRestFramework,DjangoORM,Python,PostgreSql,Админка

     ----Для запуска было использованно:
       Docker,Docker-compose
 
                               Функцианал приложения
                             Вывод приложения по URL:
                           1)http://127.0.0.1:8000/blog/show/
    Пользовательская часть:
     1)Оформлено html,css стили , js
     2)Данные(блог(тект,название),комментарии) можно отправить с помощью fron-end
     4)Комментарии состоят из любой вложенности
     5)Можно добавить неограниченное количество родительских и дочерних коментарий
     6)Отображаются коментарии состоящий из любой вложенности отдельно
     7)Блог не связан с моделью комментарий
     8)Отображаются только выбранный блог к которой крепяться комментарии,
      блогов можно добавить несколько,но выбрать нужно один из них указывая
      True либо false при отпрвке через Api или Админку по умолчанию используется
      False при добавлении блога(назв,текст),  то есть нужно указать True в полк
      модели которое является Boolean


      
      Back-end:
      1)Использованно Django 
      2)Django ORM
      3)PostgresSQL
      4)Админка
      5)DjangoRESTframework

                                    REST API:
       1)Комментарии можно получить с помощью API Методо GET
       # GET
       path('get/api/v6/comments/', SerializerComments.as_view()),
       path('get/api/v6/create/blog/show/', SerializerBlogShow.as_view()),
       Пример
    {
        "id": 9,
        "body": "adads",
        "created_on": "2021-08-04T18:04:41Z",
        "parent": null
    }
      
      2)Комментарии можно отправить с помощью API
         # Post
      path('post/api/v6/create/comments/', SerializerCommentsCreate.as_view()),
      path('post/api/v6/create/blog/', SerializerBlogCreate.as_view())

                    