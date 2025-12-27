# 9-12. Multiple Modules: Store the User class in one module, and store the
# Privileges and Admin classes in a separate module. In a separate file, create
# an Admin instance and call show_privileges() to show that everything is still
# working correctly
from modules_exercises_chapter_9.admin_class import Admin, Privileges
from modules_exercises_chapter_9.user_class import User

privileges = Privileges(['can edit post', 'can delete post', 'can ban other users'])
admin = Admin('Lucas', 'Bazzani', 1, 'lucas@email.com', '123456', privileges)

admin.privileges.show_privileges()
