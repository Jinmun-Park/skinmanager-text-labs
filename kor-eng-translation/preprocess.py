import glob
import pandas as pd

class RawDataset():
    def __init__(self, path):
        self.path = path

    def ReadFiles(self) -> pd.DataFrame:

        filenames = glob.glob(self.path + "*.tsv")
        df_lists = []
        for filename in filenames:
            df_lists.append(pd.read_csv(filename, delimiter='\t', on_bad_lines='skip', header=None))

        concat_df = pd.concat(df_lists, ignore_index=True)

        return concat_df

    def ExportFiles(self, export_name: str):

        concat_df = self.ReadFiles()

        return concat_df.to_csv(self.path + export_name + '.txt', index=False, header=None, sep="\t")


RawDataset = RawDataset(path='./data/kor-eng-translation/')
df = RawDataset.ReadFiles()
df.ExportFiles(export_name='sample_file')

"""
path = './data/kor-eng-translation/'
filenames = glob.glob(path + "*.tsv")
dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename, delimiter='\t', on_bad_lines='skip', header=None))

big_frame = pd.concat(dfs, ignore_index=True)
big_frame.to_csv(path +'sample_file.txt', index=False, header=None, sep="\t")
"""
