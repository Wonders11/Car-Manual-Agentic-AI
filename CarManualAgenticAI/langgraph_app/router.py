from agents.tata_agent import tata_agent
from agents.hyundai_agent import hyundai_agent
from agents.maruti_agent import maruti_agent

def route_request(company, model, fuel_type, query):
    if company.lower() == "tata":
        return tata_agent(model, fuel_type, query)
    elif company.lower() == "hyundai":
        return hyundai_agent(model, fuel_type, query)
    elif company.lower() == "maruti":
        return maruti_agent(model, fuel_type, query)
    else:
        return "Company not supported yet."
