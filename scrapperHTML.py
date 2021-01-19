
from bs4 import BeautifulSoup

def scrapperHTML(filename):
    """
    doc_string
    """

    def get_element_by_jsclass(jsclass=''):
        """
        doc_string
        """
        val = soup.find(class_=jsclass)
        val = str(val.next_element)
        return val


    pac_data = {}

    with open(rf"{filename}", encoding = "utf-8") as fp:
        soup = BeautifulSoup(fp, "lxml")

    if soup.find(class_ = "js flexbox canvas canvastext webgl no-touch geolocation postmessage websqldatabase indexeddb hashchange history draganddrop websockets rgba hsla multiplebgs backgroundsize borderimage borderradius boxshadow textshadow opacity cssanimations csscolumns cssgradients cssreflections csstransforms csstransforms3d csstransitions fontface generatedcontent video audio localstorage sessionstorage webworkers no-applicationcache svg inlinesvg smil svgclippaths") not in soup: 
        pac_data['nombre']     = get_element_by_jsclass("")
        pac_data['edad']       = get_element_by_jsclass("##patientIdentificationComponent.ageHN_2675324665956201694 l_form")
        pac_data['nacimiento'] = get_element_by_jsclass("##patientIdentificationComponent.birthHN_1735630509657194021 z-label")
        pac_data['expediente'] = get_element_by_jsclass("##patientIdentificationComponent.nhcHN_950462502649809883 l_form")

    else:
        pac_data['nombre']     = get_element_by_jsclass("##patientIdentificationComponent.sNameHN l_form_big namePatient")
        pac_data['edad']       = get_element_by_jsclass("##patientIdentificationComponent.ageHN_2675324665956201694")
        pac_data['nacimiento'] = get_element_by_jsclass("##patientIdentificationComponent.birthHN_3364940428062238283")
        pac_data['expediente'] = get_element_by_jsclass("##patientIdentificationComponent.nhcHN_950462502649809883")


    return pac_data