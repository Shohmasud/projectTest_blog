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
                                 

                                 Запуск приложения
      1)Скачиваем проект projectTest_blog
      2)После скачивания проекта,извлекаем папку projectTest_blog
      3) После извлечени переходи в projectTest_blog-master/blog 
      4)Переходим в родительскую папку blog
      3)переходим  в терминал вводим:
      * docker-compose build ---- запускаеться Dockerfile
      * docker-compose up------- поднимаем проект, запускается Docker-compose.yml
       в которой устанавливается база данных и джанго и миграции и запускаеться сервер

       4)Далее создадим супер пользователя не остонавливая контейнер, 
         переходим в терминал и перейдём в папку с проетом где docker 
       5) Создадим суперпользователя с помощью комманды:
         * docker exec -it название контейнера в котором запущено
           проект python manage.py createsuperuser
             -название запущенного контейнера с проектом можно получить с помощью комонды:
                * docker-compose ps -a
          
       6)Переходим на  посковик браузера и вводим 127.0.0.1 
       7)Далее вводим url из приложения  и получаем результат


                                    REST API:
       1)Комментарии можно получить с помощью API Методо GET
       # GET
       path('get/api/v6/comments/', SerializerComments.as_view()),

      2)Комментарии можно отправить с помощью API
         # Post
      path('post/api/v6/create/comments/', SerializerCommentsCreate.as_view()),
       Пример
    {
        "id": 9,
        "body": "adads",
        "created_on": "2021-08-04T18:04:41Z",
        "parent": null
    }


                                    REST API:
       1)Блоги можно получить с помощью API Методо GET
       # GET
        path('get/api/v6/blog/show/', SerializerBlogShow.as_view()),

      2)Блоги можно отправить с помощью API
         # Post
         path('post/api/v6/create/blog/', SerializerBlogCreate.as_view())

       Пример
          {
        "id": 5,
        "nameBlog": "MY BLOG",
        "textBlog": "\"But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?\"\r\n\r\nАбзац 1.10.33 \"de Finibus Bonorum et Malorum\", написанный Цицероном в 45 году н.э.\r\n\"At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.\"\r\n\r\nАнглийский перевод 1914 года, H. Rackham\r\n\"On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best, every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains.\"",
        "showBlog": true
         }
      
                                  