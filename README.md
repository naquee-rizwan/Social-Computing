Roll No. - 23CS91R06
Name - Naquee Rizwan

# Social Computing Assignment 2

All these files are named as per the guidelines provided in the Assignment.
Following are the details of various files and the models they are using :-

------------------- Intent Recognition --------------------

Initial Dataset setup logic is same in almost all the files.
So, some initial codes of these files are almost same. For details, please visit the code.

ir_svm_en.ipynb - English, TF-IDF Vectorization, SVM
ir_rob_en.ipynb - English, "roberta-base" as model checkpoint
ir_bcbert_en.ipynb - English, "emilyalsentzer/Bio_ClinicalBERT" as model checkpoint
ir_xlmr_hi.ipynb - Hindi, "xlm-roberta-base" as model checkpoint
ir_dtrans_hi.ipynb - Hindi, GoogleTranslator(Hindi to English), "emilyalsentzer/Bio_ClinicalBERT" as model checkpoint
ir_bridge_hi.ipynb - Bengali, GoogleTranslator(Bengali to Hindi), GoogleTranslator(Hindi to English), "emilyalsentzer/Bio_ClinicalBERT" as model checkpoint

------------------- Entity Extraction --------------------

For entity extraction, matching of below tags were done through fuzzywuzzy library's threshold string matching by calculating a fuzzy ratio:-
label__ = {
    'O': 0,
    'B-treatment': 1,
    'I-treatment': 2,
    'B-disease': 3,
    'I-disease': 4,
    'B-drug': 5,
    'I-drug': 6
}

Initial Dataset setup logic is same in almost all the files.
So, some initial codes of these files are almost same. For details, please visit the code.

ee_svm_en.ipynb - English, TF-IDF Vectorization, SVM
ee_rob_en.ipynb - English, "roberta-base" as model checkpoint
ee_bcbert_en.ipynb - English, "emilyalsentzer/Bio_ClinicalBERT" as model checkpoint
ee_xlmr_hi.ipynb - Hindi, "xlm-roberta-base" as model checkpoint
ee_dtrans_hi.ipynb - Hindi, GoogleTranslator(Hindi to English), "emilyalsentzer/Bio_ClinicalBERT" as model checkpoint
ee_bridge_hi.ipynb - Bengali, GoogleTranslator(Bengali to Hindi), GoogleTranslator(Hindi to English), "emilyalsentzer/Bio_ClinicalBERT" as model checkpoint

# Running these codes

1. Keep the dataset "indic-health-demo" in the parent folder only.
2. Open Jupyter notebook and start running the code one by one.
3. Try to run the code in one go itself because the dataset table values [DataFrame] get updated at run time which might cause some issues.

# Some common errors that might occur while running the code

1. Uninstalled libraries. I have added 'pip install' in almost all files to install required libraries. If not present just install the missing library.
2. Cuda memory limit exceed problem. If this problem persists, use CPU instead of GPU by just hard coding device = "cpu" in the code.
3. Dataset must be present within the same folder as the files. Use the dataset I have kept here itself "indic-health-demo".
4. To run it on Google Colab corresponding changes to dataset path must be done.
5. If facing any-other problem while running the code, please contact me.
