
from data_service import DataService


def main():
    # * test data
    print("Testing data service")
    data_service = DataService()
    data_service.get_team("T1")

main()