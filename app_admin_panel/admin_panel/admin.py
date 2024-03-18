from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportModelAdmin
from import_export.resources import ModelResource
from admin_panel.models import User, Category, SubCategory, Product, UserProduct, Order, Dispatcher, Post


class CustomImportExport(ImportExportModelAdmin, ExportActionModelAdmin):
    pass


# setup import
class UserResource(ModelResource):
    class Meta:
        model = User
        import_id_fields = ('user_id',)


@admin.register(User)
class UserAdmin(CustomImportExport):
    resource_classes = [UserResource]
    list_display = ('user_id', 'first_name', 'created_at')
    list_display_links = ('user_id', 'first_name',)


@admin.register(Category)
class CategoryAdmin(CustomImportExport):
    list_display = [field.name for field in Category._meta.fields]
    list_editable = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(CustomImportExport):
    list_display = [field.name for field in SubCategory._meta.fields]
    list_editable = ('name',)


@admin.register(UserProduct)
class UserProductAdmin(CustomImportExport):
    list_display = ('id', 'product', 'user')
    list_display_links = ('id', 'product', 'user')


@admin.register(Product)
class ProductAdmin(CustomImportExport):
    list_display = [field.name for field in Product._meta.fields]
    list_editable = [field.name for field in Product._meta.fields if field.name != 'id']


@admin.register(Order)
class OrderAdmin(CustomImportExport):
    list_display = ('id', 'user_id', 'is_paid', 'created_at')


@admin.register(Dispatcher)
class OrderAdmin(CustomImportExport):
    list_display = [field.name for field in Dispatcher._meta.fields]


@admin.register(Post)
class OrderAdmin(CustomImportExport):
    list_display = [field.name for field in Post._meta.fields]
    list_editable = [field.name for field in Post._meta.fields if field.name != 'id' and field.name != 'created_at']


# sort models from admin.py by their registering (not alphabetically)
def get_app_list(self, request, app_label=None):
    app_dict = self._build_app_dict(request, app_label)
    app_list = list(app_dict.values())
    return app_list


admin.AdminSite.get_app_list = get_app_list
