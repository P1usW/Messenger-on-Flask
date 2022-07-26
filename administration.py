from flask_admin import BaseView, AdminIndexView, expose
from flask_login import current_user, login_required
from flask import redirect, url_for

class DashboardView(AdminIndexView):
    @expose('/')
    @login_required
    def index(self):
        if current_user.admin_mode:
            return self.render('admin/admin_index.html')
        return redirect(url_for('main.index'))


