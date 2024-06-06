# Crud Cultural


Sistema CRUD com Django 

Um sistema CRUD (Create, Read, Update, Delete) construído com Django, fornecendo funcionalidades para gerenciar usuários, transações, projetos e processos. O sistema inclui autenticação de usuário e restrições de setor de acordo com os requisitos fornecidos pela Fundarpe. 

# Funcionalidades Principais 

Cadastro de usuários com autenticação. 

Operações CRUD para transações, projetos e processos. 

Restrições de setor para preenchimento de formulários. 

Interface de usuário amigável e funcionalidades de paginação, filtragem por data e barra de pesquisa. 

# Pré-requisitos 

Python 3.12.3 

Django 

Db browser Sqlite 

# Instalação e Configuração 

Instale o python na sua máquina 

Instale o Django na pasta em que você clonou o repositório, utilizando o comando pip install django 

# Para acessar a aplicação na Web, siga os seguintes passos: 

 

	* Mova sua pasta para o Disco local c: 

	* Acesse ela utilizando o CMD, e com os seguintes comandos em ordem você 	irá conseguir acessar a aplicação: 

 

cd c:/NomeDaPasta 

		cd Residencia-Fundarpe 

		cd NovaResidencia 

		cd venv/Scripts 

		activate 

		cd .. 

		cd .. 

		python manage.py runserver
                
               digite localhost:8000 na url do google e acesse o site
 

	 

 

# Uso 

Acesse o sistema através do navegador web. 

Faça o cadastro no sistema, e após isso o login utilizando suas credenciais. 

Explore as diferentes seções do sistema para criar, visualizar, editar ou excluir registros. 

Observe as restrições de setor ao preencher formulários. 

 

# Observações 

Na parte de processos a lógica ocorrerá da seguinte maneira: o setor UNAT será o único que tem acesso a criação dos processos, ele irá preencher o dado do formulário que já era de sua atribuição, porém também irá preencher os demais campos com uma data “default”, e os demais setores irão apenas editar esse processo alterando suas respectivas partes, e no final salvando o formulário.
