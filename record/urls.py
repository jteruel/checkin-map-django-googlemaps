from django.conf.urls import url

from .views import(
	create_record,
	RecordAPIView,
	record_map,
    )

urlpatterns = [
	url(r'^create/$', create_record, name="create_record"),
	url(r'^api/$', RecordAPIView.as_view(), name="record API"),
	url(r'^view/$', record_map, name="record map"),
]