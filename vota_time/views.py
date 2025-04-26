from django.shortcuts import render, redirect
from .models import Usuario

def cad_vota(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        idade = request.POST.get('idade', '').strip()

        if not nome or not idade:
            return render(request, 'voto_usuario/cad_usuario.html', {
                'mensagem': 'Preencha todos os campos!'
            })

        # Cria o usuário e redireciona para votação com o ID na URL
        usuario = Usuario.objects.create(nome=nome, idade=idade)
        return redirect('votacao', id_usuario=usuario.id_usuario)  # ID na URL

    return render(request, 'voto_usuario/cad_usuario.html')


def votacao(request, id_usuario):  # Recebe o ID pela URL
    try:
        usuario = Usuario.objects.get(id_usuario=id_usuario)
    except Usuario.DoesNotExist:
        return render(request, 'voto_usuario/voto.html', {
            'mensagem': 'Erro: Usuário não encontrado!'
        })

    if request.method == 'POST':
        time_escolhido = request.POST.get('time', '').strip()

        if not time_escolhido:
            return render(request, 'voto_usuario/voto.html', {
                'mensagem': 'Selecione um time para votar!',
                'nome_usuario': usuario.nome,
                'id_usuario': usuario.id_usuario
            })

        # Atualiza o voto e salva
        usuario.voto = time_escolhido
        usuario.save()

        return render(request, 'voto_usuario/voto.html', {
            'mensagem': f'✅ Voto registrado para {time_escolhido}!',
            'nome_usuario': usuario.nome,
            'id_usuario': usuario.id_usuario
        })

    # GET: Mostra a página de votação
    return render(request, 'voto_usuario/voto.html', {
        'nome_usuario': usuario.nome,
        'id_usuario': usuario.id_usuario
    })