import glob
import pandas as pd


def multiple_csv(extension, directory, output_file_name):
    import os
    # set working directory
    os.chdir(directory)
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
    combined_csv.to_csv(output_file_name, index=False, encoding='utf-8-sig')


multiple_csv(extension='csv', directory=path of the folder where all files are present,
             output_file_name=name of the output file)

