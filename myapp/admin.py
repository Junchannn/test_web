from django.contrib import admin
from .models import Post

# class PostAdmin(admin.ModelAdmin):
#     class Media:
#         css = {
#             'all': ('admin/css/custom.css',)  # Link to your custom CSS
#         }
#     list_display = ('title', 'created_at', 'custom_field')
#     list_filter = ('created_at',)
#     search_fields = ('title',)

#     def custom_field(self, obj):
#         return f"Custom: {obj.title}"
#     custom_field.short_description = "Custom Title"

#     # Adding a custom action
#     actions = ['mark_as_important']

#     def mark_as_important(self, request, queryset):
#         queryset.update(title='IMPORTANT: ' + queryset[0].title)
#         self.message_user(request, "Selected posts marked as important.")
#     mark_as_important.short_description = "Mark selected posts as important"

# admin.site.register(Post, PostAdmin)
