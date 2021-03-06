from functions.library_tools import from_features_to_response_of_PLS, inflate_list_format_degenerated_sequence, analyze_UTR,inflate_list_format_degenerated_sequence, list_to_degenerate_formate, degenerate_format_to_list_format
from functions.general import extract_scale_and_coefficients, coef_scales_from_dict_to_list

names_features_utr_analysis = ['dG_EFE','purineAG_in_min3','U_in_min3','A_in_min1','AA_in_min32','CG_in_min32','AC_in_min21','oof_uAUG','GACA_kmer','GG_kmer','CACC_kmer','CA_in_min76','CC_in_min76']
# Insert path to these files
coef_csvfile = '/coefficients.csv'
scales_csvfile = '/scales.csv'
coef_dict,scales_dict = extract_scale_and_coefficients(coef_csvfile,scales_csvfile)
coef_list,scales_list,intercept = coef_scales_from_dict_to_list(coef_dict,scales_dict,names_features_utr_analysis)

# Enter CDS of gene of interest
cds = ''

# Enter the UTR sequence of the gene of interest
list_of_candidates = ['']

for candidate in list_of_candidates:
#	print(candidate)
	candidate_list_format = degenerate_format_to_list_format(candidate)
	print(candidate_list_format)
	inflated_candidate = inflate_list_format_degenerated_sequence(candidate_list_format)
	response_list = []
	for candidate_utr_seq in inflated_candidate:
		utr_features = analyze_UTR(candidate_utr_seq,cds)
		response = from_features_to_response_of_PLS(utr_features,names_features_utr_analysis,coef_list,scales_list,intercept)
		response_list.append(response)
		print(candidate_utr_seq+' = '+str(response))

