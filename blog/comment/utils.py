from .models import Blog



#/// Проверяем если в модели блога ,указана True, то получаем название блога для её вывода
def blog_name():
    try:
        obj = Blog.objects.get(showBlog=True)
        show = Blog.objects.get(showBlog=True).showBlog
        if show is True:
            name = obj.nameBlog
            return name
        return None
    except:
        return None

#/// Проверяем если в модели блога ,указана True, то получаем содержание блога для её вывода
def blog_text():
    try:
        obj = Blog.objects.get(showBlog=True)
        show = Blog.objects.get(showBlog=True).showBlog
        if show is True:
            text = obj.textBlog
            return text
        return None
    except:
        return None