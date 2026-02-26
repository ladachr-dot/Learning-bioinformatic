## 🧬 Gene Expression Cancer RNA-Seq Classification

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange)
![Bioinformatics](https://img.shields.io/badge/Bioinformatics-Pipeline-green)

> Kaggle Solution: [https://www.kaggle.com/code/vladachern/gene-expression-cancer-rna-seq-solved/edit/run/297156476](https://www.kaggle.com/code/vladachern/gene-expression-cancer-rna-seq-solved)

A project focused on tumor type classification based on RNA-Seq data. The pipeline includes extensive Feature Engineering and a comparison of classical ML models with SOTA solutions (XGBoost, LightGBM, MLP).

### 📊 Dataset Overview
The project uses the "Gene Expression Cancer RNA-Seq" dataset. The data contains gene expression levels for patients with five different cancer types: BRCA, KIRC, COAD, LUAD, PRAD.

- data.csv: Feature matrix (881 patients, 20,531 genes).
- labels.csv: Target labels (5 tumor types: BRCA, KIRC, COAD, LUAD, PRAD).

---

### 🛠 Methodology (Feature Engineering)
To handle high-dimensional data (20k+ features), a multi-stage process was applied:
1. **Variance Threshold:** Removal of genes with zero variance (non-informative features).
2. **SelectKBest (f_classif):** Selection of the top 3,000 most significant genes correlating with tumor types.
3. **StandardScaler:** Feature scaling for optimal performance of neural networks and SVM.
4. **PCA (Principal Component Analysis):** Dimensionality reduction to 2D for visualizing cancer type clusters.

## 🛠 Tech Stack
* **Pandas & Numpy** — processing large data matrices.
* **Matplotlib & Seaborn** — visualization of gene clusters.
* **Scikit-Learn** — preprocessing pipelines and classical models.
* **XGBoost & LightGBM** — gradient boosting for maximum accuracy.

---

### 🤖 Модели и результаты
The project compares the following models:
| Model | Accuracy | F1-Score |
| :--- | :--- | :--- |
| **XGBoost** | 0.994 | 0.994 |
| **LightGBM** | 1.000 | 1.000 |
| **SVM (RBF)** | 1.000 | 1.000 |
| **MLP (Neural Net)** | 0.988 | 0.988 |

#### Key Metrics
- The models achieve near 99-100% accuracy due to high-quality gene selection.
- **Stratified Split:** The data was split 80/20 while maintaining class proportions.
