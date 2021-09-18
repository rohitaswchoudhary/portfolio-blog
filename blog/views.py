from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.views.generic import ListView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin



class MyPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise


class BlogListView(ListView):
    model = Post
    template_name = "blog/home.html"

    class Meta:
        ordering = ['-id']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get("page", 1)
        posts = Post.objects.all()
        paginator = self.paginator_class(posts, self.paginate_by)

        posts = paginator.page(page)

        context["posts"] = posts
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog/post_new.html"
    fields = ["title", "author", "body"]



class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("home")
