from xbrl_instance import XbrlInstance
import json 

class UsGaap:

    def __init__(self) -> None:
        pass


    @staticmethod
    def collect_properties(elms:list):
        """[Summary]
        :param [elms]: a list of beautifulsoup elements used to build a dictionary of the elements attributes and text values
        """
        res = {}
        for elm in elms:
            uid = f"{elm.name} {elm.get('contextRef').split('_')[-1]}"
            res[uid] = dict(elm.attrs, **{'name':elm.name}, **{'text':elm.text})
        return res


    @staticmethod
    def map_context(soup, elms:dict):
        """Maps datetime string to an element based on it's context.period.instant. Finds the context element based on the contextRef provided in the elements properties dict.
        
        :param [res]: a dictionary of element attributes returned by collect_properties()
        """
        for k,v in elms.items():
            period = soup.find(name="context", attrs={"id": v.get('contextRef')}).find('instant').text
            elms[k]['period'] = period
        return elms


    @classmethod
    def parse_gaap(self, xbrli:XbrlInstance = None):
        """Iterates through a list of concepts and constructs a dictionary for desired attributes of each concept
        """
        concepts = ['Assets', 'LiabilitiesAndStockholdersEquity']

        res = dict()
        for c in concepts:
            elms = xbrli.soup.find_all(c)
            concept_properties = self.collect_properties(elms)
            concept_properties = self.map_context(xbrli.soup, concept_properties)
            res = dict(res, **concept_properties)

        parsed_res = dict()
        for concept, conceptdict in res.items():
            parsed = {key: conceptdict[key] for key in ['name', 'period', 'text', 'unitRef','decimals']}
            parsed_res[concept] = parsed

        return parsed_res

    

    def serialize(self):
        pass