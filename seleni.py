from selenium import webdriver

# Configurar as informações do proxy SOCKS5
proxy_address = "127.0.0.1"
proxy_port = "9050"

# Configurar as opções do Firefox
firefox_options = webdriver.FirefoxOptions()

# Configurar as preferências do Firefox para usar o proxy SOCKS5
firefox_options.set_preference("network.proxy.type", 1)
firefox_options.set_preference("network.proxy.socks", proxy_address)
firefox_options.set_preference("network.proxy.socks_port", int(proxy_port))
firefox_options.set_preference("network.proxy.socks_version", 5)
firefox_options.set_preference("network.proxy.socks_remote_dns", True)

# Inicializar o driver do Firefox com as opções
driver = webdriver.Firefox(options=firefox_options)

# Exemplo de uso: Abrir uma página web
driver.get("https://google.com")
