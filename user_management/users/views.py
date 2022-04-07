from django.shortcuts import render, redirect

# imports to create a self-made fields view
from django.contrib.auth.views import LoginView  # import of the built-in view
from django.contrib import messages
from django.views import View
from .forms import RegisterForm, LoginForm

# imports for file uploading
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def home(request):
    return render(request, '../templates/users_templates/home.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users_templates/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        # Aquí, si el formulario es válido, se registra al usuario
        # yo quiero que se congele el registro hasta que se comprueben los datos
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for{username}')
            return redirect(to='')

        return render(request, self.template_name, {'form': form})


class LoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True
        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(LoginView, self).form_valid(form)


class ProfileView(View):
    template_name = 'users_templates/profile.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.FILES['users_file']:
            myfile = request.FILES['users_file']  # File ref
            fs = FileSystemStorage()
            filename = FileSystemStorage.save(myfile.name, myfile)  # Actual storage ¿?
            uploaded_file_url = FileSystemStorage.url(filename)
            """
            return render(request, 'core/simple_upload.html', {
                'uploaded_file_url': uploaded_file_url
            })
        
        return render(request, 'core/simple_upload.html')
            """
        # guardar el archivo
        return redirect(to='')
