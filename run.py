import os
import shutil
import subprocess

CSS_DIR = "src/css"
JS_DIR = "src/js"
HTML_FILE = "index.html"

FRAMEWORKS = {
    1: {
        "name": "Bootstrap",
        "npm": "bootstrap",
        "css": "node_modules/bootstrap/dist/css/bootstrap.min.css",
        "js": "node_modules/bootstrap/dist/js/bootstrap.bundle.min.js"
    },
    2: {
        "name": "Animate.css",
        "npm": "animate.css",
        "css": "node_modules/animate.css/animate.min.css",
        "js": None
    },
    3: {
        "name": "AOS",
        "npm": "aos",
        "css": "node_modules/aos/dist/aos.css",
        "js": "node_modules/aos/dist/aos.js"
    }
}

def instalar_pacote(pacote):
    print(f"📦 Instalando {pacote} via npm...")
    
    # Caminho direto para o npm
    npm_path = shutil.which("npm")
    
    if npm_path is None:
        print("❌ Erro: npm não encontrado no PATH do sistema.")
        print("🔧 Verifique se o Node.js está corretamente instalado e adicionado ao PATH.")
        exit(1)

    subprocess.run([npm_path, "install", pacote], check=True)

def instalar_live_server():
    # Instalar o live-server como dependência de desenvolvimento
    print("📦 Instalando live-server como dependência de desenvolvimento...")
    subprocess.run([shutil.which("npm"), "install", "live-server", "--save-dev"], check=True)

def copiar_arquivo(origem, destino_dir):
    if origem and os.path.isfile(origem):
        os.makedirs(destino_dir, exist_ok=True)
        destino = os.path.join(destino_dir, os.path.basename(origem))
        shutil.copy2(origem, destino)
        print(f"✅ Copiado {origem} para {destino}")
        return destino
    else:
        print(f"⚠️  Arquivo {origem} não encontrado ou não aplicável")
        return None

def atualizar_html(css_files, js_files):
    if not os.path.exists(HTML_FILE):
        with open(HTML_FILE, "w") as f:
            f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Projeto</title>\n</head>\n<body>\n</body>\n</html>")

    with open(HTML_FILE, "r") as f:
        conteudo = f.read()

    head_fim = conteudo.find("</head>")
    if head_fim == -1:
        print("❌ Tag </head> não encontrada em index.html")
        return

    links = ""
    for css in css_files:
        caminho = css.replace("\\", "/")
        links += f'  <link rel="stylesheet" href="{caminho}">\n'
    for js in js_files:
        caminho = js.replace("\\", "/")
        links += f'  <script src="{caminho}"></script>\n'

    novo_conteudo = conteudo[:head_fim] + "\n" + links + conteudo[head_fim:]

    with open(HTML_FILE, "w") as f:
        f.write(novo_conteudo)
    print("🎉 Links adicionados ao index.html com sucesso!")

def main():
    instalar_live_server()

    print("📚 Escolha os pacotes para instalar (use números separados por vírgula):")
    for i in FRAMEWORKS:
        print(f"{i}. {FRAMEWORKS[i]['name']}")

    escolha = input("Números (ex: 1,2,3): ").replace(" ", "")
    try:
        numeros = [int(n) for n in escolha.split(",") if n.isdigit()]
    except ValueError:
        print("❌ Entrada inválida.")
        return

    css_adicionados = []
    js_adicionados = []

    for num in numeros:
        if num in FRAMEWORKS:
            pkg = FRAMEWORKS[num]
            instalar_pacote(pkg["npm"])

            css_caminho = copiar_arquivo(pkg.get("css"), CSS_DIR)
            if css_caminho:
                css_adicionados.append(css_caminho)

            js_caminho = copiar_arquivo(pkg.get("js"), JS_DIR)
            if js_caminho:
                js_adicionados.append(js_caminho)
        else:
            print(f"⚠️  Número {num} inválido")

    atualizar_html(css_adicionados, js_adicionados)

if __name__ == "__main__":
    main()
