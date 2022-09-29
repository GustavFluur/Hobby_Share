from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponseForbidden
from .models import Post
from .forms import CommentForm, PostForm
from django.utils.text import slugify
from django.shortcuts import redirect



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


def about(request):
    return render(request, 'about.html')
    

def contact(request):
    return render(request, 'contact.html')


class EditPost(View):
    def get(self, request, id, *args, **kwargs):
        post = get_object_or_404(Post, id=id)
        return render( 
            request,
            'editpost.html',
            {
                "form": PostForm(instance=post)
            }
        )


    def post(self, request, id, *args, **kwargs):
        post = Post.objects.get(id=id)
        post_form = PostForm(request.POST, request.FILES, instance=post)

        if post_form.is_valid():
            
            post = post_form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect('post_detail', slug=post.slug)

        return render(
            request,
            "editpost.html",
            {
                "form": post_form,
            },
        )

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=False).order_by("-created_on")
        liked = post.likes.filter(id=self.request.user.id).exists()
        can_edit_post = self.request.user.id == post.author.id

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "can_edit_post": can_edit_post
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.approved = True
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

    
class CreatePost(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "create_post.html", 
            {
                "form": PostForm()
            },
        )
        

    def post(self, request, *args, **kwargs):

        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post_form.instance.author = request.user
            post = post_form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect('post_detail', slug=post.slug)

        return render(
            request,
            "create_post.html",
            {
                "form": post_form,
            },
        )


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostDelete(View):

    def get(self, request, id, *args, **kwargs):
        post = get_object_or_404(Post, id=id)
        post.delete()

        return HttpResponseRedirect(reverse('home'))

