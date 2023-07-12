

output_file = open('classified_output.txt','w')
input_file = open(
        'C:/Users/riya.srivastava/PycharmProjects/yolov5_classification/yolov5/runs/predict-cls/exp6/cat.0.jpg','r'
    )
output_file.write(
input_file
)
print(output_file)
output_file.close()

