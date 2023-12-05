# anipy-cli

Aplicação escrita em python que realiza web scraping para assistir e baixar animes diretamente do terminal (também disponível como API).

### Fonte: https://gogoanime.gg

# Conteúdo

- [Instalação](#Instalação)
- [O que pode fazer?](#O_que_pode_fazer?)
- [Importante](#Importante)
- [Config](#Config)
- [Uso](#Uso)

# Instalação

<a href="https://pypi.org/project/anipy-cli/">![PyPI](https://img.shields.io/pypi/v/anipy-cli?style=for-the-badge)</a>

Instalação recomendada:

`python3 -m pip install anipy-cli --upgrade`

Diretamente do repositório:

`python3 -m pip install git+https://github.com/sdaqo/anipy-cli`

É necessário que a máquina reconheça o formato mpv. Baixe aqui: https://mpv.io/installation/

Caso deseje utilizar outro player seu diretório precisa ser especificado na pasta "config".

É possível instalar o [ffmpeg](https://ffmpeg.org/download.html) para baixar playlists no lugar do download interno.

# O que pode fazer?

- Mais rápido do que assistir no navegador.
- Toca animes em seu player local
- Escolhe a qualidade no qual o anime será assistido/baixado.
- Baixa animes
- Histórico de episódios assistidos
- Modo múltiplo para maratonar diversos episódios.
- Modo temporada para assistir ou baixar os últimos episódios.
- Configurável com config
- (**Opcional**) Modo MAL: Semelhante ao modo temporada, contudo usa sua lista em [MyAnimeList.net](https://myanimelist.net/)
- (**Opcional**) Busca no gogoanimes por temporadas específicas.
- (**Opcional**) Ffmpeg para baixar playlists.

#### Importante:

Para importar a biblioteca não importe `anipy-cli`, mas `anipy_cli` (sem '-')

### Config

Quando iniciar o programa pela primeira vez o arquivo config é criado automaticamente

Localização do arquivo:

- Linux: ~/.config/anipy-cli/config.yaml
- Windows: %USERPROFILE%/AppData/Local/anipy-cli/config.yaml
- MacOS: ~/.config/anipy-cli/config.yaml

# Uso

```
uso: anipy-cli [-D | -B | -H | -S | -M | --deletar histórico] [-q QUALIDADE] [-f] [-o] [-a] [-p {mpv,vlc,syncplay,mpvnet}] [-l LOCALIZAÇÃO] [--mal-password SENHA_MAL] [-h] [-v] [--config-path]

Assista animes do site gogoanime no player local ou baixe-os.

Ações:
  Modos ou ações diferentes do anipy-cli (escolha um)

  -D, --download        Modo download. Baixe multiplos episódios como: primeiro_número-segundo_número (e.g. 1-3)
  -B, --binge           Modo múltiplo. Assista múltiplos episódios um após o outro assim: primeiro_número-segundo_número (e.g. 1-3)
  -H, --history         Veja o histórico de seus animes.
  -S, --seasonal        Modo temporada. Assista aos episódios mais recentes de seus animes.
  -M, --my-anime-list   Modo myanimelist. similar ao modo temporada, contudo precisa conectar com sua conta do myanimelist (As credenciais da conta são definidas em config).
  --delete-history      Deleta seu histórico.

Opções:
  Opções que mudam o comportamento do anipy-cli.

  -q QUALIDADE, --quality QUALIDADE
                        Muda a qualidade do vídeo, aceita: best, worst ou 360, 480, 720 etc. Padrão: best
  -f, --ffmpeg          Use ffmpeg para baixar playlists.
  -o, --no-seas-search  Desliga a busca por temporadas específicas (animes de inverno, verão, etc.).
  -a, --auto-update     Automaticamente atualiza e baixa os animes presentes na lista da temporada.
  -p {mpv,vlc,syncplay,mpvnet}, --player-opcional {mpv,vlc,syncplay,mpvnet}
                        Substitui o player padrão na config.
  -l LOCATION, --location LOCALIZAÇÃO
                        Sobreescreve o local de download configurado
  --mal-password SENHA_MAL
                        Especifica a senha do myanimelist (sobreescreve a senha em config)

Info:
  Informações sobre a instalação atual do anipy-cli

  -h, --help            mostra essa mensagem de ajuda.
  -v, --version         mostra o número da versão desse programa.
  --config-path         Mostra o caminho para o arquivo config.
```
