
from functions_folder.data_service import DataService
from functions_folder.coefficients_functions_folder.coefficient_evaluation_web_reader import scrape_match_links

def main():
    # * test data
    '''
    print("Testing data service")
    data_service = DataService()
    data_service.get_team("T1")
    '''
    print(scrape_match_links())
    
main()