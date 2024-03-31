# coding=utf-8
from ystream import *
#CHOOSE FROM THE INPUTES:
input_sv_file =  "../output/out_Rus_word_ngramm_tfidf_vo.txt"
input_as_file =  "../output/out_Rus_word_ngramm_tfidf_as.txt"
input_next_step = "../output/out_Rus_word_ngramm_tfidf_sv.txt"

#out_vectors_file = "../../datasets/my_out/out_Rus_word_ngramm_distances_tfidf_sv.txt"
out_vectors_file = "../output/out_Rus_word_ngramm_tfidf_sv_analogs.txt"

input_file = ySequence(input_next_step)
#input_as_file = ySequence(input_as_file)

file_lines = yInputFileLinesStream()
#file_lines_2 = yInputFileLinesStream()

split_to_key_vector = ySplitKeyVector(weightConvertFn = float)
#split_to_key_vector_2 = ySplitKeyVector(weightConvertFn = float)

key_vector_to_storage_input = yKeyVectorToKeyValueWeightStream()
#key_vector_to_storage_input_2 = yKeyVectorToKeyValueWeightStream()

storage = yStorageWithBag(iter_method="dict",
                          store_before_iter = True
                          )
#TODO if something wrong, do not forget about the mextric factor
dist_lines = yItemsSimpleFillWeight(metric=common_sum_metric,
                                    metric_factor = -1,
                                    trashhold = 50)

output_lines = yOutputFileLinesStream()

output_file = ySequence(out_vectors_file)

input_file > file_lines > split_to_key_vector>key_vector_to_storage_input > storage > dist_lines > output_lines > output_file

#for item in dist_lines:
    #pass
    #print(item)

#storage.store()
#storage.printall()


output_lines.save()

