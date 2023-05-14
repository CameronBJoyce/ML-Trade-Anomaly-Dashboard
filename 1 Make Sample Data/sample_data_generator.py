"""
This is a simplified example for demonstration purposes.
 In practice, you may need to incorporate more sophisticated 
 data generation techniques or retrieve data from external sources 
 to ensure the generated trade data reflects real-world scenarios.
"""

import pandas as pd
import random
import numpy as np

class SampleDataGenerator:
    def __init__(self, num_entries):
        self.num_entries = num_entries
        self.columns = [
            "Country",
            "Year",
            "Commodity",
            "Import Value",
            "Export Value",
            "Total Trade Value",
            "Quantity",
            "Unit",
            "Trade Balance",
            "Partner Country",
            "Partner Continent",
            "Shipping Method",
            "Transport Cost",
            "Customs Duty"
        ]
        
    def generate_trade_data(self):
        data = []
        
        for _ in range(self.num_entries):
            country = random.choice(["USA", "China", "Germany", "France", "Brazil"])
            year = random.randint(2010, 2022)
            commodity = random.choice(["Electronics", "Textiles", "Automobiles", "Chemicals", "Machinery"])
            import_value = random.randint(100000, 1000000)
            export_value = random.randint(100000, 1000000)
            total_trade_value = import_value + export_value
            quantity = random.randint(1000, 10000)
            unit = random.choice(["kg", "liters", "units"])
            trade_balance = export_value - import_value
            partner_country = random.choice(["Canada", "Australia", "India", "Mexico", "United Kingdom"])
            partner_continent = random.choice(["North America", "Asia", "Europe", "South America"])
            shipping_method = random.choice(["Air", "Sea", "Rail", "Road"])
            transport_cost = round(random.uniform(100, 1000), 2)
            customs_duty = round(random.uniform(1, 10), 2)
            
            row = [
                country,
                year,
                commodity,
                import_value,
                export_value,
                total_trade_value,
                quantity,
                unit,
                trade_balance,
                partner_country,
                partner_continent,
                shipping_method,
                transport_cost,
                customs_duty
            ]
            
            data.append(row)
        
        df = pd.DataFrame(data, columns=self.columns)
        return df

# Example usage:
generator = TradeDataGenerator(1000)  # Generate 1000 entries
trade_data = generator.generate_trade_data()
print(trade_data.head())
