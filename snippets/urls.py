from django.urls import path, include
from snippets.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import permissions, renderers

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet, basename='snippets')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
        path('', include(router.urls)),
]

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight' },
    renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})



urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])


# urlpatterns = [
#         path('', api_root),
#         path('snippets/', SnippetList.as_view()),
#         path('snippets/<int:pk>/', SnippetDetail.as_view()),
#         path('snippets/<int:pk>/highlight/', SnippetHighlight.as_view()),
#         path('users/', UserList.as_view()),
#         path('users/<int:pk>/', UserDetail.as_view()),
# ]
# 
# urlpatterns += [
#         path('api-auth/', include('rest_framework.urls'))
# ]
# 
# 
# urlpatterns = format_suffix_patterns(urlpatterns)a

