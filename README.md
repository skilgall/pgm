Code Examples for the Ph.D. seminar on PGM

## Setup instructions

- Install Anaconda Python 3.x first: https://www.continuum.io/downloads#_macosx
- Clone this repo:
```
git clone https://github.com/harrywang/pgm.git
cd pgm
```

- Create a virtual environment using conda:
```
conda create -n pgm python=3.4.3
source activate pgm
```
- Build pgmpy (http://pgmpy.org)
```
git clone https://github.com/pgmpy/pgmpy
cd pgmpy
pip install -r requirements.txt
sudo python3 setup.py install
```
- Install jupyter (http://jupyter.org)
```
conda install jupyter
```
- Install matplotlib (http://matplotlib.org)
You now can run `ipython3` and notebook `jupyter notebook`
