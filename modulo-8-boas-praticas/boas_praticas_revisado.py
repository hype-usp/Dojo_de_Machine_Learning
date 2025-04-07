# %% [markdown]
# # 📊 Boas Práticas em Projetos de Dados e IA

# %% [markdown]
# 📌 **Créditos pelo notebook:**
# 
# 📝 **Autores:** Nome1, Nome2, Nome3  
# 🔍 **Revisores:** Nome4, Nome5 

# %% [markdown]
# Parabéns por ter chegado até aqui! Agora que você aprendeu sobre Python, visualização de dados, classificação e regressão, vamos encerrar com chave de ouro: entendendo como estruturar um projeto real de forma organizada, clara e reprodutível.

# %% [markdown]
# ## 🌱 Por que boas práticas importam?
# 
# Imagine que você — ou outra pessoa — precise revisitar seu projeto daqui a 6 meses. Sem organização, isso pode virar um pesadelo. Boas práticas facilitam:
# 
# - A colaboração em grupo
# - A leitura e entendimento do código
# - A reprodutibilidade dos resultados
# - A organização e escalabilidade do projeto

# %% [markdown]
# ## 🧱 Estruturando um projeto do zero

# %% [markdown]
# Suponha que vamos criar um projeto, e o diretório root (base/principal) desse projeto se chamará _my_project_. Você acaba de criar esse diretório e entra nele com o comando:

# %%
# cd my_project

# %% [markdown]
# Qual a primeira coisa a se fazer? 🤔

# %% [markdown]
# ## 💥 Conflitos de versões entre projetos

# %% [markdown]
# Durante sua jornada na área, provavelmente você vai trabalhar em vários projetos ao mesmo tempo. 
# 
# Pode ser dois projetos no trabalho, um na iniciação científica, outro no Hype... Muitos projetos diferentes.
# 
# É comum que cada projeto exija versões específicas de bibliotecas. 
# 
# Por exemplo:
# - Um projeto exige uma versão antiga do Pandas (ex: 2.2.5).
# - Outro exige uma versão nova do Pandas (ex: 2.2.8) para funcionar com a versão mais recente do `sklearn`.
# 
# E aí que o caos começa: não dá pra ter duas versões diferentes do Pandas instaladas ao mesmo tempo no sistema. 😵

# %% [markdown]
# Dependendo do projeto, você pode até precisar de **diferentes versões do Python**. 
# 
# Então como evitar esse caos? 🤯

# %% [markdown]
# ## 🧪 Isolando ambientes com ambientes virtuais

# %% [markdown]
# Com ambientes virtuais, cada projeto tem seu próprio “universo”, onde suas dependências vivem de forma independente. 🌌
# 
# Isso é uma boa prática amplamente recomendada pela comunidade Python. Eles ajudam na:
# 
# - Organização dos projetos
# - Reprodutibilidade dos experimentos
# - Facilidade de deploy e compartilhamento
# 
# Ferramentas como `venv` ou `virtualenv` tornam isso super fácil.

# %% [markdown]
# Vamos voltar ao nosso exemplo. Dentro do diretório raiz do projeto, você pode criar uma máquina virtual com:

# %%
!python -m venv venv

# %% [markdown]
# - `venv`: é o nome da pasta da sua máquina virtual. Pode dar outro nome se quiser, mas esse é o padrão.

# %% [markdown]
# Isso cria uma pasta chamada `venv/` com uma cópia isolada do Python e seus pacotes!

# %% [markdown]
# ## 🔛 Ativando o ambiente virtual

# %% [markdown]
# Agora você precisa "entrar" na sua máquina virtual.  
# 
# **Windows:**

# %%
venv\Scripts\activate

# %% [markdown]
# **Linux/macOS:**

# %%
source venv/bin/activate

# %% [markdown]
# ✅ Agora seu terminal está **dentro** da máquina virtual. Teste com:

# %%
pip list

# %% [markdown]
# Você verá que quase nada está instalado — ou seja, seu ambiente está limpinho, pronto pra começar!

# %% [markdown]
# ## 🤯 "Mas e o Jupyter, como usa ele nesse ambiente virtual?"

# %% [markdown]
# Boa pergunta!
# 
# Não basta só abrir o Jupyter a partir do terminal e esperar que ele use sua máquina virtual automaticamente. A vida não é tão simples assim 😅

# %% [markdown]
# Mas relaxa que é fácil resolver.

# %% [markdown]
# ### 🧠 Instale o Jupyter e o kernel dentro da máquina virtual

# %%
# pip install ipykernel jupyterlab

# %% [markdown]
# - `jupyterlab`: instala o Jupyter Lab, caso ainda não tenha.
# - `ipykernel`: permite transformar o ambiente virtual em um kernel reconhecido pelo Jupyter.

# %% [markdown]
# ### ⚙️ O que é um kernel?

# %% [markdown]
# O kernel é o motor que roda o código por trás dos panos no Jupyter.  
# Cada kernel está ligado a um interpretador Python (por exemplo, seu ambiente virtual).  
# 
# Por isso, precisamos registrar esse novo ambiente como um kernel.

# %% [markdown]
# ### 🧾 Registre esse ambiente como um kernel

# %%
python -m ipykernel install --user --name meu_kernel --display-name "Python (projeto Hype)"

# %% [markdown]
# - `--name`: nome técnico (sem espaços)
# - `--display-name`: nome que aparece no Jupyter

# %% [markdown]
# ✅ Pronto! O Jupyter agora reconhece seu ambiente virtual como um kernel.

# %% [markdown]
# ### 🚀 Inicie o Jupyter Lab

# %%
jupyter lab

# %% [markdown]
# No canto superior direito, clique no kernel atual e selecione:
# 
# `Python (projeto Hype)` ✅

# %% [markdown]
# ### 🧹 Remover um kernel

# %%
jupyter kernelspec uninstall meu_kernel

# %% [markdown]
# ## 🐍 Usando diferentes versões do Python

# %% [markdown]
# ✅ Pré-requisito: ter a versão desejada do Python instalada no seu sistema.

# %% [markdown]
# 💻 **1. Crie o ambiente com a versão desejada**
# 
# No Linux/macOS:

# %%
python3.10 -m venv env_projeto

# %% [markdown]
# No Windows:

# %%
py -3.11 -m venv env_projeto

# %% [markdown]
# ## ✅ Conclusão

# %% [markdown]
# Agora você sabe como criar e usar ambientes virtuais para manter seus projetos organizados, reprodutíveis e livres de conflitos!
# 
# Com isso, você pode:
# - Instalar apenas as dependências necessárias para cada projeto
# - Ter controle total sobre versões de bibliotecas e do Python
# - Usar seu ambiente virtual no Jupyter
# 
# Bora colocar tudo isso em prática no seu próximo projeto? 💪
