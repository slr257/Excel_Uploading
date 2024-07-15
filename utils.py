# need to reload enviPath objects to make sure objects are defined in the dictionary?
from enviPath_python.enviPath import *
from enviPath_python.objects import *

# if this exists in the dictionary, then map it - these values are the only ones availabe as python objects
dict_ai = {"Addition of nutrients": NutrientsAdditionalInformation,
           "Biological treatment technology":BiologicalTreatmentTechnologyAdditionalInformation,
           "Bioreactor":BioreactorAdditionalInformation,
           "Dissolved oxygen concentration":DissolvedOxygenConcentrationAdditionalInformation,
           "pH": AcidityAdditionalInformation,
           "Temperature":TemperatureAdditionalInformation,
           "Redox condition": RedoxAdditionalInformation,
           "Name of Sampling Location":LocationAdditionalInformation, 
           "TSS":TSSAdditionInformation,
           "Inoculum source":InoculumSourceAdditionalInformation,
           "Purpose of WWTP":PurposeOfWWTPAdditionalInformation,
           "Solvent for compound addition":SolventForCompoundSolutionAdditionalInformation,
           "Type of Aeration":TypeOfAerationAdditionalInformation,
           "Type of compound addition":TypeOfAdditionAdditionalInformation,
           # values not in example template
           "Oxygen Demand":OxygenDemandAdditionalInformation,
           "Nitrogen Content":NitrogenContentAdditionalInformation,
           "Ammonia Uptake Rate (AUR)":AmmoniaUptakeRateAdditionalInformation,
           "Final compound concentration":FinalCompoundConcentrationAdditionalInformation, 
           "Dissolved organic carbon (DOC)":DissolvedOrganicCarbonAdditionalInformation, 
           "Initial amount of sludge in bioreactor":OriginalSludgeAmountAdditionalInformation, 
           "Oxygen uptake rate (OUR)":OxygenUptakeRateAdditionalInformation, 
           "Phosphorus Content":PhosphorusContentAdditionalInformation, 
           "Proposed intermediate":ProposedIntermediateAdditionalInformation, 
           "Sludge retention time":SludgeRetentionTimeAdditionalInformation, 
           "Source of liquid matrix":SourceOfLiquidMatrixAdditionalInformation, 
           "Volatile suspended solids concentration (VSS)":VolatileTSSAdditionalInformation}


# try making a dictionary of functions that will be executed if the object exists
# filter dictionary based on values in Parameters column in Excel template

def add_volatilesuspendedsolids(base_scenario, ai_list):
    ai = dict_ai["Volatile suspended solids concentration (VSS)"]()
    ai.set_volatilettsStart(base_scenario[base_scenario["Parameter"]=="Volatile suspended solids concentration (VSS)"]["Value"].values[0])
    ai.set_volatilettsEnd(base_scenario[base_scenario["Parameter"]=="Volatile suspended solids concentration (VSS)"]["Value"].values[0])
    ai_list.append(ai)

def add_sourceofliquidmatrix(base_scenario, ai_list):
    ai = dict_ai["Source of liquid matrix"]()
    ai.set_sourceofliquidmatrix(base_scenario[base_scenario["Parameter"]=="Source of liquid matrix"]["Value"].values[0])
    ai_list.append(ai)

def add_sludgeretentiontime(base_scenario, ai_list):
    ai = dict_ai["Sludge retention time"]()
    ai.set_sludgeretentiontimeType(base_scenario[base_scenario["Parameter"]=="Sludge retention time"]["Type"].values[0])
    ai.set_sludgeretentiontime(base_scenario[base_scenario["Parameter"]=="Sludge retention time"]["Value"].values[0])
    ai_list.append(ai)

def add_proposedintermediate(base_scenario, ai_list):
    ai = dict_ai["Proposed intermediate"]()
    ai.set_proposed(base_scenario[base_scenario["Parameter"]=="Proposed intermediate"]["Value"].values[0])
    ai_list.append(ai)

def add_phosphoruscontent(base_scenario, ai_list):
    ai = dict_ai["Phosphorus Content"]()
    ai.set_phosphoruscontentInfluent(base_scenario[base_scenario["Parameter"]=="Phosphorus Content"]["Value"].values[0])
    ai_list.append(ai)

def add_oxygenuptakerate(base_scenario, ai_list):
    ai = dict_ai["Oxygen uptake rate (OUR)"]()
    ai.set_oxygenuptakerateStart(base_scenario[base_scenario["Parameter"]=="Oxygen uptake rate (OUR)"]["Value"].values[0])
    ai.set_oxygenuptakerateEnd(base_scenario[base_scenario["Parameter"]=="Oxygen uptake rate (OUR)"]["Value"].values[0])
    ai_list.append(ai)

def add_initialsludgeinbioreactor(base_scenario, ai_list):
    ai = dict_ai["Initial amount of sludge in bioreactor"]()
    ai.set_originalsludgeamount(base_scenario[base_scenario["Parameter"]=="Initial amount of sludge in bioreactor"]["Value"].values[0])
    ai_list.append(ai)

def add_dissolvedorganiccarbon(base_scenario, ai_list):
    ai = dict_ai["Dissolved organic carbon (DOC)"]()
    ai.set_dissolvedorganiccarbonStart(base_scenario[base_scenario["Parameter"]=="Dissolved organic carbon (DOC)"]["Value"].values[0])
    ai_list.append(ai)

def add_finalcompoundconcentration(base_scenario, ai_list):
    ai = dict_ai["Final compound concentration"]()
    ai.set_finalcompoundconcentration(base_scenario[base_scenario["Parameter"]=="Final compound concentration"]["Value"].values[0])
    ai_list.append(ai)

def add_ammoniauptakerate(base_scenario, ai_list):
    ai = dict_ai["Ammonia Uptake Rate (AUR)"]()
    ai.set_amionauptakerateStart(base_scenario[base_scenario["Parameter"]=="Ammonia Uptake Rate (AUR)"]["Value"].values[0])
    ai_list.append(ai)

def add_nitrogencontent(base_scenario, ai_list):
    ai = dict_ai["Nitrogen Content"]()
    ai.set_nitrogencontentType(base_scenario[base_scenario["Parameter"]=="Nitrogen Content"]["Type"].values[0])
    ai.set_nitrogencontentInfluent(base_scenario[base_scenario["Parameter"]=="Nitrogen Content"]["Value"].values[0])
    ai_list.append(ai)

def add_oxygendemand(base_scenario, ai_list):
    ai = dict_ai["Oxygen Demand"]()
    ai.set_oxygendemandType(base_scenario[base_scenario["Parameter"]=="Oxygen Demand"]["Type"].values[0])
    ai.set_oxygendemandInfluent(base_scenario[base_scenario["Parameter"]=="Oxygen Demand"]["Value"].values[0])
    ai.set_oxygendemandEffluent(base_scenario[base_scenario["Parameter"]=="Oxygen Demand"]["Value"].values[0])
    ai_list.append(ai)

def add_nutrients(base_scenario, ai_list):
    ai = dict_ai["Addition of nutrients"]()
    ai.set_additionofnutrients(base_scenario[base_scenario["Parameter"]=="Addition of nutrients"]["Value"].values[0]) # must be a string value
    ai_list.append(ai)
    
def add_pH(base_scenario, ai_list):
    ai = dict_ai["pH"]()
    ai.set_lowPh(float(base_scenario[base_scenario["Parameter"]=="pH"]["Value"].values[0].split("-")[0]))
    ai.set_highPh(float(base_scenario[base_scenario["Parameter"]=="pH"]["Value"].values[0].split("-")[1]))
    ai_list.append(ai)

# def add_oxygendemand(base_scenario, ai_list):
#     ai = dict_ai["Oxygen demand"]()
#     ai.set_oxygendemandType()
#     ai.set_oxygendemandInfluent()
#     ai.set_oxygendemandEffluent()
#     ai_list.append(ai)

def add_dissolvedoxygen(base_scenario, ai_list):
    ai = dict_ai["Dissolved oxygen concentration"]()
    ai.set_DissolvedoxygenconcentrationLow(base_scenario[base_scenario["Parameter"]=="Dissolved oxygen concentration"]["Value"].values[0])
    ai.set_DissolvedoxygenconcentrationHigh(base_scenario[base_scenario["Parameter"]=="Dissolved oxygen concentration"]["Value"].values[0])
    # ai.set_DissolvedoxygenconcentrationLow()
    # ai.set_DissolvedoxygenconcentrationHigh()
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
dict_fun = {"Addition of nutrients": add_nutrients,
            "Ammonia Uptake Rate (AUR)":add_ammoniauptakerate,
            "Biological treatment technology":add_biotreattech,
            "Bioreactor":add_bioreactor,
            "Dissolved organic carbon (DOC)":add_dissolvedorganiccarbon,
            "Dissolved oxygen concentration":add_dissolvedoxygen,
            "Final compound concentration":add_finalcompoundconcentration,
            "Initial amount of sludge in bioreactor":add_initialsludgeinbioreactor,
            "Inoculum source":add_inoculum,
            "Name of Sampling Location":add_location,
            "Nitrogen Content":add_nitrogencontent,
            "Oxygen Demand":add_oxygendemand,
            "Oxygen uptake rate (OUR)":add_oxygenuptakerate,
            "pH": add_pH,
            "Phosphorus Content":add_phosphoruscontent,
            "Proposed intermediate":add_proposedintermediate,
            "Purpose of WWTP":add_purposeWWTP,
            "Redox condition": add_redox,
            "Sludge retention time":add_sludgeretentiontime,
            "Solvent for compound addition":add_solvent,
            "Source of liquid matrix":add_sourceofliquidmatrix,
            "Temperature":add_Temp,
            "TSS":add_TSS,
            "Type of Aeration":add_aeration,
            "Type of compound addition":add_compound_addition,
            "Volatile suspended solids concentration (VSS)":add_volatilesuspendedsolids}


# if parameter == dict[entry] exists
# then set enviPath object entries to the values set at these entries






# def test_function():
#     add_actidity()

# def add_acidity():
#     check_acidity()
    