import time
import random
from tkinter import Tk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

tam = 10


class Examen():
    def inicio(self):
        option = Options()
        option.add_argument("--disable-infobars")
        option.add_argument("start-maximized")
        option.add_argument("--disable-extensions")
        option.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })
        PATH = 'chromedriver.exe'
        self.driver = webdriver.Chrome(chrome_options=option, executable_path=PATH)

        self.datos = {'nombre': [], 'apellido': [], 'correo': [], 'estado': []}

    def fin(self):
        self.driver.quit()

    def get_nombres(self):
        self.driver.get("https://generadordenombres.online/")
        nom = []
        ape = []
        for i in range(0, tam):
            names = self.driver.find_element_by_id('nombreGenerado')
            name = str(names.text).split(sep=' ')
            nom.append(name[0])
            ape.append(name[1])
            self.driver.refresh()
        self.datos['nombre'] = nom
        self.datos['apellido'] = ape

    def get_correos(self):
        self.driver.get("https://10minutemail.net/")
        cor = []
        est = []
        for i in range(0, tam):
            self.driver.find_element_by_id("copy-button").click()
            cor.append(Tk().clipboard_get())
            est.append(bool(random.getrandbits(1)))
        self.datos['correo'] = cor
        self.datos['estado'] = est

    def to_correos(self):
        txt = ""
        for i in range(0, len(self.datos['correo'])):
            txt = txt + self.datos['correo'][i] + ","
        return txt

    def escribir(self, body):
        for i in range(0, len(self.datos['nombre'])):
            body.send_keys(self.datos["nombre"][i])
            time.sleep(1)
            body.send_keys(Keys.TAB)
            body.send_keys(self.datos["apellido"][i])
            time.sleep(1)
            body.send_keys(Keys.TAB)
            body.send_keys(self.datos["correo"][i])
            time.sleep(1)
            body.send_keys(Keys.TAB)
            body.send_keys(self.datos["estado"][i])
            time.sleep(1)
            body.send_keys(Keys.ENTER)
        time.sleep(1)

    def login(self, id, password):
        self.driver.get("https://www.facebook.com/")
        email = self.driver.find_element_by_id("email")
        email.send_keys(id)
        Password = self.driver.find_element_by_id("pass")
        Password.send_keys(password)
        self.driver.find_element_by_id("u_0_b").click()

    def post_content(self):
        time.sleep(1)
        self.driver.find_element_by_css_selector(".jm1wdb64 > .a8c37x1j").click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(".notranslate")
        activepostarea = self.driver.switch_to_active_element()
        activepostarea.send_keys(Keys.CONTROL, 'v')
        time.sleep(2)
        activepostarea.send_keys("02/18/2021")
        e = self.driver.find_element_by_css_selector(
            ".k4urcfbm > .oajrlxb2 > .rq0escxv > .rq0escxv > .d2edcug0 > .a8c37x1j")
        e.click()
        time.sleep(5)

    def copiar_imagen(self):
        self.driver.get(
            "https://raw.githubusercontent.com/RicardoVinicioJara/Simulacion/main/Segundo%20Interciclo/Examen/image.png")
        ele = self.driver.find_element_by_css_selector("img")
        ele.click()
        ele.click()
        activepostarea = self.driver.switch_to_active_element()
        activepostarea.send_keys(Keys.CONTROL, 'c')

    def ubicar_celdas(self, txt):
        seldas = self.driver.find_element_by_id('t-name-box')
        seldas.clear()
        seldas.send_keys(txt)
        time.sleep(1)
        seldas.send_keys(Keys.ENTER)
        time.sleep(1)

    def escribir_exel(self):
        self.driver.get(
            "https://docs.google.com/spreadsheets/d/1hASt7VUwtTyhuQy9paEWtiVFhHXbE5UeEkJ_TAdYz5U/edit#gid=0")
        self.ubicar_celdas("A2:D20")
        cel_del = self.driver.find_element_by_id('waffle-rich-text-editor')
        cel_del.send_keys(Keys.DELETE)
        time.sleep(1)
        self.ubicar_celdas("A2")
        body = self.driver.find_element_by_class_name('cell-input')
        self.escribir(body)

    def correo(self, correos, asunto="Flyer Elecciones"):
        self.driver.get(
            'https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1612797357&rver=7.0.6737.0&wp=MBI_SSL'
            '&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3db97197b5-ba7d-e675-321b'
            '-8f36488fb774&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')

        email = self.driver.find_element_by_name('loginfmt')
        email.send_keys('appdisup@hotmail.com')
        time.sleep(1)
        email.send_keys(Keys.ENTER)
        pasw = self.driver.find_element_by_name('passwd')
        pasw.send_keys('123UPS45')
        time.sleep(1)
        self.driver.find_element_by_id('idSIButton9').click()
        time.sleep(1)
        self.driver.find_element_by_id("id__5").click()
        time.sleep(2)
        para = self.driver.find_element_by_class_name("ms-BasePicker-input")
        para.send_keys(correos)
        time.sleep(1)
        para.send_keys(Keys.TAB)
        time.sleep(1)
        asu = self.driver.find_element_by_class_name("ms-TextField-field")
        asu.send_keys(asunto)
        time.sleep(1)
        asu.send_keys(Keys.TAB)
        mot = self.driver.find_element_by_class_name("_4utP_vaqQ3UQZH0GEBVQe")
        mot.send_keys(asunto)
        time.sleep(1)
        mot.send_keys(Keys.CONTROL, 'v')
        time.sleep(7)
        mot.send_keys(Keys.CONTROL, Keys.ENTER)
        time.sleep(2)
        self.driver.get("https://outlook.live.com/mail/0/sentitems")


if __name__ == '__main__':
    t = Examen()
    t.inicio()
    t.get_correos()
    t.get_nombres()
    print(t.datos)
    # t.datos = {
    #     'nombre': ['Nora', 'Carme', 'Eloisa', 'Josefa', 'Teodoro', 'Melania', 'Mariana', 'Camilo', 'Driss', 'Markel'],
    #     'apellido': ['Martos', 'Melendez', 'Díaz', 'Batista', 'Oliver', 'Prats', 'San', 'Roldan', 'Palma', 'Noguera'],
    #     'correo': ['obp10406@zwoho.com', 'obp10406@zwoho.com', 'obp10406@zwoho.com', 'obp10406@zwoho.com',
    #                'obp10406@zwoho.com', 'obp10406@zwoho.com', 'obp10406@zwoho.com', 'obp10406@zwoho.com',
    #                'obp10406@zwoho.com', 'obp10406@zwoho.com'],
    #     'estado': [True, True, False, True, False, False, False, True, False, False]}

    t.escribir_exel()
    t.copiar_imagen()
    t.login("ups_uclqlhf_chatt@tfbnw.net", "holaholahola")
    t.post_content()
    t.correo(t.to_correos(), "Examen Simulacion")
    # t.fin()
