import h5py

def read_data(path_of_data):
  """
  read data seaved in h5py format
  assuming group keys that exists are X,y 
  """
  with h5py.File(path_of_data, "r") as f:
    X,y = f["X"][:],f['y'][:]
  return X,y
