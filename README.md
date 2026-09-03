# 🚀 Microsoft Teams - Mantenedor de Status Ativo (Versão Portátil)

Uma solução leve e automatizada desenvolvida em Python para manter o status do Microsoft Teams como **Disponível / Ativo** em ambientes corporativos bloqueados do Windows.

---

## ⚡ Diferenciais desta Versão (Portátil / Zero Instalação)

* **Sem necessidade de permissão de Administrador:** Não exige senha da TI ou elevação de privilégios.
* **Sem necessidade de instalação:** Roda diretamente via versão embutida do Python (*Embedded Python*).
* **Dependências inclusas:** Não é necessário rodar `pip install` na máquina de destino.
* **Execução simples:** Inicialização através de apenas dois cliques em um arquivo `.bat`.

---

## 📂 Estrutura do Repositório

* `teams_ativo.py`: Script principal em Python responsável por simular atividade e manter o sistema ativo via `pyautogui`.
* `iniciar_teams.bat`: Arquivo de lote que inicializa o ambiente Python portátil e executa o script.
* `.gitignore`: Filtro para evitar o envio de arquivos binários pesados do Python ao repositório.

---

## 💻 Como Baixar e Executar (Para Usuários)

Se você deseja apenas utilizar a ferramenta sem configurar ambiente de desenvolvimento:

1. Acesse a aba **[Releases](../../releases)** na lateral direita deste repositório.
2. Faça o download do arquivo **`Teams_Ativo_Portatil.zip`** da versão mais recente.
3. Clique com o botão direito no arquivo `.zip` baixado e selecione **Extrair Tudo**.
4. Abra a pasta extraída e dê **dois cliques no arquivo `iniciar_teams.bat`**.

> **Nota:** É fundamental **extrair os arquivos** do `.zip` antes de executar. O script não funcionará se executado de dentro do arquivo compactado.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.11** (Versão Embeddable / Portátil)
* **PyAutoGUI** (Automação de periféricos)

---

## ⚠️ Isenção de Responsabilidade (Disclaimer)

Esta ferramenta foi desenvolvida exclusivamente para fins educacionais e de automação pessoal. O uso de scripts de automação em ambientes de trabalho deve respeitar as políticas de TI da sua organização.
