from django.shortcuts import render
from.models import Filme
import requests


API_KEY = "b7c5bb1b"




def home(request):
       
    if request.method == 'POST':


        titulo =request.POST.get('titulo')


        url = f"http://www.omdbapi.com/?t={titulo}&apikey={"b7c5bb1b"}"


        resposta = requests.get(url)


        dados = resposta.json()


        poster = dados.get('Poster')
       
        if dados ['Response'] == 'True':
            Filme.objects.create(
            titulo=dados['Title'],
            genero=dados['Genre'],
            ano=dados['Year'],
            duracao=dados['Runtime'],
            poster=poster,
            imdb_id=dados['imdbID'],
            diretor=dados['Director']
            )


    filmes = Filme.objects.all()


    query = request.GET.get('q')


    if query:
        filmes = filmes.filter(titulo__icontains=query)

    return render(request, 'filmes/home.html', {
        'filmes': filmes


    })
