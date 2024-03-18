# PyAutomation

## Descrição

- Esse é um projeto open source que conta com a contribuição da comunidade de desenvolvedores para desenvolver scripts de automação para o uso do dia a dia e disponibilizar esses scripts em uma CLI.

## Setup

#### Pré-requisitos

- Python (latest)
- pip3
- venv

#### Configurar

Para configurar o projeto na sua máquina, siga os seguintes passos:

- Crie o ambiente virtual com o comando:
`python3 -m venv .venv`

- Ative o ambiente virtual com o comando:
`source .venv/bin/activate`

- Instale as dependências:
`python3 -m pip install -r requirements.txt`

## Projetos

### YouTube Downloader

Esse projeto foi pensado para fornecer uma ferramenta de linha de comando(CLI) para realizar o download de vídeos e playlists de vídeos do YouTube para a máquina local.

Para a implementação foram utilizadas as bibliotecas ffmpeg, pytube e click.

Para utilizar rode o comando `python3 scripts/youtube.py --type=video` para download de um único vídeo, e em seguida, no terminal, cole o link do vídeo que deseja baixar.

Caso queira baixar uma playlist inteira siga oos mesmos passos acima, porém passe o argumento type com o valor playlist. Ex.: `python3 scripts/youtube.py --type=playlist`

## Para contribuir para o projeto

Para melhorar os scripts, sugerir novas implementações ou trabalhar no backlog do projeto, siga os seguintes passos:

- Crie uma nova branch a partir da branch `main` e siga o padrão de commit [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0-beta.4/). Para nomear a branch, siga o mesmo padrão.
Ex: Se seu pull request vai implementar uma correção, seus commits devem seguir o padrão `fix: <Corrige...>` e o nome da branch deve seguir o padrão `fix/<o-que-sera-corrigido-em-ingles>`;
- Após terminar sua implementação, crie um Pull Request seguindo o padrão definido e aguarde code review antes de mergear;
- Lembre-se de incluir na sua implementação a documentação necessária no README.md para o uso da nova funcionalidade, ou altere o README.md caso necessário se tiver feito uma correção.

Qualquer dúvida, fique à vontade para entrar em contato comigo pelo WhatsApp (53) 99181-7145
