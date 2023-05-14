import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import statsmodels.api as sm

class TradeDataTrendAnalysis:
    def __init__(self, trade_data):
        self.trade_data = trade_data
    
    def perform_trend_analysis(self, variables_of_interest):
        # Time Series Analysis
        self.time_series_analysis(variables_of_interest)
        
        # Multiple Linear Regression with Difference in Differences (DiD)
        self.multiple_linear_regression_did(variables_of_interest)
        
        # Clustering
        self.clustering(variables_of_interest)
        
        # Dimensionality Reduction (PCA)
        self.dimensionality_reduction(variables_of_interest)
    
    def time_series_analysis(self, variables_of_interest):
        for variable in variables_of_interest:
            ts_data = self.trade_data[['Year', variable]].groupby('Year').sum()
            ts_data.plot(figsize=(10, 6), marker='o')
            plt.title(f'Time Series Analysis: {variable}')
            plt.xlabel('Year')
            plt.ylabel(variable)
            plt.show()
    
    def multiple_linear_regression_did(self, variables_of_interest):
        for variable in variables_of_interest:
            self.trade_data['Post_Treatment'] = np.where(self.trade_data['Year'] >= 2015, 1, 0)
            self.trade_data['Treated_Group'] = np.where(self.trade_data['Country'] == 'USA', 1, 0)
            
            model = sm.OLS(self.trade_data[variable],
                           sm.add_constant(self.trade_data[['Post_Treatment', 'Treated_Group', 'Post_Treatment:Treated_Group']]))
            results = model.fit()
            print(f"Multiple Linear Regression with DiD: {variable}")
            print(results.summary())
            print()
    
    def clustering(self, variables_of_interest):
        trade_data_subset = self.trade_data[variables_of_interest]
        
        kmeans = KMeans(n_clusters=5)
        kmeans.fit(trade_data_subset)
        
        self.trade_data['Cluster'] = kmeans.labels_
        
        for variable in variables_of_interest:
            sns.boxplot(x='Cluster', y=variable, data=self.trade_data)
            plt.title(f'Clustering: {variable}')
            plt.xlabel('Cluster')
            plt.ylabel(variable)
            plt.show()
    
    def dimensionality_reduction(self, variables_of_interest):
        trade_data_subset = self.trade_data[variables_of_interest]
        
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(trade_data_subset)
        
        self.trade_data['PC1'] = pca_result[:, 0]
        self.trade_data['PC2'] = pca_result[:, 1]
        
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x='PC1', y='PC2', data=self.trade_data)
        plt.title('Dimensionality Reduction (PCA)')
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.show()