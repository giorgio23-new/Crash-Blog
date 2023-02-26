from django.views import generic
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import CommentForm

# Create your views here.
class PostDetailsView(generic.DetailView, generic.edit.FormMixin):
    model = Post
    form_class = CommentForm
    slug_field = 'slug'
    template_name = 'blog/details.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('blog:post_details', kwargs={'category_slug': self.object.posts, 'slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super(PostDetailsView, self).form_valid(form)

class CategoryListView(generic.ListView):
    template_name = 'blog/category.html'

    def get_queryset(self):
        self.categories = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(posts=self.categories)

class SearchListView(generic.ListView):
    template_name = 'core/frontpage.html'

    def get_queryset(self):
        word = self.request.GET.get('query', '')
        return Post.objects.filter(Q(title__icontains=word) | Q(intro__icontains=word) | Q(body__icontains=word))
