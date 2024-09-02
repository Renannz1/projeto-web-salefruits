from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UsuarioForm, UserLoginForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout


from usuarios.models import Usuario
from django.contrib.auth.models import User




# ------- metodo para editar usuario -------
def editar_usuario(request, usuario_id):
    # Busca o objeto Usuario correspondente ao usuario_id no banco de dados.
    # Se não encontrar, retorna uma página 404 (não encontrado).
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    # Verifica se o usuário logado tem permissão para editar o perfil:
    # Se o usuário for um administrador (is_staff) ou o próprio dono do perfil (request.user == usuario.user).
    if request.user.is_staff or request.user == usuario.user:
        # Verifica se o método da requisição é POST (submissão do formulário)
        if request.method == 'POST':
            # Cria uma instância do formulário com os dados enviados e o perfil do usuário
            form = UsuarioForm(request.POST, instance=usuario)
            # Verifica se o formulário é válido
            if form.is_valid():
                # Salva as alterações no perfil do usuário
                form.save()
                # Redireciona para a página de listagem de usuários após salvar
                return redirect('listar_mural')
        else:
            # Se a requisição não for POST, cria uma instância do formulário com os dados atuais do perfil
            form = UsuarioForm(instance=usuario)
        # Renderiza a página de edição de usuário com o formulário (vazio ou preenchido)
        return render(request, 'editar_usuario.html', {'form': form})
    else:
        # Se o usuário logado não tiver permissão, lança uma exceção de permissão negada
        raise PermissionDenied




# ------- metodo para excluir usuario -------
def excluir_usuario(request, usuario_id):
    # Tenta obter o usuário pelo id, ou retorna um erro 404 se não encontrado
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    # Verifica se o usuário logado tem permissão para excluir
    if request.user.is_staff or request.user == usuario.user:
        # Verifica se o método da requisição é POST (confirmação de exclusão)
        if request.method == 'POST':
            # Exclui o usuário do banco de dados
            usuario.delete()
            # Redireciona para a página de listagem de usuários após a exclusão
            return redirect('listar_mural')
        # Renderiza a página de confirmação de exclusão com o usuário
        return render(request, 'confirmar_exclusao.html', {'usuario': usuario})
    else:
        # Se o usuário logado não tem permissão, levanta uma exceção de permissão negada
        raise PermissionDenied




# ------- metodo para exibir o perfil do usuario -------
@login_required
def perfil_usuario(request):
    # Obtém o perfil do usuário logado
    usuario = request.user.usuario

    # Verifica se o método da requisição é POST (submissão de formulário)
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados enviados e preenche com o perfil do usuário
        form = UsuarioForm(request.POST, instance=usuario)
        # Verifica se o formulário é válido
        if form.is_valid():
            # Salva as alterações no perfil do usuário
            form.save()
            # Redireciona para a página de listagem de usuários após salvar
            return redirect('listar_mural')
    else:
        # Se a requisição não for POST, cria uma instância do formulário com os dados atuais do perfil
        form = UsuarioForm(instance=usuario)

    # Renderiza o template de perfil do usuário com o formulário (vazio ou preenchido)
    return render(request, 'perfil_usuario.html', {'form': form})




# ------- metodo para cadastrar e criar usuario -------
def register(request):
    # Verifica se o metódo da requisição é do tipo POST
    if request.method == 'POST':
        # Cria instâncias dos formulários com os dados enviados via POST
        user_form = UserRegisterForm(request.POST)
        usuario_form = UsuarioForm(request.POST)
        
        # Verifica se ambos os formulários são válidos
        if user_form.is_valid() and usuario_form.is_valid():
            # Cria uma instância do modelo User, mas não a salva ainda
            user = user_form.save(commit=False)
            # Define a senha do usuário de forma segura
            user.set_password(user_form.cleaned_data['password'])
            # Salva o usuário no banco de dados
            user.save()
            

            # Cria uma instância do modelo Usuario, mas não a salva ainda
            usuario = usuario_form.save(commit=False)
            # Associa a instância de Usuario ao usuário recém-criado
            usuario.user = user
            # Salva a instância de Usuario no banco de dados
            usuario.save()

            login(request, user)
            return redirect('login')
    else:
        # Se o método não for POST, cria instâncias vazias dos formulários
        user_form = UserRegisterForm()
        usuario_form = UsuarioForm()

    # Renderiza o template 'register.html' com os formulários
    return render(request, 'register.html', {
        'user_form': user_form,
        'usuario_form': usuario_form
    })




# ------- metodo para login do usuario -------
def login_view(request):
    # Verifica se o metódo da requisição é do tipo POST
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)

        # Verifica se o formulário é válido
        if form.is_valid():
            # Obtém o usuário autenticado do formulário
            user = form.get_user()
            # Realiza o login do usuário
            login(request, user)
            # Redireciona para a página inicial após o login
            return redirect('listar_mural')
    else:
        # Se o método não for POST, cria uma instância vazia do formulário de login
        form = UserLoginForm()

    # Renderiza o template 'login.html' com o formulario
    return render(request, 'login.html', {'form': form})



# ------- metodo para fazer logout e redirecionar o usuario -------
def custom_logout(request):
    logout(request)
    return redirect('login')