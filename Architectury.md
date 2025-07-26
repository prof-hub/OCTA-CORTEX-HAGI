# Script para criar a estrutura de diretórios da Família Caverna.
# O comando 'mkdir -p' cria os diretórios pais se não existirem e não gera erro se o diretório já existir.

# Definindo a pasta raiz do projeto
ROOT_DIR="familia_caverna"

# --- Núcleo de Governança e Estratégia ---
echo "Criando diretórios para o Núcleo de Governança e Estratégia..."
mkdir -p "$ROOT_DIR/governanca_e_estrategia/cavernildo"
mkdir -p "$ROOT_DIR/governanca_e_estrategia/teresa"
mkdir -p "$ROOT_DIR/governanca_e_estrategia/peter"
mkdir -p "$ROOT_DIR/governanca_e_estrategia/sofia"

# --- Núcleo de Conhecimento e Curadoria ---
echo "Criando diretórios para o Núcleo de Conhecimento e Curadoria..."
mkdir -p "$ROOT_DIR/conhecimento_e_curadoria/fausto"
mkdir -p "$ROOT_DIR/conhecimento_e_curadoria/mirtes"
mkdir -p "$ROOT_DIR/conhecimento_e_curadoria/atlas"
mkdir -p "$ROOT_DIR/conhecimento_e_curadoria/aurora"
mkdir -p "$ROOT_DIR/conhecimento_e_curadoria/advogado"
mkdir -p "$ROOT_DIR/conhecimento_e_curadoria/clarice"

# --- Núcleo de Criação e Conteúdo ---
echo "Criando diretórios para o Núcleo de Criação e Conteúdo..."
mkdir -p "$ROOT_DIR/criacao_e_conteudo/francisleine"
mkdir -p "$ROOT_DIR/criacao_e_conteudo/duda"
mkdir -p "$ROOT_DIR/criacao_e_conteudo/marketiane"
mkdir -p "$ROOT_DIR/criacao_e_conteudo/maestro"
mkdir -p "$ROOT_DIR/criacao_e_conteudo/socrates"

# --- Núcleo de Tecnologia e Execução ---
echo "Criando diretórios para o Núcleo de Tecnologia e Execução..."
mkdir -p "$ROOT_DIR/tecnologia_e_execucao/bismarck"
mkdir -p "$ROOT_DIR/tecnologia_e_execucao/thor"
mkdir -p "$ROOT_DIR/tecnologia_e_execucao/orfeu"
mkdir -p "$ROOT_DIR/tecnologia_e_execucao/webmonster"
mkdir -p "$ROOT_DIR/tecnologia_e_execucao/joao"

echo "Estrutura de diretórios da Família Caverna verificada/criada com sucesso."
