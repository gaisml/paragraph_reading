import os
import glob
from application.resources.Aligner import text_grid


def get_data(data_path):
    files = glob.glob('*.lab')

    with open('para.txt', 'w') as result:
        for file_ in files:
            for line in open(file_, 'r'):
                result.write(line)

    # file = '/home/hp/PycharmProjects/flask-application/application/resources/Aligner/data/para.txt'
    # convert = os.path.splitext(file)[0]
    # con_file = os.path.join(convert + ".lab")
    # print(con_file)
    # read_file = pd.read_csv(r'/home/hp/PycharmProjects/flask-application/application/resources/Aligner/data/para.txt')
    # read_file.to_lab(r'/home/hp/PycharmProjects/flask-application/application/resources/Aligner/data/para.txt', index=None)

def get_alignment(data_path,dictionary_path,acoustic_model_path,output_path):
    if not os.path.isdir(data_path):
        print("data path does not exist!")
        return False
    try:
        if os.path.exists(output_path):
            os.system('rm -rf {}'.format(output_path))
            cmds = "mfa align /home/hp/PycharmProjects/flask-application/application/resource/Aligner/data /home/hp/PycharmProjects/flask-application/application/resource/Aligner/models/english.dict /home/hp/PycharmProjects/flask-application/application/resource/Aligner/models/english.zip /home/hp/PycharmProjects/flask-application/application/resource/Aligner/data/output --clean".format(
                data_path,
                dictionary_path,
                acoustic_model_path,
                output_path)
            os.system(cmds)
    except Exception as e:
        print("Exception error occurred!")
        return False
    return True

# segments=text_grid.read_sentence_TextGrid('/home/hp/PycharmProjects/align/out/data-prog-conv.TextGrid')
# print(segments)