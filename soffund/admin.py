from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Child, Documents, FundDocuments


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
	list_display = ('id', 'surname', 'name', 'lastname', 'birthday', 'get_image', 'category', 'money')
	readonly_fields = ('get_image',)
	list_display_links = ('surname', 'name')  # Ссылка по имени и фамилии на основную запись
	list_filter = ('category',)  # Фильтр по категории
	save_on_top = True  # Кнопка Сохранить наверху

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.photo.url} width="50", height="60">')

	get_image.short_description = 'Изображение'


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
	list_display = ('child', 'document_image')
	search_fields = ('child__surname',)  # поиск по ребенку .... проверить поиск по фамилии!!!


admin.site.register(FundDocuments)
