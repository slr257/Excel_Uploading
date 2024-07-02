# need to reload enviPath objects to make sure objects are defined in the dictionary?
from enviPath_python.enviPath import *
from enviPath_python.objects import *

# if this exists in the dictionary, then map it - these values are the only ones availabe as python objects
dict_ai = {"Addition of nutrients": NutrientsAdditionalInformation,
           "Oxygen demand":OxygenDemandAdditionalInformation,
           "Dissolved oxygen concentration":DissolvedOxygenConcentrationAdditionalInformation,
           "pH": AcidityAdditionalInformation,
           "Temperature":TemperatureAdditionalInformation,
           "Redox condition": RedoxAdditionalInformation,
           "Name of Sampling Location":LocationAdditionalInformation, 
           "TSS":TSSAdditionInformation,
           "Biological treatment technology":BiologicalTreatmentTechnologyAdditionalInformation,
           "Bioreactor":BioreactorAdditionalInformation,
           "Inoculum source":InoculumSourceAdditionalInformation,
           "Purpose of WWTP":PurposeOfWWTPAdditionalInformation,
           "Solvent for compound addition":SolventForCompoundSolutionAdditionalInformation,
           "Type of Aeration":TypeOfAerationAdditionalInformation,
           "Type of compound addition":TypeOfAdditionAdditionalInformation,
           # values not in example template
           "Oxygen Demand":OxygenDemandAdditionalInformation,
           "Nitrogen Content":NitrogenContentAdditionalInformation,
           "Ammonia Uptake Rate":AmmoniaUptakeRateAdditionalInformation,
           "Half-life":HalfLifeAdditionalInformation}


# try making a dictionary of functions that will be executed if the object exists
# filter dictionary based on values in Parameters column in Excel template

def add_pH(base_scenario, ai_list):
    ai = dict_ai["pH"]()
    ai.set_lowPh(float(base_scenario[base_scenario["Parameter"]=="pH"]["Value"].values[0].split("-")[0]))
    ai.set_highPh(float(base_scenario[base_scenario["Parameter"]=="pH"]["Value"].values[0].split("-")[1]))
    ai_list.append(ai)

def add_nutrients(base_scenario, ai_list):
    ai = dict_ai["Addition of nutrients"]()
    ai.set_additionofnutrients(base_scenario[base_scenario["Parameter"]=="Addition of nutrients"]["Value"].values[0]) # must be a string value
    ai_list.append(ai)

def add_oxygendemand(base_scenario, ai_list):
    ai = dict_ai["Oxygen demand"]()
    ai.set_oxygendemandType()
    ai.set_oxygendemandInfluent()
    ai.set_oxygendemandEffluent()
    ai_list.append(ai)

def add_dissolvedoxygen(base_scenario, ai_list):
    ai = dict_ai["Dissolved oxygen concentration"]()
    ai.set_DissolvedoxygenconcentrationLow()
    ai.set_DissolvedoxygenconcentrationHigh()
    ai_list.append(ai)

def add_Temp(base_scenario, ai_list):
    ai = dict_ai["Temperature"]()
    ai.set_temperatureMin(base_scenario[base_scenario["Parameter"]=="Temperature"]["Value"].values[0])
    ai.set_temperatureMax(base_scenario[base_scenario["Parameter"]=="Temperature"]["Value"].values[0])
    ai_list.append(ai)

def add_redox(base_scenario, ai_list):
    ai = dict_ai["Redox condition"]()
    ai.set_redoxType(base_scenario[base_scenario["Parameter"]=="Redox condition"]["Value"].values[0])
    ai_list.append(ai)

def add_location(base_scenario, ai_list):
    ai = dict_ai["Name of Sampling Location"]()
    ai.set_location(base_scenario[base_scenario["Parameter"]=="Name of Sampling Location"]["Value"].values[0])
    ai_list.append(ai)

def add_TSS(base_scenario, ai_list):
    ai = dict_ai["TSS"]()
    ai.set_ttsStart(base_scenario[base_scenario["Parameter"]=="TSS"]["Value"].values[0])
    ai.set_ttsEnd(base_scenario[base_scenario["Parameter"]=="TSS"]["Value"].values[0])
    ai_list.append(ai)

def add_biotreattech(base_scenario, ai_list):
    ai = dict_ai["Biological treatment technology"]()
    ai.set_biologicaltreatmenttechnology(base_scenario[base_scenario["Parameter"]=="Biological treatment technology"]["Value"].values[0])
    ai_list.append(ai)

def add_bioreactor(base_scenario, ai_list):
    ai = dict_ai["Bioreactor"]()
    ai.set_bioreactortype(base_scenario[base_scenario["Parameter"]=="Bioreactor"]["Value"].values[0])
    #ai.set_bioreactorsize()
    ai_list.append(ai)

def add_inoculum(base_scenario, ai_list):
    ai = dict_ai["Inoculum source"]()
    ai.set_inoculumsource(base_scenario[base_scenario["Parameter"]=="Inoculum source"]["Value"].values[0])
    ai_list.append(ai)

def add_purposeWWTP(base_scenario, ai_list):
    ai = dict_ai["Purpose of WWTP"]()
    ai.set_purposeofwwtp(base_scenario[base_scenario["Parameter"]=="Purpose of WWTP"]["Value"].values[0])
    ai_list.append(ai)

def add_solvent(base_scenario, ai_list):
    ai = dict_ai["Solvent for compound addition"]()
    ai.set_solventforcompoundsolution1(base_scenario[base_scenario["Parameter"]=="Solvent for compound addition"]["Value"].values[0])
    # ai.set_solventforcompoundsolution2()
    # ai.set_solventforcompoundsolution3()
    ai_list.append(ai)

def add_aeration(base_scenario, ai_list):
    ai = dict_ai["Type of Aeration"]()
    ai.set_typeofaeration(base_scenario[base_scenario["Parameter"]=="Type of Aeration"]["Value"].values[0])
    ai_list.append(ai)

def add_compound_addition(base_scenario, ai_list):
    ai = dict_ai["Type of compound addition"]()
    ai.set_typeofaddition(base_scenario[base_scenario["Parameter"]=="Type of compound addition"]["Value"].values[0])
    ai_list.append(ai)


# dictionary of functions    
dict_fun = {"Acidity": add_pH,
           "Addition of nutrients": add_nutrients,
           "Oxygen demand":add_oxygendemand,
           "Dissolved oxygen concentration":add_dissolvedoxygen,
           "Temperature":add_Temp,
           "Redox condition": add_redox,
           "Name of Sampling Location":add_location, 
           "TSS":add_TSS,
           "Biological treatment technology":add_biotreattech,
           "Bioreactor":add_bioreactor,
           "Inoculum source":add_inoculum,
           "Purpose of WWTP":add_purposeWWTP,
           "Solvent for compound addition":add_solvent,
           "Type of Aeration":add_aeration,
           "Type of compound addition":add_compound_addition}




# if parameter == dict[entry] exists
# then set enviPath object entries to the values set at these entries






# def test_function():
#     add_actidity()

# def add_acidity():
#     check_acidity()
    