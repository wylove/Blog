from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Blog

def index(request, page_index=1):
	post_list = Blog.objects.all().order_by('-date')
	paginator = Paginator(post_list, 5)

	try:
		posts = paginator.page(page_index)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(1)

	return render_to_response('blog/index.html', {'posts': posts})

def about(request):
	return render_to_response('blog/about.html')

def detail(request, post_id):
	post = get_object_or_404(Blog, id=post_id)
	return render_to_response('blog/detail.html', {'post': post})

