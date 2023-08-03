# Git e GitHub

### Definição

**Git:** Sistema de Controle de Versão Distribuído. Registra as mudanças feitas no código fonte de um projeto, permitindo que os arquivos sejam alterados de forma simultânea por diferentes usuários. 

**Branches:** Ramificação de alterações no código de maneira independente, permitindo a criação de funcionalidades em paralelo.

**Fluxo Simples:** Clone → Branch → Commit → Push → Merge | Pull Request

**git init**: Inicializar um repositório vazio, ou reinicializar um existente
**git clone**: Clonar um repositório na máquina local
**git add**: Adiconar um arquivo na stage area, a stage area será adicionada no próximo commit
**git push**: Eviar o arquivo do repositório local para o remoto
**git merge**: Mesclar branches ou commits
**git log**: Status de commits

**GitHub:** Plataforma para armazenamento na nuvem de repositórios Git, que permite o compartilhamento de código.

### Ciclo de vida de arquivo

**Untracked**: arquivo criado, mas não rastreado
**Staged**: arquivo adicionado as repositório Git, esta preparado
**Unmodified**: arquivo salvo, estado neutro
**Modified**: arquivo modificado, já rastreado pelo Git

### Comandos Git

```bash
# Identificar o autor das mudanças
git config --global user.name "<username>"
git config --global user.email "<username>"

# Mostrar todos os arquivos alterados
git status -uall

# Excluir um repositório Git
rm -fr .git/

# Adicionar um arquivo ao repositório Git
git add <filename>

# Adicionar todos os arquivos ao repositório Git
git add .

# Remover um arquivo do repositório Git
git rm --cached <filename>

# Remover todos os arquivos do repositório Git
git rm --cached -r . 

# Salvar mudanças de uma versão
git commit -m "commit message"

# Visualizar alterações
git diff
git diff --cached
git diff --staged

# Visualizar o histórico de commits
git log # press q to quit 
git log <branch-name> 
git log --oneline # hash e mensagem do commit
git log --quantity # limitar a quantidade de commits
git log -p # mostra os commits e as mudanças feitas
git log --stat # mostra os commits e os arquivos modificados
git log --shortstat # mostra os commits e quantos arquivos foram modificados

# Alterar a mensagem de um commit
git commit --ammend -m "commit message"

# Adicinonar um arquivo faltante a um commit
git add <filename>
git commit --ammend --no-edit

# Voltar a uma versão anterior 
git checkout <commit-hash>

# Reverter um arquivo para sua versão anterior
git checkout <filename>

# Descartar alterações em arquivos untracked
git clean -f

# Descartar alterações em arquivos adicionados
git restore --staged <filename>
git rm --cached <filename>

git reset --hard

# Parar de rastrear um arquivo
git update-index --skip-worktree <filename>

# Voltar a rastrear um arquivo
git update-index --no-skip-worktree <filename>

# Listar branches 
git branch --list

# Criar uma branch 
git branch <name>

# Mudar de branch 
git checkout <branch-name>
git switch <branch-name>

# Criar uma branch e mudar para ela
git checkout -b <branch-name>
git switch -c <branch-name>

# Limpa os arquivos rastreados e muda de branch
git checkout -f <branch-name>

# Remover uma branch local
git branch -d <branch-name>
git branch -D <branch-name> # força o delete

# Remover uma branch remota
git push --delete origin <branch-name>

# Renomear uma branch local
git branch -m <branch-new-name>
git branch -m <branch-old-name> <branch-new-name>

# Renomear uma branch remota
git push --delete origin <branch-old-name>
git branch -m <branch-new-name>
git push --set-upstream origin <branch-new-name>

# Mesclar branches
git checkout <branch-without-changes>
git merge <branch-with-changes>

# Criar uma tag no útimo commit
git tag <tag-name>

# Cria uma tag annotated no útimo commit 
git tag -a -m "mensagem" <tag-name> # marca quem fez

# Mostrar uma tag
git show <tag-name>

# Mostrar todas as tag
git tag
git tag -l
git tag --list
git tag -n # Mostra a mensagem

# Criar uma tag em um commit antigo
git tag <tag-name> <commit-hash>

# Cria uma tag annotated no útimo commit 
git tag -a -m "mensagem" <tag-name> <commit-hash> # marca quem fez

# Envia uma tag ao remoto 
git push origin <tag-name>

# Envia todas as tag ao remoto 
git push --tags

# Voltar para uma versão anterior utilizando tags
git checkout <tag-name>

# Comparar diferenças entre uma versão e outra utilizando tags
git checkout <tag-name>

# Apagar uma tag localmente
git tag -d <tag-name>

# Apagar uma tag no remoto
git push --delete origin <tag-name>

# Pausar alterações em arquivos rastreados ao mudar de branch ou puxar novas alterações
git stash

# Mostar arquivos pausados em todo o repositório
git stash list

# Aplicar alterações pausadas
git stash apply

# Aplicar alterações pausadas especificas
git stash apply stash@{<posicao>}

# Remover alterações pausadas especificas
git stash drop stash@{<posicao>}

# Pausar alterações em arquivos rastreados em uma branch especifica
git stash branch <branch-name>

# Reverter commit
git revert <commit-hash> --no-edit # HEAD para o último commit

# Desfazer commit
git reset --hard HEAD~<quantity> # HEAD para o último commit

# Desfazer commit sem perder alterações para arquivos untracked
git reset --mixed HEAD~<quantity> # HEAD para o último commit

# Desfazer commit sem perder alterações para arquivos preparados
git reset --soft HEAD~<quantity> # HEAD para o último commit

# Forçar o envio de alterações para o remoto
git push --force

# Forçar o envio de alterações para o remoto sem perder nenhuma
git push --force-with-lease

# Adicionar arquivos e commitar 
git commit -a -m "commit message"

# Mudar a base dos commits | "alinhar branches"
git rebase <branch-name>

# Mesclar commits -> Squash
git rebase --interactive HEAD~<quantity>

squash "commit message" # No editor

# Trazer um commit para uma branch
git cherry-pick <commit-hash>

# Busca binária de commits -> Bisect
git bisect start

git bisect good <commit-hash>
git bisect bad <commit-hash>

# Mostrar alterações do remoto
git fetch

# Criar alias de comandos
git config --global alias.<alias> <command>
git config --global alias.<alias> "<command> --<option>"

# Descartar alias de comandos
git config --global --unset alias.<alias>

# Filtrar uma lista, case sensitive
<command> | grep <word-to-find>
```