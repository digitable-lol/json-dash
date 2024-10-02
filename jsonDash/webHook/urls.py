from rest_framework.routers import DefaultRouter
from . import views

app_name = "webHook"

router = DefaultRouter()
router.register('jsonNode',views.Node_API_View,basename='jsonNode')
urlpatterns = router.urls