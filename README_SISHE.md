# SISHE – Sistema de Horários Escolares

O **SISHE** é um sistema web desenvolvido em Django com o objetivo de **gerenciar a grade de horários escolares** do IFPI – Campus Paulistana. O sistema foi projetado para facilitar o cadastro de coordenadores, professores, componentes curriculares e alocação de horários, com validação de conflitos de carga horária e disponibilidade.

> ⚠️ **Status:** Projeto interrompido. O desenvolvimento foi pausado devido a múltiplas atribuições (docência, coordenação e transferência de campus). O repositório permanece público como demonstração técnica e pode ser retomado futuramente.

---

## 🎯 Funcionalidades

- Cadastro de **usuários** com diferentes perfis (coordenador, professor)
- Registro de **cursos**, **eixos**, **períodos letivos** e **componentes curriculares**
- Alocação de componentes em turmas por professores
- Distribuição dos componentes nos **horários semanais**
- Validação automática de **conflitos de horário** (professores alocados em mais de uma turma)
- Interface web simples e funcional para gestão escolar

---

## 🚀 Como executar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seuusuario/sishe.git
cd sishe
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Inicie o servidor
```bash
python manage.py runserver
```

Acesse no navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧭 Fluxo de uso

1. Faça login com o superusuário criado
2. No menu **Usuários**, cadastre:
   - Coordenador
   - Eixos
   - Professores
3. No menu **Escola**, cadastre:
   - Cursos
   - Períodos letivos
4. Dentro do **Período Letivo**, adicione:
   - Turmas
5. Na **Turma**, adicione os **componentes curriculares** e vincule a um professor
6. Acesse o menu **Horário**:
   - Escolha a turma
   - Alocar disciplinas nos horários disponíveis
   - O sistema valida se o professor já está lotado no horário escolhido e impede conflitos

---

## 📌 Observações

- Projeto desenvolvido inicialmente para o **IFPI - Campus Paulistana**
- A lógica de alocação respeita as regras de disponibilidade dos docentes
- Projeto pausado, mas com potencial para retomada ou uso como base para outros sistemas educacionais

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Sinta-se à vontade para estudar, adaptar ou reutilizar o código.

---

## 👨‍💻 Autor

Rafael Luz Araújo  
Desenvolvedor Full Stack | Python | Django | Educação & IA  
📧 rafaluzaraujo@ifpi.edu.br  
🔗 [github.com/rafaluz](https://github.com/rafaluz)
