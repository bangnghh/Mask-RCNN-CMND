import h5py
filename = "mask_rcnn_coco.h5"
listkey = []

file = h5py.File(filename, "r")
for group in file.keys() :
    #print (group) 
    for dset in file[group].keys() :
        
        ds_data = h5py.h5f[group][dset] # returns HDF5 dataset object
        print(ds_data)
        print (ds_data.shape, ds_data.dtype)
        arr = h5py.h5f[group][dset][:] # adding [:] returns a numpy array
        print (arr.shape, arr.dtype)
        print (arr)
    