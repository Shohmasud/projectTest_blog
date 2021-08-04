#/// Необходиммые модули для работы приложения из файла personalModul.py

#/// Rest Api методом GET
from .personalModul import  *

# API КЛАССЫ
#// Serializer для вывода ранее созданных коментарий
class SerializerComments(APIView):
    def get(self,request):
        all_object = Comments.objects.all()
        serializers = sComment(all_object,many=True)
        return Response(serializers.data)

#// Serializer для создании(отправки) элементов коментарий
class SerializerCommentsCreate(APIView):
        def post(self, request):  # отправим название файла csv,считываем и добавляем данные в базу данных
            serializer = sCommentCreate(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("OK")
            return Response("ERROR")

#// Serializer для создания(отпрвки) элементов Блога
class SerializerBlogCreate(APIView):
    def post(self, request):
        serializer = sSerializerBlogCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("OK")
        return Response("ERROR")

#// Serializer для вывода элементов Блога
class SerializerBlogShow(APIView):
    def get(self, request):
        all_object = Blog.objects.all()
        serializers = sSerializerBlogShow(all_object,many=True)
        return Response(serializers.data)


"""" Класс описывающий вывод html элементов
    и отпраку данных в форму и её вывод """
class PostListView(View):
    # /// При вызове этого метода выводим необходимые данные
    def get(self, request):
        # Пишем обработчика ошибки , при удалении самой верней вершины дерево комментарий только его
        # возникновении ошибки mptt модуля
        try:
            # /// Выполняет функцию первоначального входа на страничку приложения
            first_visitSite = 'False'

            #/// Экземпляры формы
            form = PostForm()
            form_child = PostFormChild()

            #/// Получаем название нужного блога которое нужно вывести ,если установлен True
            blog_names = blog_name()
            blog_texts = blog_text()

            # ///Модель комментов которое передаётся в mptt тег, для вывода дерево
            comments = Comments.objects.all()
            return render(request, 'post_list.html', {'form': form, 'comments': comments,
                                                      'form_child': form_child, 'i': first_visitSite,
                                                      'blog_name': blog_name, 'blog_text': blog_text})
        #// Иначе заново перезапускаемся
        except:
            delete = Comments.objects.all().delete()
            return redirect('post-list')

    # /// При вызове этого метода сохраняеем отправленые элементы в базу
    def post(self, request):
        form_child = PostFormChild()

        #/// Получаем данные из формы
        first_visitSite = 'True'
        form = PostForm(request.POST)

        #/// Если данные валидны то сохроняем полученные данные из формы в базу данных
        if form.is_valid():
            body = request.POST['body']
            createChild = Comments.objects.create(body=body,parent=None).save()

            # ///Модель комментов которое передаётся в mptt тег, для вывода дерево
            comment = Comments.objects.all()
            # /// Получаем название нужного блога которое нужно вывести ,если установлен True
            blog_names = blog_name()
            blog_texts = blog_text()
            return render(request, 'post_list.html', {'form': form,'comments':comment,
                                                      'form_child':form_child,'i': first_visitSite,
                                                      'blog_name':blog_name, 'blog_text':blog_text})
        pass



"""" Класс описывающий вывод html элементов
    и удаления данных отправленные из формы """
class PostDeleteView(View):
    # /// При вызове этого метода удаляем ранее сохранёные элементы базы
    def get(self,request,pk=None):

        #/// Выполняет функцию первоначального входа на страничку приложения
        first_visitSite = 'True'

        #/// id нужного элемета модели
        pk_num = int(pk)

        # /// Экземпляры формы
        form = PostForm()
        form_child = PostFormChild()

        # /// Выполняет функцию удаления
        delete = Comments.objects.get(pk=pk_num).delete()

        # ///Модель комментов которое передаётся в mptt тег, для вывода дерево
        comments = Comments.objects.all()
        return render(request, 'delete.html', {'form': form, 'comments': comments,
                                                  'form_child': form_child, 'i': first_visitSite,
                                                  'blog_name': blog_name, 'blog_text': blog_text})



"""" Класс описывающий вывод html элементов
    и удаления данных отправленные из формы """
class PostListCommentView(View):
    # /// Если данные валидны то сохроняем полученные данные из формы в базу данных
    def post(self, request,pk=None):

        #/// Выполняет функцию удаления
        form_child = PostFormChild(request.POST)
        if form_child.is_valid():
            body = request.POST['body']
            post_pk =Comments.objects.get(pk=pk)
            createChild = Comments.objects.create(body=body,parent=post_pk).save()

            # /// Последующие входа на страничку приложения
            first_visitSite = 'True'

            #/// Экземпляры формы
            form_child = PostFormChild()
            form = PostForm()

            # ///Модель комментов которое передаётся в mptt тег, для вывода дерево
            comments = Comments.objects.all()
            return render(request, 'delete.html', {'form': form, 'comments': comments,
                                                   'form_child': form_child, 'i': first_visitSite,
                                                   'blog_name': blog_name, 'blog_text': blog_text})