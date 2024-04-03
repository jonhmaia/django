from django.shortcuts import render
from .models import Usuario

# Create your views here.
#parametro request permite vizualizar oq esta na pagina

def home(request):
    return render(request, 'home.html') #passa os dados com request depois o nome do arquivo html

def usuarios(request):
    #salvar os dados do usuário
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
   # exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
       'usuarios':Usuario.objects.all()
    }
    #retornar os dados para pagina de listagem 
    return render(request,'usuarios.html',usuarios)
#implementar exclusão de usuarios
#implementar edição de usuarios
#implementar busca de usuarios
#implementar paginação de usuarios
#implementar ordenação de usuarios
#implementar filtro de usuarios
#implementar autenticação de usuarios (senha e login)
#implementar a troca de senha de usuarios
#implementar a tela de login 
#implementar o log out
