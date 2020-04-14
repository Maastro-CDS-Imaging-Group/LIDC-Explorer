## LIDC-Explorer

This repository can be used to explore the LIDC IDRI Dataset. A held out set can be downloaded from this URL: https://drive.google.com/open?id=1OMzluXWz2WFfUmE19MzBRI4_8sqO7PtU

Once the data has been downloaded, clone/download this repository and then install requirements using
```
pip install -r requirements.txt
```

This explorer uses pylidc library and the setup instructions can be found here: ( Basically pointing pylidc to where the data has been downloaded)
https://pylidc.github.io/install.html


Now that the environment is setup, run the jupyter notebook Clinical_Analysis.ipynb using
```
jupyter-notebook
```