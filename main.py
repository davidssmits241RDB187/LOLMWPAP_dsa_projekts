
from functions.evaluate_function import evaluate_coefficients
from classes.match_class import Match
from functions.coefficient_file_management import write_match_to_file,read_matches_from_file
from classes.coefficients_class import Coefficients
def main():
    # * test data
    print("Testing data service")
    
    match1 = Match("T1", "Los Ratones")
    match1.evaluate_team1_vs_team2_default()
    original_coeffs = Coefficients(
        gold_lead=[1.1, 2.2],
        kills=[3.3, 4.4],
        towers=[5.5, 6.6],
        dragons=[7.7, 8.8],
        barons=[9.9, 10.10],

        top_kda=[1.1, 1.2],
        top_csm=[1.3, 1.4],
        top_dpm=[1.5, 1.6],
        top_wpm=[1.7, 1.8],

        mid_kda=[2.1, 2.2],
        mid_csm=[2.3, 2.4],
        mid_dpm=[2.5, 2.6],
        mid_wpm=[2.7, 2.8],

        jungle_kda=[3.1, 3.2],
        jungle_csm=[3.3, 3.4],
        jungle_dpm=[3.5, 3.6],
        jungle_wpm=[3.7, 3.8],

        bot_kda=[4.1, 4.2],
        bot_csm=[4.3, 4.4],
        bot_dpm=[4.5, 4.6],
        bot_wpm=[4.7, 4.8],

        support_kda=[5.1, 5.2],
        support_csm=[5.3, 5.4],
        support_dpm=[5.5, 5.6],
        support_wpm=[5.7, 5.8]
    )

    write_match_to_file(original_coeffs)
    print("Original coefficients written to file.")

    loaded_coeffs = read_matches_from_file()
    print("Coefficients read from file:", loaded_coeffs.__dict__)

    if original_coeffs.__dict__ == loaded_coeffs.__dict__:
        print("Success: Loaded coefficients match the original.")
    else:
        print("Error: Loaded coefficients do NOT match the original.")
    evaluate_coefficients("T1","G2 Esports")
    match1.evaluate_team1_vs_team2_default()
main()