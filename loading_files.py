import pydicom
import numpy as np
import os.path

def data_processing(folder,list,ouput_path):

    data = np.array([])
    # Loop through the files in the folder
    for f in list:
        if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith((".dcm",".dicom",".jpg",".jpeg",".png")):
        # Read the file
         print(os.path.join(folder, f))
         ds = pydicom.dcmread(os.path.join(folder, f))
         meta_file= ds.file_meta
         # Create an array of the data
         data=np.append(data, [meta_file[2,0].value, meta_file[2,1].value, meta_file[2,2].value,meta_file[2,3].value])
         # Write the data to a csv file
    np.savetxt(ouput_path+'/metadata.csv', [data], delimiter=',',fmt = '%s')
