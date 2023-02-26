from django.views import generic
from blog.models import Post, Category

# Create your views here.
class PostListView(generic.ListView):
    model = Post
    template_name = 'core/frontpage.html'
    
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
