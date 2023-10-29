from django.shortcuts import render,HttpResponse,get_object_or_404
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from app.models import Post, Category, Comment
from .froms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

# Create your views here.

# def home(request):
#     return render(request,'app/home.html')

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'app/home.html'
    ordering = ['-post_date']
    # ordering = ['-id']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request,'app/categories.html',{'cats':cats.title(),'category_posts':category_posts})
class Article_View(DetailView):
    model = Post
    template_name = 'app/articleview.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Article_View, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'app/add_post.html'
    # fields = '__all__'
    # fields = ('title','body')

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'app/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'app/addcategory.html'
    fields = '__all__'
    # fields = ('title','body')
class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'app/updatepost.html'
    # fields = ('title','title_tag','body')

class DeletePost(DeleteView):
    model = Post
    template_name = 'app/deletepost.html'
    success_url = reverse_lazy('home')
