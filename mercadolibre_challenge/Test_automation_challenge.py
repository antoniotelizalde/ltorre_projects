#TAKE HOME CHALLENGE - TEST AUTOMATION - LUIS ANTONIO TORRES ELIZALDE 27/05/2025

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Configuracion del navegador:
options = Options()
options.add_argument("--start-maximized")

# Abrir el navegador:
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

# Abrir Mercado Libre:
driver.get("https://www.mercadolibre.com")

# Seleccionar el pais:
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'México')]"))).click()

# Buscar "PlayStation 5" en la barra de busqueda:
wait.until(EC.presence_of_element_located((By.NAME, "as_word"))).send_keys("PlayStation 5")
driver.find_element(By.NAME, "as_word").submit()

# Timer para la carga de la pagina
time.sleep(5)

# LOS FILTROS DE "CONDITION" Y "LOCATION" NO FUERON INTEGRADOS PARA MANTENER UNA EJECUCION ESTABLE Y EVITAR BLOQUEOS O REDIRECCIONES. 

# Click en "Más relevantes"
try:
    print("Click 'Más relevantes'")
    boton = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.andes-dropdown__display-values")))
    driver.execute_script("arguments[0].click();", boton)
    print("✅ Click realizado.")
except Exception as e:
    print("❌ Falló el click:", e)

print("Timer 5s")
time.sleep(5)

from selenium.webdriver.common.action_chains import ActionChains
try:
    print("Click 'Mayor precio'...")
    mayor_precio_li = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//li[@data-key='price_desc']")
    ))

    actions = ActionChains(driver)
    actions.move_to_element(mayor_precio_li).click().perform()

    print("✅ Click realizado")
except Exception as e:
    print(f"❌ Falló el Click {e}")

    from selenium.webdriver.common.by import By
import time

time.sleep(3)
print("Imprimiendo primeros 5 productos")

try:
    productos = driver.find_elements(By.CSS_SELECTOR, "div.ui-search-result__wrapper")[:5]

    for idx, producto in enumerate(productos, start=1):
        try:
            titulo = producto.find_element(By.CSS_SELECTOR, "h3.poly-component__title-wrapper a").text
            precio = producto.find_element(By.CSS_SELECTOR, "div.poly-component__price span.andes-money-amount__fraction").text
            print(f"{idx}. {titulo} - ${precio}")
        except Exception as e:
            print(f"Error al obtener los datos #{idx}:", e)
except Exception as e:
    print("❌ No se pudieron obtener los datos", e)

# No cerrar automáticamente el navegador
input("Presiona ENTER para cerrar manualmente")
driver.quit()
