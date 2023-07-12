import glob
import os
def merge_txt_files(output_file, filepath):
    with open(output_file, 'w') as outfile:
        for input_file in os.listdir(filepath):
            with open(filepath+input_file, 'r') as infile:
                outfile.write(infile.read())

if __name__ == '__main__':
    filepath = 'C:\\Users\\riya.srivastava\\PycharmProjects\\yolov5_classification\\yolov5\\runs\\predict-cls-test\\exp4\\labels\\'
    output_file = 'merged_file.txt'
    merge_txt_files(output_file, filepath)
